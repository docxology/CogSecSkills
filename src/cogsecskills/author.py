"""Deterministic authoring: render a full skill folder from a structured definition.

The workflow agents supply SUBSTANCE — a JSON *definition* of a technique (its
tool plan, inputs/outputs, the real step-by-step procedure, anti-criteria). This
module supplies FORMAT — the six conforming files (``skill.yaml``, ``SKILL.md``,
``workflow.md`` and the three harness adapters). Adapters are generated to bind
*exactly* the declared verbs, so every authored skill passes the validator by
construction; there are no format stragglers no matter how many skills are
authored in parallel.

A *definition* is a mapping with these keys (name/group/summary/ageint_topic are
filled from the registry, not the definition):

    id              : str  (must exist in the registry)
    description     : str  (2-4 sentences; falls back to the registry summary)
    tools           : [{verb, purpose}]            (>=1; verbs from the closed set)
    inputs          : [{name, type, required, description}]   (optional)
    outputs         : [{name, type, description}]             (optional)
    triggers        : [str]                          (optional)
    references      : [str]                           (optional)
    when_to_use     : [str]                           (optional)
    what_it_produces: [str]                           (optional)
    key_discipline  : [str]                           (optional)
    workflow_steps  : [{verbs:[str], title, text}]   (>=1)
    anti_criteria   : [str]                           (>=1)
    defensive_boundary     : str                          (optional; defaults used)
    misuse_redirect        : str                          (optional; defaults used)
    evidence_requirements  : [str]                        (optional; defaults used)
    confidence_rubric      : [str]                        (optional; defaults used)
    uncertainty_handling   : [str]                        (optional; defaults used)
    privacy_legal_constraints: [str]                      (optional; defaults used)
    failure_modes          : [str]                        (optional; defaults used)
    negative_controls      : [str]                        (optional; defaults used)
    harness_bindings       : {harness: {verb: [tool, note]}}  (optional; defaults used)
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import TypeAlias

import yaml

from .harness import HARNESSES
from .registry import RegistryEntry, load_registry, registry_path
from .spec import SpecError, ToolVerb

#: Default verb -> (tool, note) bindings per harness. Used when a definition does
#: not override a binding. Every closed-set verb has an entry for every harness,
#: so generated adapters always bind whatever verbs the skill declares.
DEFAULT_BINDINGS: dict[str, dict[str, tuple[str, str]]] = {
    "claude": {
        "read": (
            "`Read` / `Grep`",
            "Read supplied material and locate local evidence.",
        ),
        "search": (
            "`Grep` / `WebSearch` / `Agent`",
            "Search local and external sources.",
        ),
        "write": ("`Write` / final response", "Emit the structured product."),
        "exec": ("`Bash`", "Run commands or the project's own gates."),
        "reason": (
            "private model reasoning",
            "Apply the technique; expose concise rationale.",
        ),
        "web": ("`WebFetch` / `WebSearch`", "Fetch and inspect web sources."),
        "delegate": ("`Agent`", "Fan out independent sub-analyses."),
        "ask": (
            "`AskUserQuestion`",
            "Ask the user only for decisions you cannot resolve.",
        ),
    },
    "codex": {
        "read": ("`shell` (`cat`, `rg`)", "Read supplied files or stdin."),
        "search": (
            "`shell` + optional web",
            "Search the workspace or the web if available.",
        ),
        "write": ("`apply_patch` / stdout", "Persist the product or return Markdown."),
        "exec": ("`shell`", "Run commands or the project's gates."),
        "reason": (
            "private model reasoning",
            "Apply the technique with concise rationale.",
        ),
        "web": ("web / `curl` via `shell`", "Fetch sources where permitted."),
        "delegate": ("sub-task", "Spawn a scoped sub-task."),
        "ask": ("prompt the caller", "Surface a decision to the caller."),
    },
    "hermes": {
        "read": (
            "`fs.read` / context payload",
            "Read supplied files or prompt payload.",
        ),
        "search": ("`web.search` / `kb.query`", "Query the web or a knowledge base."),
        "write": ("`fs.write` / final message", "Write the product or return it."),
        "exec": ("`shell` / exec fn", "Invoke an execution tool when bound."),
        "reason": (
            "private model reasoning",
            "Apply the technique in-turn; expose only concise rationale.",
        ),
        "web": ("`web.fetch`", "Fetch web sources where permitted."),
        "delegate": ("`spawn`", "Delegate a sub-analysis."),
        "ask": ("clarify turn", "Ask the caller to resolve an ambiguity."),
    },
}

_HARNESS_TITLES = {"claude": "Claude Code", "codex": "Codex", "hermes": "Hermes"}


class AuthorError(SpecError):
    """Raised when a definition cannot be rendered into a conforming skill."""


QUALITY_FIELDS: tuple[str, ...] = (
    "defensive_boundary",
    "misuse_redirect",
    "evidence_requirements",
    "confidence_rubric",
    "uncertainty_handling",
    "privacy_legal_constraints",
    "failure_modes",
    "negative_controls",
)
QualityValue: TypeAlias = str | list[str]
QualityFieldMap: TypeAlias = dict[str, QualityValue]


def load_definition_file(path: Path | str) -> dict:
    """Load a JSON or YAML definition file."""
    definition_path = Path(path)
    text = definition_path.read_text(encoding="utf-8")
    if definition_path.suffix.lower() == ".json":
        loaded = json.loads(text)
    else:
        loaded = yaml.safe_load(text)
    if not isinstance(loaded, dict):
        raise AuthorError(f"definition file {definition_path} must contain a mapping")
    return loaded


def _slug(skill_id: str) -> str:
    return skill_id.split(".", 1)[-1]


def _require(definition: dict, key: str) -> object:
    if key not in definition:
        raise AuthorError(f"definition missing required key {key!r}")
    return definition[key]


def _verbs_of(definition: dict) -> list[str]:
    tools = definition.get("tools") or []
    if not isinstance(tools, list) or not tools:
        raise AuthorError("definition needs a non-empty 'tools' list")
    verbs: list[str] = []
    for tool in tools:
        if not isinstance(tool, dict) or "verb" not in tool:
            raise AuthorError(f"each tool needs a 'verb': {tool!r}")
        verb = ToolVerb.coerce(tool["verb"]).value  # validates closed set
        if not str(tool.get("purpose", "")).strip():
            raise AuthorError(f"tool {verb!r} needs a non-empty 'purpose'")
        verbs.append(verb)
    return verbs


def _list_field(definition: dict, key: str, fallback: list[str]) -> list[str]:
    source = definition.get(key)
    if isinstance(source, str):
        values = [source.strip()] if source.strip() else []
    elif isinstance(source, (list, tuple)):
        values = [str(item).strip() for item in source if str(item).strip()]
    else:
        values = []
    return values or fallback


def _text_field(definition: dict, key: str, fallback: str) -> str:
    value = str(definition.get(key, "")).strip()
    return value or fallback


GROUP_QUALITY_PROFILES: dict[str, dict[str, str]] = {
    "cognitive_security": {
        "domain": "cognitive-security defense",
        "protect": "audiences, decision-makers, and public discourse",
        "unsafe": "increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation",
        "safe": "assess supplied material for manipulation indicators and recommend resilience measures",
        "evidence": "content, behavioral, narrative, media, and audience-risk evidence",
        "failure": "mistaking persuasive resonance for verified harm or intent",
    },
    "counterintelligence": {
        "domain": "counterintelligence and analytic-process defense",
        "protect": "analytic teams, collection processes, and institutional trust boundaries",
        "unsafe": "evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft",
        "safe": "review supplied interactions or processes for deception, elicitation, or insider-risk indicators",
        "evidence": "interaction records, process artifacts, deception indicators, and alternative explanations",
        "failure": "turning defensive tradecraft recognition into operational evasion advice",
    },
    "information_environment": {
        "domain": "information-environment monitoring and platform-risk defense",
        "protect": "platform integrity, narrative context, and authentic community behavior",
        "unsafe": "amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement",
        "safe": "map supplied narratives, automation signals, or platform affordance risks for defensive review",
        "evidence": "platform observations, narrative movement, automation signals, and provenance data",
        "failure": "treating engagement volume as proof of authenticity or coordinated intent",
    },
    "osint_integrity": {
        "domain": "OSINT integrity and source-verification defense",
        "protect": "source provenance, privacy, chain of custody, and public-source accountability",
        "unsafe": "dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence",
        "safe": "verify supplied claims, media, sources, or datasets with documented public-source methods",
        "evidence": "source records, custody notes, metadata, corroborating references, and contradiction logs",
        "failure": "overstating identity, location, attribution, or source reliability from incomplete public traces",
    },
    "critical_review": {
        "domain": "critical review and assurance",
        "protect": "evidence quality, implementation integrity, and decision accountability",
        "unsafe": "launder weak claims, fabricate review findings, or produce exploit guidance without mitigation",
        "safe": "review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures",
        "evidence": "artifact excerpts, test output, citations, assumptions, and reproducibility records",
        "failure": "performing theatrical critique without concrete evidence, severity, or remediation path",
    },
    "sat": {
        "domain": "structured analytic technique support",
        "protect": "analytic rigor, alternative hypotheses, and calibrated judgment",
        "unsafe": "force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation",
        "safe": "apply the structured technique to supplied evidence while preserving alternatives and uncertainty",
        "evidence": "hypotheses, assumptions, indicators, evidence tables, and confidence notes",
        "failure": "using the method as a checklist while skipping diagnostic evidence and disconfirming tests",
    },
    "research_methods": {
        "domain": "research-methods and synthesis integrity",
        "protect": "reproducibility, calibrated confidence, and transparent synthesis",
        "unsafe": "cherry-pick sources, fabricate citations, or overstate certainty from weak evidence",
        "safe": "synthesize supplied or authorized sources with explicit confidence and uncertainty labels",
        "evidence": "study designs, source quality, reproducibility artifacts, and uncertainty records",
        "failure": "collapsing heterogeneous evidence into an unsupported single confident conclusion",
    },
}


def _quality_profile(entry: RegistryEntry) -> dict[str, str]:
    return GROUP_QUALITY_PROFILES.get(entry.group, GROUP_QUALITY_PROFILES["sat"])


def default_quality_fields(entry: RegistryEntry) -> QualityFieldMap:
    """Return defensive quality defaults for backward-compatible definitions."""
    profile = _quality_profile(entry)
    name = entry.name
    return {
        "defensive_boundary": (
            f"Use {name} only for {profile['domain']}: recognize, assess, "
            f"document, or defend {profile['protect']}. Do not use this skill "
            f"to {profile['unsafe']}."
        ),
        "misuse_redirect": (
            f"If a request asks {name} to {profile['unsafe']}, refuse that path "
            f"and redirect to the safe defensive form: {profile['safe']}."
        ),
        "evidence_requirements": [
            f"For {name}, bind each finding to a labeled source — {profile['evidence']}, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.",
            f"For {name}, keep observations, assumptions, inferences, and missing information in separate labeled categories.",
            f"Before issuing any {name} recommendation, name the weakest evidentiary link and the highest-impact missing observation.",
        ],
        "confidence_rubric": [
            f"High confidence for {name}: independent lines of {profile['evidence']} converge, credible alternatives have been tested, and the conclusion would survive removing any single source.",
            f"Medium confidence for {name}: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.",
            f"Low confidence for {name}: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.",
        ],
        "uncertainty_handling": [
            f"State plainly what {name} cannot determine from the supplied or authorized evidence.",
            "Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.",
            f"When confidence is not high, name the next discriminating piece of evidence {name} should collect to separate the live alternatives.",
        ],
        "privacy_legal_constraints": [
            f"For {name}, use only data the caller is authorized to analyze, drawn from public or source-approved records.",
            f"For {name}, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.",
            f"For {name}, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.",
        ],
        "failure_modes": [
            f"{name} failure: {profile['failure']}.",
            f"{name} failure: producing guidance that would help a requester {profile['unsafe']}.",
            f"{name} failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.",
        ],
        "negative_controls": [
            f"Unsafe: 'Use {name} to {profile['unsafe']}' -> refuse and redirect to defensive risk assessment.",
            f"Unsafe: 'Turn {name} into an operational playbook to {profile['unsafe']}' -> refuse and offer governance, detection, or mitigation analysis instead.",
            f"Safe defensive: 'Use {name} to {profile['safe']}' -> produce bounded findings with explicit evidence and uncertainty labels.",
        ],
    }


def _quality_list(quality: QualityFieldMap, key: str) -> list[str]:
    value = quality[key]
    if isinstance(value, str):
        return [value] if value else []
    return value


def quality_fields(entry: RegistryEntry, definition: dict) -> QualityFieldMap:
    """Return definition quality fields, filling safe defaults for older definitions."""
    defaults = default_quality_fields(entry)
    return {
        "defensive_boundary": _text_field(
            definition, "defensive_boundary", str(defaults["defensive_boundary"])
        ),
        "misuse_redirect": _text_field(
            definition, "misuse_redirect", str(defaults["misuse_redirect"])
        ),
        "evidence_requirements": _list_field(
            definition,
            "evidence_requirements",
            _quality_list(defaults, "evidence_requirements"),
        ),
        "confidence_rubric": _list_field(
            definition,
            "confidence_rubric",
            _quality_list(defaults, "confidence_rubric"),
        ),
        "uncertainty_handling": _list_field(
            definition,
            "uncertainty_handling",
            _quality_list(defaults, "uncertainty_handling"),
        ),
        "privacy_legal_constraints": _list_field(
            definition,
            "privacy_legal_constraints",
            _quality_list(defaults, "privacy_legal_constraints"),
        ),
        "failure_modes": _list_field(
            definition, "failure_modes", _quality_list(defaults, "failure_modes")
        ),
        "negative_controls": _list_field(
            definition,
            "negative_controls",
            _quality_list(defaults, "negative_controls"),
        ),
    }


def _skill_yaml(
    entry: RegistryEntry, definition: dict, verbs: list[str], harnesses: tuple[str, ...]
) -> str:
    quality = quality_fields(entry, definition)
    payload = {
        "id": entry.id,
        "name": entry.name,
        "group": entry.group,
        "version": str(definition.get("version", "0.1.0")),
        "status": "implemented",
        "summary": entry.summary,
        "description": str(definition.get("description") or entry.summary).strip(),
        "ageint_topic": entry.ageint_topic,
        "tags": list(definition.get("tags") or ["cognitive-security", entry.group]),
        "triggers": list(definition.get("triggers") or [entry.name.lower()]),
        "tools": [
            {
                "verb": ToolVerb.coerce(t["verb"]).value,
                "purpose": str(t["purpose"]).strip(),
            }
            for t in definition["tools"]
        ],
        "inputs": definition.get("inputs")
        or [
            {
                "name": "context",
                "type": "text",
                "required": True,
                "description": "the situation or material to analyse",
            }
        ],
        "outputs": definition.get("outputs")
        or [
            {
                "name": "product",
                "type": "markdown",
                "description": "the structured analytic product",
            }
        ],
        "workflow": "workflow.md",
        "harness": {h: f"harness/{h}.md" for h in harnesses},
        "references": list(definition.get("references") or []),
        **quality,
    }
    return yaml.safe_dump(payload, sort_keys=False, allow_unicode=True)


def _bullets(items: object, fallback: str) -> str:
    source = items if isinstance(items, (list, tuple)) else []
    seq = [str(x).strip() for x in source if str(x).strip()]
    if not seq:
        seq = [fallback]
    return "\n".join(f"- {x}" for x in seq)


def _skill_md(entry: RegistryEntry, definition: dict) -> str:
    description = str(definition.get("description") or entry.summary).strip()
    quality = quality_fields(entry, definition)
    return (
        f"---\n"
        f"name: {entry.id}\n"
        f"description: {entry.summary}\n"
        f"---\n\n"
        f"# {entry.name}\n\n"
        f"{description}\n\n"
        f"## When to use\n\n"
        f"{_bullets(definition.get('when_to_use'), entry.name.lower())}\n\n"
        f"## What it produces\n\n"
        f"{_bullets(definition.get('what_it_produces'), 'a structured analytic product')}\n\n"
        f"## Defensive boundary\n\n"
        f"{quality['defensive_boundary']}\n\n"
        f"## Misuse redirect\n\n"
        f"{quality['misuse_redirect']}\n\n"
        f"## Evidence discipline\n\n"
        f"{_bullets(quality['evidence_requirements'], 'bind every finding to evidence')}\n\n"
        f"## Confidence and uncertainty\n\n"
        f"{_bullets(quality['confidence_rubric'], 'label confidence explicitly')}\n"
        f"{_bullets(quality['uncertainty_handling'], 'state residual uncertainty')}\n\n"
        f"## Privacy, legal, and harm constraints\n\n"
        f"{_bullets(quality['privacy_legal_constraints'], 'use only authorized data')}\n\n"
        f"## Failure modes and negative controls\n\n"
        f"{_bullets(quality['failure_modes'], 'do not overclaim')}\n"
        f"{_bullets(quality['negative_controls'], 'unsafe requests must be redirected')}\n\n"
        f"## Procedure\n\n"
        f"See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).\n\n"
        f"## Key discipline\n\n"
        f"{_bullets(definition.get('key_discipline'), 'bind every finding to evidence')}\n"
    )


def _workflow_md(entry: RegistryEntry, definition: dict, verbs: list[str]) -> str:
    steps = _require(definition, "workflow_steps")
    if not isinstance(steps, list) or not steps:
        raise AuthorError("definition needs a non-empty 'workflow_steps' list")
    lines = [
        f"# Workflow — {entry.name}\n",
        "Harness-neutral agentic procedure. Each step names the tool verb(s) it uses "
        "(see `skill.yaml` → `tools`); a harness adapter binds each verb.\n",
    ]
    for i, step in enumerate(steps, start=1):
        if not isinstance(step, dict):
            raise AuthorError(f"workflow step {i} must be a mapping")
        step_verbs = (
            ", ".join(ToolVerb.coerce(v).value for v in (step.get("verbs") or []))
            or "reason"
        )
        title = str(step.get("title", f"Step {i}")).strip()
        text = str(step.get("text", "")).strip()
        lines.append(f"## Step {i} — {title} ({step_verbs})\n{text}\n")
    quality = quality_fields(entry, definition)
    lines.append(
        "## Evidence requirements\n"
        + "\n".join(
            f"- {item}" for item in _quality_list(quality, "evidence_requirements")
        )
        + "\n"
    )
    lines.append(
        "## Confidence and uncertainty\n"
        + "\n".join(f"- {item}" for item in _quality_list(quality, "confidence_rubric"))
        + "\n"
        + "\n".join(
            f"- {item}" for item in _quality_list(quality, "uncertainty_handling")
        )
        + "\n"
    )
    lines.append(
        "## Privacy, legal, and harm constraints\n"
        + "\n".join(
            f"- {item}" for item in _quality_list(quality, "privacy_legal_constraints")
        )
        + "\n"
    )
    lines.append(
        "## Failure modes\n"
        + "\n".join(f"- {item}" for item in _quality_list(quality, "failure_modes"))
        + "\n"
    )
    lines.append(
        "## Negative controls\n"
        + "\n".join(f"- {item}" for item in _quality_list(quality, "negative_controls"))
        + "\n"
    )
    anti = definition.get("anti_criteria") or []
    if not anti:
        raise AuthorError("definition needs at least one 'anti_criteria' entry")
    lines.append(
        "## Anti-criteria (must NOT happen)\n"
        + "\n".join(f"- {str(a).strip()}" for a in anti)
        + "\n"
    )
    lines.append(
        f"## AGEINT upstream\n`docs/ageint/{entry.ageint_topic or 'cognitive-security'}.md`\n"
    )
    return "\n".join(lines)


def _adapter_md(
    harness: str, entry: RegistryEntry, definition: dict, verbs: list[str]
) -> str:
    overrides = (definition.get("harness_bindings") or {}).get(harness, {})
    known = DEFAULT_BINDINGS.get(harness, {})
    rows = []
    for verb in verbs:
        binding = overrides.get(verb)
        if isinstance(binding, (list, tuple)) and len(binding) == 2:
            tool, note = str(binding[0]), str(binding[1])
        elif verb in known:
            tool, note = known[verb]
        else:
            # Generic fallback for a configured harness with no built-in bindings.
            tool, note = f"{harness} `{verb}` tool", f"Realise the {verb!r} capability."
        rows.append(f"| `{verb}` | {tool} | {note} |")
    title = _HARNESS_TITLES.get(harness, harness.title())
    outputs = (
        ", ".join(str(o.get("name", "")) for o in (definition.get("outputs") or []))
        or "the structured analytic product"
    )
    quality = quality_fields(entry, definition)
    return (
        f"# {title} adapter — {entry.name}\n\n"
        f"Binds the neutral `skill.yaml` tool verbs to {title} tools. Follow "
        f"`../workflow.md`; the logic is identical across harnesses.\n\n"
        f"| Neutral verb | {title} tool | Notes |\n"
        f"| --- | --- | --- |\n" + "\n".join(rows) + "\n\n## Invocation\n\n"
        f"Run the workflow steps in order with the caller's context as the source of "
        f"truth. Enforce the defensive boundary: {quality['defensive_boundary']} "
        f"If a required tool is unavailable, state the limitation and downgrade "
        f"the tool-dependent claim to unverified rather than fabricating evidence. "
        f"If the caller asks for prohibited manipulation, deception, targeting, evasion, "
        f"or operational influence guidance, apply this redirect: {quality['misuse_redirect']}\n\n"
        f"## Output contract\n\n"
        f"Return the `skill.yaml` outputs ({outputs}) as Markdown, with a calibrated "
        f"confidence statement, evidence labels, uncertainty notes, and any relevant "
        f"privacy/legal constraints. Keep the product defensive and accountable.\n"
    )


def render_definition(
    definition: dict, root: Path | None = None, harnesses: tuple[str, ...] | None = None
) -> list[Path]:
    """Render a structured definition into the conforming skill files.

    ``harnesses`` overrides the default harness set (resolve it from
    ``cogsecskills.yaml`` via :func:`cogsecskills.config.load_config`); an adapter
    is generated for each, binding every declared verb.
    """
    if not isinstance(definition, dict):
        raise AuthorError("definition must be a mapping")
    targets = harnesses if harnesses is not None else HARNESSES
    skill_id = str(_require(definition, "id")).strip()
    registry = load_registry(root)
    entry = registry.get(skill_id)
    if entry is None:
        raise AuthorError(f"id {skill_id!r} is not in the registry")
    verbs = _verbs_of(definition)

    base = registry_path(root).parents[1]
    target = base / "skills" / entry.group / _slug(skill_id)
    (target / "harness").mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    files = {
        "skill.yaml": _skill_yaml(entry, definition, verbs, targets),
        "SKILL.md": _skill_md(entry, definition),
        "workflow.md": _workflow_md(entry, definition, verbs),
    }
    for name, content in files.items():
        path = target / name
        path.write_text(content, encoding="utf-8")
        written.append(path)
    for harness in targets:
        path = target / "harness" / f"{harness}.md"
        path.write_text(
            _adapter_md(harness, entry, definition, verbs), encoding="utf-8"
        )
        written.append(path)
    return written


def rendered_definition_files(
    definition: dict, root: Path | None = None, harnesses: tuple[str, ...] | None = None
) -> dict[Path, str]:
    """Return the files ``render_definition`` would write, without mutating disk."""
    if not isinstance(definition, dict):
        raise AuthorError("definition must be a mapping")
    targets = harnesses if harnesses is not None else HARNESSES
    skill_id = str(_require(definition, "id")).strip()
    registry = load_registry(root)
    entry = registry.get(skill_id)
    if entry is None:
        raise AuthorError(f"id {skill_id!r} is not in the registry")
    verbs = _verbs_of(definition)

    base = registry_path(root).parents[1]
    target = base / "skills" / entry.group / _slug(skill_id)
    files = {
        target / "skill.yaml": _skill_yaml(entry, definition, verbs, targets),
        target / "SKILL.md": _skill_md(entry, definition),
        target / "workflow.md": _workflow_md(entry, definition, verbs),
    }
    for harness in targets:
        files[target / "harness" / f"{harness}.md"] = _adapter_md(
            harness, entry, definition, verbs
        )
    return files


def promote_to_implemented(ids: list[str], root: Path | None = None) -> int:
    """Flip the registry status of each id from stub/planned to implemented.

    Targeted per-line text edit so the registry's grouping and comments survive.
    Returns the number of entries changed.
    """
    path = registry_path(root)
    text = path.read_text(encoding="utf-8")
    changed = 0
    for skill_id in ids:
        pattern = re.compile(
            r"(\{id:\s*" + re.escape(skill_id) + r",[^}]*?status:\s*)(stub|planned)"
        )
        new_text, n = pattern.subn(r"\1implemented", text)
        if n:
            text = new_text
            changed += n
    path.write_text(text, encoding="utf-8")
    return changed


def author_batch(
    root: Path | None = None,
    *,
    delete_defs: bool = True,
    promote: bool = True,
    harnesses: tuple[str, ...] | None = None,
) -> dict:
    """Render every ``_def.json`` under the skills tree; report ok/failed.

    Returns ``{"rendered": [...ids], "failed": {id: error}}``.
    """
    import json

    base = registry_path(root).parents[1]
    skills_tree = base / "skills"
    rendered: list[str] = []
    failed: dict[str, str] = {}
    for def_path in sorted(skills_tree.rglob("_def.json")):
        skill_id = f"{def_path.parent.parent.name}.{def_path.parent.name}"
        try:
            definition = json.loads(def_path.read_text(encoding="utf-8"))
            definition.setdefault("id", skill_id)
            render_definition(definition, root, harnesses=harnesses)
            rendered.append(definition["id"])
            if delete_defs:
                def_path.unlink()
        except (AuthorError, SpecError, ValueError, KeyError) as exc:
            failed[skill_id] = str(exc)
    if promote and rendered:
        promote_to_implemented(rendered, root)
    return {"rendered": rendered, "failed": failed}
