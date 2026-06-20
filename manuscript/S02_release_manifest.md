# Supplemental Local Release and Render Manifest {#sec:release_manifest}

This manifest records the source and environment identifiers for the manuscript
snapshot. It is a release-provenance surface for local review; it does not claim
an archive DOI, public package publication, or empirical field validation.

## Software And Source Identity

| Field | Value |
|---|---|
| Repository | `https://github.com/docxology/CogSecSkills` |
| Citation metadata | `CITATION.cff` |
| Code metadata | `codemeta.json` |
| Package version | `0.1.0` |
| License | `Apache-2.0` |
| Source revision | `e85ecf2cc54eebee1700f60a6a354b83f093ff4b` |
| Revision descriptor | `v0.1.0-2-ge85ecf2-dirty` |
| Archive DOI | unavailable in this snapshot |
| Concept DOI | unavailable in this snapshot |

The revision descriptor is intentionally marked dirty because this manuscript
hardening pass is performed in a working tree with source edits in progress. The
manifest is therefore a local provenance record, not an immutable release
certificate [@cogsecskills2026software].

## Environment And Locking

| Field | Value |
|---|---|
| Python | `Python 3.13.14` |
| uv | `uv 0.11.6 (65950801c 2026-04-09 aarch64-apple-darwin)` |
| Python requirement | `>=3.10` |
| Runtime dependency | `pyyaml>=6.0` |
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

| Gate | Current result |
|---|---|
| `definitions --check` | `canonical definitions are current` |
| `scenarios --check` | `scenario readiness fixtures are current: 28 scenarios across 7 groups; 28 expected answers checked` |
| `examples --check` | `worked examples are current` |
| `dashboard --check` | `quality dashboard is current` |
| `manuscript-assets --check` | `manuscript assets are current` |
| `validate` | `0 error(s), 0 warning(s)` |
| `report` | `registry_total: 100`, `implemented: 100`, `on_disk_skills: 100`, `ok: true` |
| `doctor` | `validation: 0 error(s); quality: 0 finding(s)` |
| `ruff check src/cogsecskills tests` | `All checks passed!` |
| `ruff format --check src/cogsecskills tests` | `38 files already formatted` |
| `mypy` | `Success: no issues found in 19 source files` |
| `pytest --cov=src/cogsecskills` | `620 passed`; total coverage `90.10%` |
| Template markdown validation | `No issues found!` |
| Template PDF render | 13 manuscript sections rendered; 8/8 figures found; combined PDF and HTML generated |
| PDF content smoke | Required strings found: References, Supplemental 100-Skill Catalogue, Reference Density, Harness Contract, Evidence Ladder, Skill Worked Examples, Scenario Readiness, expected answers, Quality Dashboard, Release Manifest, and install cover text |
| PDF render log error scan | No unresolved-reference, missing-character, missing-file, or package-error findings |
