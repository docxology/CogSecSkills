"""Real source-file regressions for parser and filesystem boundaries."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from cogsecskills.core.config import load_config
from cogsecskills.core.loader import discover_skills, load_skill
from cogsecskills.core.locate import project_root
from cogsecskills.core.paths import (
    contained_path,
    skill_components,
    validate_component,
    validate_harnesses,
)
from cogsecskills.core.registry import load_registry
from cogsecskills.core.spec import SpecError


def _registry(root: Path) -> None:
    (root / "registry").mkdir()
    (root / "registry" / "skills.yaml").write_text(
        "skills: [{id: sat.demo, name: Demo, group: sat, summary: Summary}]\n",
        encoding="utf-8",
    )


@pytest.mark.parametrize(
    "text",
    [
        "false",
        "[]",
        "quality: false",
        "quality: []",
        "quality: {require_references: 'false'}",
        "quality: {require_references: null}",
        "quality: {min_workflow_steps: -1}",
        "quality: {min_anti_criteria: -1}",
        "harnesses: [codex, null]",
        "harnesses: [codex, codex]",
        "harnesses: [codex, '../external']",
        "runtime_eval: false",
        "runtime_eval: []",
        "runtime_eval: {harness_commands: false}",
        "runtime_eval: {harness_commands: []}",
        "runtime_eval: {harness_commands: {null: ['python', '{prompt}']}}",
        "runtime_eval: {harness_commands: {'../external': ['python', '{prompt}']}}",
        "runtime_eval: {harness_commands: {codex: [' ', '{prompt}']}}",
        "runtime_eval: {harness_commands: {codex: ['python', '']}}",
        "runtime_eval: {harness_commands: {codex: ['python', '{prompt}'], ' codex ': ['python', '{prompt}']}}",
        "quality: {require_references: false, require_references: true}",
    ],
)
def test_config_rejects_policy_and_shape_ambiguity(tmp_path, text):
    path = tmp_path / "cogsecskills.yaml"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError) as error:
        load_config(tmp_path)
    assert str(path) in str(error.value)


def test_optional_null_config_sections_and_zero_thresholds(tmp_path):
    path = tmp_path / "cogsecskills.yaml"
    path.write_text(
        "quality: {min_workflow_steps: 0, min_anti_criteria: 0}\n"
        "runtime_eval: {harness_commands: null}\n",
        encoding="utf-8",
    )
    assert load_config(tmp_path).min_workflow_steps == 0
    path.write_text("quality: null\nruntime_eval: null\n", encoding="utf-8")
    assert load_config(tmp_path).min_anti_criteria == 2
    path.write_bytes(b"\xff")
    with pytest.raises(ValueError, match="cannot read YAML"):
        load_config(tmp_path)


def test_runtime_command_strings_preserve_arguments_but_reject_nul(tmp_path):
    import yaml

    path = tmp_path / "cogsecskills.yaml"
    path.write_text(
        "runtime_eval: {harness_commands: {' codex ': ['python', ' leading ', '{prompt}']}}",
        encoding="utf-8",
    )
    assert load_config(tmp_path).runtime_eval_commands["codex"][1] == " leading "
    path.write_text(
        yaml.safe_dump(
            {"runtime_eval": {"harness_commands": {"codex": ["python", "\x00"]}}}
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="without NUL"):
        load_config(tmp_path)


@pytest.mark.parametrize("key", ["tools", "inputs", "outputs"])
@pytest.mark.parametrize("value", ["1", "false", "{}", "''"])
def test_skill_collection_errors_are_typed_and_source_labelled(tmp_path, key, value):
    path = tmp_path / "skill.yaml"
    path.write_text(
        f"id: sat.demo\nname: Demo\ngroup: sat\nsummary: Summary\n{key}: {value}\n",
        encoding="utf-8",
    )
    with pytest.raises(SpecError, match=f"field '{key}' must be a list") as error:
        load_skill(path)
    assert str(path) in str(error.value)


@pytest.mark.parametrize("value", ["false", "[]"])
def test_falsey_harness_container_is_not_silently_accepted(tmp_path, value):
    path = tmp_path / "skill.yaml"
    path.write_text(
        f"id: sat.demo\nname: Demo\ngroup: sat\nsummary: Summary\nharness: {value}\n",
        encoding="utf-8",
    )
    with pytest.raises(SpecError, match="harness.*mapping"):
        load_skill(path)


def test_optional_null_skill_collections_and_scalar_whitespace(tmp_path):
    path = tmp_path / "skill.yaml"
    path.write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: Summary\n"
        "tools: null\ninputs: null\noutputs: null\nharness: null\ntags: '  demo  '\n",
        encoding="utf-8",
    )
    assert load_skill(path).tags == ("demo",)
    path.write_bytes(b"\xff")
    with pytest.raises(SpecError, match="cannot read YAML"):
        load_skill(path)


@pytest.mark.parametrize("section", ["skills", "groups"])
@pytest.mark.parametrize("value", ["null", "false", "1", "{}"])
def test_registry_collections_are_typed(tmp_path, section, value):
    _registry(tmp_path)
    path = tmp_path / "registry" / f"{section}.yaml"
    path.write_text(f"{section}: {value}\n", encoding="utf-8")
    with pytest.raises(SpecError, match=f"'{section}' must be a list"):
        load_registry(tmp_path)


@pytest.mark.parametrize("value", ["null", "1", "false", "[]"])
def test_group_ids_cannot_be_coerced_to_text(tmp_path, value):
    _registry(tmp_path)
    (tmp_path / "registry" / "groups.yaml").write_text(
        f"groups: [{{id: {value}}}]\n", encoding="utf-8"
    )
    with pytest.raises(SpecError, match="non-empty 'id'"):
        load_registry(tmp_path)


@pytest.mark.parametrize("value", ["false", "[]"])
def test_group_document_must_be_a_mapping(tmp_path, value):
    _registry(tmp_path)
    (tmp_path / "registry" / "groups.yaml").write_text(value, encoding="utf-8")
    with pytest.raises(SpecError, match="top-level mapping"):
        load_registry(tmp_path)


def test_discovery_rejects_duplicate_ids_and_external_specs(tmp_path):
    from cogsecskills.authoring.scaffold import scaffold_skill
    from cogsecskills.quality.validate import validate_library

    _registry(tmp_path)
    scaffold_skill("sat.demo", tmp_path)
    spec = tmp_path / "skills" / "sat" / "demo" / "skill.yaml"
    other = tmp_path / "skills" / "sat" / "other" / "skill.yaml"
    other.parent.mkdir()
    other.write_bytes(spec.read_bytes())
    with pytest.raises(SpecError, match="duplicate on-disk skill id"):
        discover_skills(tmp_path)
    assert any(
        "duplicate on-disk" in item.message
        for item in validate_library(tmp_path).errors
    )
    other.unlink()
    outside = tmp_path / "outside.yaml"
    outside.write_bytes(spec.read_bytes())
    other.symlink_to(outside)
    with pytest.raises(SpecError, match="unsafe skill source"):
        discover_skills(tmp_path)
    assert any(
        "unsafe skill source" in item.message
        for item in validate_library(tmp_path).errors
    )


@pytest.mark.parametrize("section", ["skills", "groups"])
def test_registry_duplicate_keys_and_invalid_utf8_are_source_labelled(
    tmp_path, section
):
    _registry(tmp_path)
    path = tmp_path / "registry" / f"{section}.yaml"
    path.write_text(f"{section}: []\n{section}: []\n", encoding="utf-8")
    with pytest.raises(SpecError, match="duplicate mapping key"):
        load_registry(tmp_path)
    path.write_bytes(b"\xff")
    with pytest.raises(SpecError, match="cannot read YAML"):
        load_registry(tmp_path)


@pytest.mark.parametrize("value", ["", "..", "a/b", r"a\b", "/tmp", None, 1])
def test_identifier_components_are_host_independent(value):
    with pytest.raises(ValueError, match="safe non-empty path component"):
        validate_component(value, "name")


@pytest.mark.parametrize("values", [None, "codex", [], [""], ["a", " a "]])
def test_harness_sequence_is_nonempty_and_unambiguous(values):
    with pytest.raises(ValueError):
        validate_harnesses(values)


def test_safe_identifier_components_and_contained_paths(tmp_path):
    assert validate_harnesses([" codex ", "my-harness_2"]) == (
        "codex",
        "my-harness_2",
    )
    assert skill_components("sat.demo", "sat") == ("sat", "demo")
    with pytest.raises(ValueError, match="using group"):
        skill_components("other.demo", "sat")
    child = tmp_path / "child"
    child.mkdir()
    (tmp_path / "internal").symlink_to(child, target_is_directory=True)
    assert contained_path(tmp_path, "internal/test.md") == tmp_path / "internal/test.md"
    for relative in ("../external", tmp_path / "absolute"):
        with pytest.raises(ValueError, match="must stay inside"):
            contained_path(tmp_path, relative)


def test_project_root_uses_real_cwd_registry_in_a_subprocess(tmp_path):
    source_root = project_root()
    _registry(tmp_path)
    nested = tmp_path / "nested" / "deeper"
    nested.mkdir(parents=True)
    env = {**os.environ, "PYTHONPATH": str(source_root / "src")}
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "from cogsecskills.core.locate import project_root; print(project_root())",
        ],
        cwd=nested,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == str(tmp_path.resolve())


def test_unrelated_cwd_pyproject_does_not_override_source_root(tmp_path, monkeypatch):
    expected = project_root()
    (tmp_path / "pyproject.toml").write_text("[project]\nname='unrelated'\n")
    monkeypatch.chdir(tmp_path)
    assert project_root() == expected
