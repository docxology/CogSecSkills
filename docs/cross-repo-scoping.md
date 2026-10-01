# Cross-Repo Scoping

Workflows that use sibling repositories or authenticated publication services,
with their source, ownership, and verification boundaries. The v1.7.0 local
manuscript refresh was verified on 2026-10-01; v1.8.0 publication preparation
uses these same workflows and records new acceptance separately.

## 1. Manuscript PDF refresh — template rendering dependency

Manuscript sources live in this repository's `docs/manuscript/`. The renderer
lives in the sibling docxology template checkout (`../template`); its public
`RenderManager` combined PDF/HTML APIs accept explicit source and output paths.
A checkout or symlink under template/projects/ is unnecessary.

Use [`manuscript/05_reproducibility.md`](manuscript/05_reproducibility.md) for the
current portable invocation. Validate Markdown and citation/source contracts,
render with the already installed template environment and XeLaTeX, inspect the
PDF text and render log, then refresh the root `CogSecSkills.pdf` from a verified
combined PDF. Preserve the previous PDF and record the source identity and
artifact hashes. `manuscript-assets --check` remains the generated source gate;
it does not verify a rendered PDF's freshness.

The template checkout supplies imports and dependencies; configured build
outputs stay in this repository or a staging directory. Updating or installing
the template itself is separate scope. Acceptance: the PDF regenerates cleanly,
all declared figures resolve, citations have no unresolved markers, and
`S02_release_manifest.md` identifies the exact local gates supporting the source
snapshot. A refreshed local PDF is not a new archive deposit.

The completed local v1.7.0 render and its hashes are recorded in
[`review-2026-10-01.md`](review-2026-10-01.md). A new source version requires
a new staged render and receipt; preserve the prior artifacts for rollback.

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
4. **Tests without external network** — exercise real local fixture servers
   or executable processes with deterministic response/failure cases, following
   this repository's no-mock rule. Live provider calls stay opt-in like
   `eval-live`.
5. **Boundary documentation** — update `docs/connector-boundaries.md` and the
   skill `harness/*.md` adapters for any new verb surface before claiming
   support.

The `runtime_eval.harness_commands` config pattern (see
[`live-eval.md`](live-eval.md)) is the intended seam: connector-backed
harnesses would be declared as command templates, not code.

## 3. GitHub / Zenodo publication — authorized account workflow

The current software concept is `10.5281/zenodo.21513316`, recorded in
`CITATION.cff`, `codemeta.json`, and manuscript configuration. The separate
v1.0.0 manuscript archive has concept `10.5281/zenodo.20804585` and version
`10.5281/zenodo.20804586`; preserve that history without using it as the
current software release chain.

The existing software record
[`21520558`](https://zenodo.org/records/21520558) contains a source ZIP linked
to the GitHub v1.7.0 tree, while its metadata says version `1.0.0`. This
mismatch must remain explicit. The corrected `.zenodo.json` declares v1.8.0
for the next software deposit.

Publication can run through the authenticated GitHub account and its enabled
Zenodo integration, or an explicitly authorized Zenodo account workflow. The
repository supplies metadata and public assets; account authorization and live
service verification are separate requirements. The v1.8.0 candidate was
prepared on 2026-10-01 under publication authorization; consult its release
receipt for final assets and live archive acceptance.

1. Complete [`release-checklist.md`](release-checklist.md), publish the verified
   source tag and public release assets, and compare the remote tag/commit and
   asset bytes against the local receipt.
2. Inspect the resulting Zenodo record. Confirm software concept, exact
   version, related source/tag URL, archive files, checksums, and published
   state. A successful GitHub release does not establish Zenodo acceptance.
3. Record only an actual assigned version DOI and its verified status in
   citation/manuscript metadata. Keep the software concept as the stable
   all-version identifier and retain the historical manuscript identifier.
   If the integration assigns the DOI after the tag is published, record it in
   a follow-up commit; preserve the published tag's source identity.
4. Regenerate with `release-metadata --write`, then run
   `release-metadata --check`. The generated matrix records DOI declarations;
   verify the external record and its version/source identity separately.
5. Refresh public archive prose and render any manuscript metadata changes
   using the same verified process. Record whether a deposited artifact belongs
   to the release tag or a subsequent citation update.

## 4. Small residuals (any repo, next release PR)

- Keep the CodeMeta author identity and modification date synchronized with
  the source-owned release metadata.
- `hum-docxology` manuscript collector consumes this repo's `docs/manuscript/`
  publication source; after any `docs/manuscript/` structural change, its
  collector view should be re-synced (see its `AGENTS.md` cross-refs).
