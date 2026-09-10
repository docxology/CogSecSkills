# EVAL-03: 'Grader' reduces to substring presence in the fixture's own text; rubric dimensions are not measurable in code

|Field|Value|
|---|---|
|Audit ID|`EVAL-03`|
|Lens|`EVAL`|
|Severity|`medium`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
The only content-quality check on reviewed outputs is lowercase substring membership of fixed and scenario terms against a blob of the fixture's own text, plus structural checks — so rubric dimensions like `uncertainty` and `defensive_boundary` with 0/1/2 anchors in `docs/analyst-output-review.md` are not machine-measurable; mentioning 'uncertainty' once passes. Because fixture authors knew the term list (it lives in the same YAML), inclusion is by construction, not by merit. Red team adjusted severity from high to medium because the repo already extensively disclaims the epistemic status of these fixtures (`docs/evaluation-readiness.md`, `docs/claim-boundaries.md`, `QUICKSTART.md`, `docs/cli.md`), so no wrong live-model claim ships; the genuine residual gap is that `docs/evaluation-readiness.md` presents 'Passing score per dimension | 2' as if rubric conformance were validated when it is only asserted, and no doc states the term checks are vocabulary-presence-only.

## Evidence
`src/cogsecskills/artifacts/evals.py:330-342` — confirmed verbatim:

```python
text = _review_text(review)
required_terms = {"evidence", "inference", "gap", "confidence", "uncertainty", *(term.lower() for term in scenario.expected_output_terms), *(term.lower() for term in scenario.required_quality_terms)}
...
if term not in text:
    findings.append(f"{review.scenario_id}: term {term!r} is missing")
```

Adjacent line 314: `if review.rubric_scores.get(key) != 2: findings.append(f"{review.scenario_id}: rubric {key} must be 2")`. Rubric scores are self-declared in fixture YAML and never verified against content, so the `uncertainty`/`defensive_boundary` anchors cannot be distinguished by code — an overconfident output passes identically to a well-calibrated one.

## Impact
Nothing in code can distinguish an overconfident output from a model one: the term check verifies vocabulary presence only, yet `docs/evaluation-readiness.md` presents the matrix in a way that invites reading term-passing as rubric conformance. The 0/1/2 anchors in `docs/analyst-output-review.md` for dimensions like `uncertainty` and `defensive_boundary` are asserted, not measured. No wrong shipped result (the fixtures are consistently disclaimed as deterministic offline fixtures), but the presentation gap is a real contract inconsistency between the rubric doc's discriminative scale and what the code can actually check.

## Remediation
State in `docs/evaluation-readiness.md` that the term checks verify vocabulary presence only, not rubric conformance, and that the 0/1/2 rubric dimensions are not machine-measurable in the deterministic fixture path. Move actual dimension scoring to the human/live-model protocol in `docs/future-validation-protocols.md`. Optionally extend the per-fixture claim_boundary text to carry the same caveat.

## Audit trail
- Discovered by the EVAL lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Verified the mechanism: the only content-quality check on reviewed outputs is lowercase substring membership of fixed/scenario terms against a blob of the review's own text (`_review_text`), plus structural checks (>=3 sections, unique titles). Rubric scores are enforced only as `must be 2` — self-declared in fixture YAML, never verified against content, so `uncertainty`/`defensive_boundary` anchors are not machine-measurable; mentioning 'uncertainty' once passes. The term list does live in the same YAML the fixture authors wrote, so inclusion is partly by construction. However, severity is overstated as high because the repo already extensively disclaims the epistemic status: docs/evaluation-readiness.md:5 ('not live model outputs, runtime certification...') and every table row carries 'deterministic offline review fixture; not a live model output'; docs/claim-boundaries.md:21-25 excludes live-model claims; QUICKSTART.md:47-49 states gates 'prove source and contract coherence; they do not prove live model behavior or field effectiveness'; cli.md:409-411 says fixtures 'are not live model outputs or benchmark results'. So no wrong/misleading shipped result in the sense of a live-model claim. The genuine residual gap the finding correctly identifies: docs/evaluation-readiness.md presents 'Passing score per dimension | 2' as if rubric conformance were validated, when it is only asserted, and no doc states the term checks are vocabulary-presence-only. Proposed fix (add that caveat, point to human/live-model protocol in future-validation-protocols.md) is appropriate; severity medium, real defect with limited blast radius.
<!-- PR and issue links are added to the Tracking field after filing. -->