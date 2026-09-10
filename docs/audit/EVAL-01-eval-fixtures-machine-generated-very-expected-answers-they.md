# EVAL-01: Eval fixtures are machine-generated from the very expected answers they 'review' (same-source circularity)

|Field|Value|
|---|---|
|Audit ID|`EVAL-01`|
|Lens|`EVAL`|
|Severity|`high`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
The 'reviewed local output fixtures' in `evals/local_output_review.yaml` are not independently reviewed outputs: `write_evals` regenerates the entire file from `scenarios/defensive_readiness.yaml`'s `expected_answer` blocks, and `check_evals` fails on any drift, so the graded artifact and the grading key are the same authored text produced by one process. The rubric scores embedded in the eval fixture are literally copies of the scenario's self-declared `rubric_scores`, and scores are gated to stay at 2. Red team adjusted severity from critical to high because the circularity does not ship wrong or misleading results — the repo explicitly disclaims the epistemic status of these fixtures everywhere (`evals.py` CLAIM_BOUNDARY, `docs/evaluation-readiness.md`, `docs/release-claim-matrix.md`, `docs/quality-dashboard.md`, `TODO.md`) — but a residual real defect remains: the provenance string 'reviewed local fixture' asserts a review event that never occurred, a misleading claim on a public artifact surface.

## Evidence
`src/cogsecskills/artifacts/evals.py:120-135` — `_review_from_scenario(scenario)` returns a dict that copies the scenario's expected answer wholesale:

```python
{"scenario_id": scenario.id, ..., "sections": [asdict(section) for section in scenario.expected_answer.sections], "rubric_scores": dict(scenario.expected_answer.rubric_scores), "provenance": PROVENANCE, "claim_boundary": CLAIM_BOUNDARY}
```

`evals.py:349-353` — `write_evals` writes `_expected_source_text(base)` (which builds `"evaluations": [_review_from_scenario(scenario) for scenario in scenarios]`) to `evals/local_output_review.yaml`. `evals.py:365-368` — `check_evals` flags `"stale offline evaluation source"` on any byte drift. `evals.py:326-327` — `_content_findings` additionally enforces `review.rubric_scores.get(key) != 2` for every dimension. Verified: no independent outputs exist anywhere in the repo.

## Impact
There is no independent ground truth: the reviewed fixture and the grading key are the same authored text produced by one process, so the 'evaluation' cannot measure anything about skill quality. Because the repo consistently disclaims what these fixtures are, nothing false is shipped — but the machine-stamped 'reviewed local fixture' provenance on a public artifact asserts a review event that never occurred (scores are machine-copied from self-declared expected-answer rubric scores and gated to stay 2), which is a misleading claim on the artifact surface.

## Remediation
Separate provenance: generate the eval source from scenarios only as an 'expected answer key' (clearly labeled as such in `_expected_source_text` and the fixture description), and require actual independently produced outputs (live model or human) with distinct reviewer metadata before any rubric scores are attached. Never let `write_evals` emit scores into the reviewed fixture — remove the `rubric_scores` copy in `_review_from_scenario` (src/cogsecskills/artifacts/evals.py:120-135) and the corresponding `must be 2` enforcement in `_content_findings` (evals.py:326-327). Also correct the provenance wording so it does not assert a past-tense review event (see EVAL-05).

## Audit trail
- Discovered by the EVAL lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Mechanism confirmed end-to-end: evals/local_output_review.yaml is byte-regenerated from scenarios/defensive_readiness.yaml's expected_answer blocks (copied sections + rubric_scores), and check_evals fails on drift, so the reviewed fixture and grading key are the same authored text and scores are hard-pinned to 2. Verified no independent outputs exist. Severity ADJUSTED critical -> high: the circularity does not ship wrong/misleading results because the repo explicitly disclaims what this is everywhere — evals.py CLAIM_BOUNDARY 'deterministic offline review fixture; not a live model output...'; docs/evaluation-readiness.md:5 'not live model outputs, runtime certification, field validation, or benchmark results'; docs/release-claim-matrix.md:26 'Live runtime certification or field validation | prohibited without external evaluation'; docs/quality-dashboard.md:39 'Deterministic local fixture only, not benchmark or runtime certification'; TODO.md:81 lists the live-runtime eval harness as unstarted future work. Nothing claims these fixtures measure skill quality. Residual real defect: provenance string 'reviewed local fixture' asserts a review event that never occurred (scores machine-copied from self-declared expected-answer rubric_scores and gated to stay 2) — a misleading claim on a public artifact surface. Minor line correction: cited 130-146 is ~10 lines off; the function sits at ~120-135.
<!-- PR and issue links are added to the Tracking field after filing. -->