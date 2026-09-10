# TEST-08: Contract tests pin exact doc prose and heading inventory — high churn coupling

|Field|Value|
|---|---|
|Audit ID|`TEST-08`|
|Lens|`TEST`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/54) |

## Summary
Contract tests pin exact manuscript H1 title+anchor tuples for 13 files, 24 bib keys, ~25 literal phrases across QUICKSTART/README/DESIGN, exact phrases across 8 AGENTS.md files, and a hard-coded `len(file_lines) == 24` count of transcript bullets. These are deliberately drift-guarding tests (the agents_contract even documents why), so they are partially defensible — but exact-title pinning of every manuscript heading means routine copyedits break the suite, training maintainers to loosen tests even though tests/AGENTS.md:9 explicitly forbids that ("Do not weaken or delete failing tests to make gates pass"). Red team verdict ADJUSTED: the mechanisms are confirmed but the original line numbers and counts were wrong (REQUIRED_BIB_KEYS is at :19-45, EXPECTED_MANUSCRIPT_H1S at :63-125, docs_contract phrase pins ~25 not ~50); severity stays low since a copyedit breaks the suite loudly rather than shipping wrong results.

## Evidence
- tests/contract/test_cogsecskills_manuscript_contract.py:19-45 — `REQUIRED_BIB_KEYS` pins 24 bib keys ("sandve2013reproducible", "wilkinson2016fair", "smith2016softwareCitation", ...); :63-125 — `EXPECTED_MANUSCRIPT_H1S` pins exact title+anchor for 13 files (`("00_abstract.md", "Abstract", "sec:abstract")`, ..., `("99_references.md", "References", "sec:references")`); :152-160 — `test_manuscript_h1_inventory_is_informative_and_stable` asserts `tuple(seen) == EXPECTED_MANUSCRIPT_H1S`.
- tests/contract/test_cogsecskills_docs_contract.py:60-88 — ~25 literal `in`-phrase assertions across QUICKSTART/README/DESIGN; :205-212 — `assert len(file_lines) == 24` hard-coded count of `- skills/` transcript bullets.
- tests/contract/test_cogsecskills_agents_contract.py:44-88 — exact phrase pins across 8 AGENTS.md files; :212-213 comment: "finding the basename elsewhere is precisely the drift being guarded against".
- tests/AGENTS.md:9 — "Do not weaken or delete failing tests to make gates pass".

## Impact
Routine copyedits of a manuscript heading or docs phrase break the suite, and the only remedy maintainers are taught is weakening tests — which tests/AGENTS.md:9 forbids, creating a churn-vs-discipline trap. The `len(file_lines) == 24` transcript count breaks on any example edit; a structural version (each `- skills/` path resolves) would catch the same drift without the exact-count brittleness. Severity low is appropriate: these are stability gates, not correctness gates — a copyedit breaks the suite loudly rather than shipping wrong results.

## Remediation
1. tests/contract/test_cogsecskills_manuscript_contract.py:152-160 — replace the exact `tuple(seen) == EXPECTED_MANUSCRIPT_H1S` equality with structural properties: each manuscript md file has exactly one H1 with a unique anchor; keep the file inventory itself (which files exist) as the stable part of the contract.
2. tests/contract/test_cogsecskills_docs_contract.py:205-212 — replace `assert len(file_lines) == 24` with a structural assertion that every `- skills/` transcript path resolves (the test already partially does this).
3. Keep path-resolution assertions, forbidden-phrase assertions, and REQUIRED_BIB_KEYS subset pinning (they guard a real release contract) — the relaxation targets the exact-title/exact-count pins only, per the original fix.
4. For the AGENTS.md phrase pins, retain only phrases that carry claim-boundary meaning; drop stylistic pins.

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Confirmed the mechanisms exist: exact H1 title+anchor tuple equality, REQUIRED_BIB_KEYS subset pin, dozens of literal phrase assertions in docs/agents contract tests, and the hard-coded `len(file_lines) == 24` transcript count (exact count is brittle; structural version would check each `- skills/` path resolves, which the test already partially does). Verified tests/AGENTS.md:9 — "Do not weaken or delete failing tests to make gates pass" — so the churn-loosens-tests concern is real. Also verified the tests are deliberately drift-guarding (test_cogsecskills_agents_contract.py:212-213 comment: 'finding the basename elsewhere is precisely the drift being guarded against'). Corrections to the finding: line numbers are wrong — REQUIRED_BIB_KEYS is at :19-45 (not :57-83), EXPECTED_MANUSCRIPT_H1S at :63-125 (not :88-152); docs_contract phrase pins are ~25 assertions not ~50 (counting occurrences in the 47-88 range). No other gate/test mitigates the brittleness; severity low is appropriate since these are stability gates, not correctness gates — a copyedit breaks the suite loudly rather than shipping wrong results.
<!-- PR and issue links are added to the Tracking field after filing. -->