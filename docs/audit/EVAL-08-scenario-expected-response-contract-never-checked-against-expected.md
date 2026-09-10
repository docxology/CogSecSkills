# EVAL-08: Scenario expected_response contract is never checked against the expected answer that supposedly satisfies it

|Field|Value|
|---|---|
|Audit ID|`EVAL-08`|
|Lens|`EVAL`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
`_check_expected_response` validates the contract's self-declared term counts and `_check_expected_answer` validates the answer against its own term/rubric lists, but nothing cross-checks that the authored expected answer satisfies the scenario's own `required_sections`/term lists — the 'expected response-shape contract' is two independently authored YAML blobs with no join. The mismatch is not an isolated case: every scenario pairs a bespoke 4-section contract with a generic 3-section answer (e.g. `sat-ach-safe` requires an 'Analyst next checks' section its own expected answer never contains). Verdict ADJUSTED with corrected line citations; severity low is correct because the blast radius is authored-fixture integrity only — nothing downstream consumes `required_sections` against real answers.

## Evidence
`scenarios/defensive_readiness.yaml:16-17` (finding cited 31-33; line refs wrong):

```yaml
expected_response:
  required_sections: [Defensive purpose, Evidence matrix, Confidence and uncertainty, Analyst next checks]
```

The paired `expected_answer:` begins at line 20 and contains exactly three sections (Defensive purpose, Evidence matrix, Confidence and uncertainty) ending ~line 46, with 'Analyst next checks' nowhere in it. `src/cogsecskills/artifacts/scenarios.py:378-426` — `_check_expected_response` validates only the contract's own term lists ('response_text' is built from required_sections+must_include_terms+must_exclude_terms, lines 398-403); `scenarios.py:429-456` — `_check_expected_answer` validates the answer only against ANSWER_KINDS/rubric/required_terms and never reads `scenario.expected_response.required_sections` or its term lists. The two checks share zero state; no gate or test enforces coverage (`tests/artifacts/test_cogsecskills_scenarios.py:334-347`, `test_cogsecskills_scenarios_branches.py`, `test_cogsecskills_scenarios_coverage.py` all mutate `required_sections` and only assert contract-term findings).

## Impact
The response-shape contract could be violated by its own paired expected answer without any gate noticing — here it is violated systematically, in every scenario. This is authored-fixture hygiene rather than a runtime defect (nothing downstream consumes `required_sections` against real answers, per the `scenarios.py` header stating fixtures 'do not call external model runtimes'), but the contract described in `docs/claim-boundaries.md` ('include expected response-shape and expected-answer contracts') is not actually joined, weakening fixture integrity as evidence of contract coherence.

## Remediation
Add a cross-check in `src/cogsecskills/artifacts/scenarios.py` (alongside `_check_expected_answer`, lines 429-456): expected_answer section titles must cover `scenario.expected_response.required_sections`, and the answer text must satisfy `must_include_terms` / avoid `must_exclude_terms`. Then reconcile the systematically inconsistent fixtures in `scenarios/defensive_readiness.yaml` — either align each 4-section contract with its paired 3-section answer or add the missing sections.

## Audit trail
- Discovered by the EVAL lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Checked: (1) the cited contract and answer exist and the sat-ach-safe mismatch is real — required_sections lists 4 sections including 'Analyst next checks', the expected answer has 3 and never mentions it; (2) re-read all of _check_expected_response and _check_expected_answer in full (scenarios.py:378-456): the two checks share zero state — no join between contract and answer exists; (3) searched the whole repo for any other gate/test enforcing coverage (grep required_sections/_check_expected): tests/artifacts/test_cogsecskills_scenarios.py:334-347, test_cogsecskills_scenarios_branches.py, test_cogsecskills_scenarios_coverage.py all mutate required_sections and only assert contract-term findings, never answer-section coverage — no existing gate mitigates; (4) the mismatch is NOT unique to sat-ach-safe: every scenario pairs a bespoke 4-section contract with a generic 3-section answer (e.g. 'Threat confidence, Uncertainty and gaps' vs 'Confidence and uncertainty' at lines 84-96), so the fixtures are systematically inconsistent — this strengthens the finding but confirms it is authored-fixture hygiene, not a runtime defect: scenarios.py header states fixtures 'do not call external model runtimes', so nothing downstream consumes required_sections against real answers; the docs claim-boundaries contract ('include expected response-shape and expected-answer contracts') is indeed two unjoined YAML blobs. Corrections: line numbers 31-33 → 16-17 and 42-59 → 20-46; blast radius is test-fixture integrity only (a violated contract would never surface in shipped results), so severity low is correct. Fix as proposed (cross-check answer sections against required_sections + term lists, reconcile fixtures) is appropriate.
<!-- PR and issue links are added to the Tracking field after filing. -->