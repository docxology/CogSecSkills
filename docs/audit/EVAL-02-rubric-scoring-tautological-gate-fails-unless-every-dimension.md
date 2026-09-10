# EVAL-02: Rubric scoring is tautological: the gate fails unless every dimension scores the maximum 2

|Field|Value|
|---|---|
|Audit ID|`EVAL-02`|
|Lens|`EVAL`|
|Severity|`medium`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/28)|

## Summary
The rubric in `docs/analyst-output-review.md` defines a genuine 0/1/2 scale with distinct semantics per level, but both gates hard-require every rubric dimension to equal exactly 2 — so a 0/1 score is unreachable in any passing fixture and the 'Passing score per dimension: 2' summary row carries zero information. Red team adjusted severity from critical to medium because the 'misleading results shipped' claim is substantially mitigated: these scores are authored deterministic fixture data, and every surface says so explicitly (`docs/evaluation-readiness.md`, per-fixture claim_boundary text, `docs/cli.md`, `TODO.md`). The defect is a real contract inconsistency with limited blast radius, not a published false evaluation result.

## Evidence
`src/cogsecskills/artifacts/evals.py:307-309`:

```python
for key in RUBRIC_KEYS:
    if review.rubric_scores.get(key) != 2:
        findings.append(f"{review.scenario_id}: rubric {key} must be 2")
```

`src/cogsecskills/artifacts/scenarios.py:445-447` (inside `_check_expected_answer`):

```python
if answer.rubric_scores.get(key) != 2:
    findings.append(f"{scenario.id}: expected answer rubric {key} must be 2")
```

`docs/analyst-output-review.md:9` defines the scale the code inverts: 'Score each dimension as `0`, `1`, or `2`'.

## Impact
The code inverts grading: instead of measuring quality against a threshold, it mandates perfect scores. The generated report (`docs/evaluation-readiness.md`, 28 rows all `=2`) is a structurally guaranteed outcome, not an evaluation result — a 0/1 score is unreachable by construction, so the `passing_score: 2` metric carries zero information and the 0/1/2 rubric is never exercised discriminatively. No misleading evaluation result is published (fixtures are consistently labeled as authored), but the contract inconsistency is real.

## Remediation
Either remove scores from deterministic fixtures entirely (they are authored, not measured), or permit 0/1/2 in the data and treat `< passing_score` as a genuine finding: change the `!= 2` hard requirement in `src/cogsecskills/artifacts/evals.py:307-309` and `src/cogsecskills/artifacts/scenarios.py:445-447` to a `< passing_score` comparison that appends a genuine finding. Validate the rubric's discriminative ability on real scored outputs (per `docs/future-validation-protocols.md`) before publishing any pass-rate.

## Audit trail
- Discovered by the EVAL lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Confirmed the mechanism: both gates hard-require every RUBRIC_KEYS dimension to equal exactly 2, while docs/analyst-output-review.md:9 defines a genuine 0/1/2 scale ('Score each dimension as `0`, `1`, or `2`') with distinct semantics per level — so the code inverts the rubric into a pass-only-if-perfect mandate and a 0/1 score is unreachable in any passing fixture. Corrected line numbers: evals.py is 307-309 (finding cited 316-319), scenarios.py is 445-447 inside _check_expected_answer. Severity adjusted from critical to medium because the 'misleading results shipped' claim is substantially mitigated: these scores are authored deterministic fixture data, and every surface says so explicitly — docs/evaluation-readiness.md:5 ('The fixtures are reviewed local answers ... not live model outputs, runtime certification, field validation, or benchmark results'), every fixture row carries 'deterministic offline review fixture; not a live model output...', docs/cli.md:409-410 and TODO.md:81-82 frame live scoring as future work. No misleading evaluation result is published; the defect is a real contract inconsistency (the 0/1/2 rubric is never exercised discriminatively and the 'Passing score per dimension: 2' summary row carries zero information) with limited blast radius. The finding's fix suggestion is reasonable but not required for the repo to be honest as currently worded.
<!-- PR and issue links are added to the Tracking field after filing. -->