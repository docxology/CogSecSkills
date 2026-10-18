# Supplemental Local Release and Render Manifest {#sec:release_manifest}

This manifest records the source and environment identifiers for the manuscript
snapshot. It is a release-provenance surface for local review; declared concept
and historical archive identifiers do not establish a new version deposit,
public package publication, or empirical field validation.

## Software And Source Identity

| Field | Value |
|---|---|
| Repository | `https://github.com/docxology/CogSecSkills` |
| Citation metadata | `CITATION.cff` |
| Code metadata | `codemeta.json` |
| Package version | `1.8.0` |
| Declared manuscript base date | `2026-10-01` |
| License | `Apache-2.0` |
| Source revision | runtime-observed by `release-metadata --write`; not embedded in committed files |
| Software archive | concept `10.5281/zenodo.21513316`; v1.8.0 version DOI unavailable in this snapshot |
| Historical manuscript archive | v1.0.0: concept `10.5281/zenodo.20804585`, version `10.5281/zenodo.20804586` |
| Concept DOI | `10.5281/zenodo.21513316` (software release chain) |

The revision descriptor and dirty-state are intentionally observed at runtime by
`release-metadata --write` rather than embedded in committed files, so the
`--check` gate remains stable after a release-metadata commit.

## Environment And Locking

| Field | Value |
|---|---|
| Python (local candidate checks) | `Python 3.14.8` |
| uv (local candidate checks) | `uv 0.13.0` |
| Python requirement | `>=3.10` |
| Runtime dependencies | `pyyaml>=6.0`; `tomli>=2.0` on Python 3.10 |
| Development gates | `pytest`, `pytest-cov`, `mypy`, `ruff` |
| Lockfile | `uv.lock` present |

## Generated Figure Inventory

| Figure file | Manuscript label |
|---|---|
| `output/figures/cogsecskills_taxonomy_counts.png` | `@fig:taxonomy-counts` |
| `output/figures/cogsecskills_skill_grid.png` | `@fig:skill-grid` |
| `output/figures/cogsecskills_verb_heatmap.png` | `@fig:verb-heatmap` |
| `output/figures/cogsecskills_ageint_network.png` | `@fig:ageint-network` |
| `output/figures/cogsecskills_plan_build_teach_flow.png` | `@fig:plan-build-teach-flow` |
| `output/figures/cogsecskills_reference_density.png` | `@fig:reference-density` |
| `output/figures/cogsecskills_harness_contract.png` | `@fig:harness-contract` |
| `output/figures/cogsecskills_cover_installation.png` | title-page cover image |

## Verification Gates

The current post-v1.8.0 source gates below were measured on 2026-10-18.
The published v1.8.0 acceptance remains historical in
`docs/release-1.8.0-acceptance.md`; the earlier v1.7.0 review remains in
`docs/review-2026-10-01.md`. Each rendered source snapshot has its own receipt.
These maintenance checks do not create a new software release or archive.
Results describe the local source/render snapshot. They do not establish
a hosted CI result, a fresh run of every supported Python version, live model
behavior, or a new archive deposit. The archive DOI fields above are historical
source declarations; this local gate sweep does not check their resolution or
source/version identity.

The earlier software record `10.5281/zenodo.21520558` links to the GitHub
v1.7.0 tree and contains its source ZIP, while its public metadata says version
`1.0.0`. That metadata mismatch is preserved here; it is not evidence of a
v1.8.0 deposit. The separate historical manuscript archive contains the v1.0.0
PDF and is not the current software concept.

| Gate | Local candidate result (2026-10-18) |
|---|---|
| `definitions --check` | `canonical definitions are current` |
| `scenarios --check` | `scenario readiness fixtures are current: 28 scenarios across 7 groups; 28 expected answers checked` |
| `examples --check` | `worked examples are current` |
| `evals --check` | `offline evaluation fixtures are current` |
| `dashboard --check` | `quality dashboard is current` |
| `release-metadata --check` | `release metadata is current (local mode)` |
| `manuscript-assets --check` | `manuscript assets are current` |
| `validate` | `0 error(s), 0 warning(s)` |
| `report` | `registry_total: 100`, `implemented: 100`, `on_disk_skills: 100`, `ok: true` |
| `doctor` | `validation: 0 error(s); quality: 0 finding(s)` |
| `ruff check src/cogsecskills tests` | `All checks passed!` |
| `ruff format --check src/cogsecskills tests` | `124 files already formatted` |
| `mypy` | `Success: no issues found in 51 source files` |
| `uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=99` | `1291 passed` in `103.27s`; total coverage `99.54%` with branch measurement enabled (Python 3.14.8, macOS) |
| Template Markdown and pre-render validation | No issues found; no render-blocking pitfalls or undefined citations |
| Template PDF/HTML render | Required: all 14 source sections, seven body figures, and resolved references; the PDF includes the title-page cover; both formats retain all 100 catalogue rows; final receipt accompanies the generated artifacts |
| PDF content smoke | Required: References, Supplemental 100-Skill Catalogue, Reference Density, Harness Contract, Evidence Ladder, Skill Worked Examples, Scenario Readiness, expected answers, Quality Dashboard, Release Manifest, and install cover text |
| PDF render log error scan | Required: no unresolved-reference, missing-character, missing-file, or package-error findings |
