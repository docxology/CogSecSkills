"""Tests for on-disk discovery and the registry catalogue.

Uses real temp directories (tmp_path) with hand-written YAML — no mocks.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from cogsecskills.loader import discover_skills, load_skill, skill_dir, skills_root
from cogsecskills.registry import (
    RegistryEntry,
    load_registry,
    registry_path,
)
from cogsecskills.spec import SpecError


def _write_skill(
    root: Path,
    group: str,
    slug: str,
    *,
    status: str = "implemented",
    with_tools: bool = True,
) -> Path:
    d = root / "skills" / group / slug
    (d / "harness").mkdir(parents=True, exist_ok=True)
    lines = [
        f"id: {group}.{slug}",
        f"name: {slug.replace('_', ' ').title()}",
        f"group: {group}",
        f"status: {status}",
        "summary: A test skill.",
    ]
    if with_tools:
        lines += ["tools:", "  - verb: read", "    purpose: gather"]
    lines += [
        "harness:",
        "  claude: harness/claude.md",
        "  codex: harness/codex.md",
        "  hermes: harness/hermes.md",
    ]
    (d / "skill.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (d / "SKILL.md").write_text("# skill\n", encoding="utf-8")
    (d / "workflow.md").write_text("# workflow\n", encoding="utf-8")
    for h in ("claude", "codex", "hermes"):
        (d / "harness" / f"{h}.md").write_text(f"# {h}\n", encoding="utf-8")
    return d


def _write_registry(root: Path, entries: list[dict]) -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    lines = ["skills:"]
    for e in entries:
        lines.append(
            f"  - {{id: {e['id']}, name: {e['name']}, group: {e['group']}, "
            f'status: {e.get("status", "planned")}, summary: "{e["summary"]}"}}'
        )
    (root / "registry" / "skills.yaml").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )


# --- loader --------------------------------------------------------------
def test_discover_empty_tree_returns_empty(tmp_path):
    assert discover_skills(tmp_path) == []
    assert skills_root(tmp_path) == tmp_path / "skills"


def test_discover_and_sort(tmp_path):
    _write_skill(tmp_path, "sat", "bbb")
    _write_skill(tmp_path, "sat", "aaa")
    specs = discover_skills(tmp_path)
    assert [s.id for s in specs] == ["sat.aaa", "sat.bbb"]


def test_load_skill_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_skill(tmp_path / "nope.yaml")


def test_load_skill_bad_yaml(tmp_path):
    bad = tmp_path / "skill.yaml"
    bad.write_text("id: [unclosed\n", encoding="utf-8")
    with pytest.raises(SpecError, match="invalid YAML"):
        load_skill(bad)


def test_load_skill_spec_error_includes_path(tmp_path):
    bad = tmp_path / "skill.yaml"
    bad.write_text("name: no id\n", encoding="utf-8")
    with pytest.raises(SpecError, match="key 'id' must be a non-empty string"):
        load_skill(bad)


def test_skill_dir(tmp_path):
    d = _write_skill(tmp_path, "sat", "ccc")
    assert skill_dir(d / "skill.yaml") == d.resolve()


# --- registry ------------------------------------------------------------
def test_registry_entry_from_obj_errors():
    with pytest.raises(SpecError, match="must be a mapping"):
        RegistryEntry.from_obj(["x"])
    with pytest.raises(SpecError, match="missing required key"):
        RegistryEntry.from_obj({"id": "a", "name": "A", "group": "sat"})
    with pytest.raises(SpecError, match="invalid status"):
        RegistryEntry.from_obj(
            {"id": "a.b", "name": "A", "group": "sat", "summary": "s", "status": "x"}
        )


def test_load_registry_ok_and_queries(tmp_path):
    _write_registry(
        tmp_path,
        [
            {
                "id": "sat.a",
                "name": "A",
                "group": "sat",
                "status": "implemented",
                "summary": "s",
            },
            {
                "id": "sat.b",
                "name": "B",
                "group": "sat",
                "status": "planned",
                "summary": "s",
            },
        ],
    )
    reg = load_registry(tmp_path)
    assert len(reg) == 2
    assert reg.ids == ("sat.a", "sat.b")
    assert reg.by_group("sat")[0].id == "sat.a"
    assert reg.get("sat.a").status == "implemented"
    assert reg.get("missing") is None
    assert reg.status_counts()["implemented"] == 1
    assert reg.groups["sat"] == "SAT"


def test_load_registry_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_registry(tmp_path)
    assert registry_path(tmp_path) == tmp_path / "registry" / "skills.yaml"


def test_load_registry_duplicate_id(tmp_path):
    _write_registry(
        tmp_path,
        [
            {"id": "sat.a", "name": "A", "group": "sat", "summary": "s"},
            {"id": "sat.a", "name": "A2", "group": "sat", "summary": "s"},
        ],
    )
    with pytest.raises(SpecError, match="duplicate registry id"):
        load_registry(tmp_path)


def test_load_registry_wrong_shape(tmp_path):
    (tmp_path / "registry").mkdir()
    (tmp_path / "registry" / "skills.yaml").write_text(
        "- just\n- a\n- list\n", encoding="utf-8"
    )
    with pytest.raises(SpecError, match="expected top-level mapping"):
        load_registry(tmp_path)


def test_load_registry_malformed_groups_rejected(tmp_path):
    _write_registry(
        tmp_path,
        [
            {
                "id": "sat.a",
                "name": "A",
                "group": "sat",
                "status": "stub",
                "summary": "s",
            }
        ],
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - just-a-string\n", encoding="utf-8"
    )
    with pytest.raises(SpecError, match="must be a mapping with a non-empty 'id'"):
        load_registry(tmp_path)


def test_load_registry_groups_wrong_top_shape(tmp_path):
    _write_registry(
        tmp_path,
        [
            {
                "id": "sat.a",
                "name": "A",
                "group": "sat",
                "status": "stub",
                "summary": "s",
            }
        ],
    )
    (tmp_path / "registry" / "groups.yaml").write_text("- a\n- b\n", encoding="utf-8")
    with pytest.raises(SpecError, match="expected a top-level mapping"):
        load_registry(tmp_path)
