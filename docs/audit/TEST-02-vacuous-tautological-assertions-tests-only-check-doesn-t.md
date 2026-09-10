# TEST-02: Vacuous/tautological assertions: tests that only check 'it doesn't crash' or 'list is non-empty'

|Field|Value|
|---|---|
|Audit ID|`TEST-02`|
|Lens|`TEST`|
|Severity|`medium`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
Four tests assert only `isinstance(findings, list)` or `len(findings) > 0`, and their own comments admit the expected outcome is unknown ("the important thing is it doesn't crash"). A regression that changes the failure reason — or reports the wrong skill/path — still passes, because these tests were written to hit coverage lines rather than pin behavior. Red team adjusted severity from high to medium because precise message pins exist elsewhere for the "not present in registry" branch and these are coverage-chasing near-duplicates rather than shipped-behavior gates; however, the route-no-match case has no other precise pin anywhere, so real coverage gaps remain.

## Evidence
All quotes verified verbatim; the finding's original line numbers were stale — actual locations below.

- tests/quality/test_cogsecskills_edge_cases.py:315-317

```python
# The route check may or may not flag depending on token overlap;
# the important thing is it doesn't crash
assert isinstance(findings, list)
```

- tests/artifacts/test_cogsecskills_artifact_branches.py:223-225

```python
# This will flag both "not present in registry" or "rendered skill is missing"
# depending on whether sat.nonexistent is in the registry
assert len(findings) > 0
```

- tests/authoring/test_cogsecskills_author_defs_coverage.py:157-158

```python
# Should report missing rendered files or render failure
assert len(findings) > 0
```

- tests/authoring/test_cogsecskills_definitions_branches.py:259-261

```python
# The definition has no on-disk skill, so rendering will fail or
# report missing rendered files
assert len(findings) > 0
```

## Impact
These tests pass for any non-empty findings list, so a regression that makes the route check return garbage-but-nonempty, or that breaks the route-no-match check entirely, goes undetected. Wrong-path or wrong-reason findings pass the artifact/definitions tests. The mitigating picture: the "not present in registry" branch IS pinned precisely elsewhere (tests/artifacts/test_cogsecskills_examples_branches.py:113 — `assert any("not present in registry" in f for f in findings)` — and tests/quality/test_cogsecskills_edge_cases.py:150), so the artifact_branches test is partially redundant coverage; the route-no-match case, however, has no other precise pin, so it is a genuine hole.

## Remediation
Assert the specific finding rather than the container:

1. tests/quality/test_cogsecskills_edge_cases.py:315-317 — make the route-no-match fixture deterministic (fixed token set) and assert the expected finding instead of `isinstance(list)`; this case has no other precise pin, so it is the priority.
2. tests/artifacts/test_cogsecskills_artifact_branches.py:223-225 — match the exact message fragment and skill id, e.g. `any('not present in registry' in f and 'sat.nonexistent' in f for f in findings)`, or drop the test as redundant with examples_branches.py:113 / edge_cases.py:150.
3. tests/authoring/test_cogsecskills_author_defs_coverage.py:157-158 and tests/authoring/test_cogsecskills_definitions_branches.py:259-261 — converge the two near-duplicate render-failure tests into one that asserts the specific render-failure message and skill id (see TEST-07 for the duplication).

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: All four quotes exist verbatim; cited line numbers were stale — actual: edge_cases 315-317 (not 296-298), artifact_branches 223-225 (not 230-232), author_defs_coverage 157-158, definitions_branches 259-261. Re-derived: the route test genuinely pins only isinstance(list) — a regression that makes check_scenarios return garbage-but-nonempty, or that breaks the route-no-match check entirely, passes; and the artifact/definitions tests accept any non-empty findings, so a wrong-path or wrong-reason finding passes. Mitigation check: the 'not present in registry' branch IS pinned precisely elsewhere — tests/artifacts/test_cogsecskills_examples_branches.py:113 ('assert any("not present in registry" in f for f in findings)') and tests/quality/test_cogsecskills_edge_cases.py:150 — so the artifact_branches test is partially redundant coverage, not the sole guard. The route-no-match case, however, has no other precise pin anywhere. That redundancy, plus these being coverage-chasing near-duplicates rather than shipped-behavior gates, lowers real blast radius: severity adjusted high→medium. The fix recommendation (assert exact message fragment + skill id; make route fixture deterministic) is sound and still applies.
<!-- PR and issue links are added to the Tracking field after filing. -->
