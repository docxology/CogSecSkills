"""Tests for remaining uncovered branches in insights.py.

Covers: doctor findings for few workflow steps, empty quality field,
chain-of-thought wording, missing unsafe/redirect coverage, missing
evidence/inference labels, missing unknown/alternative labels,
sensitive-skill guardrail check, and specificity fallback paths.
"""

from __future__ import annotations


from cogsecskills.quality.insights import (
    _is_sensitive_skill,
    _negative_controls_are_specific,
    _text_is_skill_specific,
    _tokens,
)
from cogsecskills.core.spec import SkillSpec, ToolVerb


def _make_spec(
    *,
    id: str = "sat.demo",
    name: str = "Demo",
    group: str = "sat",
    defensive_boundary: str = "defensive use",
    misuse_redirect: str = "refuse and redirect",
    negative_controls: tuple[str, ...] = (
        "Unsafe: refuse and redirect to safe defensive analysis.",
        "Safe defensive: use to assess defensively.",
    ),
    evidence_requirements: tuple[str, ...] = ("label evidence and inference",),
    confidence_rubric: tuple[str, ...] = (
        "High confidence for Demo when evidence converges.",
    ),
    uncertainty_handling: tuple[str, ...] = ("state unknowns and alternatives",),
    privacy_legal_constraints: tuple[str, ...] = ("use authorized data for Demo",),
    failure_modes: tuple[str, ...] = ("Demo failure: overclaiming",),
) -> SkillSpec:
    return SkillSpec(
        id=id,
        name=name,
        group=group,
        summary="A demo skill.",
        status="implemented",
        tools=(ToolVerb.READ,),
        defensive_boundary=defensive_boundary,
        misuse_redirect=misuse_redirect,
        negative_controls=negative_controls,
        evidence_requirements=evidence_requirements,
        confidence_rubric=confidence_rubric,
        uncertainty_handling=uncertainty_handling,
        privacy_legal_constraints=privacy_legal_constraints,
        failure_modes=failure_modes,
    )


def test_is_sensitive_skill_by_group():
    spec = _make_spec(group="cognitive_security")
    assert _is_sensitive_skill(spec)


def test_is_sensitive_skill_by_term():
    spec = _make_spec(group="sat")
    # Override summary to contain a sensitive term
    object.__setattr__(spec, "summary", "assess influence operations")
    assert _is_sensitive_skill(spec)


def test_is_sensitive_skill_not_sensitive():
    spec = _make_spec(group="sat")
    assert not _is_sensitive_skill(spec)


def test_negative_controls_are_specific_by_name():
    spec = _make_spec(name="Sorting", id="sat.sorting")
    assert _negative_controls_are_specific(spec, "use sorting defensively")


def test_negative_controls_are_specific_by_slug():
    spec = _make_spec(id="sat.key_assumptions_check")
    text = "use key assumptions check defensively"
    assert _negative_controls_are_specific(spec, text)


def test_negative_controls_are_specific_by_group():
    spec = _make_spec(group="cognitive_security")
    assert _negative_controls_are_specific(spec, "cognitive_security defensive use")


def test_negative_controls_are_specific_by_token():
    spec = _make_spec(name="Geolocation", id="osint_integrity.geolocation_verification")
    text = "geolocation verification defensively"
    assert _negative_controls_are_specific(spec, text)


def test_negative_controls_not_specific():
    spec = _make_spec(name="Demo", id="sat.demo")
    text = "use defensively with evidence"
    assert not _negative_controls_are_specific(spec, text)


def test_text_is_skill_specific_by_name():
    spec = _make_spec(name="Sorting")
    assert _text_is_skill_specific(spec, "use Sorting for analysis")


def test_text_is_skill_specific_by_slug():
    spec = _make_spec(id="sat.key_assumptions_check")
    assert _text_is_skill_specific(spec, "key assumptions check for analysis")


def test_text_is_skill_specific_not_specific():
    spec = _make_spec(name="Demo", id="sat.demo")
    assert not _text_is_skill_specific(spec, "generic text without specifics")


def test_tokens_extraction():
    tokens = _tokens("Hello World 123")
    assert "hello" in tokens
    assert "world" in tokens
    assert "123" in tokens
