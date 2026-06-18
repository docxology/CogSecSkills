"""Intelligent affordances over the skill library.

Pure, tested helpers that turn the catalogue into something an agent or human can
navigate quickly:

- :func:`route_query` — given a free-text need, rank the skills that fit it
  (token overlap across name, triggers, tags, summary, group). The "which skill
  should I use?" router.
- :func:`library_stats` — counts by group / status / verb and AGEINT coverage.
- :func:`render_catalogue_markdown` — a navigable Markdown index of all skills,
  grouped, generated from the registry (keeps docs in sync with the catalogue).
- :func:`doctor` — quality lint: flag thin or under-referenced skills against the
  configurable thresholds in :class:`cogsecskills.config.Config`.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from .config import Config
from .loader import SPEC_FILENAME, discover_skills, load_skill, skill_dir, skills_root
from .registry import load_registry
from .spec import SkillSpec

_TOKEN = re.compile(r"[a-z0-9]+")


def _tokens(text: str) -> list[str]:
    return _TOKEN.findall(text.lower())


def _spec_haystack(spec: SkillSpec) -> Counter:
    """Weighted bag of tokens describing a skill (higher weight = stronger signal)."""
    bag: Counter = Counter()
    for token in _tokens(spec.name):
        bag[token] += 4
    for trigger in spec.triggers:
        for token in _tokens(trigger):
            bag[token] += 3
    for tag in spec.tags:
        for token in _tokens(tag):
            bag[token] += 2
    for token in _tokens(spec.summary):
        bag[token] += 1
    for token in _tokens(spec.group.replace("_", " ")):
        bag[token] += 1
    return bag


def route_query(
    query: str, root: Path | None = None, limit: int = 5
) -> list[tuple[SkillSpec, int]]:
    """Rank on-disk skills by relevance to a free-text ``query``.

    Returns up to ``limit`` ``(spec, score)`` pairs, highest score first; only
    skills with a positive score are included.
    """
    q_tokens = set(_tokens(query))
    if not q_tokens:
        return []
    scored: list[tuple[SkillSpec, int]] = []
    for spec in discover_skills(root):
        bag = _spec_haystack(spec)
        score = sum(weight for token, weight in bag.items() if token in q_tokens)
        if score > 0:
            scored.append((spec, score))
    scored.sort(key=lambda pair: (-pair[1], pair[0].id))
    return scored[:limit]


def library_stats(root: Path | None = None) -> dict:
    """Counts across the catalogue and on-disk skills."""
    registry = load_registry(root)
    specs = discover_skills(root)
    by_group = Counter(e.group for e in registry.entries)
    verb_use: Counter = Counter()
    for spec in specs:
        for verb in spec.verbs:
            verb_use[verb.value] += 1
    topics = Counter(e.ageint_topic for e in registry.entries if e.ageint_topic)
    return {
        "registry_total": len(registry),
        "on_disk": len(specs),
        "by_status": registry.status_counts(),
        "by_group": dict(sorted(by_group.items())),
        "verb_usage": dict(sorted(verb_use.items(), key=lambda kv: -kv[1])),
        "ageint_topics": dict(sorted(topics.items())),
        "groups_defined": len(registry.groups),
    }


def render_catalogue_markdown(root: Path | None = None) -> str:
    """Render the full catalogue as a grouped, navigable Markdown index."""
    registry = load_registry(root)
    counts = registry.status_counts()
    lines = [
        "# CogSecSkills — Skill Catalogue",
        "",
        "> Generated from `registry/skills.yaml` by `cogsecskills catalogue --markdown`.",
        "> Do not edit by hand — regenerate after changing the registry.",
        "",
        f"**{len(registry)} skill areas** — "
        + ", ".join(f"{k}: {v}" for k, v in counts.items() if v),
        "",
    ]
    for group_id in sorted({e.group for e in registry.entries}):
        title = registry.groups.get(group_id, group_id)
        rows = registry.by_group(group_id)
        lines.append(f"## {title} (`{group_id}`) — {len(rows)}")
        lines.append("")
        lines.append("| Skill | Status | Summary |")
        lines.append("| --- | --- | --- |")
        for entry in rows:
            slug = entry.id.split(".", 1)[1]
            link = f"[`{entry.id}`](../skills/{group_id}/{slug}/SKILL.md)"
            lines.append(f"| {link} | {entry.status} | {entry.summary} |")
        lines.append("")
    return "\n".join(lines)


def doctor(root: Path | None = None, config: Config | None = None) -> list[dict]:
    """Quality lint: flag skills that fall below the configured quality bar.

    Returns a list of ``{skill_id, level, message}`` findings. Structural
    validity is covered by :func:`cogsecskills.validate.validate_library`; this
    is about *depth*, not conformance.
    """
    cfg = config or Config.defaults()
    findings: list[dict] = []
    tree = skills_root(root)
    if not tree.is_dir():
        return findings
    for spec_path in sorted(tree.rglob(SPEC_FILENAME)):
        spec = load_skill(spec_path)
        directory = skill_dir(spec_path)
        workflow = directory / spec.workflow
        text = workflow.read_text(encoding="utf-8") if workflow.is_file() else ""
        steps = _count_steps(text)
        anti = _count_anti_criteria(text)
        if spec.status == "implemented" and steps < cfg.min_workflow_steps:
            findings.append(
                {
                    "skill_id": spec.id,
                    "level": "warn",
                    "message": f"{steps} workflow steps (< {cfg.min_workflow_steps})",
                }
            )
        if spec.status == "implemented" and anti < cfg.min_anti_criteria:
            findings.append(
                {
                    "skill_id": spec.id,
                    "level": "warn",
                    "message": f"{anti} anti-criteria (< {cfg.min_anti_criteria})",
                }
            )
        if (
            cfg.require_references
            and spec.status == "implemented"
            and not spec.references
        ):
            findings.append(
                {"skill_id": spec.id, "level": "warn", "message": "no references"}
            )
    return findings


def _count_steps(workflow_text: str) -> int:
    """Count procedure steps, recognizing both step formats used in the library.

    The deterministic renderer emits ``## Step N — ...`` headings; the
    hand-authored exemplars use a top-level numbered list (``1. **read** — ...``).
    Count whichever the document uses.
    """
    headings = len(re.findall(r"^##\s+Step\s", workflow_text, flags=re.MULTILINE))
    if headings:
        return headings
    return len(re.findall(r"^\d+\.\s", workflow_text, flags=re.MULTILINE))


def _count_anti_criteria(workflow_text: str) -> int:
    """Count bullet items under an Anti-criteria heading in a workflow doc."""
    count = 0
    in_section = False
    for line in workflow_text.splitlines():
        if line.strip().lower().startswith("## anti-criteria"):
            in_section = True
            continue
        if in_section:
            if line.startswith("## "):
                break
            if line.strip().startswith("- "):
                count += 1
    return count
