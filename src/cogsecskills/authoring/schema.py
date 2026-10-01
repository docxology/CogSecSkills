"""Type checks for source definitions before rendering their declarative content."""

from __future__ import annotations

from cogsecskills.core.paths import validate_component
from cogsecskills.core.spec import SkillIO, SpecError, ToolVerb


def validate_definition_fields(definition: dict) -> None:
    """Reject malformed present fields while preserving optional defaults."""
    for key in (
        "description",
        "version",
        "defensive_boundary",
        "misuse_redirect",
    ):
        value = definition.get(key)
        if value is not None and not isinstance(value, str):
            raise SpecError(f"definition field {key!r} must be a string")
    for key in (
        "tags",
        "triggers",
        "references",
        "when_to_use",
        "what_it_produces",
        "key_discipline",
        "evidence_requirements",
        "confidence_rubric",
        "uncertainty_handling",
        "privacy_legal_constraints",
        "failure_modes",
        "negative_controls",
    ):
        value = definition.get(key)
        if value is None:
            continue
        if not isinstance(value, list) or not all(
            isinstance(item, str) for item in value
        ):
            raise SpecError(f"definition field {key!r} must be a list of strings")
    for key in ("inputs", "outputs"):
        channels = definition.get(key)
        if channels is None:
            continue
        if not isinstance(channels, list):
            raise SpecError(f"definition field {key!r} must be a list")
        for channel in channels:
            SkillIO.from_obj(channel)
    steps = definition.get("workflow_steps")
    if isinstance(steps, list):
        for index, step in enumerate(steps, 1):
            if isinstance(step, dict):
                for key in ("title", "text"):
                    if key in step and not isinstance(step[key], str):
                        raise SpecError(f"workflow step {index} {key} must be a string")
    bindings = definition.get("harness_bindings")
    if bindings is None:
        return
    if not isinstance(bindings, dict):
        raise SpecError("definition 'harness_bindings' must be a mapping")
    for harness, overrides in bindings.items():
        validate_component(harness, "harness binding name")
        if not isinstance(overrides, dict):
            raise SpecError(f"harness bindings for {harness!r} must be a mapping")
        for verb, binding in overrides.items():
            ToolVerb.coerce(verb)
            if (
                not isinstance(binding, (list, tuple))
                or len(binding) != 2
                or not all(isinstance(part, str) and part.strip() for part in binding)
            ):
                raise SpecError(
                    f"harness binding {harness!r}.{verb} must contain two non-empty strings"
                )
