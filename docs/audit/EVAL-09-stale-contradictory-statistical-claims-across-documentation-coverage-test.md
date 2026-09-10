# EVAL-09: Stale and contradictory statistical claims across documentation (coverage %, test counts, score matrix presentation)

|Field|Value|
|---|---|
|Audit ID|`EVAL-09`|
|Lens|`EVAL`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
Version-labeled statistics contradict each other across docs: the stale 90.94% coverage figure in `docs/architecture.md` conflicts with CHANGELOG's 98.84% and TODO/dashboard's 99.91%, and the same v1.7.0 tag carries two different test counts (873 in `ISA.md` vs 899 in `TODO.md` and `docs/quality-dashboard.md`). Additionally, coverage percentages and 100/100 counts are quoted in prose adjacent to `docs/evaluation-readiness.md`'s 28 perfect-score rows with no per-row honesty marker beyond one header sentence, inviting readers to skim scores and counts as evaluation evidence. Verdict VALID, severity confirmed low: this is a presentation-consistency/doc-hygiene defect — no wrong shipped results, the claims are internally gated but contradictory across docs for the same release tag.

## Evidence
All quotes verified verbatim at current line numbers:

```
docs/architecture.md:299 — '- **90% coverage gate** on `src/`; the current focused suite reports 90.94% coverage.'
docs/claim-boundaries.md:14 — '| `examples --check` | Source-owned worked examples cover all 100 skills |'
CHANGELOG.md:28 — '- Coverage: 98.21% -> 98.84%, tests: 847 -> 873.'
ISA.md:6 — 'v1.7.0 release — 873 tests/98.84% coverage'
TODO.md:18 — 'Test gate: `pytest --cov=cogsecskills --cov-fail-under=97` -> `899 passed`, `99.91% coverage`.'
docs/quality-dashboard.md:29 — same 899/99.91% line.
```

The 90.94% figure persists only in `docs/architecture.md` plus generated manuscript artifacts (`output/pdf/_combined_manuscript.md:622`, `output/web/_combined_manuscript.md:613`, `ISA.md:222` historical record), while CHANGELOG/TODO/dashboard report 98.84%/99.91%. No test or gate forces `docs/architecture.md` prose to match the dashboard, so nothing already handles the staleness.

## Impact
A reader skimming the generated reports sees scores and counts, not the claim boundary: the fixture matrix (28 perfect-score rows) sits adjacent to these numbers with no per-row honesty marker beyond one header sentence. The same release tag carries two different test counts (873 vs 899) and two different coverage figures (90.94% vs 98.84%/99.91%), so version-labeled statistics contradict each other — a presentation-validity risk rather than a false claim, since the header disclaimers exist and the 90% gate is enforced in CI config regardless of the stale prose number.

## Remediation
Add a per-table caveat line under the Fixture Matrix in `_render_markdown` (`src/cogsecskills/artifacts/evals.py`) reiterating that all scores are authored constants, not measured results. Update `docs/architecture.md:299` to the current coverage figure and label it with its measurement date/commit. Reconcile the v1.7.0 test-count conflict between `ISA.md:6` (873/98.84%) and `TODO.md:18`/`docs/quality-dashboard.md:29` (899/99.91%), and add a consistency check (or generated-doc derivation) so prose statistics cannot drift from the dashboard registry.

## Audit trail
- Discovered by the EVAL lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified all cited quotes verbatim at current line numbers (architecture.md:299, claim-boundaries.md:14, CHANGELOG.md:28, ISA.md:6, TODO.md:18, quality-dashboard.md:29). The 90.94% figure is stale: grep shows it persists only in architecture.md plus generated manuscript artifacts (output/pdf/_combined_manuscript.md:622, output/web/_combined_manuscript.md:613, ISA.md:222 historical record), while CHANGELOG/TODO/dashboard report 98.84%/99.91%. The test-count conflict is real: ISA.md:6 labels v1.7.0 as 873 tests/98.84% while TODO.md:18 and quality-dashboard.md:29 (dashboard --check gated against live registry) say 899/99.91% — two different counts for the same release state. Mitigations checked: docs/claim-boundaries.md explicitly disclaims field effectiveness and defines wording rules, and the finding itself already acknowledges the header disclaimer exists; the 90% gate is enforced in CI config regardless of the stale prose number. No test or gate forces architecture.md prose to match the dashboard, so nothing already handles the staleness. The reasoning holds: presentation-consistency/doc-hygiene defect, no wrong shipped results, claims are internally gated but contradictory across docs for the same tag. Severity low is correct. Suggested fix (per-table caveat in evals.py _render_markdown + date-stamping the 90.94% figure) is appropriate and not already present.
<!-- PR and issue links are added to the Tracking field after filing. -->