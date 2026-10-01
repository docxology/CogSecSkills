"""Authoring must reject malformed source and unsafe writes before mutation."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from cogsecskills.authoring.author import (
    AuthorError,
    author_batch,
    load_definition_file,
    render_definition,
)
from cogsecskills.authoring.definitions import (
    check_definitions,
    definition_from_skill,
    definition_path,
    load_definitions,
    write_definitions,
)
from cogsecskills.authoring.scaffold import scaffold_skill
from cogsecskills.core.spec import SpecError
from cogsecskills.core.loader import load_skill


def _seed(root: Path, ids: tuple[str, ...] = ("sat.demo",)) -> None:
    directory = root / "registry"
    directory.mkdir()
    (directory / "skills.yaml").write_text(
        yaml.safe_dump(
            {
                "skills": [
                    dict(
                        id=skill_id,
                        group="sat",
                        name="Demo",
                        summary="Summary",
                        status="stub",
                    )
                    for skill_id in ids
                ]
            }
        ),
        encoding="utf-8",
    )


def _definition(**overrides) -> dict:
    return {
        "id": "sat.demo",
        "tools": [{"verb": "read", "purpose": "Read supplied evidence"}],
        "workflow_steps": [
            {"verbs": ["read"], "title": "Read", "text": "Read evidence."}
        ],
        "anti_criteria": ["Do not fabricate evidence."],
        **overrides,
    }


@pytest.mark.parametrize(
    "overrides",
    [
        {"id": None},
        {"tools": [{"verb": "read", "purpose": None}]},
        {"tools": [{"verb": "read", "purpose": 1}]},
        {"workflow_steps": [{"verbs": "read"}]},
        {"workflow_steps": [{"verbs": ["write"]}]},
        {"workflow_steps": [{"verbs": ["read"], "title": 42}]},
        {"workflow_steps": [{"verbs": ["read"], "text": None}]},
        {"anti_criteria": "Do not fabricate"},
        {"anti_criteria": [None]},
        {"description": {}},
        {"tags": "a-tag"},
        {"triggers": [None]},
        {"references": [1]},
        {"what_it_produces": [{"unquoted": "prose"}]},
        {"outputs": "product"},
        {"inputs": [{"name": "context", "required": "false"}]},
        {"harness_bindings": []},
        {"harness_bindings": {"codex": []}},
        {"harness_bindings": {"../external": {}}},
        {"harness_bindings": {"codex": {"read": ["tool", None]}}},
        {"harness_bindings": {"codex": {"teleport": ["tool", "note"]}}},
    ],
)
def test_bad_definition_cannot_leave_partial_skill(tmp_path, overrides):
    _seed(tmp_path)
    with pytest.raises((AuthorError, SpecError)):
        render_definition(_definition(**overrides), tmp_path)
    assert not (tmp_path / "skills").exists()


@pytest.mark.parametrize("harnesses", [("../external",), (), ("codex", "codex")])
def test_unsafe_harness_set_cannot_write_or_overwrite(tmp_path, harnesses):
    _seed(tmp_path)
    files = scaffold_skill("sat.demo", tmp_path)
    original = {path: path.read_bytes() for path in files}
    with pytest.raises(SpecError):
        scaffold_skill("sat.demo", tmp_path, overwrite=True, harnesses=harnesses)
    assert {path: path.read_bytes() for path in files} == original
    with pytest.raises(AuthorError):
        render_definition(_definition(), tmp_path, harnesses=harnesses)
    assert {path: path.read_bytes() for path in files} == original


@pytest.mark.parametrize("writer", [render_definition, scaffold_skill])
def test_symlinked_skill_parent_cannot_redirect_generated_files(tmp_path, writer):
    root = tmp_path / "root"
    root.mkdir()
    _seed(root)
    external = tmp_path / "external"
    external.mkdir()
    (root / "skills").symlink_to(external, target_is_directory=True)
    with pytest.raises(SpecError, match="unsafe"):
        writer(_definition() if writer is render_definition else "sat.demo", root)
    assert list(external.iterdir()) == []


@pytest.mark.parametrize("writer", [render_definition, scaffold_skill])
def test_internal_group_symlink_cannot_write_outside_skill_tree(tmp_path, writer):
    _seed(tmp_path)
    victim = tmp_path / "unrelated"
    victim.mkdir()
    tree = tmp_path / "skills"
    tree.mkdir()
    (tree / "sat").symlink_to(victim, target_is_directory=True)
    with pytest.raises(SpecError, match="unsafe"):
        writer(_definition() if writer is render_definition else "sat.demo", tmp_path)
    assert list(victim.iterdir()) == []


def test_one_symlinked_output_cannot_trigger_partial_render(tmp_path):
    _seed(tmp_path)
    files = scaffold_skill("sat.demo", tmp_path)
    before = {path: path.read_bytes() for path in files}
    victim = tmp_path / "private.txt"
    victim.write_text("private unchanged", encoding="utf-8")
    workflow = tmp_path / "skills" / "sat" / "demo" / "workflow.md"
    workflow.unlink()
    workflow.symlink_to(victim)
    with pytest.raises(AuthorError, match="unsafe generated destination"):
        render_definition(_definition(), tmp_path)
    assert victim.read_text(encoding="utf-8") == "private unchanged"
    for path, content in before.items():
        if path != workflow:
            assert path.read_bytes() == content


@pytest.mark.parametrize(
    "skill_id", ["sat../external", "sat...", "sat./external", "sat."]
)
def test_definition_paths_reject_unsafe_ids(tmp_path, skill_id):
    with pytest.raises(AuthorError, match="unsafe definition path"):
        definition_path(skill_id, tmp_path)


def test_definition_check_reports_malformed_lists_without_traceback(tmp_path):
    _seed(tmp_path)
    path = definition_path("sat.demo", tmp_path)
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(_definition(negative_controls=1)), encoding="utf-8")
    assert any(
        "must be a list of strings" in item for item in check_definitions(tmp_path)
    )


def test_definition_write_preflights_every_source_before_canonicalizing(tmp_path):
    _seed(tmp_path, ("sat.demo", "sat.second"))
    first = definition_path("sat.demo", tmp_path)
    second = definition_path("sat.second", tmp_path)
    first.parent.mkdir(parents=True)
    first.write_text(yaml.safe_dump(_definition()), encoding="utf-8")
    second.write_text(
        yaml.safe_dump(_definition(id="sat.second", outputs=1)), encoding="utf-8"
    )
    before = first.read_bytes(), second.read_bytes()
    with pytest.raises(AuthorError, match="outputs.*must be a list"):
        write_definitions(tmp_path)
    assert (first.read_bytes(), second.read_bytes()) == before
    assert not (tmp_path / "skills").exists()


def test_canonical_definition_write_preflights_output_symlinks(tmp_path):
    _seed(tmp_path)
    scaffold_skill("sat.demo", tmp_path)
    definition = definition_path("sat.demo", tmp_path)
    definition.parent.mkdir(parents=True)
    definition.write_text(yaml.safe_dump(_definition()), encoding="utf-8")
    before = definition.read_bytes()
    victim = tmp_path / "private.md"
    victim.write_text("private unchanged", encoding="utf-8")
    workflow = tmp_path / "skills" / "sat" / "demo" / "workflow.md"
    workflow.unlink()
    workflow.symlink_to(victim)
    with pytest.raises(AuthorError, match="unsafe generated destination"):
        write_definitions(tmp_path)
    assert definition.read_bytes() == before
    assert victim.read_text(encoding="utf-8") == "private unchanged"


def test_definition_bootstrap_rejects_external_companion_reads(tmp_path):
    _seed(tmp_path)
    scaffold_skill("sat.demo", tmp_path)
    directory = tmp_path / "skills" / "sat" / "demo"
    spec = load_skill(directory / "skill.yaml")
    external = tmp_path / "private.md"
    external.write_text("private", encoding="utf-8")
    (directory / "SKILL.md").unlink()
    (directory / "SKILL.md").symlink_to(external)
    with pytest.raises(AuthorError, match="cannot bootstrap definition"):
        definition_from_skill(spec, tmp_path)


def test_missing_canonical_path_is_not_hidden_by_matching_id(tmp_path):
    _seed(tmp_path)
    directory = tmp_path / "definitions" / "sat"
    directory.mkdir(parents=True)
    (directory / "misplaced.yaml").write_text(
        yaml.safe_dump(_definition()), encoding="utf-8"
    )
    assert any(
        "missing canonical definition at expected path" in item
        for item in check_definitions(tmp_path)
    )


def test_definition_tree_symlink_cannot_escape_project_root(tmp_path):
    root = tmp_path / "root"
    root.mkdir()
    _seed(root)
    external = tmp_path / "external" / "sat"
    external.mkdir(parents=True)
    (external / "demo.yaml").write_text(yaml.safe_dump(_definition()), encoding="utf-8")
    (root / "definitions").symlink_to(external.parent, target_is_directory=True)
    with pytest.raises(AuthorError, match="unsafe definition source"):
        load_definitions(root)
    with pytest.raises(AuthorError, match="unsafe definition path"):
        definition_path("sat.demo", root)


def test_registered_unsafe_slug_cannot_be_rendered_or_scaffolded(tmp_path):
    _seed(tmp_path, ("sat.../../private",))
    with pytest.raises(AuthorError, match="safe non-empty path component"):
        render_definition(_definition(id="sat.../../private"), tmp_path)
    with pytest.raises(SpecError, match="unsafe scaffold destination"):
        scaffold_skill("sat.../../private", tmp_path)
    assert not (tmp_path / "skills").exists()


def test_canonical_bootstrap_preserves_the_skill_version(tmp_path):
    _seed(tmp_path)
    render_definition(_definition(version="2.3.4"), tmp_path)
    write_definitions(tmp_path)
    source = yaml.safe_load(
        definition_path("sat.demo", tmp_path).read_text(encoding="utf-8")
    )
    assert source["version"] == "2.3.4"
    spec = load_skill(tmp_path / "skills" / "sat" / "demo" / "skill.yaml")
    assert spec.version == "2.3.4"


def test_definition_loader_and_compatibility_batch_report_bad_sources(tmp_path):
    _seed(tmp_path)
    definition = tmp_path / "definition.yaml"
    definition.write_text("id: sat.demo\nid: sat.other\n", encoding="utf-8")
    with pytest.raises(AuthorError, match="duplicate mapping key"):
        load_definition_file(definition)
    definition = tmp_path / "definition.json"
    definition.write_text("{", encoding="utf-8")
    with pytest.raises(AuthorError, match="definition file"):
        load_definition_file(definition)
    directory = tmp_path / "skills" / "sat" / "demo"
    directory.mkdir(parents=True)
    source = directory / "_def.json"
    source.write_text(json.dumps([]), encoding="utf-8")
    result = author_batch(tmp_path, promote=False)
    assert result["rendered"] == []
    assert "must contain a mapping" in result["failed"]["sat.demo"]
    assert source.is_file()
