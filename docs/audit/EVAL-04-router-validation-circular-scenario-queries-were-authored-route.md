# EVAL-04: Router 'validation' is circular: scenario queries were authored to route, and routing is only checked against the author's own expectation

|Field|Value|
|---|---|
|Audit ID|`EVAL-04`|
|Lens|`EVAL`|
|Severity|`medium`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/30)|

## Summary
The scenario route gate feeds each fixture query into `route_query` and only checks that the expected skill lands in the top-10 of a weighted token-overlap router — but all 20 queries in `scenarios/defensive_readiness.yaml` contain the expected skill's own display name verbatim (name tokens weight 4, triggers 3), so the check is self-fulfilling: it validates fixture authoring, not routing effectiveness, and no paraphrased/adversarial query corpus exists. Red team adjusted severity from high to medium because `docs/claim-boundaries.md:19-21` explicitly lists 'A live model will select the same skill' under Not Proved and `manuscript/04_artifacts_and_evidence.md:62` says the gates 'do not show that a live runtime will select the same skill'; the claim wording 'fixtures route to expected skills' is literally accurate about the fixtures, though it does not disclose the query-echo construction.

## Evidence
`src/cogsecskills/artifacts/scenarios.py:488-493` (finding cited 483-490; actual 488-493):

```python
def _check_route(base: Path, scenario: Scenario, findings: list[str]) -> None:
    matches = route_query(scenario.query, root=base, limit=10)
    ...
    if scenario.expected_skill not in routed_ids:
```

Router: `src/cogsecskills/quality/insights.py:50-84` — weighted token overlap, `spec.name` tokens weight 4, triggers 3, tags 2. Fixture queries: `scenarios/defensive_readiness.yaml` — every query embeds the expected skill's display name verbatim, e.g. lines 11-13 'Use Analysis of Competing Hypotheses defensively to compare competing hypotheses...' for `sat.analysis_of_competing_hypotheses`.

## Impact
The gate proves only that authored queries — written alongside the token-overlap router, echoing the skill's name/triggers — land the expected skill in top-10 token overlap. This validates authoring discipline, not routing effectiveness. `docs/claim-boundaries.md` correctly lists live-model skill selection as Not Proved, but the scenario gate is still described as proving fixtures 'route to expected skills' in the evidence ladder without disclosing that query text embeds skill identity. One name-free paraphrase exists only in a unit test (`tests/quality/test_cogsecskills_insights.py:89-92`) on a 2-skill synthetic library, not the real 100-skill registry.

## Remediation
Label the route check as 'query-echo self-consistency' in `docs/claim-boundaries.md` (the 'fixtures route to expected skills' row and any README/claim-matrix presentation), and evaluate routing with paraphrased/adversarial queries that do not contain the skill name or triggers — e.g. add a paraphrased query corpus over the real 100-skill registry modeled on the `tests/quality/test_cogsecskills_insights.py:89-92` paraphrase ('rule out competing hypotheses for an event' -> `sat.ach`).

## Audit trail
- Discovered by the EVAL lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Verified: (1) mechanism exists exactly as described — _check_route feeds each fixture query into route_query and only checks expected_skill lands in top-10 of a weighted token-overlap router; (2) all 20 queries in scenarios/defensive_readiness.yaml contain the skill's own name (name tokens weight 4, triggers 3), so the check is self-fulfilling — it validates fixture authoring, not routing effectiveness; no paraphrased/adversarial query corpus exists. Mitigations found that lower severity from high: (a) docs/claim-boundaries.md:19-21 explicitly lists 'A live model will select the same skill' under Not Proved, and manuscript/04_artifacts_and_evidence.md:62 says the gates 'do not show that a live runtime will select the same skill' — the claim wording in claim-boundaries.md:13 ('fixtures route to expected skills') is literally accurate about the fixtures, though it does not disclose that query text echoes skill names; (b) tests/quality/test_cogsecskills_insights.py:89-92 does route one name-free paraphrase ('rule out competing hypotheses for an event' -> sat.ach), but only on a 2-skill synthetic tmp library, not the real 100-skill registry. So the circularity is real and the suggested relabeling is warranted, but the docs' Not-Proved disclaimers and the literal accuracy of the claim reduce it to a medium documentation/eval-hygiene defect, not a broken contract. Fix line-number citation in the finding.
<!-- PR and issue links are added to the Tracking field after filing. -->