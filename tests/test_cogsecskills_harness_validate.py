"""Tests for multiharness conformance and the validation gates."""

from __future__ import annotations

from pathlib import Path

from cogsecskills.harness import (
    HARNESSES,
    HARNESS_VERB_SUPPORT,
    check_conformance,
    is_multiharness,
)
from cogsecskills.spec import SkillSpec, ToolVerb
from cogsecskills.validate import (
    conformance_report,
    validate_library,
    validate_skill,
)


def _spec(**overrides) -> SkillSpec:
    data = {
        "id": "sat.x",
        "name": "X",
        "group": "sat",
        "summary": "s",
        "status": "implemented",
        "tools": [{"verb": "read", "purpose": "p"}],
        "harness": {h: f"harness/{h}.md" for h in HARNESSES},
    }
    data.update(overrides)
    return SkillSpec.from_mapping(data)


def _materialize(root: Path, spec: SkillSpec, *, omit: set[str] | None = None) -> Path:
    """Write the skill.yaml + companion files for a spec, optionally omitting some."""
    import yaml

    omit = omit or set()
    d = root / "skills" / spec.group / spec.id.split(".", 1)[1]
    (d / "harness").mkdir(parents=True, exist_ok=True)
    spec_payload = {
        "id": spec.id,
        "name": spec.name,
        "group": spec.group,
        "status": spec.status,
        "summary": spec.summary,
        "tools": [{"verb": t.verb.value, "purpose": t.purpose} for t in spec.tools],
        "workflow": spec.workflow,
        "harness": dict(spec.harness),
    }
    (d / "skill.yaml").write_text(yaml.safe_dump(spec_payload), encoding="utf-8")
    if "SKILL.md" not in omit:
        (d / "SKILL.md").write_text("# s\n", encoding="utf-8")
    if "workflow.md" not in omit:
        (d / spec.workflow).write_text("# w\n", encoding="utf-8")
    for h in HARNESSES:
        if f"{h}.md" not in omit:
            rows = "\n".join(
                f"| `{tool.verb.value}` | {h}-tool | {tool.purpose} |"
                for tool in spec.tools
            )
            (d / "harness" / f"{h}.md").write_text(
                f"# {h}\n\n"
                f"| Neutral verb | Tool | Notes |\n"
                f"| --- | --- | --- |\n"
                f"{rows}\n",
                encoding="utf-8",
            )
    return d


# --- harness -------------------------------------------------------------
def test_all_harnesses_support_all_verbs():
    for h in HARNESSES:
        assert HARNESS_VERB_SUPPORT[h] == frozenset(ToolVerb)


def test_check_conformance_ok():
    spec = _spec()
    confs = check_conformance(spec)
    assert set(confs) == set(HARNESSES)
    assert all(c.ok for c in confs.values())
    assert is_multiharness(spec) is True


def test_conformance_missing_adapter_declaration():
    spec = _spec(harness={"claude": "harness/claude.md"})  # codex/hermes absent
    confs = check_conformance(spec)
    assert confs["claude"].has_adapter is True
    assert confs["codex"].has_adapter is False
    assert is_multiharness(spec) is False


# --- validate_skill ------------------------------------------------------
def test_validate_skill_all_present(tmp_path):
    spec = _spec()
    d = _materialize(tmp_path, spec)
    result = validate_skill(spec, d)
    assert result.ok
    assert result.errors == []


def test_validate_skill_missing_files(tmp_path):
    spec = _spec()
    d = _materialize(tmp_path, spec, omit={"SKILL.md", "workflow.md", "codex.md"})
    result = validate_skill(spec, d)
    msgs = " ".join(i.message for i in result.errors)
    assert "missing SKILL.md" in msgs
    assert "missing workflow" in msgs
    assert "codex" in msgs


def test_validate_skill_implemented_without_tools(tmp_path):
    spec = _spec(tools=[])
    d = _materialize(tmp_path, spec)
    result = validate_skill(spec, d)
    assert any("declares no tool-use" in i.message for i in result.errors)


def test_validate_skill_group_mismatch_errors(tmp_path):
    spec = _spec()
    # Put it under the wrong group directory.
    d = tmp_path / "skills" / "WRONG" / "x"
    (d / "harness").mkdir(parents=True)
    (d / "SKILL.md").write_text("# s\n", encoding="utf-8")
    (d / "workflow.md").write_text("# w\n", encoding="utf-8")
    for h in HARNESSES:
        (d / "harness" / f"{h}.md").write_text(
            "# h\n\n| Neutral verb | Tool | Notes |\n| --- | --- | --- |\n| `read` | tool | ok |\n",
            encoding="utf-8",
        )
    result = validate_skill(spec, d)
    assert any("on-disk group" in i.message for i in result.errors)


def test_validate_skill_adapter_must_bind_declared_verbs(tmp_path):
    spec = _spec(
        tools=[{"verb": "read", "purpose": "p1"}, {"verb": "write", "purpose": "p2"}]
    )
    d = _materialize(tmp_path, spec)
    (d / "harness" / "codex.md").write_text(
        "# codex\n\n| Neutral verb | Tool | Notes |\n| --- | --- | --- |\n| `read` | shell | ok |\n",
        encoding="utf-8",
    )
    result = validate_skill(spec, d)
    assert any("codex" in i.message and "write" in i.message for i in result.errors)


def test_validate_skill_declared_paths_cannot_escape_directory(tmp_path):
    spec = _spec(workflow="../workflow.md")
    d = _materialize(tmp_path, spec, omit={"workflow.md"})
    result = validate_skill(spec, d)
    assert any(
        "must stay inside the skill directory" in i.message for i in result.errors
    )


def test_validate_skill_undeclared_harness(tmp_path):
    spec = _spec(harness={"claude": "harness/claude.md", "codex": "harness/codex.md"})
    d = _materialize(tmp_path, spec)
    result = validate_skill(spec, d)
    assert any("does not declare a 'hermes'" in i.message for i in result.errors)


# --- validate_library ----------------------------------------------------
def _write_registry(root: Path, rows: list[str]) -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n" + "\n".join(rows) + "\n", encoding="utf-8"
    )


def test_validate_library_coherent(tmp_path):
    spec = _spec()
    _materialize(tmp_path, spec)
    _write_registry(
        tmp_path,
        ["  - {id: sat.x, name: X, group: sat, status: implemented, summary: s}"],
    )
    result = validate_library(tmp_path)
    assert result.ok, [i.message for i in result.errors]


def test_validate_library_on_disk_not_in_registry(tmp_path):
    spec = _spec()
    _materialize(tmp_path, spec)
    _write_registry(
        tmp_path,
        ["  - {id: sat.other, name: O, group: sat, status: planned, summary: s}"],
    )
    result = validate_library(tmp_path)
    assert any("not enumerated in the registry" in i.message for i in result.errors)


def test_validate_library_implemented_missing_on_disk(tmp_path):
    _write_registry(
        tmp_path,
        ["  - {id: sat.ghost, name: G, group: sat, status: implemented, summary: s}"],
    )
    result = validate_library(tmp_path)
    assert any("no on-disk skill found" in i.message for i in result.errors)


def test_validate_library_group_mismatch_error(tmp_path):
    spec = _spec()
    _materialize(tmp_path, spec)
    _write_registry(
        tmp_path,
        [
            "  - {id: sat.x, name: X, group: osint_integrity, status: implemented, summary: s}"
        ],
    )
    result = validate_library(tmp_path)
    assert any("registry group" in i.message for i in result.errors)


def test_validate_library_registry_id_must_match_group(tmp_path):
    _write_registry(
        tmp_path,
        [
            "  - {id: osint_integrity.x, name: X, group: sat, status: planned, summary: s}"
        ],
    )
    result = validate_library(tmp_path)
    assert any("registry id must be" in i.message for i in result.errors)


def test_validate_library_missing_registry(tmp_path):
    result = validate_library(tmp_path)
    assert any("registry could not be loaded" in i.message for i in result.errors)


def test_conformance_report_shape(tmp_path):
    spec = _spec()
    _materialize(tmp_path, spec)
    _write_registry(
        tmp_path,
        ["  - {id: sat.x, name: X, group: sat, status: implemented, summary: s}"],
    )
    report = conformance_report(tmp_path)
    assert report["registry_total"] == 1
    assert report["on_disk_skills"] == 1
    assert report["ok"] is True


def test_conformance_report_no_registry(tmp_path):
    report = conformance_report(tmp_path)
    assert report["registry_total"] == 0
    assert report["ok"] is False


# --- new strict-validator branches (Forge + convergent-automation hardening) ---
def test_check_conformance_verb_axis_is_non_vacuous():
    """Narrowing a harness's verb support must surface unsupported verbs."""
    spec = _spec(tools=[{"verb": "web", "purpose": "fetch"}])
    narrowed = {h: frozenset() for h in HARNESSES}
    confs = check_conformance(spec, support=narrowed)
    assert all(c.unsupported_verbs for c in confs.values())


def test_validate_skill_adapter_missing_verb_binding(tmp_path):
    spec = _spec(
        tools=[{"verb": "read", "purpose": "p"}, {"verb": "write", "purpose": "q"}]
    )
    d = _materialize(tmp_path, spec)
    # Replace the claude adapter with prose that binds no verbs.
    (d / "harness" / "claude.md").write_text("# claude\n\nno table\n", encoding="utf-8")
    result = validate_skill(spec, d)
    assert any("does not bind declared tool verbs" in i.message for i in result.errors)


def test_validate_skill_rejects_path_escape(tmp_path):
    spec = _spec(
        harness={
            "claude": "../escape.md",
            "codex": "harness/codex.md",
            "hermes": "harness/hermes.md",
        }
    )
    d = _materialize(tmp_path, spec)
    result = validate_skill(spec, d)
    assert any(
        "must stay inside the skill directory" in i.message for i in result.errors
    )


def test_validate_skill_id_group_prefix_mismatch(tmp_path):
    spec = _spec(id="other.x", group="sat")
    d = _materialize(tmp_path, spec)
    result = validate_skill(spec, d)
    assert any("skill id must be '<group>.<slug>'" in i.message for i in result.errors)


def test_validate_skill_slug_mismatch(tmp_path):
    spec = _spec(id="sat.realslug")
    # Materialize under the right group but a wrong leaf folder name.
    d = tmp_path / "skills" / "sat" / "wrongfolder"
    (d / "harness").mkdir(parents=True)
    (d / "SKILL.md").write_text("# s\n", encoding="utf-8")
    (d / "workflow.md").write_text("# w\n", encoding="utf-8")
    for h in HARNESSES:
        (d / "harness" / f"{h}.md").write_text(
            "| Neutral verb | Tool | Notes |\n| --- | --- | --- |\n| `read` | t | n |\n",
            encoding="utf-8",
        )
    result = validate_skill(spec, d)
    assert any("!= skill slug" in i.message for i in result.errors)


def test_validate_library_malformed_skill_on_disk(tmp_path):
    d = tmp_path / "skills" / "sat" / "x"
    d.mkdir(parents=True)
    (d / "skill.yaml").write_text("id: [unterminated\n", encoding="utf-8")
    _write_registry(
        tmp_path,
        ["  - {id: sat.x, name: X, group: sat, status: stub, summary: s}"],
    )
    result = validate_library(tmp_path)
    assert any("skills could not be loaded" in i.message for i in result.errors)


def test_validate_library_registry_id_prefix_mismatch(tmp_path):
    _write_registry(
        tmp_path,
        ["  - {id: other.x, name: X, group: sat, status: stub, summary: s}"],
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    result = validate_library(tmp_path)
    assert any("registry id must be" in i.message for i in result.errors)


def test_validate_library_undefined_group(tmp_path):
    _write_registry(
        tmp_path,
        ["  - {id: ghost.x, name: X, group: ghost, status: stub, summary: s}"],
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    result = validate_library(tmp_path)
    assert any("not defined in groups.yaml" in i.message for i in result.errors)
