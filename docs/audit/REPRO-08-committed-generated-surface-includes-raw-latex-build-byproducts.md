# REPRO-08: Committed generated surface includes raw LaTeX build byproducts with no provenance manifest

|Field|Value|
|---|---|
|Audit ID|`REPRO-08`|
|Lens|`REPRO`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/45) |

## Summary
`.gitignore` deliberately re-includes the entire `output/` tree ("Generated outputs ... ARE committed"), which sweeps in raw LaTeX build byproducts (`.aux`, `.bbl`, `.blg`, `.log`, `.toc`, `_xelatex_stdout.log`) that are environment-dependent compiler scratch rather than deliverables. The repo also tracks two diverging copies of the combined manuscript (`output/pdf/_combined_manuscript.md` vs `output/web/_combined_manuscript.md`), and none of the drift gates cover `output/pdf` or `output/web` at all, and no SHA256 provenance manifest exists. Verdict VALID; severity adjusted from the original medium to low — a hygiene/drift risk where the deliverable content itself is not wrong.

## Evidence
- `.gitignore:1-2` — "Generated outputs (PDFs, figures, data, web, slides) ARE committed so the / rendered deliverables travel with the repo; regenerate with the pipeline." plus `!output/` / `!output/**` at `.gitignore:4-5`.
- `output/pdf` contains `_combined_manuscript.aux`, `.bbl`, `.blg`, `.log` (62.5KB), `.toc`, `_xelatex_stdout.log`.
- `output/pdf/_combined_manuscript.md` and `output/web/_combined_manuscript.md` are two separately tracked copies that already diverge (verifier: the same reproducibility code block sits at lines 385-387 in the pdf copy vs 380-382 in the web copy; original finding reported 302.1KB vs 302.5KB).
- Gate coverage: `manuscript-assets --check` and the `generated_files` list in `release_metadata.py:133-179` (plus `assets_io.py:66`) cover only `docs/`, `output/data/`, `output/figures/` — nothing covers `output/pdf` or `output/web`; no `manifest.json`/SHA256 provenance exists in the repo.
- Verifier nuance: the `.log` is deliberately grepped in the release checklist (`docs/release-checklist.md:46`), a flimsy justification for committing it; no gitignore of `.aux`/`.blg` either.

## Impact
Compiler byproducts (`.aux/.log/.blg`) are environment-dependent scratch, not deliverables — committing them adds noise and false drift signals to the generated surface. The duplicated combined-manuscript markdown in two directories is already diverging, proving copy drift is happening, and no drift gate covers either directory, so the divergence can grow unchecked. Without a provenance manifest, committed binaries (PDFs, figures) have no checkable correspondence to a known build. Deliverable content is not wrong (hence low), but the committed generated surface is inconsistent and ungoverned.

## Remediation
1. Add gitignore rules for the LaTeX byproducts (`.aux`, `.log`, `.blg`, `.toc`, `.bbl`) under `output/pdf/` and remove the committed ones from the index, keeping the committed-surface promise focused on actual deliverables (if the release-checklist grep of the `.log` is valued, extract that check into the pipeline instead).
2. Resolve the duplicated `_combined_manuscript.md`: either drop one of the two tracked copies, or bring the pair under a drift gate (e.g. add them to the `generated_files` list in `src/cogsecskills/artifacts/release_metadata.py` or a `manuscript-assets` check) so divergence fails CI.
3. Add a SHA256 provenance manifest (e.g. `output/manifest.json`) covering the committed binaries (PDFs, figures) with a gate that recomputes hashes, so committed artifacts have checkable provenance.

## Audit trail
- Discovered by the REPRO lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified: .gitignore re-includes the entire output/ tree including LaTeX byproducts (.aux/.bbl/.blg/.log/.toc/_xelatex_stdout.log present on disk under output/pdf). Divergence of the duplicated combined-manuscript .md confirmed via content offsets: the same reproducibility code block sits at lines 385-387 in output/pdf/_combined_manuscript.md vs 380-382 in output/web/_combined_manuscript.md, so the copies differ (exact byte sizes 302.1/302.5KB not independently re-verified, no bash). Gate coverage: manuscript-assets check and release_metadata generated_files cover only docs/, output/data/, output/figures/ (release_metadata.py:133-179, assets_io.py:66) — nothing covers output/pdf or output/web, as claimed; no manifest.json/SHA256 provenance exists in the repo. Nuance: the .log is deliberately grepped in the release checklist (docs/release-checklist.md:46), a flimsy justification for committing it; no gitignore of .aux/.blg either. Severity low fair — hygiene/drift risk, deliverable content not wrong.
<!-- PR and issue links are added to the Tracking field after filing. -->