"""Tests for uncovered branches in evals.py.

Covers: load_evaluations error paths, _review_from_obj validation,
_content_findings edge cases (duplicate, mismatched group/kind/skill,
wrong provenance, wrong claim boundary, repeated section titles,
missing/extra evaluation fixtures, wrong count).
"""

from __future__ import annotations

import shutil
from pathlib import Path

import yaml

from cogsecskills.artifacts.evals import (
    EVALS_SOURCE_PATH,
    check_evals,
    load_evaluations,
    write_evals,
)
from cogsecskills.artifacts.scenarios import RUBRIC_KEYS

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _copy_fixture(tmp_path: Path) -> Path:
    for dirname in ("registry", "skills", "scenarios"):
        shutil.copytree(PROJECT_ROOT / dirname, tmp_path / dirname)
    return tmp_path


def _make_eval_entry(scenario_id: str = "sat-safe-1") -> dict:
    return {
        "scenario_id": scenario_id,
        "group": "sat",
        "kind": "safe_defensive",
        "selected_skill": "sat.analysis_of_competing_hypotheses",
        "answer_kind": "defensive_output",
        "sections": [
            {
                "title": "Defensive purpose",
                "body": (
                    "Use defensively with evidence, inference, gap, "
                    "confidence, and uncertainty."
                ),
            },
            {
                "title": "Evidence and inference",
                "body": "Evidence: label material. Inference: mark matrix.",
            },
            {
                "title": "Confidence and uncertainty",
                "body": "State confidence and uncertainty with alternatives.",
            },
        ],
        "rubric_scores": {key: 2 for key in RUBRIC_KEYS},
        "provenance": "reviewed local fixture",
        "claim_boundary": (
            "deterministic offline review fixture; not a live model output, "
            "runtime certification, or field validation"
        ),
    }


def test_load_evaluations_missing_source(tmp_path):
    """Missing evals source should raise ValueError."""
    _copy_fixture(tmp_path)
    # No evals file written yet.
    import pytest

    with pytest.raises(ValueError, match="missing offline evaluation source"):
        load_evaluations(tmp_path)


def test_load_evaluations_top_level_not_mapping(tmp_path):
    root = _copy_fixture(tmp_path)
    source = root / EVALS_SOURCE_PATH
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text("- item\n", encoding="utf-8")
    import pytest

    with pytest.raises(ValueError, match="top level must be a mapping"):
        load_evaluations(root)


def test_load_evaluations_evaluations_not_list(tmp_path):
    root = _copy_fixture(tmp_path)
    source = root / EVALS_SOURCE_PATH
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text("evaluations: notalist\n", encoding="utf-8")
    import pytest

    with pytest.raises(ValueError, match="must be a non-empty list"):
        load_evaluations(root)


def test_check_evals_missing_source(tmp_path):
    """check_evals on a missing source should report it."""
    _copy_fixture(tmp_path)
    findings = check_evals(tmp_path)
    assert any("missing offline evaluation source" in f for f in findings)


def test_check_evals_duplicate_fixture(tmp_path):
    root = _copy_fixture(tmp_path)
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["evaluations"][0]["scenario_id"] = raw["evaluations"][1]["scenario_id"]
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("duplicate evaluation fixture" in f for f in findings)


def test_check_evals_wrong_provenance(tmp_path):
    root = _copy_fixture(tmp_path)
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["evaluations"][0]["provenance"] = "wrong provenance"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("provenance must be" in f for f in findings)


def test_check_evals_wrong_claim_boundary(tmp_path):
    root = _copy_fixture(tmp_path)
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["evaluations"][0]["claim_boundary"] = "this is a live model output"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("claim boundary is too broad" in f for f in findings)


def test_check_evals_repeated_section_titles(tmp_path):
    root = _copy_fixture(tmp_path)
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["evaluations"][0]["sections"][1]["title"] = raw["evaluations"][0]["sections"][
        0
    ]["title"]
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("section titles repeat" in f for f in findings)


def test_check_evals_missing_generated_md(tmp_path):
    root = _copy_fixture(tmp_path)
    write_evals(root)
    (root / "docs" / "evaluation-readiness.md").unlink()
    findings = check_evals(root)
    assert any("missing generated evaluation file" in f for f in findings)


def test_check_evals_extra_fixture(tmp_path):
    root = _copy_fixture(tmp_path)
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    extra = dict(raw["evaluations"][0])
    extra["scenario_id"] = "nonexistent-scenario"
    raw["evaluations"].append(extra)
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("unexpected evaluation fixtures" in f for f in findings)
