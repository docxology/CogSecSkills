"""Generate and check the CogSecSkills quality dashboard.

The dashboard is a deterministic navigation and drift surface. It summarizes
the live registry, rendered skill specs, scenario fixtures, and current TODO
verification lines without claiming live runtime behavior or field efficacy.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TypedDict

from .evals import load_evaluations
from .examples import load_examples
from .manuscript_assets import GENERATED_HEADER, SkillRow, collect_skill_rows
from .registry import load_registry
from .scenarios import SCENARIO_KINDS, load_scenarios, scenario_summary

DASHBOARD_MD_PATH = Path("docs/quality-dashboard.md")
DASHBOARD_JSON_PATH = Path("output/data/quality_dashboard.json")


class DashboardWriteResult(TypedDict):
    markdown: str
    data: str
    skills: int
    scenarios: int
    examples: int


def _project_root(root: Path | None = None) -> Path:
    return Path(root) if root is not None else Path(__file__).resolve().parents[2]


def _clean_cell(value: object) -> str:
    return " ".join(str(value).split()).replace("|", r"\|")


def _verified_state(root: Path) -> list[str]:
    path = root / "TODO.md"
    if not path.is_file():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    collecting = False
    rows: list[str] = []
    for line in lines:
        if line.startswith("## Verified State"):
            collecting = True
            continue
        if collecting and line.startswith("## "):
            break
        if collecting and line.startswith("- "):
            rows.append(line[2:].strip())
    return rows


def _quality_present(row: SkillRow) -> bool:
    fields = (
        row.defensive_boundary,
        row.evidence_discipline,
        row.confidence_anchor,
        row.unsafe_redirect,
        row.safe_defensive_pattern,
    )
    return all(field and field != "not declared" for field in fields)


def _dashboard_payload(root: Path | None = None) -> dict:
    base = _project_root(root)
    rows = collect_skill_rows(base)
    scenarios = load_scenarios(base)
    examples = load_examples(base)
    evaluations = load_evaluations(base)
    registry = load_registry(base)
    scenario_counts = scenario_summary(base)

    scenario_ids_by_skill: dict[str, list[str]] = {}
    scenarios_by_skill: dict[str, list[dict]] = {}
    for scenario in scenarios:
        scenario_ids_by_skill.setdefault(scenario.expected_skill, []).append(
            scenario.id
        )
        scenarios_by_skill.setdefault(scenario.expected_skill, []).append(
            {
                "id": scenario.id,
                "kind": scenario.kind,
                "answer_kind": scenario.expected_answer.answer_kind,
                "section_titles": [
                    section.title for section in scenario.expected_answer.sections
                ],
                "selected_skill_matches": (
                    scenario.expected_answer.selected_skill == scenario.expected_skill
                ),
            }
        )
    examples_by_skill = {example.skill_id: example for example in examples}
    evaluations_by_scenario = {review.scenario_id: review for review in evaluations}

    skill_rows = []
    for row in rows:
        scenario_ids = sorted(scenario_ids_by_skill.get(row.id, []))
        scenario_trace = sorted(
            scenarios_by_skill.get(row.id, []), key=lambda item: item["id"]
        )
        evaluation_ids = [
            scenario_id
            for scenario_id in scenario_ids
            if scenario_id in evaluations_by_scenario
        ]
        worked_example = examples_by_skill.get(row.id)
        skill_rows.append(
            {
                "id": row.id,
                "name": row.name,
                "group": row.group,
                "verbs": list(row.verbs),
                "harnesses": list(row.harnesses),
                "references": row.references_count,
                "quality_capsule_present": _quality_present(row),
                "scenario_ids": scenario_ids,
                "scenario_kinds": [item["kind"] for item in scenario_trace],
                "expected_answer_kinds": [
                    item["answer_kind"] for item in scenario_trace
                ],
                "expected_answer_sections": {
                    item["id"]: item["section_titles"] for item in scenario_trace
                },
                "selected_skill_consistent": all(
                    item["selected_skill_matches"] for item in scenario_trace
                ),
                "worked_example_id": worked_example.skill_id
                if worked_example is not None
                else "",
                "worked_example_source": str(
                    Path("examples/skill-worked-examples.yaml")
                )
                if worked_example is not None
                else "",
                "worked_example_sections": [
                    section.title for section in worked_example.sections
                ]
                if worked_example is not None
                else [],
                "evaluation_scenario_ids": evaluation_ids,
                "scenario_summary_consistent": (
                    len(scenarios) == scenario_counts["count"]
                    and scenario_counts["expected_answers"] == len(scenarios)
                ),
                "claim_boundary_status": "local deterministic fixture only",
                "evidence_ladder": (
                    f"{len(scenario_ids)} scenario(s); "
                    f"{len(evaluation_ids)} eval fixture(s); "
                    f"{'worked example' if worked_example else 'no worked example'}"
                ),
                "source_path": row.source_path,
            }
        )

    scenario_rows = [
        {
            "id": scenario.id,
            "group": scenario.group,
            "kind": scenario.kind,
            "expected_skill": scenario.expected_skill,
            "answer_kind": scenario.expected_answer.answer_kind,
            "selected_skill": scenario.expected_answer.selected_skill,
            "sections": [
                section.title for section in scenario.expected_answer.sections
            ],
        }
        for scenario in scenarios
    ]

    return {
        "summary": {
            "skills": len(rows),
            "groups": len(registry.groups),
            "scenarios": len(scenarios),
            "worked_examples": len(examples),
            "offline_evaluations": len(evaluations),
            "expected_answers": len(
                [scenario for scenario in scenarios if scenario.expected_answer]
            ),
            "scenario_kinds": list(SCENARIO_KINDS),
            "scenario_summary_consistent": (
                scenario_counts["count"] == len(scenarios)
                and scenario_counts["expected_answers"] == len(scenarios)
            ),
        },
        "verified_state": _verified_state(base),
        "skills": skill_rows,
        "scenarios": scenario_rows,
        "worked_examples": [
            {
                "skill_id": example.skill_id,
                "title": example.title,
                "sections": [section.title for section in example.sections],
                "provenance": example.provenance,
            }
            for example in examples
        ],
        "offline_evaluations": [
            {
                "scenario_id": review.scenario_id,
                "selected_skill": review.selected_skill,
                "answer_kind": review.answer_kind,
                "sections": [section.title for section in review.sections],
                "provenance": review.provenance,
            }
            for review in evaluations
        ],
    }


def _render_markdown(payload: dict) -> str:
    summary = payload["summary"]
    lines = [
        GENERATED_HEADER,
        "",
        "# CogSecSkills Quality Dashboard",
        "",
        "This generated dashboard is a local navigation and drift surface. It "
        "summarizes source-owned skills, quality capsules, harness coverage, "
        "scenario coverage, and current verification lines; it is not field "
        "validation.",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Skills | {summary['skills']} |",
        f"| Groups | {summary['groups']} |",
        f"| Scenario fixtures | {summary['scenarios']} |",
        f"| Expected answers | {summary['expected_answers']} |",
        f"| Worked examples | {summary['worked_examples']} |",
        f"| Offline evaluation fixtures | {summary['offline_evaluations']} |",
        "",
        "## Latest Gate Results",
        "",
    ]
    for item in payload["verified_state"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## Evidence Ladder",
            "",
            "| Surface | Local evidence checked | Boundary |",
            "|---|---|---|",
            "| Scenario readiness | Routed safe and unsafe fixtures with expected answers | No live model runtime or field-effectiveness claim |",
            "| Skill worked examples | One deterministic local worked example per skill | Reviewed examples are fixtures, not model transcripts |",
            "| Offline output review | Scenario-linked reviewed answers scored with the analyst-output rubric | Deterministic local fixture only, not benchmark or runtime certification |",
            "| Quality dashboard | Cross-checks quality capsule, scenarios, worked examples, harnesses, references, and source paths | Drift and navigation surface only |",
            "",
            "## Scenario Coverage",
            "",
            "| Scenario | Kind | Expected skill | Answer kind | Sections |",
            "|---|---|---|---|---|",
        ]
    )
    for scenario in payload["scenarios"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{_clean_cell(scenario['id'])}`",
                    _clean_cell(scenario["kind"]),
                    f"`{_clean_cell(scenario['expected_skill'])}`",
                    _clean_cell(scenario["answer_kind"]),
                    _clean_cell(", ".join(scenario["sections"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Skill Quality Rows",
            "",
            "| Skill | Group | Verbs | Harnesses | Refs | Quality capsule | Scenarios | Answer kinds | Eval fixtures | Worked example | Claim boundary | Source |",
            "|---|---|---|---|---:|---|---|---|---|---|---|---|",
        ]
    )
    for row in payload["skills"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{_clean_cell(row['id'])}`",
                    f"`{_clean_cell(row['group'])}`",
                    _clean_cell(", ".join(row["verbs"])),
                    _clean_cell(", ".join(row["harnesses"])),
                    str(row["references"]),
                    "yes" if row["quality_capsule_present"] else "no",
                    _clean_cell(", ".join(row["scenario_ids"]) or "none"),
                    _clean_cell(", ".join(row["expected_answer_kinds"]) or "none"),
                    _clean_cell(", ".join(row["evaluation_scenario_ids"]) or "none"),
                    "yes" if row["worked_example_id"] else "no",
                    _clean_cell(row["claim_boundary_status"]),
                    f"`{_clean_cell(row['source_path'])}`",
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _expected_outputs(root: Path | None = None) -> dict[Path, str]:
    payload = _dashboard_payload(root)
    return {
        DASHBOARD_MD_PATH: _render_markdown(payload),
        DASHBOARD_JSON_PATH: json.dumps(payload, indent=2, sort_keys=True) + "\n",
    }


def _payload_findings(payload: dict) -> list[str]:
    findings: list[str] = []
    summary = payload["summary"]
    if summary["skills"] != 100:
        findings.append(f"expected 100 skills, found {summary['skills']}")
    if summary["groups"] != 7:
        findings.append(f"expected 7 groups, found {summary['groups']}")
    if summary["scenarios"] != 28:
        findings.append(f"expected 28 scenario fixtures, found {summary['scenarios']}")
    if summary["worked_examples"] != 100:
        findings.append(
            f"expected 100 worked examples, found {summary['worked_examples']}"
        )
    if summary["offline_evaluations"] != summary["scenarios"]:
        findings.append(
            "offline evaluation fixtures do not match scenario fixture count"
        )
    if summary["expected_answers"] != summary["scenarios"]:
        findings.append("not every scenario has an expected answer")
    if len({row["group"] for row in payload["skills"]}) != 7:
        findings.append("skill rows do not cover all seven groups")
    scenario_ids = {scenario["id"] for scenario in payload["scenarios"]}
    if len(scenario_ids) != summary["scenarios"]:
        findings.append("scenario ids are missing or duplicated")
    if any(not row["quality_capsule_present"] for row in payload["skills"]):
        findings.append("one or more skills are missing a quality capsule")
    if any(not row["worked_example_id"] for row in payload["skills"]):
        findings.append("one or more skills are missing a worked example")
    if any(
        row["scenario_ids"]
        and set(row["evaluation_scenario_ids"]) != set(row["scenario_ids"])
        for row in payload["skills"]
    ):
        findings.append("one or more scenario-covered skills lack eval fixtures")
    if any(not row["selected_skill_consistent"] for row in payload["skills"]):
        findings.append("one or more scenario selected-skill checks are inconsistent")
    if not summary["scenario_summary_consistent"]:
        findings.append("scenario summary does not match dashboard scenario rows")
    if any(
        row["claim_boundary_status"] != "local deterministic fixture only"
        for row in payload["skills"]
    ):
        findings.append("one or more skills are missing a local claim boundary")
    if not payload["verified_state"]:
        findings.append("verified-state lines are missing from TODO.md")
    return findings


def write_dashboard(root: Path | None = None) -> DashboardWriteResult:
    """Write generated quality dashboard Markdown and JSON."""
    base = _project_root(root)
    outputs = _expected_outputs(base)
    for rel_path, text in outputs.items():
        path = base / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    payload = _dashboard_payload(base)
    return {
        "markdown": str(DASHBOARD_MD_PATH),
        "data": str(DASHBOARD_JSON_PATH),
        "skills": int(payload["summary"]["skills"]),
        "scenarios": int(payload["summary"]["scenarios"]),
        "examples": int(payload["summary"]["worked_examples"]),
    }


def check_dashboard(root: Path | None = None) -> list[str]:
    """Return findings for generated quality-dashboard drift."""
    base = _project_root(root)
    findings = _payload_findings(_dashboard_payload(base))
    for rel_path, expected in _expected_outputs(base).items():
        path = base / rel_path
        if not path.is_file():
            findings.append(f"missing generated dashboard file: {rel_path}")
            continue
        if path.read_text(encoding="utf-8") != expected:
            findings.append(f"stale generated dashboard file: {rel_path}")
    return findings
