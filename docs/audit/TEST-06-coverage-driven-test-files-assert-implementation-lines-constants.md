# TEST-06: Coverage-driven test files assert implementation lines and constants, not behavior

|Field|Value|
|---|---|
|Audit ID|`TEST-06`|
|Lens|`TEST`|
|Severity|`medium`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
Test files are named after coverage targets and their docstrings cite coverage percentages and line numbers, and they contain threshold-of-constant assertions (`FIGURE_DPI >= 200`, `COVER_COMMAND_SIZE >= 12`) that have no failing behavior — any plausible regression passes them. This is the classic "tests written so the change has coverage" anti-pattern, inflating the coverage gate with weightless checks. Red team confirmed the mechanism but adjusted the details: the gate is `fail_under = 90` (pyproject.toml:122), not 97% as originally claimed, and not all coverage-file content is weightless — lowgap_coverage's `_latex_escape`/`_group_title` checks and final_coverage's adapter-verb validation are real behavioral assertions, so only the constant-pin subset is truly weightless.

## Evidence
- tests/quality/test_cogsecskills_lowgap_coverage.py:1-5

```python
"""Coverage tests for remaining low-gap modules.
dashboard.py (98.64%), figures.py (98.35%), rows.py (98.29%),
tables.py (99.05%), evals.py (99.27%).
"""
```

- tests/quality/test_cogsecskills_final_coverage.py:3-4 — "These are the final coverage gaps identified by the v1.4.0 coverage report."
- tests/artifacts/test_cogsecskills_manuscript_assets.py:159-165 — `test_cover_readability_constants_are_pdf_first` asserts `COVER_COMMAND_SIZE >= 12`, `COVER_LABEL_SIZE >= 16`, `COVER_PANEL_TITLE_SIZE >= 22`.
- tests/artifacts/test_cogsecskills_figures.py:52-54 — `test_figure_dpi_is_reasonable`: `assert FIGURE_DPI >= 200` (the finding's citation of :76-79 was stale).
- File inventory confirmed: 6 `*_coverage` test files (quality/coverage_gaps, final_coverage, lowgap_coverage, validate_coverage; authoring/author_defs_coverage; artifacts/scenarios_coverage) plus 7 `*_branches` files; pyproject.toml:122 `fail_under = 90`.

## Impact
Threshold-of-constant assertions have no failing behavior: any plausible regression passes them, so they add gate weight without defect detection. Six coverage-named files plus seven branches files make the suite structure track coverage reports rather than behaviors, which inflates the `fail_under = 90` gate and misleads maintainers about what is actually guarded. No wrong results ship — this is test-suite hygiene — hence medium.

## Remediation
1. Delete the constant-pin tests that assert no consumer-observable contract: `test_figure_dpi_is_reasonable` (tests/artifacts/test_cogsecskills_figures.py:52-54), `test_cover_readability_constants_are_pdf_first` (tests/artifacts/test_cogsecskills_manuscript_assets.py:159-165), and similar FIGURE_SIZES key-set pins.
2. Keep the behavioral tests that already cover these modules: `test_write_figures_generates_all_pngs`, `test_write_assets_creates_markdown_data_and_figures`, `test_check_assets_detects_missing_and_stale_files`, and the edge-case drift tests — the verifier confirmed behavioral coverage exists, so deleting the constant pins loses no consumer contract.
3. Preserve the real behavioral assertions inside the coverage files (lowgap_coverage's `_latex_escape`/`_group_title` checks, final_coverage's adapter-verb validation) by folding them into the topical test files; drop the rest of the coverage-chasing wrappers and rename the files away from coverage-report naming.

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: All quotes verified verbatim; line numbers mostly current — DPI test is actually at :52-54, not :76-79 as cited. Mechanism confirmed: coverage-named files, docstrings citing percentages/line numbers, threshold-of-constant assertions with no failing behavior. Two corrections to the finding: (1) the coverage gate is fail_under = 90, not 97% as the 'why' claims; (2) the *_branches family (7 files) exists beyond the six coverage files. Mitigation check: behavioral tests of these modules exist elsewhere (test_write_figures_generates_all_pngs, test_write_assets_creates_markdown_data_and_figures, test_check_assets_detects_missing_and_stale_files, edge-case drift tests), so deleting constant-pin tests loses no consumer contract — supports the fix. Caveat: not all coverage-file content is weightless — lowgap_coverage's _latex_escape/_group_title checks and final_coverage's adapter-verb validation are real behavioral assertions exercising error paths; the truly weightless subset is the constant pins (DPI>=200, font sizes, FIGURE_SIZES key sets). Severity medium is fair: test-suite hygiene plus a gate inflated by untestable asserts; no wrong results ship.
<!-- PR and issue links are added to the Tracking field after filing. -->