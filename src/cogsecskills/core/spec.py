"""The generated harness-neutral skill specification (``skill.yaml``).

A :class:`SkillSpec` is the runtime contract for one rendered CogSecSkill. In
the repository authoring flow, canonical YAML under ``definitions/`` owns the
skill substance and renders ``skill.yaml`` plus the companion harness files.
The spec is deliberately declarative: it names *what* the skill does, *what*
tools it is allowed to use (as harness-neutral verbs), and *what* it consumes
and produces — never harness-specific syntax. The per-harness adapter files
translate this one contract into Claude Code / Codex / Hermes idioms.

All parsing is total: malformed input raises :class:`SpecError` with a precise
message rather than producing a half-built object.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence

#: Lifecycle status of a skill within the library.
SKILL_STATUSES: tuple[str, ...] = ("implemented", "stub", "planned")


class SpecError(ValueError):
    """Raised when a ``skill.yaml`` mapping cannot form a valid :class:`SkillSpec`."""


class ToolVerb(str, Enum):
    """Harness-neutral agentic tool-use verbs.

    A skill declares the *capabilities* it needs, not the concrete tools of any
    one harness. Each harness adapter maps these verbs onto its own tools
    (e.g. ``read`` → Claude Code ``Read``/``Grep``; Codex ``shell cat``;
    Hermes ``fs.read``). Keeping the vocabulary closed makes conformance
    checkable and keeps skills portable.
    """

    READ = "read"
    SEARCH = "search"
    WRITE = "write"
    EXEC = "exec"
    REASON = "reason"
    WEB = "web"
    DELEGATE = "delegate"
    ASK = "ask"

    @classmethod
    def coerce(cls, value: object) -> "ToolVerb":
        """Return the :class:`ToolVerb` for ``value`` or raise :class:`SpecError`."""
        if isinstance(value, ToolVerb):
            return value
        if isinstance(value, str):
            try:
                return cls(value.strip().lower())
            except ValueError as exc:  # pragma: no cover - message path tested
                allowed = ", ".join(v.value for v in cls)
                raise SpecError(
                    f"unknown tool verb {value!r}; allowed verbs: {allowed}"
                ) from exc
        raise SpecError(f"tool verb must be a string, got {type(value).__name__}")


@dataclass(frozen=True)
class SkillTool:
    """One declared tool-use capability: a verb plus why the skill needs it."""

    verb: ToolVerb
    purpose: str

    @classmethod
    def from_obj(cls, obj: Any) -> "SkillTool":
        if not isinstance(obj, Mapping):
            raise SpecError(f"tool entry must be a mapping, got {type(obj).__name__}")
        if "verb" not in obj:
            raise SpecError("tool entry missing required key 'verb'")
        purpose = str(obj.get("purpose", "")).strip()
        if not purpose:
            raise SpecError(f"tool {obj.get('verb')!r} missing non-empty 'purpose'")
        return cls(verb=ToolVerb.coerce(obj["verb"]), purpose=purpose)


@dataclass(frozen=True)
class SkillIO:
    """One declared input or output channel for the skill."""

    name: str
    type: str
    required: bool = False
    description: str = ""

    @classmethod
    def from_obj(cls, obj: Any) -> "SkillIO":
        if not isinstance(obj, Mapping):
            raise SpecError(f"io entry must be a mapping, got {type(obj).__name__}")
        name = str(obj.get("name", "")).strip()
        if not name:
            raise SpecError("io entry missing non-empty 'name'")
        required = obj.get("required", False)
        if not isinstance(required, bool):
            # The string "false" is truthy — coercing it would invert the channel's
            # required semantics. Demand a real boolean.
            raise SpecError(f"io {name!r} field 'required' must be a boolean")
        return cls(
            name=name,
            type=str(obj.get("type", "any")).strip() or "any",
            required=required,
            description=str(obj.get("description", "")).strip(),
        )


def _require_text(data: Mapping, key: str) -> str:
    """Return a required, non-empty *string* field — never a coerced non-string.

    Coercion (``str(...)``) would silently accept ``id: 0`` / ``id: []`` / ``id:
    null`` as the strings ``"0"`` / ``"[]"`` / ``"None"``. Require the real type.
    """
    value = data.get(key, None)
    if not isinstance(value, str) or not value.strip():
        raise SpecError(f"skill spec key {key!r} must be a non-empty string")
    return value.strip()


def _as_str_list(value: object, *, field_name: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return (value,) if value.strip() else ()
    if isinstance(value, Sequence):
        items: list[str] = []
        for item in value:
            if not isinstance(item, str):
                raise SpecError(
                    f"field {field_name!r} items must be strings, got "
                    f"{type(item).__name__}"
                )
            if item.strip():
                items.append(item.strip())
        return tuple(items)
    raise SpecError(f"field {field_name!r} must be a string or list of strings")


@dataclass(frozen=True)
class SkillSpec:
    """A parsed, validated harness-neutral skill specification."""

    id: str
    name: str
    group: str
    summary: str
    status: str = "planned"
    version: str = "0.1.0"
    description: str = ""
    ageint_topic: str = ""
    tags: tuple[str, ...] = ()
    triggers: tuple[str, ...] = ()
    tools: tuple[SkillTool, ...] = ()
    inputs: tuple[SkillIO, ...] = ()
    outputs: tuple[SkillIO, ...] = ()
    references: tuple[str, ...] = ()
    defensive_boundary: str = ""
    misuse_redirect: str = ""
    evidence_requirements: tuple[str, ...] = ()
    confidence_rubric: tuple[str, ...] = ()
    uncertainty_handling: tuple[str, ...] = ()
    privacy_legal_constraints: tuple[str, ...] = ()
    failure_modes: tuple[str, ...] = ()
    negative_controls: tuple[str, ...] = ()
    workflow: str = "workflow.md"
    harness: Mapping[str, str] = field(default_factory=dict)

    # --- construction -----------------------------------------------------
    @classmethod
    def from_mapping(cls, data: Any) -> "SkillSpec":
        """Build a :class:`SkillSpec` from a parsed ``skill.yaml`` mapping."""
        if not isinstance(data, Mapping):
            raise SpecError(
                f"skill spec must be a mapping at top level, got {type(data).__name__}"
            )
        skill_id = _require_text(data, "id")
        name = _require_text(data, "name")
        group = _require_text(data, "group")
        summary = _require_text(data, "summary")

        status_raw = data.get("status", "planned")
        if not isinstance(status_raw, str):
            raise SpecError("field 'status' must be a string")
        status = status_raw.strip().lower()
        if status not in SKILL_STATUSES:
            raise SpecError(
                f"status {status!r} invalid; allowed: {', '.join(SKILL_STATUSES)}"
            )

        harness = data.get("harness", {}) or {}
        if not isinstance(harness, Mapping):
            raise SpecError("field 'harness' must be a mapping of harness->path")

        return cls(
            id=skill_id,
            name=name,
            group=group,
            summary=summary,
            status=status,
            version=str(data.get("version", "0.1.0")).strip() or "0.1.0",
            description=str(data.get("description", "")).strip(),
            ageint_topic=str(data.get("ageint_topic", "")).strip(),
            tags=_as_str_list(data.get("tags"), field_name="tags"),
            triggers=_as_str_list(data.get("triggers"), field_name="triggers"),
            tools=tuple(SkillTool.from_obj(t) for t in data.get("tools", []) or []),
            inputs=tuple(SkillIO.from_obj(i) for i in data.get("inputs", []) or []),
            outputs=tuple(SkillIO.from_obj(o) for o in data.get("outputs", []) or []),
            references=_as_str_list(data.get("references"), field_name="references"),
            defensive_boundary=str(data.get("defensive_boundary", "")).strip(),
            misuse_redirect=str(data.get("misuse_redirect", "")).strip(),
            evidence_requirements=_as_str_list(
                data.get("evidence_requirements"), field_name="evidence_requirements"
            ),
            confidence_rubric=_as_str_list(
                data.get("confidence_rubric"), field_name="confidence_rubric"
            ),
            uncertainty_handling=_as_str_list(
                data.get("uncertainty_handling"), field_name="uncertainty_handling"
            ),
            privacy_legal_constraints=_as_str_list(
                data.get("privacy_legal_constraints"),
                field_name="privacy_legal_constraints",
            ),
            failure_modes=_as_str_list(
                data.get("failure_modes"), field_name="failure_modes"
            ),
            negative_controls=_as_str_list(
                data.get("negative_controls"), field_name="negative_controls"
            ),
            workflow=str(data.get("workflow", "workflow.md")).strip() or "workflow.md",
            harness={str(k): str(v) for k, v in harness.items()},
        )

    # --- derived properties ----------------------------------------------
    @property
    def verbs(self) -> frozenset[ToolVerb]:
        """The set of distinct tool verbs this skill is allowed to use."""
        return frozenset(t.verb for t in self.tools)

    @property
    def is_implemented(self) -> bool:
        return self.status == "implemented"
