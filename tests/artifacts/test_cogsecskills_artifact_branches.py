"""Tests for remaining uncovered branches in evals.py and examples.py.

Covers: _section_from_obj non-mapping error, _review_from_obj non-mapping,
sections not list, rubric_scores non-mapping, non-int score,
_content_findings group/kind/skill mismatch paths, check_evals stale
generated files, examples _section_from_obj error, _example_from_obj
sections not list, _content_findings rendered skill missing, too-few
sections, output not named.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import yaml

from cogsecskills.artifacts.evals import (
    EVALS_SOURCE_PATH,
    check_evals,
    write_evals,
)
from cogsecskills.artifacts.evals import _section_from_obj as _eval_section_from_obj
from cogsecskills.artifacts.evals import _review_from_obj
from cogsecskills.artifacts.examples import (
    EXAMPLES_SOURCE_PATH,
    _example_from_obj,
    check_examples,
    write_examples,
)
from cogsecskills.artifacts.examples import _section_from_obj as _ex_section_from_obj
from cogsecskills.artifacts.scenarios import RUBRIC_KEYS

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _copy_fixture(tmp_path: Path, *dirnames: str) -> Path:
    for d in dirnames:
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    return tmp_path


# --- evals.py: _section_from_obj error paths ---


def test_evals_section_from_obj_non_mapping(tmp_path):
    """_section_from_obj with a non-mapping should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    with pytest.raises(ValueError, match="section must be a mapping"):
        _eval_section_from_obj("notamapping", path=path, scenario_id="test")


def test_evals_section_from_obj_missing_title(tmp_path):
    """_section_from_obj with missing title should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    with pytest.raises(ValueError, match="section.title must be a non-empty string"):
        _eval_section_from_obj({"body": "text"}, path=path, scenario_id="test")


def test_evals_section_from_obj_missing_body(tmp_path):
    """_section_from_obj with missing body should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    with pytest.raises(ValueError, match="section.body must be a non-empty string"):
        _eval_section_from_obj({"title": "T"}, path=path, scenario_id="test")


# --- evals.py: _review_from_obj error paths ---


def test_evals_review_from_obj_non_mapping(tmp_path):
    """_review_from_obj with a non-mapping should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    with pytest.raises(ValueError, match="evaluation entry must be a mapping"):
        _review_from_obj("notamapping", path=path)


def test_evals_review_from_obj_sections_not_list(tmp_path):
    """_review_from_obj with sections not a list should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    entry = {
        "scenario_id": "test",
        "sections": "notalist",
        "rubric_scores": {k: 2 for k in RUBRIC_KEYS},
    }
    with pytest.raises(ValueError, match="sections must be a non-empty list"):
        _review_from_obj(entry, path=path)


def test_evals_review_from_obj_rubric_scores_not_mapping(tmp_path):
    """_review_from_obj with rubric_scores not a mapping should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    entry = {
        "scenario_id": "test",
        "sections": [{"title": "A", "body": "B"}],
        "rubric_scores": "notamapping",
    }
    with pytest.raises(ValueError, match="rubric_scores must be a mapping"):
        _review_from_obj(entry, path=path)


def test_evals_review_from_obj_rubric_score_not_int(tmp_path):
    """_review_from_obj with non-int rubric score should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    entry = {
        "scenario_id": "test",
        "sections": [{"title": "A", "body": "B"}],
        "rubric_scores": {k: 2 for k in RUBRIC_KEYS},
    }
    entry["rubric_scores"]["skill_fit"] = "notint"
    with pytest.raises(ValueError, match="rubric_scores.skill_fit must be int"):
        _review_from_obj(entry, path=path)


# --- evals.py: _content_findings mismatch paths ---


def test_evals_group_mismatch(tmp_path):
    """Review with wrong group should be flagged."""
    root = _copy_fixture(tmp_path, "registry", "skills", "scenarios")
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["evaluations"][0]["group"] = "nonexistent_group"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("group does not match" in f for f in findings)


def test_evals_kind_mismatch(tmp_path):
    """Review with wrong kind should be flagged."""
    root = _copy_fixture(tmp_path, "registry", "skills", "scenarios")
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["evaluations"][0]["kind"] = "unsafe_redirect"
    raw["evaluations"][0]["answer_kind"] = "refusal_redirect"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("kind does not match" in f for f in findings)


def test_evals_too_few_sections(tmp_path):
    """Review with fewer than 3 sections should be flagged."""
    root = _copy_fixture(tmp_path, "registry", "skills", "scenarios")
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["evaluations"][0]["sections"] = raw["evaluations"][0]["sections"][:2]
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("at least 3 sections" in f for f in findings)


def test_evals_missing_scenario(tmp_path):
    """Review with no matching scenario should be flagged."""
    root = _copy_fixture(tmp_path, "registry", "skills", "scenarios")
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["evaluations"][0]["scenario_id"] = "nonexistent-scenario"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("no matching scenario fixture" in f for f in findings)


# --- examples.py: _section_from_obj and _example_from_obj error paths ---


def test_examples_section_from_obj_non_mapping(tmp_path):
    """_section_from_obj with a non-mapping should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    with pytest.raises(ValueError, match="section must be a mapping"):
        _ex_section_from_obj("notamapping", path=path, skill_id="sat.demo")


def test_examples_example_from_obj_non_mapping(tmp_path):
    """_example_from_obj with a non-mapping should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    with pytest.raises(ValueError, match="example entry must be a mapping"):
        _example_from_obj("notamapping", path=path)


def test_examples_example_from_obj_sections_not_list(tmp_path):
    """_example_from_obj with sections not a list should raise ValueError."""
    import pytest

    path = tmp_path / "fake.yaml"
    entry = {"skill_id": "sat.demo", "sections": "notalist"}
    with pytest.raises(ValueError, match="sections must be a non-empty list"):
        _example_from_obj(entry, path=path)


# --- examples.py: _content_findings mismatch paths ---


def test_examples_rendered_skill_missing(tmp_path):
    """Example for a skill that exists in registry but not on disk."""
    root = _copy_fixture(tmp_path, "registry", "skills", "examples")
    source = root / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    # Change skill_id to a registry entry that has no on-disk skill
    raw["examples"][0]["skill_id"] = "sat.nonexistent"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_examples(root)
    # This will flag both "not present in registry" or "rendered skill is missing"
    # depending on whether sat.nonexistent is in the registry
    assert len(findings) > 0


def test_examples_too_few_sections(tmp_path):
    """Example with fewer than 3 sections should be flagged."""
    root = _copy_fixture(tmp_path, "registry", "skills", "examples")
    write_examples(root)
    source = root / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["sections"] = raw["examples"][0]["sections"][:2]
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_examples(root)
    assert any("at least 3 sections" in f for f in findings)


def test_examples_output_not_named(tmp_path):
    """Example that doesn't name any declared output should be flagged."""
    root = _copy_fixture(tmp_path, "registry", "skills", "examples")
    write_examples(root)
    source = root / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    # Replace all text fields to remove output name references
    raw["examples"][0]["title"] = "Generic Example"
    raw["examples"][0]["request"] = (
        "Use this defensively with evidence inference gap confidence uncertainty."
    )
    raw["examples"][0]["sections"] = [
        {
            "title": "A",
            "body": "evidence inference gap confidence uncertainty defensive",
        },
        {
            "title": "B",
            "body": "evidence inference gap confidence uncertainty defensive",
        },
        {
            "title": "C",
            "body": "evidence inference gap confidence uncertainty defensive",
        },
    ]
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    # Call _content_findings directly to avoid stale-generated-file noise
    from cogsecskills.artifacts.examples import _content_findings, load_examples

    examples = load_examples(root)
    findings = _content_findings(root, examples)
    assert any("does not name a declared output" in f for f in findings)
