# Cross-Repo Scoping

Work that completes CogSecSkills' major-lane goals but belongs partly or
wholly in sibling repositories, with the prerequisites each item needs before
it can be executed. Nothing here is claimed as done; each section states the
boundary that currently blocks it.

## 1. Manuscript PDF re-render — docxology template repo

The root `CogSecSkills.pdf` renders the v1.0.0-era manuscript (last
PDF-touching commit `79da8bd`, 2026-06-22) while the library is at 1.7.0+ and
every generated supplement (`S10`, `S11`, figures, dashboard, release matrix)
is current per the `manuscript-assets`/`dashboard`/`release-metadata` `--check`
gates. The render pipeline lives in the **sibling docxology template**
checkout (`../template` relative to this repo), not here.

Steps once a template working copy is authorized:

1. Provide the project working copy the template expects:
   `../template/projects/working/CogSecSkills` (a checkout or symlink of this
   repo — the render pipeline resolves the project from there).
2. Markdown validation from the template checkout:
   `uv run python -m infrastructure.validation.cli markdown projects/working/CogSecSkills/manuscript/`
3. PDF render: `uv run python scripts/03_render_pdf.py --project working/CogSecSkills`
   (XeLaTeX required; the cover image resolves from `docs/manuscript/` and is
   mirrored to top-level `figures/` by `manuscript-assets --write`).
4. Copy the rendered PDF to this repo's root `CogSecSkills.pdf`, regenerate
   `output/pdf/` artifacts, and run this repo's full gate sweep
   (`manuscript-assets --check` must stay current).

Boundary: steps 1–3 write inside the template checkout (dependency install,
LaTeX build artifacts). Requires the owner's go-ahead to touch that repo, plus
XeLaTeX locally. Acceptance: PDF regenerates cleanly and `S02_release_manifest`
reflects the 1.7.x library numbers.

## 2. Live connector integrations — this repo + hum-search

The TODO major lane permits connector-specific harness notes only when a live
connector is intentionally wired, gated on privacy/legal checks, source
custody, rate-limit handling, and connector-specific tests. None are wired.

Prerequisites before any connector is described as supported:

1. **Provider selection** — the platform's `hum-search` service is reported
   (in the platform registry and `projects/platform/` docs) to unify Exa,
   Semantic Scholar, Tavily, ArXiv, and DuckDuckGo behind one process
   contract; wrapping `hum-search` (rather than adding direct provider SDKs)
   would keep this repo dependency-free and reuse-first. Verify its current
   contract in its own repo before designing against it.
2. **Privacy/legal review** — what queries leave the machine, provider data
   retention, and the defensive-only boundary applied to query construction.
3. **Source custody + rate limits** — per-provider limits, retry/backoff, and
   where evidence provenance (URL, retrieval date) is recorded.
4. **Tests without network** — connector behavior behind an injectable fetch
   callable (the pattern `hum-docxology` discovery uses), so CI stays
   deterministic; live calls stay opt-in like `eval-live`.
5. **Boundary documentation** — update `docs/connector-boundaries.md` and the
   skill `harness/*.md` adapters for any new verb surface before claiming
   support.

The `runtime_eval.harness_commands` config pattern (see
[`live-eval.md`](live-eval.md)) is the intended seam: connector-backed
harnesses would be declared as command templates, not code.

## 3. Zenodo deposit / version DOI — owner action

`CITATION.cff` currently cites the v1.0.0 version DOI
(`10.5281/zenodo.20804586`) while `codemeta.json` carries the concept DOI
only; `.zenodo.json` now says version `1.7.0` for the next deposit. When the
owner deposits a new version on Zenodo:

1. Record the new version DOI in `CITATION.cff` (identifier list) and
   `codemeta.json` (`identifier`), keeping the concept DOI
   `10.5281/zenodo.20804585` as the always-latest pointer.
2. Update the version-DOI description (currently "Version DOI (v1.0.0)") and
   `codemeta.json` `dateModified`.
3. Refresh README badge/DOI prose if the concept-DOI framing changes.
4. Re-run `release-metadata --check` and update `docs/release-claim-matrix.md`
   if the public-archive claim flips from unavailable to present.

This cannot be executed from the repo — it requires the owner's Zenodo
account and a release publication decision.

## 4. Small residuals (any repo, next release PR)

- `codemeta.json`: add the author email from `pyproject.toml`
  (`daniel@activeinference.institute`) and bump `dateModified` at release
  time.
- `hum-docxology` manuscript collector consumes this repo's `manuscript/`
  publication source; after any `docs/manuscript/` structural change, its
  collector view should be re-synced (see its `AGENTS.md` cross-refs).
