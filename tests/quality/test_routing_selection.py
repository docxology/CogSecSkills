"""Closed-catalogue selection controls, including known retrieval failures."""

from pathlib import Path

import pytest
import yaml

from cogsecskills.quality.insights import route_query

ROOT = Path(__file__).resolve().parents[2]
CASES = yaml.safe_load((ROOT / "tests/fixtures/routing_selection.yaml").read_text())[
    "cases"
]
# Counterexamples in this source document observed behavior for comparison runs.
# An improvement in those cases should not fail the software conformance gate.
GATED_CASES = [
    case
    for case in CASES
    if case["disposition"] in {"shortlist", "compare", "exact", "empty"}
]


@pytest.mark.parametrize("case", GATED_CASES, ids=lambda case: case["id"])
def test_selection_controls(case):
    matches = [spec.id for spec, _ in route_query(case["query"], ROOT, limit=5)]
    disposition = case["disposition"]
    if disposition == "empty":
        assert matches == []
    elif disposition == "exact":
        assert matches[0] == case["shortlisted"][0]
    else:
        assert set(case["shortlisted"]).issubset(matches)
