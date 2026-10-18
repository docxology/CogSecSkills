"""Behavioral artifacts failures using real source inputs."""

from __future__ import annotations


from tests._support.cli_artifact_inputs import (
    _VALID_SCENARIO,
    _seed_registry,
    _write_scenario_fixture,
    copy,
    pytest,
    re,
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
            "rubric_scores must be an empty mapping",
        ),
        (
            "expected_answer.rubric_scores",
            {"skill_fit": "notint"},
            "cannot carry rubric scores",
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
