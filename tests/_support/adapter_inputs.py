"""Shared real inputs for adapter inputs tests."""

from __future__ import annotations

from pathlib import Path

import pytest

import yaml

from cogsecskills.core.spec import SkillSpec, ToolVerb


def _make_spec(skills_dir: Path) -> SkillSpec:
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n  codex: harness/codex.md\n  hermes: harness/hermes.md\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# Demo\n", encoding="utf-8")
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nText.\n", encoding="utf-8"
    )
    harness_dir = skills_dir / "harness"
    harness_dir.mkdir()
    for h in ("claude", "codex", "hermes"):
        (harness_dir / f"{h}.md").write_text(
            "| `read` | tool | note |\n", encoding="utf-8"
        )
    return SkillSpec.from_mapping(
        yaml.safe_load((skills_dir / "skill.yaml").read_text(encoding="utf-8"))
    )


__all__ = ["ToolVerb", "_make_spec", "pytest"]
