"""Canonical skill-definition source layer.

The rendered ``skills/**`` tree is useful to humans and harnesses, but a
repo-wide improvement pass needs a durable, compact source of truth. This module
stores one YAML definition per registry entry under ``definitions/<group>/<slug>.yaml``
and checks that the rendered skill files match those definitions.
"""

from __future__ import annotations

from collections import defaultdict
import re
from pathlib import Path
from typing import TypedDict

import yaml

from .author import (
    QUALITY_FIELDS,
    AuthorError,
    default_quality_fields,
    load_definition_file,
    render_definition,
    rendered_definition_files,
)
from .loader import discover_skills, skills_root
from .registry import RegistryEntry, load_registry
from .spec import SkillSpec, SpecError, ToolVerb

DEFINITIONS_DIRNAME = "definitions"
DEFINITION_SUFFIX = ".yaml"
REQUIRED_DEFINITION_FIELDS: tuple[str, ...] = (
    "id",
    "description",
    "tags",
    "triggers",
    "tools",
    "inputs",
    "outputs",
    "references",
    "when_to_use",
    "what_it_produces",
    "key_discipline",
    "workflow_steps",
    "anti_criteria",
    *QUALITY_FIELDS,
)
OPTIONAL_DEFINITION_FIELDS: tuple[str, ...] = ("harness_bindings",)
ALLOWED_DEFINITION_FIELDS: tuple[str, ...] = (
    *REQUIRED_DEFINITION_FIELDS,
    *OPTIONAL_DEFINITION_FIELDS,
)
GENERIC_NEGATIVE_CONTROL_PHRASES = (
    "help me manipulate this audience",
    "optimize this influence operation",
    "assess this material for manipulation indicators",
)
QUALITY_SPECIFICITY_FIELDS = (
    "confidence_rubric",
    "evidence_requirements",
    "privacy_legal_constraints",
    "failure_modes",
)
REUSED_QUALITY_FIELDS = (
    "confidence_rubric",
    "evidence_requirements",
    "privacy_legal_constraints",
)
ALLOWED_SHARED_QUALITY_ITEMS: dict[str, set[str]] = {
    "confidence_rubric": set(),
    "evidence_requirements": set(),
    "privacy_legal_constraints": set(),
}


class DefinitionWriteResult(TypedDict):
    definitions: list[Path]
    rendered: list[str]


def _project_root(root: Path | None = None) -> Path:
    return Path(root) if root is not None else Path(__file__).resolve().parents[2]


def definitions_root(root: Path | None = None) -> Path:
    return _project_root(root) / DEFINITIONS_DIRNAME


def definition_path(skill_id: str, root: Path | None = None) -> Path:
    group, slug = skill_id.split(".", 1)
    return definitions_root(root) / group / f"{slug}{DEFINITION_SUFFIX}"


def load_definitions(root: Path | None = None) -> dict[str, dict]:
    """Load every checked-in canonical definition."""
    base = definitions_root(root)
    if not base.is_dir():
        return {}
    definitions: dict[str, dict] = {}
    for path in sorted(base.glob(f"*/*{DEFINITION_SUFFIX}")):
        definition = load_definition_file(path)
        skill_id = str(definition.get("id", "")).strip()
        if not skill_id:
            raise AuthorError(f"definition {path} missing id")
        if skill_id in definitions:
            raise AuthorError(f"duplicate definition id {skill_id!r}")
        definitions[skill_id] = definition
    return definitions


def _heading_body(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        re.M | re.S,
    )
    match = pattern.search(text)
    return match.group("body").strip() if match else ""


def _bullets_from_section(text: str, heading: str) -> list[str]:
    body = _heading_body(text, heading)
    return [line[2:].strip() for line in body.splitlines() if line.startswith("- ")]


def _workflow_steps(text: str) -> list[dict[str, object]]:
    pattern = re.compile(
        r"^## Step (?P<num>\d+) [—-] (?P<title>.*?) \((?P<verbs>[^)]*)\)\s*$\n"
        r"(?P<body>.*?)(?=^##\s+|\Z)",
        re.M | re.S,
    )
    steps: list[dict[str, object]] = []
    for match in pattern.finditer(text):
        verbs = [
            ToolVerb.coerce(verb.strip()).value
            for verb in match.group("verbs").split(",")
            if verb.strip()
        ]
        steps.append(
            {
                "verbs": verbs,
                "title": match.group("title").strip(),
                "text": match.group("body").strip(),
            }
        )
    return steps


def _anti_criteria(text: str) -> list[str]:
    return _bullets_from_section(text, "Anti-criteria (must NOT happen)")


def _field_or_default(spec: SkillSpec, key: str) -> object:
    raw = getattr(spec, key, None)
    if raw:
        return list(raw) if isinstance(raw, tuple) else raw
    entry = RegistryEntry(
        id=spec.id,
        name=spec.name,
        group=spec.group,
        status=spec.status,
        ageint_topic=spec.ageint_topic,
        summary=spec.summary,
    )
    return default_quality_fields(entry)[key]


def definition_from_skill(spec: SkillSpec, root: Path | None = None) -> dict:
    """Bootstrap a canonical definition from the current rendered skill files."""
    group, slug = spec.id.split(".", 1)
    directory = skills_root(root) / group / slug
    skill_md = (directory / "SKILL.md").read_text(encoding="utf-8")
    workflow_md = (directory / spec.workflow).read_text(encoding="utf-8")
    steps = _workflow_steps(workflow_md)
    if not steps:
        steps = [
            {
                "verbs": sorted(verb.value for verb in spec.verbs) or ["reason"],
                "title": "Apply the method",
                "text": "Apply the skill procedure to the supplied material and write the bounded result.",
            }
        ]
    anti = _anti_criteria(workflow_md) or [
        "Do not fabricate evidence, sources, confidence, or operational guidance."
    ]
    return {
        "id": spec.id,
        "description": spec.description or spec.summary,
        "tags": list(spec.tags),
        "triggers": list(spec.triggers),
        "tools": [
            {"verb": tool.verb.value, "purpose": tool.purpose} for tool in spec.tools
        ],
        "inputs": [
            {
                "name": channel.name,
                "type": channel.type,
                "required": channel.required,
                "description": channel.description,
            }
            for channel in spec.inputs
        ],
        "outputs": [
            {
                "name": channel.name,
                "type": channel.type,
                "description": channel.description,
            }
            for channel in spec.outputs
        ],
        "references": list(spec.references),
        "when_to_use": _bullets_from_section(skill_md, "When to use")
        or list(spec.triggers)
        or [spec.name.lower()],
        "what_it_produces": _bullets_from_section(skill_md, "What it produces")
        or [channel.description or channel.name for channel in spec.outputs]
        or ["a structured analytic product"],
        "key_discipline": _bullets_from_section(skill_md, "Key discipline")
        or ["bind every finding to evidence and defensive use"],
        "workflow_steps": steps,
        "anti_criteria": anti,
        "defensive_boundary": _field_or_default(spec, "defensive_boundary"),
        "misuse_redirect": _field_or_default(spec, "misuse_redirect"),
        "evidence_requirements": _field_or_default(spec, "evidence_requirements"),
        "confidence_rubric": _field_or_default(spec, "confidence_rubric"),
        "uncertainty_handling": _field_or_default(spec, "uncertainty_handling"),
        "privacy_legal_constraints": _field_or_default(
            spec, "privacy_legal_constraints"
        ),
        "failure_modes": _field_or_default(spec, "failure_modes"),
        "negative_controls": _field_or_default(spec, "negative_controls"),
    }


def canonical_definition_text(definition: dict) -> str:
    """Return stable YAML text for a canonical definition."""
    ordered = {
        key: definition.get(key)
        for key in ALLOWED_DEFINITION_FIELDS
        if key in definition
    }
    return yaml.safe_dump(ordered, sort_keys=False, allow_unicode=True)


def _definitions_for_write(root: Path | None = None) -> dict[str, dict]:
    registry = load_registry(root)
    existing = load_definitions(root)
    specs = {spec.id: spec for spec in discover_skills(root)}
    definitions: dict[str, dict] = {}
    for entry in registry.entries:
        if entry.id in existing:
            definitions[entry.id] = existing[entry.id]
        elif entry.id in specs:
            definitions[entry.id] = definition_from_skill(specs[entry.id], root)
    return definitions


def write_definitions(
    root: Path | None = None, harnesses: tuple[str, ...] | None = None
) -> DefinitionWriteResult:
    """Write canonical definitions and render every definition-owned skill."""
    definitions = _definitions_for_write(root)
    written_defs: list[Path] = []
    rendered: list[str] = []
    for skill_id, definition in sorted(definitions.items()):
        path = definition_path(skill_id, root)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(canonical_definition_text(definition), encoding="utf-8")
        written_defs.append(path)
        render_definition(definition, root=root, harnesses=harnesses)
        rendered.append(skill_id)
    return {"definitions": written_defs, "rendered": rendered}


def _definition_tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[a-z0-9]+", text.lower()) if len(token) >= 5
    }


def _specificity_tokens(skill_id: str, entry: RegistryEntry | None) -> set[str]:
    ignored = {"analysis", "review", "assessment"}
    if entry:
        source = f"{entry.name} {skill_id.split('.', 1)[-1].replace('_', ' ')} {entry.summary}"
    else:
        source = skill_id.split(".", 1)[-1].replace("_", " ")
    return _definition_tokens(source) - ignored


def _negative_controls_are_specific(
    skill_id: str, entry: RegistryEntry | None, negative_text: str
) -> bool:
    if entry and entry.name.lower() in negative_text:
        return True
    slug_phrase = skill_id.split(".", 1)[-1].replace("_", " ").lower()
    if slug_phrase in negative_text:
        return True
    if entry and entry.group.lower() in negative_text:
        return True
    return any(token in negative_text for token in _specificity_tokens(skill_id, entry))


def _negative_control_item_is_specific(
    skill_id: str, entry: RegistryEntry | None, item: str
) -> bool:
    lower = item.lower()
    if entry and entry.name.lower() in lower:
        return True
    slug_phrase = skill_id.split(".", 1)[-1].replace("_", " ").lower()
    if slug_phrase in lower:
        return True
    return any(token in lower for token in _specificity_tokens(skill_id, entry))


def _quality_item_is_specific(
    skill_id: str, entry: RegistryEntry | None, item: object
) -> bool:
    lower = str(item).lower()
    if entry and entry.name.lower() in lower:
        return True
    slug_phrase = skill_id.split(".", 1)[-1].replace("_", " ").lower()
    if slug_phrase in lower:
        return True
    return any(token in lower for token in _specificity_tokens(skill_id, entry))


def _normalize_negative_control(item: object) -> str:
    return " ".join(str(item).lower().split())


def _reused_negative_control_findings(definitions: dict[str, dict]) -> list[str]:
    seen: dict[str, list[str]] = defaultdict(list)
    for skill_id, definition in sorted(definitions.items()):
        for item in definition.get("negative_controls", []) or []:
            normalized = _normalize_negative_control(item)
            if normalized:
                seen[normalized].append(skill_id)
    findings: list[str] = []
    for normalized, skill_ids in sorted(seen.items()):
        if len(skill_ids) > 1:
            sample = normalized[:120]
            suffix = "" if len(skill_ids) <= 5 else f", +{len(skill_ids) - 5} more"
            findings.append(
                "negative_control entry reused across definitions: "
                f"{sample!r} ({', '.join(skill_ids[:5])}{suffix})"
            )
    return findings


def _normalize_quality_item(item: object) -> str:
    return " ".join(str(item).lower().split())


def _reused_quality_field_findings(definitions: dict[str, dict]) -> list[str]:
    findings: list[str] = []
    for field in REUSED_QUALITY_FIELDS:
        seen: dict[str, list[str]] = defaultdict(list)
        for skill_id, definition in sorted(definitions.items()):
            for item in definition.get(field, []) or []:
                normalized = _normalize_quality_item(item)
                if normalized:
                    seen[normalized].append(skill_id)
        allowed = ALLOWED_SHARED_QUALITY_ITEMS.get(field, set())
        for normalized, skill_ids in sorted(seen.items()):
            if normalized in allowed or len(skill_ids) <= 1:
                continue
            sample = normalized[:120]
            suffix = "" if len(skill_ids) <= 5 else f", +{len(skill_ids) - 5} more"
            findings.append(
                f"{field} entry reused across definitions: "
                f"{sample!r} ({', '.join(skill_ids[:5])}{suffix})"
            )
    return findings


def _definition_quality_findings(
    skill_id: str, definition: dict, entry: RegistryEntry | None = None
) -> list[str]:
    findings: list[str] = []
    for key in sorted(set(definition) - set(ALLOWED_DEFINITION_FIELDS)):
        findings.append(f"{skill_id}: unknown definition field {key!r}")
    for key in REQUIRED_DEFINITION_FIELDS:
        value = definition.get(key)
        if key == "references" and isinstance(value, list):
            missing = False
        elif isinstance(value, str):
            missing = not value.strip()
        elif isinstance(value, list):
            missing = not any(str(item).strip() for item in value)
        else:
            missing = value is None
        if missing:
            findings.append(f"{skill_id}: definition field {key!r} is missing or empty")
    controls = [
        str(item).strip()
        for item in definition.get("negative_controls", []) or []
        if str(item).strip()
    ]
    negative = "\n".join(item.lower() for item in controls)
    if "unsafe" not in negative or "redirect" not in negative:
        findings.append(
            f"{skill_id}: negative_controls must include unsafe redirect coverage"
        )
    if "safe" not in negative or "defensive" not in negative:
        findings.append(
            f"{skill_id}: negative_controls must include a safe defensive example"
        )
    if not any(
        "unsafe" in item.lower()
        and _negative_control_item_is_specific(skill_id, entry, item)
        for item in controls
    ):
        findings.append(
            f"{skill_id}: negative_controls must include a skill-specific unsafe example"
        )
    if not any(
        ("safe" in item.lower() or "defensive" in item.lower())
        and _negative_control_item_is_specific(skill_id, entry, item)
        for item in controls
    ):
        findings.append(
            f"{skill_id}: negative_controls must include a skill-specific safe defensive example"
        )
    if not _negative_controls_are_specific(skill_id, entry, negative):
        findings.append(
            f"{skill_id}: negative_controls are too generic for the skill or group"
        )
    if any(phrase in negative for phrase in GENERIC_NEGATIVE_CONTROL_PHRASES):
        findings.append(
            f"{skill_id}: negative_controls repeat generic boilerplate examples"
        )
    for field in QUALITY_SPECIFICITY_FIELDS:
        items = [item for item in definition.get(field, []) or [] if str(item).strip()]
        if items and not any(
            _quality_item_is_specific(skill_id, entry, item) for item in items
        ):
            findings.append(f"{skill_id}: {field} must include skill-specific language")
    boundary = str(definition.get("defensive_boundary", "")).lower()
    redirect = str(definition.get("misuse_redirect", "")).lower()
    if "defensive" not in boundary and "defend" not in boundary:
        findings.append(
            f"{skill_id}: defensive_boundary must explicitly state defensive use"
        )
    if "refuse" not in redirect or "defensive" not in redirect:
        findings.append(
            f"{skill_id}: misuse_redirect must refuse and redirect defensively"
        )
    evidence = "\n".join(
        str(item).lower() for item in definition.get("evidence_requirements", [])
    )
    if "evidence" not in evidence or "inference" not in evidence:
        findings.append(
            f"{skill_id}: evidence_requirements must label evidence and inference"
        )
    uncertainty = "\n".join(
        str(item).lower() for item in definition.get("uncertainty_handling", [])
    )
    if "unknown" not in uncertainty or "alternative" not in uncertainty:
        findings.append(
            f"{skill_id}: uncertainty_handling must preserve unknowns and alternatives"
        )
    return findings


def check_definitions(
    root: Path | None = None, harnesses: tuple[str, ...] | None = None
) -> list[str]:
    """Return drift findings for canonical definitions and rendered skill files."""
    findings: list[str] = []
    registry = load_registry(root)
    entries = {entry.id: entry for entry in registry.entries}
    definitions = load_definitions(root)
    expected_ids = set(registry.ids)
    actual_ids = set(definitions)
    for missing in sorted(expected_ids - actual_ids):
        findings.append(
            f"missing canonical definition: {definition_path(missing, root).relative_to(_project_root(root))}"
        )
    for extra in sorted(actual_ids - expected_ids):
        findings.append(f"definition is not in registry: {extra}")
    findings.extend(_reused_negative_control_findings(definitions))
    findings.extend(_reused_quality_field_findings(definitions))

    for skill_id, definition in sorted(definitions.items()):
        expected_path = definition_path(skill_id, root)
        if expected_path.is_file():
            expected_text = canonical_definition_text(definition)
            actual_text = expected_path.read_text(encoding="utf-8")
            if actual_text != expected_text:
                findings.append(
                    f"stale canonical definition: {expected_path.relative_to(_project_root(root))}"
                )
        findings.extend(
            _definition_quality_findings(skill_id, definition, entries.get(skill_id))
        )
        if skill_id not in expected_ids:
            continue
        try:
            rendered = rendered_definition_files(
                definition, root=root, harnesses=harnesses
            )
        except (AuthorError, SpecError, ValueError) as exc:
            findings.append(f"{skill_id}: cannot render definition: {exc}")
            continue
        for path, expected in rendered.items():
            if not path.is_file():
                findings.append(
                    f"{skill_id}: missing rendered file: {path.relative_to(_project_root(root))}"
                )
                continue
            if path.read_text(encoding="utf-8") != expected:
                findings.append(
                    f"{skill_id}: stale rendered file: {path.relative_to(_project_root(root))}"
                )
    return findings
