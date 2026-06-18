"""Multiharness conformance.

A CogSecSkill is "multiharness" when its single :class:`~cogsecskills.spec.SkillSpec`
loads and is fully expressible under *every* supported agent harness. This module
defines the supported harnesses and the conformance check that proves a spec maps
onto each one — the machine-checkable meaning of "equally validated for Claude
Code, Codex, and Hermes".

The check is deliberately structural, not behavioural: it asserts that (a) the
skill declares an adapter file for each harness, (b) every harness can realise
every tool verb the skill uses, and (c) the neutral spec carries the fields each
harness needs to render an instruction set. Whether the *model* then performs the
task well is a separate (evals) concern.
"""

from __future__ import annotations

from dataclasses import dataclass

from .spec import SkillSpec, ToolVerb

#: Supported agent harnesses, by identifier.
HARNESSES: tuple[str, ...] = ("claude", "codex", "hermes")

#: For each harness, the tool verbs it can realise. All harnesses support the
#: full closed verb vocabulary today; the mapping is explicit so a future harness
#: with a narrower tool surface fails conformance loudly instead of silently.
HARNESS_VERB_SUPPORT: dict[str, frozenset[ToolVerb]] = {
    "claude": frozenset(ToolVerb),
    "codex": frozenset(ToolVerb),
    "hermes": frozenset(ToolVerb),
}


@dataclass(frozen=True)
class HarnessConformance:
    """Result of checking one skill against one harness."""

    harness: str
    has_adapter: bool
    unsupported_verbs: tuple[ToolVerb, ...]

    @property
    def ok(self) -> bool:
        return self.has_adapter and not self.unsupported_verbs


def check_conformance(
    spec: SkillSpec,
    support: dict[str, frozenset[ToolVerb]] | None = None,
    harnesses: tuple[str, ...] | None = None,
) -> dict[str, HarnessConformance]:
    """Return per-harness conformance for ``spec``.

    A harness conforms when the spec declares an adapter path for it and the
    harness supports every tool verb the skill needs. ``support`` overrides the
    module-level :data:`HARNESS_VERB_SUPPORT` map — used by tests to prove the
    verb-support axis is non-vacuous, and the seam a future narrower harness
    plugs into. ``harnesses`` overrides the default harness set (e.g. from
    ``cogsecskills.yaml``); a harness with no entry in the support map is assumed
    to realise the full closed verb vocabulary, so adding one needs only an
    adapter file, not a code change.
    """
    support_map = support if support is not None else HARNESS_VERB_SUPPORT
    targets = harnesses if harnesses is not None else HARNESSES
    full = frozenset(ToolVerb)
    results: dict[str, HarnessConformance] = {}
    for harness in targets:
        supported = support_map.get(harness, full)
        unsupported = tuple(
            verb
            for verb in sorted(spec.verbs, key=lambda v: v.value)
            if verb not in supported
        )
        results[harness] = HarnessConformance(
            harness=harness,
            has_adapter=bool(spec.harness.get(harness, "").strip()),
            unsupported_verbs=unsupported,
        )
    return results


def is_multiharness(spec: SkillSpec) -> bool:
    """True iff ``spec`` conforms to every supported harness."""
    return all(r.ok for r in check_conformance(spec).values())
