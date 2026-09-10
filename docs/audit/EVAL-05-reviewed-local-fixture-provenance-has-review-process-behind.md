# EVAL-05: 'Reviewed local fixture' provenance has no review process behind it; selection is 1:1 authored self-consistent fixtures (survivorship)

|Field|Value|
|---|---|
|Audit ID|`EVAL-05`|
|Lens|`EVAL`|
|Severity|`medium`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
No reviewer identity, review date, rubric-scoring session, or inter-rater process exists anywhere in the repo for the 28 fixtures in `evals/local_output_review.yaml` — they are 'reviewed' only in the sense that the generator stamped the `provenance` constant, and the repo's own rubric doc (`docs/analyst-output-review.md:3-4`) says the review protocol 'is for future scenario-output review', yet the fixtures stamp past-tense 'reviewed local fixture' and a gate actively enforces the mislabel. The fixture set is perfectly survivorship-biased: exactly the authored answers that satisfy the authors' own term/shape contracts, one per scenario, with zero failed/ambiguous samples, so the 28/28 matrix cannot evidence output quality even at fixture level. Verdict ADJUSTED, severity confirmed medium: the misleading provenance wording is real, but its blast radius is bounded because empirical-claim boundaries are consistently disclaimed elsewhere and no benchmark or quality claim is staked on the matrix.

## Evidence
`evals/local_output_review.yaml:1-2`:

```yaml
description: 'Offline reviewed local output fixtures derived from defensive scenario expected answers. These are not live model outputs.'
```

Every entry carries `provenance: reviewed local fixture` (28 entries). The gate at `src/cogsecskills/artifacts/evals.py:303-304` enforces the constant:

```python
if review.provenance != PROVENANCE:
    findings.append(... provenance must be ...)
```

(`PROVENANCE` defined at `evals.py:29`; the finding cited line 313, actual 303-304.) Survivorship is confirmed by construction: `evals.py:117-123` copies `rubric_scores` straight from `scenario.expected_answer` (the same authored YAML), stamps the constants, and the check at `evals.py:307-309` requires every rubric dimension to equal 2 — a 28/28 passing matrix is guaranteed for any fixture that round-trips. Meanwhile `docs/analyst-output-review.md:3-4` states 'This protocol is for future scenario-output review. It is not an empirical claim by itself' and `docs/cli.md:352` says fixtures 'carry a reviewed local expected-answer fixture'.

## Impact
The repo simultaneously says review is future work and labels all fixtures as reviewed, with a gate enforcing the mislabel. A reader of the 28/28 matrix has no way to know there was never a review event — no reviewer identity, scoring session, or rejected/low-scoring example exists anywhere. No empirical or benchmark claim is staked on the matrix (disclaimers cover that), so the defect is a misleading past-tense provenance label on public artifacts rather than a false evaluation result.

## Remediation
Drop the word 'reviewed' from the provenance constant (`PROVENANCE` at `src/cogsecskills/artifacts/evals.py:29`) and the fixture description in `evals/local_output_review.yaml:1-2`, or record actual reviewer identity/date/method per fixture. Include rejected/low-scoring examples if the set is meant to demonstrate a review process. Update the enforcing gate at `evals.py:303-304` and the prose in `docs/cli.md:352` to match.

## Audit trail
- Discovered by the EVAL lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Verified all core claims. (1) Quote is verbatim; description text confirmed at yaml lines 1-2 (finding's 1-5 range slightly wide but quote exists). (2) The gate exists exactly as described but at evals.py:303-304, not 313. (3) Review-process search found NO reviewer identity, review date, rubric-scoring session record, inter-rater artifact, or rejected/low-scoring example anywhere in the repo. Critically, docs/analyst-output-review.md:3-4 states 'This protocol is for future scenario-output review. It is not an empirical claim by itself' — the repo's own rubric doc says review is future work, yet fixtures stamp past-tense 'reviewed local fixture' and docs/cli.md:352 says fixtures 'carry a reviewed local expected-answer fixture'. (4) Survivorship confirmed by construction: evals.py:117-123 copies rubric_scores straight from scenario.expected_answer (same authored YAML), stamps PROVENANCE/CLAIM_BOUNDARY constants, and the check at evals.py:307-309 requires every rubric dimension to equal 2 — a 28/28 passing matrix is guaranteed for any fixture that round-trips; it cannot evidence output quality. (5) Mitigations exist but do not neutralize the finding: per-entry claim_boundary text, docs/claim-boundaries.md, docs/AGENTS.md, evaluation-readiness.md, and manuscript limitations all disclaim live-model/empirical claims, and future-validation-protocols.md defers real review to future protocols. None of these disclaimers address the fabricated past-tense 'reviewed' provenance itself — the repo simultaneously says review is future work and labels fixtures as reviewed, and the gate actively enforces the mislabel. Severity medium correct: real misleading provenance wording, bounded blast radius since empirical-claim boundaries are consistently disclaimed elsewhere and no benchmark/quality claim is staked on the 28/28 matrix.
<!-- PR and issue links are added to the Tracking field after filing. -->