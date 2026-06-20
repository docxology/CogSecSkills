"""Tests for the deterministic skill authoring renderer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from cogsecskills.author import (
    AuthorError,
    author_batch,
    promote_to_implemented,
    render_definition,
)
from cogsecskills.harness import HARNESSES
from cogsecskills.loader import load_skill
from cogsecskills.spec import SpecError
from cogsecskills.validate import validate_skill


def _seed_registry(root: Path, *, status: str = "stub") -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n"
        f"  - {{id: sat.demo, name: Demo Technique, group: sat, status: {status}, "
        "ageint_topic: structured-analytic-techniques, summary: A demo technique.}\n",
        encoding="utf-8",
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )


def _seed_two_skill_registry(root: Path, *, status: str = "stub") -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n"
        f"  - {{id: sat.demo, name: Demo Technique, group: sat, status: {status}, "
        "ageint_topic: structured-analytic-techniques, summary: A demo technique.}\n"
        f"  - {{id: sat.second_demo, name: Second Demo, group: sat, status: {status}, "
        "ageint_topic: structured-analytic-techniques, summary: Another demo technique.}\n",
        encoding="utf-8",
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )


def _good_def() -> dict:
    return {
        "id": "sat.demo",
        "description": "A real description of the demo technique spanning a sentence or two.",
        "tools": [
            {"verb": "read", "purpose": "ingest the inputs"},
            {"verb": "reason", "purpose": "apply the technique"},
            {"verb": "write", "purpose": "emit the product"},
        ],
        "workflow_steps": [
            {"verbs": ["read"], "title": "Gather", "text": "Collect the inputs."},
            {"verbs": ["reason", "write"], "title": "Analyse", "text": "Do the work."},
        ],
        "anti_criteria": ["Do not skip the evidence step."],
        "when_to_use": ["a demo is needed"],
        "what_it_produces": ["a demo product"],
        "key_discipline": ["stay rigorous"],
    }


def test_render_definition_is_conforming(tmp_path):
    _seed_registry(tmp_path)
    written = render_definition(_good_def(), root=tmp_path)
    assert len(written) == 6
    directory = tmp_path / "skills" / "sat" / "demo"
    spec = load_skill(directory / "skill.yaml")
    assert spec.status == "implemented"
    assert {v.value for v in spec.verbs} == {"read", "reason", "write"}
    result = validate_skill(spec, directory)
    assert result.ok, [i.message for i in result.errors]


def test_render_adapters_bind_every_verb(tmp_path):
    _seed_registry(tmp_path)
    render_definition(_good_def(), root=tmp_path)
    directory = tmp_path / "skills" / "sat" / "demo"
    for harness in HARNESSES:
        text = (directory / "harness" / f"{harness}.md").read_text(encoding="utf-8")
        for verb in ("read", "reason", "write"):
            assert f"| `{verb}` |" in text


def test_render_rejects_missing_tools(tmp_path):
    _seed_registry(tmp_path)
    bad = _good_def()
    bad["tools"] = []
    with pytest.raises(AuthorError, match="non-empty 'tools'"):
        render_definition(bad, root=tmp_path)


def test_render_rejects_unknown_verb(tmp_path):
    _seed_registry(tmp_path)
    bad = _good_def()
    bad["tools"] = [{"verb": "teleport", "purpose": "x"}]
    with pytest.raises(SpecError, match="unknown tool verb"):
        render_definition(bad, root=tmp_path)


def test_render_rejects_unknown_id(tmp_path):
    _seed_registry(tmp_path)
    bad = _good_def()
    bad["id"] = "sat.nope"
    with pytest.raises(AuthorError, match="not in the registry"):
        render_definition(bad, root=tmp_path)


def test_render_requires_workflow_steps(tmp_path):
    _seed_registry(tmp_path)
    bad = _good_def()
    bad["workflow_steps"] = []
    with pytest.raises(AuthorError, match="workflow_steps"):
        render_definition(bad, root=tmp_path)


def test_render_requires_anti_criteria(tmp_path):
    _seed_registry(tmp_path)
    bad = _good_def()
    bad["anti_criteria"] = []
    with pytest.raises(AuthorError, match="anti_criteria"):
        render_definition(bad, root=tmp_path)


def test_promote_to_implemented(tmp_path):
    _seed_registry(tmp_path, status="stub")
    changed = promote_to_implemented(["sat.demo"], root=tmp_path)
    assert changed == 1
    text = (tmp_path / "registry" / "skills.yaml").read_text(encoding="utf-8")
    assert "status: implemented" in text
    assert "status: stub" not in text


def test_author_batch_renders_and_promotes(tmp_path):
    _seed_registry(tmp_path, status="stub")
    directory = tmp_path / "skills" / "sat" / "demo"
    directory.mkdir(parents=True)
    (directory / "_def.json").write_text(json.dumps(_good_def()), encoding="utf-8")
    result = author_batch(root=tmp_path)
    assert result["rendered"] == ["sat.demo"]
    assert result["failed"] == {}
    assert not (directory / "_def.json").exists()  # deleted by default
    reg = (tmp_path / "registry" / "skills.yaml").read_text(encoding="utf-8")
    assert "status: implemented" in reg


def test_author_batch_reports_malformed(tmp_path):
    _seed_registry(tmp_path)
    directory = tmp_path / "skills" / "sat" / "demo"
    directory.mkdir(parents=True)
    (directory / "_def.json").write_text("{not valid json", encoding="utf-8")
    result = author_batch(root=tmp_path)
    assert result["rendered"] == []
    assert "sat.demo" in result["failed"]


def test_cli_author_renders(tmp_path, capsys):
    from cogsecskills.cli import main

    _seed_registry(tmp_path)
    def_path = tmp_path / "def.json"
    def_path.write_text(json.dumps(_good_def()), encoding="utf-8")
    rc = main(["--root", str(tmp_path), "author", str(def_path)])
    assert rc == 0
    assert "authored 6 files" in capsys.readouterr().out


def test_cli_author_batch_renders_and_reports(tmp_path, capsys):
    from cogsecskills.cli import main

    _seed_registry(tmp_path)
    directory = tmp_path / "skills" / "sat" / "demo"
    directory.mkdir(parents=True)
    (directory / "_def.json").write_text(json.dumps(_good_def()), encoding="utf-8")
    rc = main(["--root", str(tmp_path), "author-batch"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "rendered 1 skills" in out


def test_cli_author_accepts_yaml_definition(tmp_path, capsys):
    from cogsecskills.cli import main

    import yaml

    _seed_registry(tmp_path)
    def_path = tmp_path / "def.yaml"
    def_path.write_text(yaml.safe_dump(_good_def(), sort_keys=False), encoding="utf-8")
    rc = main(["--root", str(tmp_path), "author", str(def_path)])
    assert rc == 0
    assert "authored 6 files" in capsys.readouterr().out


def test_renderer_emits_quality_sections(tmp_path):
    _seed_registry(tmp_path)
    render_definition(_good_def(), root=tmp_path)
    directory = tmp_path / "skills" / "sat" / "demo"
    skill = (directory / "SKILL.md").read_text(encoding="utf-8")
    workflow = (directory / "workflow.md").read_text(encoding="utf-8")
    adapter = (directory / "harness" / "codex.md").read_text(encoding="utf-8")
    assert "## Defensive boundary" in skill
    assert "## Evidence requirements" in workflow
    assert "## Negative controls" in workflow
    assert "defensive boundary" in adapter.lower()
    assert "chain-of-thought" not in adapter.lower()


def test_cli_definitions_write_check_and_drift(tmp_path, capsys):
    from cogsecskills.cli import main

    _seed_registry(tmp_path)
    render_definition(_good_def(), root=tmp_path)

    assert main(["--root", str(tmp_path), "definitions", "--check"]) == 1
    assert "missing canonical definition" in capsys.readouterr().out

    assert main(["--root", str(tmp_path), "definitions", "--write"]) == 0
    assert "1 definitions, 1 rendered skills" in capsys.readouterr().out

    assert main(["--root", str(tmp_path), "definitions", "--check"]) == 0
    assert "canonical definitions are current" in capsys.readouterr().out

    definition = tmp_path / "definitions" / "sat" / "demo.yaml"
    definition.write_text(
        definition.read_text(encoding="utf-8") + "\nextra: drift\n",
        encoding="utf-8",
    )
    assert main(["--root", str(tmp_path), "definitions", "--check"]) == 1
    assert "stale canonical definition" in capsys.readouterr().out


def test_check_definitions_reports_parser_errors_without_crashing(tmp_path):
    from cogsecskills.definitions import (
        canonical_definition_text,
        check_definitions,
        definition_path,
        write_definitions,
    )

    _seed_registry(tmp_path)
    render_definition(_good_def(), root=tmp_path)
    write_definitions(tmp_path)

    path = definition_path("sat.demo", tmp_path)
    definition = yaml.safe_load(path.read_text(encoding="utf-8"))
    definition["tools"][0]["verb"] = "teleport"
    path.write_text(canonical_definition_text(definition), encoding="utf-8")

    findings = check_definitions(tmp_path)
    assert any(
        "sat.demo: cannot render definition" in finding
        and "unknown tool verb" in finding
        for finding in findings
    )


def test_check_definitions_reports_rendered_file_drift(tmp_path):
    from cogsecskills.definitions import check_definitions, write_definitions

    _seed_registry(tmp_path)
    render_definition(_good_def(), root=tmp_path)
    write_definitions(tmp_path)

    skill_md = tmp_path / "skills" / "sat" / "demo" / "SKILL.md"
    skill_md.write_text(
        skill_md.read_text(encoding="utf-8") + "\nmanual drift\n",
        encoding="utf-8",
    )

    findings = check_definitions(tmp_path)
    assert any(
        "sat.demo: stale rendered file: skills/sat/demo/SKILL.md" in f for f in findings
    )


def test_check_definitions_reports_missing_and_extra_definitions(tmp_path):
    from cogsecskills.definitions import (
        canonical_definition_text,
        check_definitions,
        definitions_root,
    )

    _seed_registry(tmp_path)
    base = definitions_root(tmp_path) / "sat"
    base.mkdir(parents=True)
    extra = _good_def()
    extra["id"] = "sat.extra"
    (base / "extra.yaml").write_text(canonical_definition_text(extra), encoding="utf-8")

    findings = check_definitions(tmp_path)
    assert any(
        "missing canonical definition: definitions/sat/demo.yaml" in f for f in findings
    )
    assert "definition is not in registry: sat.extra" in findings


def test_check_definitions_reports_reused_negative_control_entry(tmp_path):
    from cogsecskills.definitions import (
        canonical_definition_text,
        check_definitions,
        definition_path,
        write_definitions,
    )

    _seed_two_skill_registry(tmp_path)
    render_definition(_good_def(), root=tmp_path)
    second = _good_def()
    second["id"] = "sat.second_demo"
    render_definition(second, root=tmp_path)
    write_definitions(tmp_path)

    first_path = definition_path("sat.demo", tmp_path)
    second_path = definition_path("sat.second_demo", tmp_path)
    first = yaml.safe_load(first_path.read_text(encoding="utf-8"))
    second = yaml.safe_load(second_path.read_text(encoding="utf-8"))
    second["negative_controls"][1] = first["negative_controls"][1]
    second_path.write_text(canonical_definition_text(second), encoding="utf-8")

    findings = check_definitions(tmp_path)
    assert any(
        "negative_control entry reused across definitions" in f for f in findings
    )


def test_check_definitions_reports_reused_quality_entry(tmp_path):
    from cogsecskills.definitions import (
        canonical_definition_text,
        check_definitions,
        definition_path,
        write_definitions,
    )

    _seed_two_skill_registry(tmp_path)
    render_definition(_good_def(), root=tmp_path)
    second = _good_def()
    second["id"] = "sat.second_demo"
    render_definition(second, root=tmp_path)
    write_definitions(tmp_path)

    first_path = definition_path("sat.demo", tmp_path)
    second_path = definition_path("sat.second_demo", tmp_path)
    first = yaml.safe_load(first_path.read_text(encoding="utf-8"))
    second = yaml.safe_load(second_path.read_text(encoding="utf-8"))
    second["confidence_rubric"][1] = first["confidence_rubric"][1]
    second_path.write_text(canonical_definition_text(second), encoding="utf-8")

    findings = check_definitions(tmp_path)
    assert any(
        "confidence_rubric entry reused across definitions" in f for f in findings
    )


# --- additional branch coverage -------------------------------------------
def test_render_missing_workflow_steps_key(tmp_path):
    _seed_registry(tmp_path)
    bad = _good_def()
    del bad["workflow_steps"]
    with pytest.raises(AuthorError, match="missing required key 'workflow_steps'"):
        render_definition(bad, root=tmp_path)


def test_render_tool_not_a_mapping(tmp_path):
    _seed_registry(tmp_path)
    bad = _good_def()
    bad["tools"] = ["notamapping"]
    with pytest.raises(AuthorError, match="each tool needs a 'verb'"):
        render_definition(bad, root=tmp_path)


def test_render_tool_empty_purpose(tmp_path):
    _seed_registry(tmp_path)
    bad = _good_def()
    bad["tools"] = [{"verb": "read", "purpose": "   "}]
    with pytest.raises(AuthorError, match="needs a non-empty 'purpose'"):
        render_definition(bad, root=tmp_path)


def test_render_workflow_step_not_a_mapping(tmp_path):
    _seed_registry(tmp_path)
    bad = _good_def()
    bad["workflow_steps"] = ["notamapping"]
    with pytest.raises(AuthorError, match="workflow step 1 must be a mapping"):
        render_definition(bad, root=tmp_path)


def test_render_honours_harness_binding_override(tmp_path):
    _seed_registry(tmp_path)
    d = _good_def()
    d["harness_bindings"] = {"claude": {"read": ["MyReadTool", "custom note"]}}
    render_definition(d, root=tmp_path)
    text = (tmp_path / "skills" / "sat" / "demo" / "harness" / "claude.md").read_text()
    assert "MyReadTool" in text and "custom note" in text


def test_render_custom_harness_uses_fallback_bindings(tmp_path):
    _seed_registry(tmp_path)
    render_definition(_good_def(), root=tmp_path, harnesses=("claude", "gemini"))
    gemini = tmp_path / "skills" / "sat" / "demo" / "harness" / "gemini.md"
    assert gemini.is_file()
    text = gemini.read_text()
    assert "gemini `read` tool" in text  # generic fallback binding
    # the spec declares only the two configured harnesses
    from cogsecskills.loader import load_skill

    spec = load_skill(tmp_path / "skills" / "sat" / "demo" / "skill.yaml")
    assert set(spec.harness) == {"claude", "gemini"}
