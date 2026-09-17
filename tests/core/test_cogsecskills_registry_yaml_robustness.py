"""Regression tests: registry/config YAML errors surface as typed exceptions.

Malformed YAML used to escape as a raw ``yaml.YAMLError`` traceback; the loader
contract (``core/loader.py``) is that malformed input raises the module's
documented error type with a precise, path-prefixed message.
"""

from __future__ import annotations

import pytest
import yaml

from cogsecskills.core.config import load_config
from cogsecskills.core.registry import RegistryEntry, load_registry
from cogsecskills.core.spec import SpecError


def _seed_valid_skills_registry(root) -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n"
        "  - {id: sat.demo, name: Demo Technique, group: sat, status: stub, "
        "summary: A demo technique.}\n",
        encoding="utf-8",
    )


def test_malformed_skills_yaml_raises_specerror(tmp_path):
    skills_file = tmp_path / "registry" / "skills.yaml"
    skills_file.parent.mkdir(parents=True)
    skills_file.write_text("skills: [unclosed\n", encoding="utf-8")
    with pytest.raises(SpecError, match="invalid YAML"):
        load_registry(tmp_path)


def test_malformed_skills_yaml_message_names_the_file(tmp_path):
    skills_file = tmp_path / "registry" / "skills.yaml"
    skills_file.parent.mkdir(parents=True)
    skills_file.write_text("skills: [unclosed\n", encoding="utf-8")
    with pytest.raises(SpecError) as exc_info:
        load_registry(tmp_path)
    assert str(skills_file) in str(exc_info.value)


def test_malformed_groups_yaml_raises_specerror(tmp_path):
    _seed_valid_skills_registry(tmp_path)
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups: {unclosed\n", encoding="utf-8"
    )
    with pytest.raises(SpecError, match="invalid YAML"):
        load_registry(tmp_path)


def test_duplicate_group_id_raises_specerror(tmp_path):
    """A duplicated group id used to silently overwrite its predecessor."""
    _seed_valid_skills_registry(tmp_path)
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n"
        "  - {id: sat, title: First Title}\n"
        "  - {id: sat, title: Second Title}\n",
        encoding="utf-8",
    )
    with pytest.raises(SpecError, match="duplicate group id 'sat'"):
        load_registry(tmp_path)


def test_distinct_group_ids_still_load(tmp_path):
    _seed_valid_skills_registry(tmp_path)
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n  - {id: osint, title: OSINT Integrity}\n",
        encoding="utf-8",
    )
    registry = load_registry(tmp_path)
    assert registry.groups == {"sat": "SAT", "osint": "OSINT Integrity"}


@pytest.mark.parametrize("bad_id", [0, None, ["sat.demo"], ""])
def test_registry_entry_required_keys_must_be_real_strings(bad_id):
    entry = {
        "id": bad_id,
        "name": "Demo Technique",
        "group": "sat",
        "summary": "A demo technique.",
    }
    with pytest.raises(SpecError, match="missing required key 'id'"):
        RegistryEntry.from_obj(entry)


def test_registry_entry_numeric_summary_rejected():
    entry = {
        "id": "sat.demo",
        "name": "Demo Technique",
        "group": "sat",
        "summary": 42,
    }
    with pytest.raises(SpecError, match="missing required key 'summary'"):
        RegistryEntry.from_obj(entry)


def test_registry_entry_valid_strings_still_accepted():
    entry = RegistryEntry.from_obj(
        {
            "id": "sat.demo",
            "name": "Demo Technique",
            "group": "sat",
            "summary": "A demo technique.",
        }
    )
    assert entry.id == "sat.demo"
    assert entry.status == "planned"


def test_registry_entry_non_mapping_rejected():
    with pytest.raises(SpecError, match="must be a mapping"):
        RegistryEntry.from_obj("sat.demo")


def test_load_config_invalid_yaml_raises_valueerror(tmp_path):
    """A malformed config must raise ValueError (docstring contract), not crash."""
    (tmp_path / "cogsecskills.yaml").write_text(
        "harnesses: [unclosed\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="invalid YAML"):
        load_config(tmp_path)


def test_load_config_invalid_yaml_is_not_yamlerscaping(tmp_path):
    """The ValueError wraps the original YAMLError via ``from`` (chained)."""
    (tmp_path / "cogsecskills.yaml").write_text(
        "harnesses: [unclosed\n", encoding="utf-8"
    )
    with pytest.raises(ValueError) as exc_info:
        load_config(tmp_path)
    assert isinstance(exc_info.value.__cause__, yaml.YAMLError)
