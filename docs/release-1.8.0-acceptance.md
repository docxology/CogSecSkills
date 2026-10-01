# CogSecSkills v1.8.0 — local release acceptance

Measured on 2026-10-01, before GitHub release publication and the resulting
Zenodo version deposit. This receipt records local source, package, and rendered
artifact acceptance. It does not establish hosted CI, external publication,
live model behavior, or defensive effectiveness. The separate
[v1.7.0 review](review-2026-10-01.md) remains a historical baseline.

## Source and package checks

| Check | Result |
|---|---|
| Full suite | `uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=99`: **1248 passed in 276.31s**, **99.65% total coverage**, branch measurement enabled; Python 3.14.4/macOS |
| Coverage detail | 3890 statements, 8 misses; 1314 branches, 10 partial branches |
| Ruff | All checks passed; 108 files already formatted |
| mypy | No issues in 51 source files |
| Corpus gates | 100 implemented skills; `validate`: zero errors/warnings; `doctor`: zero findings |
| Generated source gates | Definitions, 28 scenarios/expected answers, examples, evals, dashboard, release metadata, manuscript assets, and catalogue all current |
| Post-render documentation contracts | 29 documentation/manuscript contract tests passed in 0.06s |
| Package acceptance | 17 isolated build/install/import/CLI commands passed across Python 3.14.4 and 3.10.20; runtime-only installed wheels run outside the checkout with explicit root and discover the checkout root by default |
| Build metadata | SPDX license and explicit license files; final 1.8.0 wheel/sdist built with the normal backend. Minimum-backend `setuptools==77.0.3` SPDX compatibility was verified on the preceding 1.7.0 snapshot, including Python 3.10 |

The README embedded in the release wheel has SHA256
`328bcc1f0a36ec5a252832ba03748b175a311d7b4cc408b5ea045e5712c5470a`.
Source commit/tag identity is recorded and verified at publication; these local
checks do not substitute for comparing the published ref and asset bytes.

## Verified public artifacts

| Artifact | Bytes | SHA256 |
|---|---:|---|
| `CogSecSkills.pdf` and `output/pdf/CogSecSkills_combined.pdf` (identical) | 3,310,510 each | `795e4217f0e22bde2617e729f8b10f00694a2d95036aae16d0af3d0e891ba7fc` |
| `output/web/index.html` | 426,231 | `0349b95488e28beb83fa67e74c342c54420ee8ded25bdc16c666a3f72f1ec284` |
| `cogsecskills-1.8.0-py3-none-any.whl` | 129,475 | `7af2cf3af7a04f732802dd620e2c3d84207a5abfe2e1ce7d741d0df338c5638e` |
| `cogsecskills-1.8.0.tar.gz` | 110,125 | `5fd138979e623e24da27a135960e8eb24f2ee0697e57656ee05104ae6566bd90` |

The staged render used the sibling template's public combined PDF/HTML APIs.
All **14 manuscript sections** and **26 manuscript/configuration/bibliography/
image inputs** matched their source hashes before retention. Template Markdown
validation returned `No issues found!`; strict pre-render validation returned
`No render-blocking pitfalls or undefined citations found.` Both exited zero.

The retained PDF has **71 pages**, all 100 exact skill identifiers after
whitespace normalization of raw extracted text, and eight embedded color images.
Fifteen content checks cover v1.8.0, the final test/coverage receipt, software
concept DOI, source/evidence surfaces, and installation text. HTML contains
exactly **100 ordered rows across seven catalogue tables**, all 14 displayed
fields per skill, and the exact seven-by-eight verb matrix. Its seven relative
image references resolve to the retained figure files.

Render logs have no unresolved citations/references, missing characters/files,
package errors, or fatal errors. PDF text/bytes and HTML have no private
filesystem paths. Visual inspection of physical PDF pages 1, 29, 30, and 67
confirmed the cover, manifest, catalogue metadata, and matrix are legible with
no collisions. One **0.56659-point** overfull box remains in ordinary prose.
The current browser surface was unavailable, so current HTML acceptance uses
parsed payload and image-reference checks; the prior v1.7.0 browser review is
historical, not a new browser result. Web formulas use the existing MathJax CDN
and require network access; a downloadable web bundle must include the seven
relative figure files.

Renderer environment: template version 4.0.0 at
`f1914383a08f0f4195134ed33a359b7aacc4f978`, Python 3.14.4, uv 0.12.19,
Pandoc 3.11, pandoc-crossref 0.3.25, and XeTeX 0.999998/TeX Live 2026.
The installed environment was reused without installing or updating dependencies.

Rollback copies of the prior v1.7.0 PDFs and HTML were preserved locally. Their
PDF SHA256 is `e50d15140610f2d194db2a27c56a31af29832c42b43c2f2ee759f84a75a2cf7c`;
HTML SHA256 is `652909d3f60f716192e67029ef5d46ef5b5d9f2c0e5bccfaefa9eae30b344d05`.
Only verified PDF/HTML artifacts were retained; this render's intermediates and
logs remain outside the repository.

## Archive identity and publication follow-up

The current software concept is
[10.5281/zenodo.21513316](https://doi.org/10.5281/zenodo.21513316). The earlier
[software record 21520558](https://zenodo.org/records/21520558) links to the
GitHub v1.7.0 tree and contains its source ZIP, but its metadata says `1.0.0`.
The historical v1.0.0 manuscript archive remains separate: concept
`10.5281/zenodo.20804585`, version `10.5281/zenodo.20804586`.

The v1.8.0 source candidate carries the software concept DOI. Before tagging,
require all five Python 3.10–3.14 hosted CI jobs for its published source commit.
Then verify GitHub release assets and the resulting Zenodo record's assigned
version DOI, exact version, related tag URL, published state, and file identity.
Record the confirmed DOI in a follow-up citation/ledger commit without moving
the published tag. No v1.8.0 version DOI is invented by this local receipt.
