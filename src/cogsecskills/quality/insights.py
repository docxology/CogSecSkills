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
from collections import Counter, defaultdict
from pathlib import Path

from cogsecskills.core.config import Config
from cogsecskills.core.loader import (
    SPEC_FILENAME,
    discover_skills,
    load_skill,
    skill_dir,
    skills_root,
)
from cogsecskills.core.quality_constants import (
    ALLOWED_SHARED_QUALITY_ITEMS,
    GENERIC_NEGATIVE_CONTROL_PHRASES,
    QUALITY_FIELD_NAMES,
    QUALITY_SPECIFICITY_FIELDS,
    REUSED_QUALITY_FIELDS,
    SENSITIVE_GROUPS,
    SENSITIVE_TERMS,
    normalize_quality_item,
)
from cogsecskills.core.registry import load_registry
from cogsecskills.core.spec import SkillSpec

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
    by_group: Counter[str] = Counter(e.group for e in registry.entries)
    verb_use: Counter[str] = Counter()
    for spec in specs:
        for verb in spec.verbs:
            verb_use[verb.value] += 1
    topics: Counter[str] = Counter(
        e.ageint_topic for e in registry.entries if e.ageint_topic
    )
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
    specs: list[SkillSpec] = []
    for spec_path in sorted(tree.rglob(SPEC_FILENAME)):
        spec = load_skill(spec_path)
        specs.append(spec)
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
        if spec.status == "implemented":
            findings.extend(_quality_findings(spec, text))
    findings.extend(_reused_quality_field_findings(specs))
    return findings


def _quality_findings(spec: SkillSpec, workflow_text: str) -> list[dict]:
    findings: list[dict] = []
    for field in QUALITY_FIELD_NAMES:
        value = getattr(spec, field)
        if isinstance(value, str):
            empty = not value.strip()
        else:
            empty = not value
        if empty:
            findings.append(
                {
                    "skill_id": spec.id,
                    "level": "warn",
                    "message": f"missing quality field: {field}",
                }
            )

    lower = "\n".join(
        [
            spec.defensive_boundary,
            spec.misuse_redirect,
            "\n".join(spec.negative_controls),
            workflow_text,
        ]
    ).lower()
    if "chain-of-thought" in lower:
        findings.append(
            {
                "skill_id": spec.id,
                "level": "warn",
                "message": "forbidden chain-of-thought wording",
            }
        )
    if "unsafe" not in lower or "redirect" not in lower:
        findings.append(
            {
                "skill_id": spec.id,
                "level": "warn",
                "message": "negative controls must include unsafe redirect coverage",
            }
        )
    negative = "\n".join(spec.negative_controls).lower()
    if "safe" not in negative or "defensive" not in negative:
        findings.append(
            {
                "skill_id": spec.id,
                "level": "warn",
                "message": "negative controls must include a safe defensive example",
            }
        )
    if not _negative_controls_are_specific(spec, negative):
        findings.append(
            {
                "skill_id": spec.id,
                "level": "warn",
                "message": "negative controls are too generic for the skill or group",
            }
        )
    if any(phrase in negative for phrase in GENERIC_NEGATIVE_CONTROL_PHRASES):
        findings.append(
            {
                "skill_id": spec.id,
                "level": "warn",
                "message": "negative controls repeat generic boilerplate examples",
            }
        )
    for field in QUALITY_SPECIFICITY_FIELDS:
        values = getattr(spec, field)
        items = [
            str(item) for item in (values if isinstance(values, tuple) else (values,))
        ]
        if items and not any(_text_is_skill_specific(spec, item) for item in items):
            findings.append(
                {
                    "skill_id": spec.id,
                    "level": "warn",
                    "message": f"{field} must include skill-specific language",
                }
            )
    evidence = "\n".join(spec.evidence_requirements).lower()
    if "evidence" not in evidence or "inference" not in evidence:
        findings.append(
            {
                "skill_id": spec.id,
                "level": "warn",
                "message": "evidence requirements must label evidence and inference",
            }
        )
    uncertainty = "\n".join(spec.uncertainty_handling).lower()
    if "unknown" not in uncertainty or "alternative" not in uncertainty:
        findings.append(
            {
                "skill_id": spec.id,
                "level": "warn",
                "message": "uncertainty handling must preserve unknowns and alternatives",
            }
        )
    if _is_sensitive_skill(spec) and (
        "refuse" not in lower
        or "defensive" not in lower
        or "privacy" not in lower
        or "authorized" not in lower
    ):
        findings.append(
            {
                "skill_id": spec.id,
                "level": "warn",
                "message": "sensitive skill missing defensive/privacy misuse guardrails",
            }
        )
    return findings


def _reused_quality_field_findings(specs: list[SkillSpec]) -> list[dict]:
    findings: list[dict] = []
    implemented = [spec for spec in specs if spec.status == "implemented"]
    for field in REUSED_QUALITY_FIELDS:
        seen: dict[str, list[str]] = defaultdict(list)
        for spec in implemented:
            for item in getattr(spec, field):
                normalized = normalize_quality_item(item)
                if normalized:
                    seen[normalized].append(spec.id)
        allowed = ALLOWED_SHARED_QUALITY_ITEMS.get(field, set())
        for normalized, skill_ids in sorted(seen.items()):
            if normalized in allowed or len(skill_ids) <= 1:
                continue
            sample = normalized[:100]
            suffix = "" if len(skill_ids) <= 5 else f", +{len(skill_ids) - 5} more"
            findings.append(
                {
                    "skill_id": ",".join(skill_ids[:5]),
                    "level": "warn",
                    "message": (
                        f"{field} entry reused across skills: {sample!r} "
                        f"({', '.join(skill_ids[:5])}{suffix})"
                    ),
                }
            )
    return findings


def _negative_controls_are_specific(spec: SkillSpec, negative_text: str) -> bool:
    if spec.name.lower() in negative_text:
        return True
    slug_phrase = spec.id.split(".", 1)[-1].replace("_", " ").lower()
    if slug_phrase in negative_text:
        return True
    name_tokens = {
        token
        for token in _tokens(spec.name)
        if len(token) >= 5 and token not in {"analysis", "review", "assessment"}
    }
    slug_tokens = {
        token
        for token in _tokens(spec.id.split(".", 1)[-1].replace("_", " "))
        if len(token) >= 5 and token not in {"analysis", "review", "assessment"}
    }
    return bool(
        spec.group.lower() in negative_text
        or any(token in negative_text for token in name_tokens | slug_tokens)
    )


def _text_is_skill_specific(spec: SkillSpec, text: str) -> bool:
    lower = text.lower()
    if spec.name.lower() in lower:
        return True
    slug_phrase = spec.id.split(".", 1)[-1].replace("_", " ").lower()
    if slug_phrase in lower:
        return True
    name_tokens = {
        token
        for token in _tokens(spec.name)
        if len(token) >= 5 and token not in {"analysis", "review", "assessment"}
    }
    slug_tokens = {
        token
        for token in _tokens(spec.id.split(".", 1)[-1].replace("_", " "))
        if len(token) >= 5 and token not in {"analysis", "review", "assessment"}
    }
    return any(token in lower for token in name_tokens | slug_tokens)


def _is_sensitive_skill(spec: SkillSpec) -> bool:
    haystack = " ".join(
        [
            spec.id,
            spec.group,
            spec.name,
            spec.summary,
            spec.description,
            " ".join(spec.triggers),
            " ".join(spec.tags),
        ]
    ).lower()
    return spec.group in SENSITIVE_GROUPS or any(
        term in haystack for term in SENSITIVE_TERMS
    )


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
