"""Shared real inputs for validation artifact sources tests."""

from __future__ import annotations

import shutil

from pathlib import Path

import pytest

import yaml

from cogsecskills.core.spec import SkillSpec, SkillTool, ToolVerb

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _spec_with_harness_path(skills_dir, declared_path: str) -> SkillSpec:
    """Build a minimal spec whose claude adapter points at ``declared_path``."""
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        f"harness:\n  claude: {declared_path}\n",
        encoding="utf-8",
    )
    return SkillSpec.from_mapping(
        yaml.safe_load((skills_dir / "skill.yaml").read_text(encoding="utf-8"))
    )


__all__ = [
    "PROJECT_ROOT",
    "SkillSpec",
    "SkillTool",
    "ToolVerb",
    "_spec_with_harness_path",
    "pytest",
    "shutil",
    "yaml",
]
