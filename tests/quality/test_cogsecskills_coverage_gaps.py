"""Behavioral edge cases for the CLI and the scenario/row artifact surfaces.

Covers: CLI list with empty results, dashboard/examples/evals/release-metadata
--check drift failure paths, author-batch with failures, malformed scenario
fields rejected by ``load_scenarios``, and undeclared-field fallbacks in the
manuscript row collector and catalogue renderer.
"""

from __future__ import annotations

import copy
import re
import shutil
from pathlib import Path

import pytest
import yaml

from cogsecskills.cli import main

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _seed_registry(root: Path, *rows: str) -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n" + "\n".join(rows) + "\n", encoding="utf-8"
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )


_ROW = (
    "  - {id: sat.demo, name: Demo, group: sat, status: planned, summary: A demo area.}"
)


def _copy_fixture(tmp_path: Path, *dirnames: str) -> Path:
    for d in dirnames:
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    return tmp_path


# --- CLI: list with empty results ----------------------------------------


def test_cli_list_group_with_no_matches(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "list", "--group", "nonexistent"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "0 of 1 skill areas" in out


def test_cli_list_status_with_no_matches(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "list", "--status", "implemented"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "0 of 1 skill areas" in out


def test_cli_list_limit_zero(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "list", "--limit", "0"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "0 of 1 skill areas" in out


# --- CLI: dashboard/examples/evals/release-metadata --check failure paths -


def test_cli_dashboard_check_with_drift(tmp_path, capsys):
    root = _copy_fixture(
        tmp_path, "registry", "skills", "scenarios", "examples", "evals"
    )
    from cogsecskills.artifacts.dashboard import write_dashboard

    write_dashboard(root)
    # Corrupt a dashboard file to trigger drift
    (root / "docs" / "quality-dashboard.md").write_text(
        "manual edit\n", encoding="utf-8"
    )
    rc = main(["--root", str(root), "dashboard", "--check"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "DASHBOARD" in out
    assert "dashboard issue(s)" in out


def test_cli_examples_check_with_drift(tmp_path, capsys):
    root = _copy_fixture(tmp_path, "registry", "skills", "examples")
    from cogsecskills.artifacts.examples import write_examples

    write_examples(root)
    (root / "docs" / "skill-worked-examples.md").write_text(
        "manual edit\n", encoding="utf-8"
    )
    rc = main(["--root", str(root), "examples", "--check"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "EXAMPLES" in out
    assert "worked example issue(s)" in out


def test_cli_evals_check_with_drift(tmp_path, capsys):
    root = _copy_fixture(tmp_path, "registry", "skills", "scenarios")
    from cogsecskills.artifacts.evals import write_evals

    write_evals(root)
    (root / "docs" / "evaluation-readiness.md").write_text(
        "manual edit\n", encoding="utf-8"
    )
    rc = main(["--root", str(root), "evals", "--check"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "EVALS" in out
    assert "offline eval issue(s)" in out


def test_cli_release_metadata_check_with_drift(tmp_path, capsys):
    root = tmp_path
    for f in ("pyproject.toml", "CITATION.cff", "codemeta.json", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / f, root / f)
    for d in ("docs", "manuscript", "output", "figures"):
        if (PROJECT_ROOT / d).exists():
            shutil.copytree(PROJECT_ROOT / d, root / d)
    from cogsecskills.artifacts.release_metadata import write_release_metadata

    write_release_metadata(root)
    (root / "docs" / "release-claim-matrix.md").write_text(
        "manual edit\n", encoding="utf-8"
    )
    rc = main(["--root", str(root), "release-metadata", "--check"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "RELEASE" in out
    assert "release metadata issue(s)" in out


# --- CLI: author-batch with failures -------------------------------------


def test_cli_author_batch_with_bad_def(tmp_path, capsys):
    _seed_registry(
        tmp_path,
        "  - {id: sat.good, name: Good, group: sat, status: implemented, summary: s}",
        "  - {id: sat.bad, name: Bad, group: sat, status: implemented, summary: s}",
    )
    # Create a _def.json with a bad verb
    skill_dir = tmp_path / "skills" / "sat" / "bad"
    skill_dir.mkdir(parents=True)
    (skill_dir / "_def.json").write_text(
        '{"id": "sat.bad", "tools": [{"verb": "badverb", "purpose": "p"}], '
        '"workflow_steps": [{"verbs": ["reason"], "title": "S", "text": "T"}], '
        '"anti_criteria": ["Do not."]}',
        encoding="utf-8",
    )
    rc = main(["--root", str(tmp_path), "author-batch", "--keep-defs"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "FAIL" in out


# --- scenarios.py: malformed fixture fields via load_scenarios -----------

_VALID_SCENARIO: dict = {
    "id": "no-route",
    "group": "sat",
    "kind": "safe_defensive",
    "query": "zzqxzzwvk authorized qqpzwwkx",
    "expected_skill": "sat.x",
    "expected_output_terms": ["product"],
    "required_quality_terms": ["evidence"],
    "expected_response": {
        "required_sections": ["s1", "s2", "s3"],
        "must_include_terms": ["evidence", "confidence", "uncertainty", "defensive"],
        "must_exclude_terms": ["x", "y"],
    },
    "expected_answer": {
        "selected_skill": "sat.x",
        "answer_kind": "defensive_output",
        "sections": [
            {"title": "A", "body": "evidence inference gap confidence"},
            {"title": "B", "body": "uncertainty"},
            {"title": "C", "body": "defensive"},
        ],
        "rubric_scores": {
            "skill_fit": 2,
            "evidence_labeling": 2,
            "uncertainty": 2,
            "defensive_boundary": 2,
            "output_usefulness": 2,
        },
    },
}


def _write_scenario_fixture(root: Path, scenario: dict) -> None:
    (root / "scenarios").mkdir(exist_ok=True)
    (root / "scenarios" / "defensive_readiness.yaml").write_text(
        yaml.safe_dump({"scenarios": [scenario]}, sort_keys=False), encoding="utf-8"
    )


@pytest.mark.parametrize(
    ("field_path", "bad_value", "expected_message"),
    [
        ("expected_response", "notamapping", "expected_response must be a mapping"),
        ("expected_answer", "notamapping", "expected_answer must be a mapping"),
        (
            "expected_answer",
            {"answer_kind": "defensive_output"},
            "must include selected_skill and answer_kind",
        ),
        ("expected_answer.sections", "notalist", "must be a non-empty list"),
        ("expected_answer.sections", [], "must be a non-empty list"),
        ("expected_answer.sections", ["notamapping"], "sections[1] must be a mapping"),
        (
            "expected_answer.sections",
            [{"title": "T"}],
            "sections[1] must include title and body",
        ),
        (
            "expected_answer.sections",
            [{"body": "B"}],
            "sections[1] must include title and body",
        ),
        (
            "expected_answer.rubric_scores",
            "notamapping",
            "rubric_scores must be a mapping",
        ),
        (
            "expected_answer.rubric_scores",
            {"skill_fit": "notint"},
            "rubric_scores.skill_fit must be an integer",
        ),
    ],
)
def test_load_scenarios_rejects_malformed_fields(
    tmp_path, field_path, bad_value, expected_message
):
    """A malformed scenario field raises ValueError naming the offending field."""
    from cogsecskills.artifacts.scenarios import load_scenarios

    scenario = copy.deepcopy(_VALID_SCENARIO)
    node = scenario
    *parents, leaf = field_path.split(".")
    for part in parents:
        node = node[part]
    node[leaf] = bad_value
    _write_scenario_fixture(tmp_path, scenario)
    with pytest.raises(ValueError, match=re.escape(expected_message)):
        load_scenarios(tmp_path)


# --- rows.py: undeclared-field fallbacks via public surfaces --------------


def test_collect_skill_rows_reports_undeclared_quality_fields(tmp_path):
    """A skill without quality fields gets 'not declared' in each row field."""
    from cogsecskills.artifacts.manuscript_assets.rows import collect_skill_rows

    _seed_registry(
        tmp_path,
        "  - {id: sat.demo, name: Demo, group: sat, status: stub, summary: A demo area.}",
    )
    skill_dir = tmp_path / "skills" / "sat" / "demo"
    skill_dir.mkdir(parents=True)
    (skill_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: A demo area.\nstatus: stub\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n"
        "negative_controls:\n  - 'Always be careful before acting.'\n",
        encoding="utf-8",
    )
    rows = collect_skill_rows(tmp_path)
    assert len(rows) == 1
    row = rows[0]
    assert row.evidence_discipline == "not declared"
    assert row.confidence_anchor == "not declared"
    assert row.unsafe_redirect == "not declared"
    assert row.safe_defensive_pattern == "not declared"


def test_render_skill_catalogue_renders_none_for_empty_row_fields():
    """Empty row verb/input/output lists render as 'none' in the catalogue."""
    from cogsecskills.artifacts.manuscript_assets.rows import SkillRow
    from cogsecskills.artifacts.manuscript_assets.tables import render_skill_catalogue

    def _row(**overrides: object) -> SkillRow:
        fields: dict[str, object] = dict(
            id="sat.demo",
            name="Demo",
            group="sat",
            group_title="SAT",
            status="stub",
            functionality="s",
            use_when="u",
            ageint_topic="t",
            verbs=(),
            inputs=(),
            outputs=(),
            tags=(),
            harnesses=("claude",),
            references_count=0,
            defensive_boundary="b",
            evidence_discipline="e",
            confidence_anchor="c",
            unsafe_redirect="u",
            safe_defensive_pattern="s",
            source_path="p",
        )
        fields.update(overrides)
        return SkillRow(**fields)

    catalogue = render_skill_catalogue([_row()])
    assert "Verbs: none" in catalogue
    assert "Inputs: none" in catalogue
    assert "Outputs: none" in catalogue

    filled = render_skill_catalogue(
        [_row(verbs=("read",), inputs=("ctx",), outputs=("product",))]
    )
    assert "Verbs: read" in filled
    assert "Inputs: ctx" in filled
    assert "Outputs: product" in filled


def test_rows_group_ids_first_seen_order():
    """Group ids are collected in first-seen row order."""
    from cogsecskills.artifacts.manuscript_assets.rows import SkillRow, _group_ids

    def _row(group: str) -> SkillRow:
        return SkillRow(
            id=f"{group}.demo",
            name="Demo",
            group=group,
            group_title=group.upper(),
            status="implemented",
            functionality="s",
            use_when="u",
            ageint_topic="t",
            verbs=("read",),
            inputs=("ctx",),
            outputs=("out",),
            tags=("tag",),
            harnesses=("claude",),
            references_count=1,
            defensive_boundary="b",
            evidence_discipline="e",
            confidence_anchor="c",
            unsafe_redirect="u",
            safe_defensive_pattern="s",
            source_path="p",
        )

    assert _group_ids([]) == ()
    assert _group_ids([_row("sat"), _row("osint_integrity"), _row("sat")]) == (
        "sat",
        "osint_integrity",
    )


def test_rows_first_containing_fallback():
    """No matching value falls back to 'not declared' (helper contract; no
    production consumer reaches this branch through a public entry point)."""
    from cogsecskills.artifacts.manuscript_assets.rows import _first_containing

    assert _first_containing([], ("a",)) == "not declared"
    assert _first_containing(["hello"], ("xyz",)) == "not declared"
    assert _first_containing(["hello world"], ("hello", "world")) == "hello world"
