# REPRO-05: CI enforces gates the contributor docs never mention; docs mention a gate CI does not run

|Field|Value|
|---|---|
|Audit ID|`REPRO-05`|
|Lens|`REPRO`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
CI's "Coherence gates (no generated-file drift)" step runs seven `--check` commands (definitions, scenarios, examples, evals, dashboard, release-metadata, manuscript-assets), but CONTRIBUTING.md's "Before opening a PR" checklist mentions none of them — a contributor following the documented checklist will be surprised by CI failures on the drift gates. Conversely, the docs/catalogue.md regeneration instruction has no CI gate anywhere, so `docs/catalogue.md` can go stale forever. Verdict was adjusted after verification found one mitigating test: the conformance test `test_registry_enumerates_one_hundred_areas` pins the catalogue total when registry size changes, catching registry-size drift even though prose drift is not caught; severity confirmed low (doc-hygiene/contributor-surprise issue, no incorrect shipped artifact).

## Evidence
- `.github/workflows/ci.yml:49-56` — 'Coherence gates (no generated-file drift)' run block listing (lines 50-56):
  ```
  definitions --check
  scenarios --check
  examples --check
  evals --check
  dashboard --check
  release-metadata --check
  manuscript-assets --check
  ```
- `CONTRIBUTING.md:47-54` — '## Before opening a PR' checklist: validate, doctor, pytest ≥90%, ruff, and 'If you changed the catalogue size, regenerate `docs/catalogue.md` … and update the README group-count table and the conformance test's expected total' — none of the seven `--check` gates mentioned. (The doc's coverage number, 90%, also disagrees with CI's 97% — a further doc/CI drift detail.)
- Catalogue staleness verified: `release_metadata.py:133-141` `generated_files` list omits `docs/catalogue.md` (it lists quality-dashboard, worked examples, evals, claim-matrix, S10/S11, figures); ci.yml has no catalogue gate; and `docs/catalogue.md:3-4` says 'Do not edit by hand — regenerate after changing the registry' with nothing enforcing it.
- Mitigating factor (verifier): `AGENTS.md:74-77` and `CONTRIBUTING.md:53` point to the conformance test `test_registry_enumerates_one_hundred_areas`, which pins the catalogue total when the registry size changes — so registry-size drift is caught by pytest even if prose drift is not.

## Impact
A contributor following the documented PR checklist will hit unexpected CI failures on drift gates they were never told to run locally. In the other direction, `docs/catalogue.md` is documented as "do not edit by hand — regenerate" but nothing anywhere checks that it was regenerated, so it can drift from the registry indefinitely with no signal. Maintenance cost and contributor footgun; no incorrect shipped artifact.

## Remediation
1. In `CONTRIBUTING.md` ('## Before opening a PR', lines 47-54), add the seven `--check` gates (definitions, scenarios, examples, evals, dashboard, release-metadata, manuscript-assets) to the checklist so contributors can pre-run what CI enforces.
2. For `docs/catalogue.md`: either add a `catalogue --check` gate to `.github/workflows/ci.yml` (and optionally to the `generated_files` list in `src/cogsecskills/artifacts/release_metadata.py`), or drop the regeneration instruction from the docs since nothing enforces it.

## Audit trail
- Discovered by the REPRO lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Substance of the finding confirmed, one line-number correction. (1) CI gates are at ci.yml:50-56, not 31-33 — the finding's cited line range is wrong (31-33 is the ruff lint step); all seven --check gates verbatim as quoted. (2) CONTRIBUTING.md 'Before opening a PR' is lines 47-54 (not 31-40); it lists exactly validate/doctor/pytest/ruff/regenerate-catalogue — confirmed no mention of any --check gate; the doc's coverage number (90%) also disagrees with CI's 97% (--cov-fail-under=97), a further doc/CI drift detail. (3) catalogue staleness claim verified: release_metadata.py:133-141 generated_files list omits docs/catalogue.md (it lists quality-dashboard, worked examples, evals, claim-matrix, S10/S11, figures), ci.yml has no catalogue gate, and docs/catalogue.md:3-4 says 'Do not edit by hand — regenerate after changing the registry' with nothing enforcing it. However, one mitigating test partially limits blast radius: AGENTS.md:74-77 and CONTRIBUTING.md:53 point to the conformance test test_registry_enumerates_one_hundred_areas which pins the catalogue total when the registry size changes — so registry-size drift is caught by pytest even if prose drift is not. Severity stays low: doc-hygiene/contributor-surprise issue, no incorrect shipped artifact.
<!-- PR and issue links are added to the Tracking field after filing. -->