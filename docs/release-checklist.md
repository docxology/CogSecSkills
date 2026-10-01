# Release Checklist

This checklist is for preparing a local release candidate for
`github.com/docxology/CogSecSkills`. It does not publish, tag, or archive a
release by itself.

## Source Gates

```bash
uv sync --locked --extra dev --extra figures
uv run python -m cogsecskills definitions --write
uv run python -m cogsecskills definitions --check
uv run python -m cogsecskills scenarios --check
uv run python -m cogsecskills examples --write
uv run python -m cogsecskills examples --check
uv run python -m cogsecskills evals --write
uv run python -m cogsecskills evals --check
uv run python -m cogsecskills dashboard --write
uv run python -m cogsecskills dashboard --check
uv run python -m cogsecskills manuscript-assets --write
uv run python -m cogsecskills manuscript-assets --check
uv run python -m cogsecskills release-metadata --write
uv run python -m cogsecskills release-metadata --check
uv run python -m cogsecskills catalogue --markdown --output docs/catalogue.md
uv run python -m cogsecskills catalogue --check
uv run python -m cogsecskills validate
uv run python -m cogsecskills report
uv run python -m cogsecskills doctor
uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=99
git diff --check
```

## Style And Type Gates

```bash
uv run ruff check src/cogsecskills tests
uv run ruff format --check src/cogsecskills tests
uv run mypy
```

## Manuscript Gates

With `PROJECT_ROOT` pointing to this checkout, run from the sibling template
checkout:

```bash
uv run --no-sync python -m infrastructure.validation.cli markdown "${PROJECT_ROOT}/docs/manuscript" --repo-root "${PROJECT_ROOT}"
# Run the combined PDF/HTML invocation documented in:
# docs/manuscript/05_reproducibility.md (from the template environment).
pdftotext "${PROJECT_ROOT}/output/pdf/CogSecSkills_combined.pdf" - | rg "Evidence Ladder|Skill Worked Examples|Scenario Readiness|expected answers|Quality Dashboard|Supplemental 100-Skill Catalogue|github.com/docxology/CogSecSkills"
rg -n "Citation .*undefined|undefined references|LaTeX Warning: Reference.*undefined|Missing character|Package .* Error|File .* not found|^!|LaTeX Error|Fatal error|Emergency stop" "${PROJECT_ROOT}/output/pdf/_combined_manuscript.log"
```

The combined-render procedure uses explicit source/output paths and the
template's public API; it does not require a mirror under template/projects/.
Retain the prior PDF before refreshing `CogSecSkills.pdf`, and record source
revision and final PDF hashes only after the gates and content checks pass.

## Human Review

- Confirm `TODO.md` reflects only forward-looking work.
- Confirm `docs/manuscript/references.bib` contains verified entries only.
- Confirm generated files carry generated headers where expected.
- Confirm claim wording stays local: structural conformance and deterministic
  readiness, not field effectiveness.
- Confirm any release tag or archive DOI is real before adding it to prose.
  `public-archive` mode checks a declaration and local readiness only; verify
  the archive record and its source/version identity directly before claiming
  that the current revision was deposited.

## Public Assets And Source Identity

Before tagging, align the package version, lockfile project version, citation
metadata, `.zenodo.json`, changelog, and manuscript version/date. Keep per-skill
specification versions independent. A concept DOI identifies the software
release chain; the older manuscript archive remains a separate historical
record. An assigned version DOI must carry its actual reservation or published
status.

Retain only verified public artifacts: the manuscript PDF, web manuscript,
and built distributions selected for the release. Keep render intermediates,
private paths, credentials, and account/service logs outside the release.
Record each selected asset's filename, byte count, and SHA256 in a release
receipt or checksum file. Verify the installed wheel outside the checkout with
only runtime dependencies before offering it as a release asset.

For an authorized publication:

1. Record the exact source commit and tag target. Push without rewriting remote
   history, then read the remote ref back and compare the full commit IDs.
   Require all five configured Python 3.10–3.14 CI jobs to pass on that release
   candidate before tagging.
2. Publish the GitHub release with the verified assets. Read the live release
   back; check tag, commit, publication state, asset names, sizes, and downloaded
   bytes or authoritative service digests against the local receipt.
3. Check the enabled Zenodo integration's resulting record independently.
   Confirm concept DOI, version, related tag/source URL, attached archive,
   checksums, and published state. Preserve metadata mismatches explicitly.
4. Add the confirmed version DOI to source metadata and public docs. If that
   DOI was assigned after tagging, use a citation follow-up commit without
   moving the published tag; describe the identities of the tagged archive and
   any refreshed manuscript separately.
5. Recheck hosted CI for the published source revision. Report local gates,
   hosted checks, GitHub publication, and Zenodo acceptance as separate results.

The current software concept is `10.5281/zenodo.21513316`; the historical
v1.0.0 manuscript concept/version are `10.5281/zenodo.20804585` and
`10.5281/zenodo.20804586`. See [`cross-repo-scoping.md`](cross-repo-scoping.md)
for the existing software record's source/version metadata mismatch.
