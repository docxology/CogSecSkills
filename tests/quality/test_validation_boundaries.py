"""Validation keeps companion reads inside the declared skill directory."""

from __future__ import annotations

from pathlib import Path

import pytest

from cogsecskills.authoring.scaffold import scaffold_skill
from cogsecskills.core.loader import load_skill
from cogsecskills.quality.validate import validate_skill


def _skill(root: Path):
    (root / "registry").mkdir()
    (root / "registry" / "skills.yaml").write_text(
        "skills: [{id: sat.demo, name: Demo, group: sat, summary: Summary}]\n",
        encoding="utf-8",
    )
    scaffold_skill("sat.demo", root)
    directory = root / "skills" / "sat" / "demo"
    return directory, load_skill(directory / "skill.yaml")


@pytest.mark.parametrize("relative", ["SKILL.md", "workflow.md", "harness/codex.md"])
def test_external_companion_symlinks_are_validation_errors(tmp_path, relative):
    directory, spec = _skill(tmp_path)
    external = tmp_path / "private.md"
    external.write_text("| `read` | private | private |", encoding="utf-8")
    companion = directory / relative
    companion.unlink()
    companion.symlink_to(external)
    result = validate_skill(spec, directory)
    assert not result.ok
    assert any(
        "must stay inside the skill directory" in item.message for item in result.errors
    )


@pytest.mark.parametrize("relative", ["workflow.md", "harness/codex.md"])
def test_invalid_utf8_companion_is_an_unreadable_error(tmp_path, relative):
    directory, spec = _skill(tmp_path)
    (directory / relative).write_bytes(b"\xff")
    result = validate_skill(spec, directory)
    assert any("unreadable" in item.message for item in result.errors)


def test_internal_companion_symlink_is_valid(tmp_path):
    directory, spec = _skill(tmp_path)
    workflow = directory / "workflow.md"
    actual = directory / "procedure.md"
    workflow.rename(actual)
    workflow.symlink_to(actual)
    assert validate_skill(spec, directory).ok
