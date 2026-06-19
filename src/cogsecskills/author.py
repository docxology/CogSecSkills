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
    harness_bindings: {harness: {verb: [tool, note]}}  (optional; defaults used)
"""

from __future__ import annotations

import re
from pathlib import Path

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
        "reason": ("chain-of-thought", "Reason through the steps in-turn."),
        "web": ("`web.fetch`", "Fetch web sources where permitted."),
        "delegate": ("`spawn`", "Delegate a sub-analysis."),
        "ask": ("clarify turn", "Ask the caller to resolve an ambiguity."),
    },
}

_HARNESS_TITLES = {"claude": "Claude Code", "codex": "Codex", "hermes": "Hermes"}


class AuthorError(SpecError):
    """Raised when a definition cannot be rendered into a conforming skill."""


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


def _skill_yaml(
    entry: RegistryEntry, definition: dict, verbs: list[str], harnesses: tuple[str, ...]
) -> str:
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
    return (
        f"# {title} adapter — {entry.name}\n\n"
        f"Binds the neutral `skill.yaml` tool verbs to {title} tools. Follow "
        f"`../workflow.md`; the logic is identical across harnesses.\n\n"
        f"| Neutral verb | {title} tool | Notes |\n"
        f"| --- | --- | --- |\n" + "\n".join(rows) + "\n\n## Invocation\n\n"
        f"Run the workflow steps in order with the caller's context as the source of "
        f"truth. If a required tool is unavailable, state the limitation and downgrade "
        f"the tool-dependent claim to unverified rather than fabricating evidence.\n\n"
        f"## Output contract\n\n"
        f"Return the `skill.yaml` outputs ({outputs}) as Markdown, with a calibrated "
        f"confidence statement. Keep the product defensive and accountable.\n"
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
