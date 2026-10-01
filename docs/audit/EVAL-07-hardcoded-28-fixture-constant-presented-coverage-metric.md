# EVAL-07: Hardcoded '28 fixture' constant presented as a coverage metric

|Field|Value|
|---|---|
|Audit ID|`EVAL-07`|
|Lens|`EVAL`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/32)|

## Summary
The `!= 28` fixture-count check hardcodes the literal 28 while `load_scenarios(base)` is already in scope, and the number flows into generated docs (`docs/evaluation-readiness.md` 'Evaluation fixtures | 28', `docs/cli.md`) that read like empirical counts. The check is actually fully redundant — the missing/extra check against `expected_ids` already catches drift — so a scenario-set change yields a confusing 'expected 28 evaluation fixtures' failure rather than a wrong pass. Verdict VALID, severity confirmed low: currently consistent (28 == `len(load_scenarios())`), redundant check, cosmetic/misleading-on-drift only.

## Evidence
`src/cogsecskills/artifacts/evals.py:351-352` (finding cited 342-343; line numbers stale):

```python
if len(reviews) != 28:
    findings.append(f"expected 28 evaluation fixtures, found {len(reviews)}")
```

Mechanism verified: `_content_findings` hardcodes 28 while `load_scenarios(base)` is already in scope (line 282). Docs claims confirmed: `docs/evaluation-readiness.md:11` 'Evaluation fixtures | 28', `docs/cli.md:367/428`, `docs/quality-dashboard.md`/html — all generated files that read like empirical counts. Tests only pin the current value (`test_cogsecskills_evals.py:25-38` asserts 28); no test or code derives the constant.

## Impact
The '28' in generated docs is a frozen snapshot posing as a statistic: it is a compile-time constant duplicated in code, not a value derived from the scenario set. It does not mask drift — the missing/extra check (evals.py:337-350, comparing `seen` against `expected_ids = set(scenario_by_id)`) already flags it — but if the scenario set changes, the gate fails with a misleading hardcoded 'expected 28' message instead of a derived count. Currently consistent, so impact is maintenance cost and presentation honesty only.

## Remediation
In `src/cogsecskills/artifacts/evals.py:351-352`, replace the literal comparison with `if len(reviews) != len(load_scenarios(base)):` and derive the message from that length — or, since the check is redundant with the missing/extra check at lines 337-350, simply delete it. Keep the generated-doc counts derived rather than literal.

## Audit trail
- Discovered by the EVAL lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Confirmed the literal exists, but at lines 351-352 of 400, not 342-343 (finding's line numbers are stale). Mechanism verified: `_content_findings` hardcodes 28 while `load_scenarios(base)` is already in scope (line 282). Cross-checked whether an existing gate already enforces the property: the missing/extra check (lines 337-350) compares `seen` against `expected_ids = set(scenario_by_id)` and duplicates are blocked, so the `!= 28` check is fully redundant — it can only fire when `len(load_scenarios()) != 28`, and it would then flag the drift (so it does NOT mask drift, it just reports it with a misleading hardcoded 'expected 28' message). Docs claims confirmed: docs/evaluation-readiness.md:11 'Evaluation fixtures | 28', docs/cli.md:367/428, quality-dashboard.md/html — all generated files that read like empirical counts. Tests only pin the current value (test_cogsecskills_evals.py:25-38 asserts 28), so updating the scenario set without updating the constant yields a confusing gate failure, not a wrong pass. No test or code derives the constant. Severity low is honest: currently consistent (28 == len(load_scenarios())), redundant check, cosmetic/misleading-on-drift only. Suggested fix (compare against len(load_scenarios(base))) is sound and would make the check robust — or, since it is redundant with the missing/extra check, it could simply be deleted. Quote verbatim correct; only line numbers adjusted.
<!-- PR and issue links are added to the Tracking field after filing. -->