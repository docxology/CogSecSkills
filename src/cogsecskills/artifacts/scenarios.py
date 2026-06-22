"""Deterministic defensive-scenario readiness checks.

The scenario gate is intentionally repo-local. It does not call an external
model runtime or claim field effectiveness; it checks that curated defensive
requests route to the expected skill and that the referenced skill carries the
quality, evidence, output, expected-response, expected-answer, and redirect
metadata needed by an agent harness.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, TypedDict

import yaml

from cogsecskills.quality.insights import route_query
from cogsecskills.core.loader import discover_skills, skills_root
from cogsecskills.core.registry import load_registry
from cogsecskills.core.spec import SkillSpec

SCENARIOS_DIRNAME = "scenarios"
SCENARIO_FILENAME = "defensive_readiness.yaml"
SCENARIO_KINDS = ("safe_defensive", "unsafe_redirect")

# These phrases indicate that a fixture is asking for operational misuse detail
# instead of a bounded refusal/defensive transformation probe.
OPERATIONAL_MISUSE_PHRASES = (
    "step-by-step",
    "step by step",
    "operational playbook",
    "target list",
    "private address",
    "credential",
    "bypass access",
    "evade moderation",
    "evade detection",
    "bot farm",
    "sockpuppet network",
    "deanonymize",
    "dox",
    "exploit payload",
    "phishing",
    "harass",
    "microtarget",
)


@dataclass(frozen=True)
class ExpectedResponse:
    """Expected answer-shape contract for one deterministic scenario."""

    required_sections: tuple[str, ...]
    must_include_terms: tuple[str, ...]
    must_exclude_terms: tuple[str, ...]


@dataclass(frozen=True)
class AnswerSection:
    """One expected-answer section."""

    title: str
    body: str


@dataclass(frozen=True)
class ExpectedAnswer:
    """Reviewed local expected-answer fixture for one scenario."""

    selected_skill: str
    answer_kind: str
    sections: tuple[AnswerSection, ...]
    rubric_scores: dict[str, int]


@dataclass(frozen=True)
class Scenario:
    """One curated repository-local readiness fixture."""

    id: str
    group: str
    kind: str
    query: str
    expected_skill: str
    expected_output_terms: tuple[str, ...]
    required_quality_terms: tuple[str, ...]
    expected_response: ExpectedResponse
    expected_answer: ExpectedAnswer


class ScenarioSummary(TypedDict):
    count: int
    expected_answers: int
    kinds: list[str]
    by_group: dict[str, dict[str, int]]


ANSWER_KINDS = {
    "safe_defensive": "defensive_output",
    "unsafe_redirect": "refusal_redirect",
}

RUBRIC_KEYS = (
    "skill_fit",
    "evidence_labeling",
    "uncertainty",
    "defensive_boundary",
    "output_usefulness",
)


def _project_root(root: Path | None = None) -> Path:
    return Path(root) if root is not None else Path(__file__).resolve().parents[3]


def scenario_path(root: Path | None = None) -> Path:
    """Return the canonical scenario fixture path."""
    return _project_root(root) / SCENARIOS_DIRNAME / SCENARIO_FILENAME


def _as_text_list(value: object, *, field: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return (value.strip(),) if value.strip() else ()
    if isinstance(value, Mapping):
        raise ValueError(f"{field} must be a string or list of strings")
    if isinstance(value, Iterable):
        items: list[str] = []
        for item in value:
            text = str(item).strip()
            if text:
                items.append(text)
        return tuple(items)
    raise ValueError(f"{field} must be a string or list of strings")


def _expected_response_from_mapping(
    obj: Any, *, path: Path, scenario_id: str
) -> ExpectedResponse:
    if not isinstance(obj, Mapping):
        raise ValueError(
            f"{path}: scenario {scenario_id!r} expected_response must be a mapping"
        )
    return ExpectedResponse(
        required_sections=_as_text_list(
            obj.get("required_sections"), field="expected_response.required_sections"
        ),
        must_include_terms=_as_text_list(
            obj.get("must_include_terms"), field="expected_response.must_include_terms"
        ),
        must_exclude_terms=_as_text_list(
            obj.get("must_exclude_terms"), field="expected_response.must_exclude_terms"
        ),
    )


def _answer_sections_from_obj(
    obj: object, *, path: Path, scenario_id: str
) -> tuple[AnswerSection, ...]:
    if not isinstance(obj, list) or not obj:
        raise ValueError(
            f"{path}: scenario {scenario_id!r} expected_answer.sections must be "
            "a non-empty list"
        )
    sections: list[AnswerSection] = []
    for index, item in enumerate(obj, start=1):
        if not isinstance(item, Mapping):
            raise ValueError(
                f"{path}: scenario {scenario_id!r} expected_answer.sections[{index}] "
                "must be a mapping"
            )
        title = str(item.get("title", "")).strip()
        body = str(item.get("body", "")).strip()
        if not title or not body:
            raise ValueError(
                f"{path}: scenario {scenario_id!r} expected_answer.sections[{index}] "
                "must include title and body"
            )
        sections.append(AnswerSection(title=title, body=body))
    return tuple(sections)


def _rubric_scores_from_obj(
    obj: object, *, path: Path, scenario_id: str
) -> dict[str, int]:
    if not isinstance(obj, Mapping):
        raise ValueError(
            f"{path}: scenario {scenario_id!r} expected_answer.rubric_scores "
            "must be a mapping"
        )
    scores: dict[str, int] = {}
    for key in RUBRIC_KEYS:
        value = obj.get(key)
        if not isinstance(value, int):
            raise ValueError(
                f"{path}: scenario {scenario_id!r} expected_answer.rubric_scores."
                f"{key} must be an integer"
            )
        scores[key] = value
    return scores


def _expected_answer_from_mapping(
    obj: Any, *, path: Path, scenario_id: str
) -> ExpectedAnswer:
    if not isinstance(obj, Mapping):
        raise ValueError(
            f"{path}: scenario {scenario_id!r} expected_answer must be a mapping"
        )
    selected_skill = str(obj.get("selected_skill", "")).strip()
    answer_kind = str(obj.get("answer_kind", "")).strip()
    if not selected_skill or not answer_kind:
        raise ValueError(
            f"{path}: scenario {scenario_id!r} expected_answer must include "
            "selected_skill and answer_kind"
        )
    return ExpectedAnswer(
        selected_skill=selected_skill,
        answer_kind=answer_kind,
        sections=_answer_sections_from_obj(
            obj.get("sections"), path=path, scenario_id=scenario_id
        ),
        rubric_scores=_rubric_scores_from_obj(
            obj.get("rubric_scores"), path=path, scenario_id=scenario_id
        ),
    )


def _scenario_from_mapping(obj: Any, *, path: Path) -> Scenario:
    if not isinstance(obj, Mapping):
        raise ValueError(f"{path}: scenario entry must be a mapping")
    required = ("id", "group", "kind", "query", "expected_skill")
    missing = [key for key in required if not str(obj.get(key, "")).strip()]
    if missing:
        raise ValueError(
            f"{path}: scenario missing required fields: {', '.join(missing)}"
        )
    kind = str(obj["kind"]).strip()
    if kind not in SCENARIO_KINDS:
        raise ValueError(
            f"{path}: scenario {obj['id']!r} kind {kind!r} must be one of "
            f"{', '.join(SCENARIO_KINDS)}"
        )
    scenario_id = str(obj["id"]).strip()
    return Scenario(
        id=scenario_id,
        group=str(obj["group"]).strip(),
        kind=kind,
        query=str(obj["query"]).strip(),
        expected_skill=str(obj["expected_skill"]).strip(),
        expected_output_terms=_as_text_list(
            obj.get("expected_output_terms"), field="expected_output_terms"
        ),
        required_quality_terms=_as_text_list(
            obj.get("required_quality_terms"), field="required_quality_terms"
        ),
        expected_response=_expected_response_from_mapping(
            obj.get("expected_response"), path=path, scenario_id=scenario_id
        ),
        expected_answer=_expected_answer_from_mapping(
            obj.get("expected_answer"), path=path, scenario_id=scenario_id
        ),
    )


def load_scenarios(root: Path | None = None) -> list[Scenario]:
    """Load deterministic defensive-scenario fixtures."""
    path = scenario_path(root)
    if not path.is_file():
        raise ValueError(
            f"missing scenario fixture: {path.relative_to(_project_root(root))}"
        )
    loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(loaded, Mapping):
        raise ValueError(f"{path}: top level must be a mapping")
    raw_scenarios = loaded.get("scenarios")
    if not isinstance(raw_scenarios, list) or not raw_scenarios:
        raise ValueError(f"{path}: 'scenarios' must be a non-empty list")
    return [_scenario_from_mapping(item, path=path) for item in raw_scenarios]


def scenario_summary(root: Path | None = None) -> ScenarioSummary:
    """Return small machine-readable counts for the scenario fixture set."""
    scenarios = load_scenarios(root)
    by_group: dict[str, dict[str, int]] = {}
    for scenario in scenarios:
        group_counts = by_group.setdefault(
            scenario.group, {kind: 0 for kind in SCENARIO_KINDS}
        )
        group_counts[scenario.kind] += 1
    return {
        "count": len(scenarios),
        "expected_answers": len(scenarios),
        "kinds": list(SCENARIO_KINDS),
        "by_group": dict(sorted(by_group.items())),
    }


def check_scenarios(root: Path | None = None) -> list[str]:
    """Return findings for deterministic scenario-readiness drift."""
    base = _project_root(root)
    findings: list[str] = []
    try:
        scenarios = load_scenarios(base)
    except ValueError as exc:
        return [str(exc)]

    registry = load_registry(base)
    groups = set(registry.groups)
    specs = {spec.id: spec for spec in discover_skills(base)}

    seen_ids: set[str] = set()
    coverage: dict[str, set[str]] = {group: set() for group in groups}
    for scenario in scenarios:
        if scenario.id in seen_ids:
            findings.append(f"{scenario.id}: duplicate scenario id")
            continue
        seen_ids.add(scenario.id)
        if scenario.group not in groups:
            findings.append(f"{scenario.id}: unknown group {scenario.group!r}")
            continue
        coverage[scenario.group].add(scenario.kind)

        _check_scenario_text(scenario, findings)
        _check_expected_response(scenario, findings)
        _check_expected_answer(scenario, findings)
        spec = specs.get(scenario.expected_skill)
        if spec is None:
            findings.append(
                f"{scenario.id}: expected skill is not implemented on disk: "
                f"{scenario.expected_skill}"
            )
            continue
        if spec.group != scenario.group:
            findings.append(
                f"{scenario.id}: expected skill group {spec.group!r} does not match "
                f"scenario group {scenario.group!r}"
            )
        _check_route(base, scenario, findings)
        _check_spec_contract(base, scenario, spec, findings)

    for group in sorted(groups):
        missing_kinds = set(SCENARIO_KINDS) - coverage.get(group, set())
        for kind in sorted(missing_kinds):
            findings.append(f"{group}: missing {kind} scenario")
    return findings


def _check_scenario_text(scenario: Scenario, findings: list[str]) -> None:
    lower = scenario.query.lower()
    for phrase in OPERATIONAL_MISUSE_PHRASES:
        if phrase in lower:
            findings.append(
                f"{scenario.id}: scenario query contains operational misuse detail "
                f"{phrase!r}"
            )
    if scenario.kind == "safe_defensive":
        if "defensive" not in lower and "authorized" not in lower:
            findings.append(
                f"{scenario.id}: safe scenario must name defensive or authorized use"
            )
    if scenario.kind == "unsafe_redirect":
        if "unsafe" not in lower and "misuse" not in lower:
            findings.append(
                f"{scenario.id}: unsafe scenario must name unsafe or misuse framing"
            )
        if "redirect" not in lower and "refuse" not in lower:
            findings.append(
                f"{scenario.id}: unsafe scenario must request refusal or redirect handling"
            )


def _check_expected_response(scenario: Scenario, findings: list[str]) -> None:
    contract = scenario.expected_response
    if len(contract.required_sections) < 3:
        findings.append(
            f"{scenario.id}: expected response must declare at least 3 sections"
        )
    if len(contract.must_include_terms) < 4:
        findings.append(
            f"{scenario.id}: expected response must declare at least 4 include terms"
        )
    if len(contract.must_exclude_terms) < 2:
        findings.append(
            f"{scenario.id}: expected response must declare at least 2 exclude terms"
        )

    sections = {section.lower() for section in contract.required_sections}
    if len(sections) != len(contract.required_sections):
        findings.append(f"{scenario.id}: expected response repeats section labels")

    response_text = " ".join(
        (
            *contract.required_sections,
            *contract.must_include_terms,
            *contract.must_exclude_terms,
        )
    ).lower()
    expected_basics = {"evidence", "uncertainty", "confidence"}
    if scenario.kind == "safe_defensive":
        expected_basics |= {"defensive"}
    if scenario.kind == "unsafe_redirect":
        expected_basics |= {"refuse", "redirect", "safe"}
    for term in sorted(expected_basics):
        if term not in response_text:
            findings.append(
                f"{scenario.id}: expected response term {term!r} is missing"
            )

    if not any(
        term.lower() in response_text for term in scenario.expected_output_terms
    ):
        findings.append(
            f"{scenario.id}: expected response does not name any expected output term"
        )
    for term in scenario.required_quality_terms:
        if term.lower() not in response_text:
            findings.append(
                f"{scenario.id}: expected response does not name quality term {term!r}"
            )


def _check_expected_answer(scenario: Scenario, findings: list[str]) -> None:
    answer = scenario.expected_answer
    if answer.selected_skill != scenario.expected_skill:
        findings.append(
            f"{scenario.id}: expected answer selected_skill {answer.selected_skill!r} "
            f"does not match expected_skill {scenario.expected_skill!r}"
        )

    expected_kind = ANSWER_KINDS[scenario.kind]
    if answer.answer_kind != expected_kind:
        findings.append(
            f"{scenario.id}: expected answer kind {answer.answer_kind!r} must be "
            f"{expected_kind!r}"
        )

    for key in RUBRIC_KEYS:
        if answer.rubric_scores.get(key) != 2:
            findings.append(f"{scenario.id}: expected answer rubric {key} must be 2")

    titles = [section.title.strip().lower() for section in answer.sections]
    if len(titles) != len(set(titles)):
        findings.append(f"{scenario.id}: expected answer repeats section titles")
    if len(answer.sections) < 3:
        findings.append(
            f"{scenario.id}: expected answer must include at least 3 sections"
        )

    answer_text = " ".join(
        [
            *(section.title for section in answer.sections),
            *(section.body for section in answer.sections),
        ]
    ).lower()
    required_terms = {
        "evidence",
        "inference",
        "gap",
        "confidence",
        "uncertainty",
    }
    if scenario.kind == "safe_defensive":
        required_terms |= {"defensive"}
    if scenario.kind == "unsafe_redirect":
        required_terms |= {"refuse", "redirect", "safe"}
    required_terms |= {term.lower() for term in scenario.required_quality_terms}
    required_terms |= {term.lower() for term in scenario.expected_output_terms}
    for term in sorted(required_terms):
        if term not in answer_text:
            findings.append(f"{scenario.id}: expected answer term {term!r} is missing")

    for phrase in OPERATIONAL_MISUSE_PHRASES:
        if phrase in answer_text:
            findings.append(
                f"{scenario.id}: expected answer contains operational misuse detail "
                f"{phrase!r}"
            )


def _check_route(base: Path, scenario: Scenario, findings: list[str]) -> None:
    matches = route_query(scenario.query, root=base, limit=10)
    routed_ids = [spec.id for spec, _score in matches]
    if scenario.expected_skill not in routed_ids:
        findings.append(
            f"{scenario.id}: expected skill {scenario.expected_skill} not in top "
            f"10 route matches ({', '.join(routed_ids) or 'none'})"
        )


def _check_spec_contract(
    base: Path, scenario: Scenario, spec: SkillSpec, findings: list[str]
) -> None:
    if spec.status != "implemented":
        findings.append(f"{scenario.id}: expected skill {spec.id} is not implemented")
    directory = skills_root(base) / spec.group / spec.id.split(".", 1)[-1]
    workflow = directory / spec.workflow
    if not workflow.is_file():
        findings.append(f"{scenario.id}: expected workflow missing for {spec.id}")
    elif (
        len(
            [
                line
                for line in workflow.read_text(encoding="utf-8").splitlines()
                if line.startswith("## Step ")
            ]
        )
        < 3
    ):
        findings.append(f"{scenario.id}: expected workflow has fewer than 3 steps")

    output_text = " ".join(
        f"{channel.name} {channel.description}" for channel in spec.outputs
    ).lower()
    for term in scenario.expected_output_terms:
        if term.lower() not in output_text:
            findings.append(
                f"{scenario.id}: expected output term {term!r} missing from {spec.id}"
            )

    quality_text = " ".join(
        [
            spec.defensive_boundary,
            spec.misuse_redirect,
            " ".join(spec.evidence_requirements),
            " ".join(spec.confidence_rubric),
            " ".join(spec.uncertainty_handling),
            " ".join(spec.privacy_legal_constraints),
            " ".join(spec.failure_modes),
            " ".join(spec.negative_controls),
        ]
    ).lower()
    required = {"defensive", "evidence", "inference", "unknown", "alternative"}
    if scenario.kind == "unsafe_redirect":
        required |= {"unsafe", "refuse", "redirect"}
    if scenario.kind == "safe_defensive":
        required |= {"safe"}
    required |= {term.lower() for term in scenario.required_quality_terms}
    for term in sorted(required):
        if term not in quality_text:
            findings.append(
                f"{scenario.id}: quality term {term!r} missing from {spec.id}"
            )

    adapter_paths = set(spec.harness.values())
    for harness, rel_path in sorted(spec.harness.items()):
        adapter = directory / rel_path
        if not adapter.is_file():
            findings.append(
                f"{scenario.id}: harness adapter {harness!r} missing for {spec.id}"
            )
    if not adapter_paths:
        findings.append(f"{scenario.id}: expected skill {spec.id} declares no adapters")
