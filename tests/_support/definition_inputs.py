"""Shared real inputs for definition inputs tests."""

from __future__ import annotations

import pytest

from cogsecskills.authoring.author import (
    AuthorError,
    _list_field,
    _quality_list,
    load_definition_file,
    rendered_definition_files,
)

from cogsecskills.authoring.definitions import (
    _definitions_for_write,
    _negative_control_item_is_specific,
    _negative_controls_are_specific,
    _quality_item_is_specific,
    check_definitions,
)

from cogsecskills.core.registry import RegistryEntry

__all__ = [
    "AuthorError",
    "RegistryEntry",
    "_definitions_for_write",
    "_list_field",
    "_negative_control_item_is_specific",
    "_negative_controls_are_specific",
    "_quality_item_is_specific",
    "_quality_list",
    "check_definitions",
    "load_definition_file",
    "pytest",
    "rendered_definition_files",
]
