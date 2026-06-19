"""Scaffold a planned skill area into a real on-disk skill folder.

Filling the remaining (planned) skill areas is one command each: this reads the
registry entry, creates ``skills/<group>/<slug>/`` and writes the multiharness
file set (``skill.yaml``, ``SKILL.md``, ``workflow.md`` and the three harness
adapters) pre-populated from the catalogue row. The author then deepens the
content; the structure already conforms.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import yaml

from .harness import HARNESSES
from .registry import RegistryEntry, load_registry, registry_path
from .spec import SpecError

#: Default tool plan for a freshly scaffolded skill (authors refine it).
_DEFAULT_TOOLS = [
    {"verb": "read", "purpose": "gather the inputs and context the analysis needs"},
    {"verb": "reason", "purpose": "apply the technique's structured procedure"},
    {"verb": "write", "purpose": "emit the structured analytic product"},
]

_HARNESS_BINDINGS = {
    "claude": {
        "label": "Claude Code tool",
        "read": ("`Read` / `Grep`", "Read supplied files and locate local evidence."),
        "reason": (
            "private model reasoning",
            "Apply the workflow steps and expose only concise rationale in the product.",
        ),
        "write": (
            "`Write` / final response",
            "Emit the structured product, writing a file only when requested.",
        ),
    },
    "codex": {
        "label": "Codex binding",
        "read": (
            "`shell` (`cat`, `sed`, `rg`)",
            "Read supplied files or stdin and capture file:line evidence.",
        ),
        "reason": (
            "private model reasoning",
            "Apply the workflow steps and keep the final rationale concise.",
        ),
        "write": (
            "`apply_patch` / stdout",
            "Persist the product when a path is requested; otherwise return Markdown.",
        ),
    },
    "hermes": {
        "label": "Hermes tool",
        "read": (
            "`fs.read` / context payload",
            "Read supplied files or prompt payloads before analysis.",
        ),
        "reason": (
            "private model reasoning",
            "Apply the workflow steps and expose only the decision rationale.",
        ),
        "write": (
            "`fs.write` / final message",
            "Write the product when a filesystem tool is bound; otherwise return it.",
        ),
    },
}


def _slug_from_id(skill_id: str) -> str:
    return skill_id.split(".", 1)[-1]


def _skill_yaml_payload(entry: RegistryEntry, harnesses: tuple[str, ...]) -> dict:
    return {
        "id": entry.id,
        "name": entry.name,
        "group": entry.group,
        "version": "0.1.0",
        "status": "stub",
        "summary": entry.summary,
        "description": entry.summary,
        "ageint_topic": entry.ageint_topic,
        "tags": ["cognitive-security", entry.group],
        "triggers": [entry.name.lower()],
        "tools": _DEFAULT_TOOLS,
        "inputs": [
            {
                "name": "context",
                "type": "text",
                "required": True,
                "description": "the situation or material to analyse",
            }
        ],
        "outputs": [
            {
                "name": "product",
                "type": "markdown",
                "description": "the structured analytic product",
            }
        ],
        "workflow": "workflow.md",
        "harness": {h: f"harness/{h}.md" for h in harnesses},
        "references": [],
    }


def scaffold_skill(
    skill_id: str,
    root: Path | None = None,
    overwrite: bool = False,
    harnesses: tuple[str, ...] | None = None,
) -> list[Path]:
    """Create the on-disk file set for ``skill_id`` from its registry entry.

    Returns the list of files written. Raises :class:`SpecError` if the id is
    not in the registry, or if files already exist and ``overwrite`` is False.
    ``harnesses`` overrides the default harness set (one adapter per harness).
    """
    targets = harnesses if harnesses is not None else HARNESSES
    registry = load_registry(root)
    entry = registry.get(skill_id)
    if entry is None:
        raise SpecError(f"skill id {skill_id!r} is not in the registry")

    base = registry_path(root).parents[1]
    target = base / "skills" / entry.group / _slug_from_id(entry.id)
    if target.exists():
        if not overwrite:
            raise SpecError(f"skill directory already exists: {target}")
        # Replace, not merge — stale files from a prior partial scaffold must not
        # survive and validate clean.
        shutil.rmtree(target)
    (target / "harness").mkdir(parents=True, exist_ok=True)

    written: list[Path] = []

    spec_file = target / "skill.yaml"
    spec_file.write_text(
        yaml.safe_dump(
            _skill_yaml_payload(entry, targets), sort_keys=False, allow_unicode=True
        ),
        encoding="utf-8",
    )
    written.append(spec_file)

    skill_md = target / "SKILL.md"
    skill_md.write_text(_skill_md(entry), encoding="utf-8")
    written.append(skill_md)

    workflow = target / "workflow.md"
    workflow.write_text(_workflow_md(entry), encoding="utf-8")
    written.append(workflow)

    for harness in targets:
        adapter = target / "harness" / f"{harness}.md"
        adapter.write_text(_adapter_md(entry, harness), encoding="utf-8")
        written.append(adapter)

    return written


def _skill_md(entry: RegistryEntry) -> str:
    return (
        f"---\n"
        f"name: {entry.id}\n"
        f"description: {entry.summary}\n"
        f"---\n\n"
        f"# {entry.name}\n\n"
        f"> Status: **stub** — scaffolded from the registry. Deepen the workflow,\n"
        f"> tool plan, and examples before promoting to `implemented`.\n\n"
        f"{entry.summary}\n\n"
        f"## When to use\n\n"
        f"- {entry.name.lower()}\n\n"
        f"## Procedure\n\nSee [`workflow.md`](workflow.md).\n"
    )


def _workflow_md(entry: RegistryEntry) -> str:
    return (
        f"# Workflow — {entry.name}\n\n"
        f"Harness-neutral agentic procedure. Each step names the tool verb it uses.\n\n"
        f"1. **read** — gather the inputs and context.\n"
        f"2. **reason** — apply the {entry.name} technique.\n"
        f"3. **write** — emit the structured analytic product.\n\n"
        f"AGEINT upstream: {entry.ageint_topic or 'cognitive-security'}\n"
    )


def _adapter_md(entry: RegistryEntry, harness: str) -> str:
    bindings = _HARNESS_BINDINGS.get(harness, {"label": f"{harness} tool"})

    def _binding(verb: str) -> tuple[str, str]:
        val = bindings.get(verb)
        if isinstance(val, tuple) and len(val) == 2:
            return (str(val[0]), str(val[1]))
        return (f"{harness} `{verb}` tool", f"Realise the {verb!r} capability.")

    rows = "\n".join(
        f"| `{tool['verb']}` | {_binding(tool['verb'])[0]} | {_binding(tool['verb'])[1]} |"
        for tool in _DEFAULT_TOOLS
    )
    return (
        f"# {harness.title()} adapter - {entry.name}\n\n"
        f"Maps the neutral `skill.yaml` tool verbs onto {harness} tools for this\n"
        f"scaffolded skill. Follow `../workflow.md`; this adapter binds the verbs\n"
        f"that appear in the current spec.\n\n"
        f"| Neutral verb | {bindings['label']} | Notes |\n"
        f"| --- | --- | --- |\n"
        f"{rows}\n\n"
        f"## Invocation\n\n"
        f"Run the workflow in order with the caller's context as the source of truth.\n"
        f"If a required tool is unavailable, state the limitation and downgrade the\n"
        f"tool-dependent claim to unverified rather than fabricating evidence.\n\n"
        f"## Output contract\n\n"
        f"Return the `skill.yaml` outputs as Markdown. Keep the product defensive,\n"
        f"evidence-bound, and scoped to recognition, assessment, and protection.\n"
    )
