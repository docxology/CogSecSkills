# TEST-03: Hard-coded catalogue totals (100/28/7/8) pinned in many tests — silent drift pins acknowledged in CONTRIBUTING but spread across 5+ files

|Field|Value|
|---|---|
|Audit ID|`TEST-03`|
|Lens|`TEST`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/49) |

## Summary
Five test files pin literal catalogue totals (`len(registry) == 100`, `result["scenarios"] == 28`, `html.count("data-skill-id=") == 100`, per-figure pixel minimums) instead of deriving them from the registry. Every catalogue addition requires hand-updating counts in at least 5 test files plus docs, and CONTRIBUTING.md:54 openly documents this update duty. A missed update fails the build spuriously, or worse, tests pass while docs/dashboard drift. The verifier confirmed no centralized `EXPECTED_TOTAL` constant or cross-file consistency assertion exists anywhere in tests/, while the proposed structural-derivation pattern already exists in-repo (test_cogsecskills_scenarios.py:438).

## Evidence
- tests/conformance/test_skill_library_conformance.py:43

```python
assert len(registry) == 100, "the catalogue is defined as 100 skill areas"
```

- tests/artifacts/test_cogsecskills_dashboard.py:32-34 — `assert result["skills"] == 100` / `result["scenarios"] == 28` / `result["examples"] == 100`; :97 — `assert html.count("data-skill-id=") == 100` (counts at lines 32-34, 53-60, 86, 97).
- tests/artifacts/test_cogsecskills_examples.py:36 — `assert len(examples) == 100` (also 47, 56-57).
- tests/artifacts/test_cogsecskills_evals.py:25 — `assert result["evaluations"] == 28` (also 27, 36-38).
- tests/artifacts/test_cogsecskills_manuscript_assets.py:39-46 — `MIN_FIGURE_PIXELS` dict with per-figure (width,height) minimums.
- CONTRIBUTING.md:54 — "update ... the conformance test's expected total".

## Impact
Every catalogue addition is a five-file-plus-docs manual edit; CONTRIBUTING.md documents the duty, but that is an admission of the maintenance cost, not a mitigation. A missed update fails the build spuriously, or worse, tests pass while docs/dashboard drift out of sync with the real registry. The `html.count("data-skill-id=") == 100` pin (dashboard.py:97) is especially brittle — it breaks on any HTML restructuring, not just count drift. Severity medium is right: this is a maintenance/hygiene defect that cannot ship wrong runtime results, and the update process is documented.

## Remediation
Derive expected counts from the registry instead of pinning literals:

1. Adopt the in-repo pattern from tests/artifacts/test_cogsecskills_scenarios.py:438 — `assert len(scenarios) == len(groups) * len(SCENARIO_KINDS) * 2` — for the structural relationship between registry, scenarios, and examples.
2. Centralize the expected totals in one conformance module imported by all artifact tests (dashboard.py, examples.py, evals.py), and assert cross-file consistency (dashboard payload total == registry size) instead of literal `100`/`28`.
3. Replace `html.count("data-skill-id=") == 100` (dashboard.py:97) with a structural assertion that counts parsed skill elements (e.g. via the same data source the dashboard builder consumes) so HTML restructuring does not break the test.
4. Review tests/artifacts/test_cogsecskills_manuscript_assets.py:39-46 `MIN_FIGURE_PIXELS` — keep only minimums that guard a real consumer contract.

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: All cited quotes verified verbatim at the cited line numbers (dashboard counts at lines 32-34, 53-60, 86, 97; examples at 36/47/56-57; evals at 25/27/36-38). Checked for mitigations: no centralized EXPECTED_TOTAL constant or cross-file consistency assertion exists anywhere in tests/ (grep for TOTAL/consistency found only fixture-local counts). The scenarios test does derive totals structurally (test_cogsecskills_scenarios.py:438 `assert len(scenarios) == len(groups) * len(SCENARIO_KINDS) * 2` — line corrected from 440 to 438), proving the proposed pattern already exists in-repo. CONTRIBUTING.md documents the update duty but that is an admission, not a mitigation. The `html.count("data-skill-id=") == 100` pin (line 97) is indeed brittle to HTML restructuring. Severity medium is right: maintenance/hygiene defect, cannot ship wrong runtime results, process documented. Count of files confirmed: 4 artifact test files + 1 conformance file = 5.
<!-- PR and issue links are added to the Tracking field after filing. -->
