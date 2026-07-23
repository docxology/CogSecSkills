"""Tests for project-root location and shared quality constants."""

from __future__ import annotations

import pytest

from cogsecskills.core.locate import project_root
from cogsecskills.core.quality_constants import (
    ALLOWED_SHARED_QUALITY_ITEMS,
    GENERIC_NEGATIVE_CONTROL_PHRASES,
    QUALITY_FIELD_NAMES,
    QUALITY_SPECIFICITY_FIELDS,
    REUSED_QUALITY_FIELDS,
    SENSITIVE_GROUPS,
    SENSITIVE_TERMS,
    normalize_quality_item,
)


# ---------------------------------------------------------------------------
# locate.py
# ---------------------------------------------------------------------------


def test_project_root_finds_sentinel():
    """project_root() finds the real project root by walking up to the sentinel."""
    root = project_root()
    assert (root / "registry" / "skills.yaml").is_file()
    assert (root / "pyproject.toml").is_file()


def test_project_root_is_absolute_and_resolved():
    root = project_root()
    assert root.is_absolute()
    assert root == root.resolve()


def test_project_root_outside_tree_raises(tmp_path):
    """If we monkeypatch __file__ to a location outside any project tree,
    the function should raise RuntimeError."""
    from cogsecskills.core import locate

    original_file = locate.__file__
    fake_file = tmp_path / "fake_module.py"
    fake_file.write_text("# placeholder", encoding="utf-8")
    try:
        locate.__file__ = str(fake_file)
        with pytest.raises(RuntimeError, match="could not locate"):
            locate.project_root()
    finally:
        locate.__file__ = original_file


# ---------------------------------------------------------------------------
# quality_constants.py
# ---------------------------------------------------------------------------


def test_quality_field_names_complete():
    """All 8 quality fields are present."""
    assert len(QUALITY_FIELD_NAMES) == 8
    for name in QUALITY_FIELD_NAMES:
        assert isinstance(name, str)
        assert name.islower()


def test_generic_negative_control_phrases_non_empty():
    assert len(GENERIC_NEGATIVE_CONTROL_PHRASES) >= 1


def test_quality_specificity_fields_subset_of_quality_fields():
    assert set(QUALITY_SPECIFICITY_FIELDS).issubset(set(QUALITY_FIELD_NAMES))


def test_reused_quality_fields_subset_of_quality_fields():
    assert set(REUSED_QUALITY_FIELDS).issubset(set(QUALITY_FIELD_NAMES))


def test_allowed_shared_quality_items_keys_match_reused():
    assert set(ALLOWED_SHARED_QUALITY_ITEMS) == set(REUSED_QUALITY_FIELDS)


def test_sensitive_groups_is_frozen():
    assert isinstance(SENSITIVE_GROUPS, frozenset)


def test_sensitive_terms_non_empty():
    assert len(SENSITIVE_TERMS) >= 1


def test_normalize_quality_item_lowercases_and_collapses_whitespace():
    assert normalize_quality_item("  Hello   World  ") == "hello world"
    assert normalize_quality_item("MixedCase") == "mixedcase"
    assert normalize_quality_item("tabs\there") == "tabs here"


def test_normalize_quality_item_non_string():
    assert normalize_quality_item(42) == "42"
    assert normalize_quality_item(None) == "none"


def test_sensitive_groups_contents():
    expected = {
        "cognitive_security",
        "counterintelligence",
        "information_environment",
        "osint_integrity",
    }
    assert SENSITIVE_GROUPS == expected
