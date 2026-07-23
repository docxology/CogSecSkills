"""Tests for uncovered branches in examples.py.

Covers: load_examples error paths, _example_from_obj validation,
_content_findings edge cases (duplicate, missing from registry,
wrong provenance, repeated titles, missing output name, missing/extra skills).
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml

from cogsecskills.artifacts.examples import (
    EXAMPLES_SOURCE_PATH,
    check_examples,
    load_examples,
    write_examples,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _copy_fixture(tmp_path: Path) -> Path:
    """Copy registry, skills, and examples for full-fixture tests."""
    for dirname in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / dirname, tmp_path / dirname)
    return tmp_path


def _copy_fixture_no_examples(tmp_path: Path) -> Path:
    """Copy registry and skills but NOT examples."""
    for dirname in ("registry", "skills"):
        shutil.copytree(PROJECT_ROOT / dirname, tmp_path / dirname)
    return tmp_path


def test_load_examples_missing_source(tmp_path):
    _copy_fixture_no_examples(tmp_path)
    with pytest.raises(ValueError, match="missing worked examples source"):
        load_examples(tmp_path)


def test_load_examples_top_level_not_mapping(tmp_path):
    root = _copy_fixture(tmp_path)
    (root / EXAMPLES_SOURCE_PATH).write_text("- item\n", encoding="utf-8")
    with pytest.raises(ValueError, match="top level must be a mapping"):
        load_examples(root)


def test_load_examples_examples_not_list(tmp_path):
    root = _copy_fixture(tmp_path)
    (root / EXAMPLES_SOURCE_PATH).write_text("examples: notalist\n", encoding="utf-8")
    with pytest.raises(ValueError, match="must be a non-empty list"):
        load_examples(root)


def test_check_examples_duplicate(tmp_path):
    root = _copy_fixture(tmp_path)
    write_examples(root)
    source = root / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["skill_id"] = raw["examples"][1]["skill_id"]
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_examples(root)
    assert any("duplicate worked example" in f for f in findings)


def test_check_examples_wrong_provenance(tmp_path):
    root = _copy_fixture(tmp_path)
    write_examples(root)
    source = root / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["provenance"] = "wrong"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_examples(root)
    assert any("provenance must be" in f for f in findings)


def test_check_examples_repeated_section_titles(tmp_path):
    root = _copy_fixture(tmp_path)
    write_examples(root)
    source = root / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["sections"][1]["title"] = raw["examples"][0]["sections"][0][
        "title"
    ]
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_examples(root)
    assert any("repeats section titles" in f for f in findings)


def test_check_examples_missing_generated_json(tmp_path):
    root = _copy_fixture(tmp_path)
    write_examples(root)
    (root / "output" / "data" / "skill_worked_examples.json").unlink()
    findings = check_examples(root)
    assert any("missing generated examples file" in f for f in findings)


def test_check_examples_extra_skill_not_in_registry(tmp_path):
    root = _copy_fixture(tmp_path)
    write_examples(root)
    source = root / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    extra = dict(raw["examples"][0])
    extra["skill_id"] = "sat.nonexistent_skill"
    raw["examples"].append(extra)
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_examples(root)
    assert any("not present in registry" in f for f in findings)
