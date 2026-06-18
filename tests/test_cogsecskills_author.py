"""Tests for the deterministic skill authoring renderer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

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
