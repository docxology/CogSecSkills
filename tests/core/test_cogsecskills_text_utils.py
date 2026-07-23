"""Tests for shared text utilities."""

from __future__ import annotations

import pytest

from cogsecskills.core.text_utils import as_text, clean_cell


def test_clean_cell_collapses_whitespace():
    assert clean_cell("  hello   world  ") == "hello world"


def test_clean_cell_escapes_pipe():
    assert clean_cell("a|b") == "a\\|b"


def test_clean_cell_non_string():
    assert clean_cell(42) == "42"
    assert clean_cell(None) == "None"


def test_clean_cell_empty():
    assert clean_cell("") == ""


def test_as_text_valid_string():
    from pathlib import Path

    assert as_text("hello", field="test", path=Path("/fake")) == "hello"


def test_as_text_strips_whitespace():
    from pathlib import Path

    assert as_text("  hello  ", field="test", path=Path("/fake")) == "hello"


def test_as_text_empty_raises():
    from pathlib import Path

    with pytest.raises(ValueError, match="must be a non-empty string"):
        as_text("", field="test", path=Path("/fake"))


def test_as_text_whitespace_only_raises():
    from pathlib import Path

    with pytest.raises(ValueError, match="must be a non-empty string"):
        as_text("   ", field="test", path=Path("/fake"))


def test_as_text_non_string_raises():
    from pathlib import Path

    with pytest.raises(ValueError, match="must be a non-empty string"):
        as_text(42, field="test", path=Path("/fake"))


def test_as_text_none_raises():
    from pathlib import Path

    with pytest.raises(ValueError, match="must be a non-empty string"):
        as_text(None, field="test", path=Path("/fake"))
