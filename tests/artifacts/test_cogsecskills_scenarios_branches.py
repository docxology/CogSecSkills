"""Tests for uncovered branches in scenarios.py.

Covers: load_scenarios error paths, _scenario_from_mapping validation,
_as_text_list edge cases, duplicate scenario ids, unknown groups,
missing scenario files, malformed expected_response/expected_answer.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from cogsecskills.artifacts.scenarios import (
    _as_text_list,
    check_scenarios,
    load_scenarios,
    scenario_path,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_as_text_list_none():
    assert _as_text_list(None, field="test") == ()


def test_as_text_list_empty_string():
    assert _as_text_list("", field="test") == ()


def test_as_text_list_string():
    assert _as_text_list("hello", field="test") == ("hello",)


def test_as_text_list_list():
    assert _as_text_list(["a", "b", "  "], field="test") == ("a", "b")


def test_as_text_list_mapping_raises():
    with pytest.raises(ValueError, match="must be a string or list"):
        _as_text_list({"key": "val"}, field="test")


def test_as_text_list_int_raises():
    with pytest.raises(ValueError, match="must be a string or list"):
        _as_text_list(42, field="test")


def test_scenario_path_returns_expected():
    """scenario_path returns the canonical fixture path."""
    assert scenario_path() == scenario_path(None)


def test_load_scenarios_missing_file(tmp_path):
    with pytest.raises(ValueError, match="missing scenario fixture"):
        load_scenarios(tmp_path)


def test_load_scenarios_top_level_not_mapping(tmp_path):
    (tmp_path / "scenarios").mkdir()
    (tmp_path / "scenarios" / "defensive_readiness.yaml").write_text(
        "- item\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="top level must be a mapping"):
        load_scenarios(tmp_path)


def test_load_scenarios_scenarios_not_list(tmp_path):
    (tmp_path / "scenarios").mkdir()
    (tmp_path / "scenarios" / "defensive_readiness.yaml").write_text(
        "scenarios: notalist\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="must be a non-empty list"):
        load_scenarios(tmp_path)


def test_load_scenarios_entry_not_mapping(tmp_path):
    (tmp_path / "scenarios").mkdir()
    (tmp_path / "scenarios" / "defensive_readiness.yaml").write_text(
        "scenarios:\n  - justastring\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="scenario entry must be a mapping"):
        load_scenarios(tmp_path)


def test_load_scenarios_missing_required_fields(tmp_path):
    (tmp_path / "scenarios").mkdir()
    (tmp_path / "scenarios" / "defensive_readiness.yaml").write_text(
        "scenarios:\n  - {id: test}\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="missing required fields"):
        load_scenarios(tmp_path)


def test_load_scenarios_invalid_kind(tmp_path):
    (tmp_path / "scenarios").mkdir()
    (tmp_path / "scenarios" / "defensive_readiness.yaml").write_text(
        "scenarios:\n  - {id: test, group: sat, kind: bogus, "
        "query: q, expected_skill: sat.x}\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="kind 'bogus' must be one of"):
        load_scenarios(tmp_path)


def test_check_scenarios_missing_fixture(tmp_path):
    findings = check_scenarios(tmp_path)
    assert len(findings) == 1
    assert "missing scenario fixture" in findings[0]


def test_check_scenarios_duplicate_id(tmp_path):
    """Duplicate scenario ids should be flagged."""

    # Build two scenarios with the same id
    raw = {
        "id": "dup",
        "group": "sat",
        "kind": "safe_defensive",
        "query": "defensive use",
        "expected_skill": "sat.x",
        "expected_output_terms": ["product"],
        "required_quality_terms": ["evidence"],
        "expected_response": {
            "required_sections": ["s1", "s2", "s3"],
            "must_include_terms": [
                "evidence",
                "confidence",
                "uncertainty",
                "defensive",
            ],
            "must_exclude_terms": ["x", "y"],
        },
        "expected_answer": {
            "selected_skill": "sat.x",
            "answer_kind": "defensive_output",
            "sections": [
                {
                    "title": "A",
                    "body": "evidence inference gap confidence uncertainty defensive",
                },
                {"title": "B", "body": "evidence"},
                {"title": "C", "body": "evidence"},
            ],
            "rubric_scores": {
                k: 2
                for k in (
                    "skill_fit",
                    "evidence_labeling",
                    "uncertainty",
                    "defensive_boundary",
                    "output_usefulness",
                )
            },
        },
    }
    path = tmp_path / "scenarios" / "defensive_readiness.yaml"
    path.parent.mkdir(parents=True)
    # We need a minimal registry for check_scenarios to work
    (tmp_path / "registry").mkdir()
    (tmp_path / "registry" / "skills.yaml").write_text(
        "skills:\n  - {id: sat.x, name: X, group: sat, status: implemented, "
        "summary: s}\n",
        encoding="utf-8",
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    yaml_data = {"scenarios": [raw, dict(raw)]}
    path.write_text(yaml.safe_dump(yaml_data, sort_keys=False), encoding="utf-8")
    findings = check_scenarios(tmp_path)
    assert any("duplicate scenario id" in f for f in findings)


def _seed_minimal(root: Path, groups: list[tuple[str, str]] | None = None) -> None:
    """Seed a minimal registry for scenario tests."""
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n  - {id: sat.x, name: X, group: sat, status: implemented, summary: s}\n",
        encoding="utf-8",
    )
    gs = groups or [("sat", "SAT")]
    lines = ["groups:"]
    for gid, title in gs:
        lines.append(f"  - {{id: {gid}, title: {title}}}")
    (root / "registry" / "groups.yaml").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def _make_safe_scenario(
    scenario_id: str = "test-safe",
    group: str = "sat",
    query: str = "defensive use with evidence",
) -> dict:
    return {
        "id": scenario_id,
        "group": group,
        "kind": "safe_defensive",
        "query": query,
        "expected_skill": "sat.x",
        "expected_output_terms": ["product"],
        "required_quality_terms": ["evidence"],
        "expected_response": {
            "required_sections": ["s1", "s2", "s3"],
            "must_include_terms": [
                "evidence",
                "confidence",
                "uncertainty",
                "defensive",
            ],
            "must_exclude_terms": ["x", "y"],
        },
        "expected_answer": {
            "selected_skill": "sat.x",
            "answer_kind": "defensive_output",
            "sections": [
                {
                    "title": "A",
                    "body": "evidence inference gap confidence uncertainty defensive",
                },
                {"title": "B", "body": "evidence"},
                {"title": "C", "body": "evidence"},
            ],
            "rubric_scores": {
                k: 2
                for k in (
                    "skill_fit",
                    "evidence_labeling",
                    "uncertainty",
                    "defensive_boundary",
                    "output_usefulness",
                )
            },
        },
    }


def _write_scenarios(root: Path, scenarios: list[dict]) -> None:
    (root / "scenarios").mkdir(parents=True, exist_ok=True)
    data = {"scenarios": scenarios}
    (root / "scenarios" / "defensive_readiness.yaml").write_text(
        yaml.safe_dump(data, sort_keys=False), encoding="utf-8"
    )


def test_check_scenarios_unknown_group(tmp_path):
    """Scenarios with an unknown group should be flagged."""
    _seed_minimal(tmp_path, [("sat", "SAT"), ("cog", "COG")])
    sc = _make_safe_scenario(group="nonexistent")
    _write_scenarios(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("unknown group" in f for f in findings)


def test_check_scenarios_missing_kind_per_group(tmp_path):
    """Missing scenario kinds per group should be flagged."""
    _seed_minimal(tmp_path, [("sat", "SAT"), ("cog", "COG")])
    sc = _make_safe_scenario()
    _write_scenarios(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("cog: missing safe_defensive scenario" in f for f in findings)
    assert any("cog: missing unsafe_redirect scenario" in f for f in findings)
    assert any("sat: missing unsafe_redirect scenario" in f for f in findings)


def test_check_scenarios_safe_without_defensive_keyword(tmp_path):
    """A safe scenario that doesn't mention defensive/authorized should be flagged."""
    _seed_minimal(tmp_path)
    sc = _make_safe_scenario(query="use this skill to analyze stuff")
    _write_scenarios(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("must name defensive or authorized use" in f for f in findings)


def test_check_scenarios_unsafe_without_redirect_keyword(tmp_path):
    """An unsafe scenario missing redirect/refuse should be flagged."""
    _seed_minimal(tmp_path)
    sc = _make_safe_scenario()
    sc["kind"] = "unsafe_redirect"
    sc["query"] = "unsafe misuse probe: force a conclusion"
    sc["expected_response"]["required_sections"] = [
        "Refusal and redirect",
        "Safe alternative",
        "Evidence",
        "Confidence",
    ]
    sc["expected_response"]["must_include_terms"] = [
        "refuse",
        "redirect",
        "safe",
        "evidence",
        "confidence",
        "uncertainty",
    ]
    sc["expected_answer"]["answer_kind"] = "refusal_redirect"
    sc["expected_answer"]["sections"][0]["body"] = (
        "refuse redirect safe evidence inference gap confidence uncertainty"
    )
    _write_scenarios(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("must request refusal or redirect handling" in f for f in findings)


def test_check_scenarios_expected_response_too_few_sections(tmp_path):
    """Expected response with fewer than 3 sections should be flagged."""
    _seed_minimal(tmp_path)
    sc = _make_safe_scenario()
    sc["expected_response"]["required_sections"] = ["s1", "s2"]
    _write_scenarios(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("must declare at least 3 sections" in f for f in findings)


def test_check_scenarios_expected_response_too_few_include_terms(tmp_path):
    """Expected response with fewer than 4 include terms should be flagged."""
    _seed_minimal(tmp_path)
    sc = _make_safe_scenario()
    sc["expected_response"]["must_include_terms"] = ["evidence", "confidence"]
    _write_scenarios(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("must declare at least 4 include terms" in f for f in findings)


def test_check_scenarios_expected_response_too_few_exclude_terms(tmp_path):
    """Expected response with fewer than 2 exclude terms should be flagged."""
    _seed_minimal(tmp_path)
    sc = _make_safe_scenario()
    sc["expected_response"]["must_exclude_terms"] = ["x"]
    _write_scenarios(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("must declare at least 2 exclude terms" in f for f in findings)


def test_check_scenarios_expected_response_repeated_sections(tmp_path):
    """Expected response with repeated section labels should be flagged."""
    _seed_minimal(tmp_path)
    sc = _make_safe_scenario()
    sc["expected_response"]["required_sections"] = ["s1", "s1", "s3"]
    _write_scenarios(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("repeats section labels" in f for f in findings)
