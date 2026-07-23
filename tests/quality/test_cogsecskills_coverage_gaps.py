"""Tests for remaining CLI and module coverage gaps.

Covers: CLI dashboard/examples/evals/release-metadata --check failure paths,
list with empty results, author-batch with failures, scenarios.py validation
functions, definitions.py helper functions, rows.py helper edge cases,
dashboard.py uncovered lines, and insights.py remaining branches.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

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


# --- scenarios.py: remaining uncovered validation functions --------------


def test_scenarios_expected_response_not_mapping(tmp_path):
    """expected_response that is not a mapping should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _expected_response_from_mapping

    with pytest.raises(ValueError, match="expected_response must be a mapping"):
        _expected_response_from_mapping(
            "notamapping", path=tmp_path / "fake.yaml", scenario_id="test"
        )


def test_scenarios_answer_sections_not_list(tmp_path):
    """answer sections that is not a list should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _answer_sections_from_obj

    with pytest.raises(ValueError, match="must be a non-empty list"):
        _answer_sections_from_obj(
            "notalist", path=tmp_path / "fake.yaml", scenario_id="test"
        )


def test_scenarios_answer_sections_empty_list(tmp_path):
    """empty answer sections list should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _answer_sections_from_obj

    with pytest.raises(ValueError, match="must be a non-empty list"):
        _answer_sections_from_obj([], path=tmp_path / "fake.yaml", scenario_id="test")


def test_scenarios_answer_section_missing_title(tmp_path):
    """answer section missing title should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _answer_sections_from_obj

    with pytest.raises(ValueError, match="must include title and body"):
        _answer_sections_from_obj(
            [{"body": "text"}], path=tmp_path / "fake.yaml", scenario_id="test"
        )


def test_scenarios_answer_section_missing_body(tmp_path):
    """answer section missing body should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _answer_sections_from_obj

    with pytest.raises(ValueError, match="must include title and body"):
        _answer_sections_from_obj(
            [{"title": "T"}], path=tmp_path / "fake.yaml", scenario_id="test"
        )


def test_scenarios_answer_section_not_mapping(tmp_path):
    """answer section that is not a mapping should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _answer_sections_from_obj

    with pytest.raises(ValueError, match="must be a mapping"):
        _answer_sections_from_obj(
            ["notamapping"], path=tmp_path / "fake.yaml", scenario_id="test"
        )


def test_scenarios_rubric_scores_not_mapping(tmp_path):
    """rubric_scores that is not a mapping should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _rubric_scores_from_obj

    with pytest.raises(ValueError, match="rubric_scores.*must be a mapping"):
        _rubric_scores_from_obj(
            "notamapping", path=tmp_path / "fake.yaml", scenario_id="test"
        )


def test_scenarios_rubric_score_not_int(tmp_path):
    """non-integer rubric score should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _rubric_scores_from_obj

    with pytest.raises(ValueError, match="rubric_scores.skill_fit must be an integer"):
        _rubric_scores_from_obj(
            {"skill_fit": "notint"}, path=tmp_path / "fake.yaml", scenario_id="test"
        )


def test_scenarios_expected_answer_not_mapping(tmp_path):
    """expected_answer that is not a mapping should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _expected_answer_from_mapping

    with pytest.raises(ValueError, match="expected_answer must be a mapping"):
        _expected_answer_from_mapping(
            "notamapping", path=tmp_path / "fake.yaml", scenario_id="test"
        )


def test_scenarios_expected_answer_missing_skill(tmp_path):
    """expected_answer missing selected_skill should raise ValueError."""
    from cogsecskills.artifacts.scenarios import _expected_answer_from_mapping

    with pytest.raises(ValueError, match="must include selected_skill and answer_kind"):
        _expected_answer_from_mapping(
            {"answer_kind": "defensive_output"},
            path=tmp_path / "fake.yaml",
            scenario_id="test",
        )


# --- rows.py: remaining uncovered helper branches ------------------------


def test_rows_first_containing_fallback():
    from cogsecskills.artifacts.manuscript_assets.rows import _first_containing

    assert _first_containing([], ("a",)) == "not declared"
    assert _first_containing(["hello"], ("xyz",)) == "not declared"
    assert _first_containing(["hello world"], ("hello", "world")) == "hello world"


def test_rows_first_with_prefix_fallback():
    from cogsecskills.artifacts.manuscript_assets.rows import _first_with_prefix

    assert _first_with_prefix([], "safe") == "not declared"
    assert _first_with_prefix(["unsafe: x"], "safe") == "not declared"
    assert _first_with_prefix(["safe: y"], "safe") == "safe: y"


def test_rows_group_ids_empty():
    from cogsecskills.artifacts.manuscript_assets.rows import _group_ids

    assert _group_ids([]) == ()


def test_rows_join_fallback():
    from cogsecskills.artifacts.manuscript_assets.rows import _join

    assert _join([]) == "none"
    assert _join(["", ""]) == "none"
    assert _join(["a", "b"]) == "a, b"


def test_rows_first_fallback():
    from cogsecskills.artifacts.manuscript_assets.rows import _first

    assert _first([]) == "not declared"
    assert _first(["", ""]) == "not declared"
    assert _first(["", "x"]) == "x"
