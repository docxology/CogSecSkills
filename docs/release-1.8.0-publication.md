# CogSecSkills v1.8.0 — publication receipt

Verified on 2026-10-01. The [GitHub release](https://github.com/docxology/CogSecSkills/releases/tag/v1.8.0)
and [Zenodo record](https://zenodo.org/records/23090954) are published; the
complete deposited source matches the immutable release tag. Local
test/package/render evidence remains in the separate
[acceptance receipt](release-1.8.0-acceptance.md). Publication and byte identity
do not establish live-model correctness, connector support, field effectiveness,
or peer review.

## Source and hosted checks

| Field | Verified value |
|---|---|
| Release | `v1.8.0`; GitHub release ID `401359356` |
| Source commit | `38f4b8e17c97d18a69a906f4a895a7cbb730e786` |
| Annotated tag object | `89f78cf3384cc96b3b8db2564dda466a9a5dd45c`, peeling to the source commit above |
| GitHub state | Published, non-draft, non-prerelease; six uploaded assets |
| Publication timestamp | `2026-10-01T21:11:13Z` |
| Hosted CI | [Run 36925387817](https://github.com/docxology/CogSecSkills/actions/runs/36925387817), push to `main` at the exact release commit; completed, `success` |

All five CI jobs passed: Python **3.10, 3.11, 3.12, 3.13, and 3.14**. Each job
accepted the locked environment, Ruff, mypy, tests/coverage gate, skill
validation, doctor, generated-source coherence, and clean installed-wheel smoke
outside the checkout. The release was published after those jobs completed.
Remote tag identity was read back and compared with the local annotated tag and
peeled commit.

The complete public job logs record the following test results. Coverage is the
combined statement/branch measure; each job measured 3890 statements and 1314
branches.

| Python job | Tests | Duration | Total coverage | Statement misses / partial branches |
|---|---:|---:|---:|---:|
| 3.10 | 1248 passed | 539.14s | 99.65% | 9 / 9 |
| 3.11 | 1248 passed | 488.57s | 99.67% | 8 / 9 |
| 3.12 | 1248 passed | 495.77s | 99.67% | 8 / 9 |
| 3.13 | 1248 passed | 395.98s | 99.67% | 8 / 9 |
| 3.14 | 1248 passed | 126.00s | 99.65% | 8 / 10 |

## GitHub release assets

All six assets were downloaded after publication. Every download matched its
verified local bytes, byte count, and SHA256; the checksum manifest matched all
five payload assets. GitHub's reported SHA256 digests also agree.

| Asset | Bytes | SHA256 |
|---|---:|---|
| `CogSecSkills-v1.8.0.pdf` | 3,310,510 | `795e4217f0e22bde2617e729f8b10f00694a2d95036aae16d0af3d0e891ba7fc` |
| `CogSecSkills-v1.8.0-web.zip` | 2,287,034 | `9e778679e933f3047d73295c890e62a4d829f1b3aea2ad82b865598afbc749d0` |
| `CogSecSkills-v1.8.0-source.zip` | 12,358,910 | `66e6d049e09de58952b132869f9471a208afafb21e9ae57a150032b58bc77115` |
| `cogsecskills-1.8.0-py3-none-any.whl` | 129,475 | `7af2cf3af7a04f732802dd620e2c3d84207a5abfe2e1ce7d741d0df338c5638e` |
| `cogsecskills-1.8.0.tar.gz` | 110,125 | `5fd138979e623e24da27a135960e8eb24f2ee0697e57656ee05104ae6566bd90` |
| `SHA256SUMS` | 475 | `2d168e097d3b68f0b94fd3703a4cef917eb76585af4a9765d10ff90c2386692c` |

The PDF is identical to the verified root and combined PDFs. The web bundle
preserves the HTML manuscript and its seven relative figure references; formulas
use the existing MathJax CDN and require network access. The source ZIP includes
the full tagged repository. Wheel/sdist acceptance and the exact rendered HTML
hash are recorded in the local receipt. A GitHub source ZIP and a Zenodo ZIP can
have different archive bytes because their prefixes and metadata differ; source
payload identity is verified separately below.

## Zenodo version and complete source identity

| Field | Verified value |
|---|---|
| Record | [23090954](https://zenodo.org/records/23090954) |
| Version DOI | [10.5281/zenodo.23090954](https://doi.org/10.5281/zenodo.23090954) |
| Software concept DOI | [10.5281/zenodo.21513316](https://doi.org/10.5281/zenodo.21513316) |
| Version / publication date | `1.8.0` / `2026-10-01` |
| Record state | `submitted: true`, `state: done` |
| Related source | `https://github.com/docxology/CogSecSkills/tree/v1.8.0`, `isSupplementTo`, software |
| Archived filename | `docxology/CogSecSkills-v1.8.0.zip` |
| Archive size | 12,385,090 bytes |
| Record MD5 / downloaded MD5 | `e20c89ea4c91c13aaf0433a5cf10feb7` / identical |
| Downloaded SHA256 | `94c1cf431550159fa949850ec4404bfea5e78f4244e9de348369b9c7c1175587` |

The public API record was inspected directly. Independent archive review checked
the downloaded ZIP's complete inventory against the Git blobs at
`38f4b8e17c97d18a69a906f4a895a7cbb730e786`: **941 of 941 files**, totaling
**19,833,777 source bytes**, matched byte-for-byte. Paths were unique and safe
under one GitHub prefix; the ZIP comment carried the full release commit ID.
This comparison binds the actual archived payload to the tagged source rather
than relying only on a DOI declaration, related URL, or archive checksum.

The earlier software record `21520558` links to the v1.7.0 tree while its
metadata says `1.0.0`; that historical mismatch is preserved. The separate
v1.0.0 manuscript archive remains under concept `20804585`, version `20804586`.
Neither is used as the current v1.8.0 version identity.

## Citation follow-up and immutable release boundary

The release tag was created with the software concept DOI. Zenodo assigned the
new version DOI after publication. The subsequent `main` citation/ledger and
documentation update records that confirmed DOI without moving the tag or
replacing its released assets. The deposited ZIP remains the exact tagged
source; it does not include the later citation follow-up.

The released wheel's embedded README remains the tagged snapshot with SHA256
`328bcc1f0a36ec5a252832ba03748b175a311d7b4cc408b5ea045e5712c5470a`.
The retained manuscript configuration, release manifest, PDF, and HTML likewise
retain their release-snapshot bytes. This receipt documents publication without
rebuilding those artifacts or implying their concept DOI was a version DOI.
