"""Shared quality-policy constants and helpers.

Both the definition-layer checker (:mod:`cogsecskills.authoring.definitions`)
and the on-disk quality lint (:mod:`cogsecskills.quality.insights`) enforce
the same quality policies.  Centralizing the constants and normalization
helpers here prevents the two copies from drifting and keeps each consumer
focused on its own logic.
"""

from __future__ import annotations

#: Quality fields that every ``implemented`` skill must populate.
QUALITY_FIELD_NAMES: tuple[str, ...] = (
    "defensive_boundary",
    "misuse_redirect",
    "evidence_requirements",
    "confidence_rubric",
    "uncertainty_handling",
    "privacy_legal_constraints",
    "failure_modes",
    "negative_controls",
)

#: Phrases that indicate a negative-control entry is generic boilerplate
#: rather than skill-specific defensive language.
GENERIC_NEGATIVE_CONTROL_PHRASES: tuple[str, ...] = (
    "help me manipulate this audience",
    "optimize this influence operation",
    "assess this material for manipulation indicators",
)

#: Quality fields that must contain skill-specific language (not just generic
#: group-level boilerplate).
QUALITY_SPECIFICITY_FIELDS: tuple[str, ...] = (
    "confidence_rubric",
    "evidence_requirements",
    "privacy_legal_constraints",
    "failure_modes",
)

#: Quality fields checked for cross-skill reuse (the same exact entry text
#: appearing verbatim in multiple skills signals boilerplate, not depth).
REUSED_QUALITY_FIELDS: tuple[str, ...] = (
    "confidence_rubric",
    "evidence_requirements",
    "privacy_legal_constraints",
)

#: Items allowed to be shared across skills even in the reused-quality-field
#: check (e.g. genuinely common legal constraints).  Each key maps to a set
#: of normalized strings that are exempt from the reuse finding.
ALLOWED_SHARED_QUALITY_ITEMS: dict[str, set[str]] = {
    "confidence_rubric": set(),
    "evidence_requirements": set(),
    "privacy_legal_constraints": set(),
}

#: Groups whose skills touch sensitive domains and require extra defensive
#: guardrails (privacy, refusal, authorization language).
SENSITIVE_GROUPS: frozenset[str] = frozenset(
    {
        "cognitive_security",
        "counterintelligence",
        "information_environment",
        "osint_integrity",
    }
)

#: Terms that flag a skill as sensitive even outside the sensitive groups.
SENSITIVE_TERMS: tuple[str, ...] = (
    "audience",
    "account",
    "person",
    "platform",
    "influence",
    "deception",
    "attribution",
    "insider",
    "bot",
    "sock",
)


def normalize_quality_item(item: object) -> str:
    """Return a whitespace-normalized lowercase string for reuse comparison."""
    return " ".join(str(item).lower().split())
