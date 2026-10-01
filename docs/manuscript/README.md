# Manuscript - CogSecSkills

This directory is the rendered manuscript source for:

**CogSecSkills: Multiharness Cognitive Security Skill Library**

A defensive, educational, harness-neutral library of Cognitive Security and analytic tradecraft skills with registry, AGEINT upstream, and conformance tests.

## File Inventory

- `config.yaml`
- `preamble.md`
- `references.bib`
- `00_abstract.md`
- `01_introduction.md`
- `02_system_context.md`
- `03_methods.md`
- `04_artifacts_and_evidence.md`
- `05_reproducibility.md`
- `06_limitations_and_next_steps.md`
- `07_ethics_and_responsible_use.md`
- `S01_source_surface.md`
- `S02_release_manifest.md`
- `S10_skill_catalogue.md` - generated; do not edit by hand
- `S11_skill_metadata_matrix.md` - generated; do not edit by hand
- `98_symbols_glossary.md`
- `99_references.md`
- `AGENTS.md`
- `README.md`
- `SYNTAX.md`

Generated figures are written under `../../output/figures/` and referenced by the
main manuscript. The title-page cover is also mirrored to `../../figures/` because
the shared PDF renderer resolves configured cover images from `docs/manuscript/` but
XeLaTeX compiles from `output/pdf`. Generated catalogue, worked-example, and
quality-dashboard data are written under `../../output/data/`.

## Source Surfaces

| Surface | Role |
|---|---|
| `registry/` | Source directory to inspect before turning prose into claims. |
| `definitions/` | Canonical skill-definition source directory; render `skills/` from here. |
| `skills/` | Source directory to inspect before turning prose into claims. |
| `scenarios/` | Curated safe-use, unsafe-redirect, expected-response, and expected-answer fixtures for deterministic readiness checks. |
| `examples/skill-worked-examples.yaml` | Source-owned deterministic worked examples, one per skill. |
| `docs/skill-worked-examples.md` | Generated worked-example view over all 100 skills. |
| `docs/quality-dashboard.md` / `docs/quality-dashboard.html` | Generated dashboard views over all 100 skills, scenarios, worked examples, and quality capsules. |
| `docs/ageint/` | Source directory to inspect before turning prose into claims. |
| `src/cogsecskills/` | Source directory to inspect before turning prose into claims. |
| `tests/` | Source directory to inspect before turning prose into claims. |

## Generated Supplements And Figures

Regenerate synchronized manuscript assets from the project root:

```bash
uv run python -m cogsecskills manuscript-assets --write
uv run python -m cogsecskills manuscript-assets --check
```

`--write` updates:

- `docs/manuscript/S10_skill_catalogue.md`
- `docs/manuscript/S11_skill_metadata_matrix.md`
- `output/data/skill_catalogue.json`
- `output/data/skill_catalogue.csv`
- `output/figures/cogsecskills_taxonomy_counts.png`
- `output/figures/cogsecskills_skill_grid.png`
- `output/figures/cogsecskills_verb_heatmap.png`
- `output/figures/cogsecskills_ageint_network.png`
- `output/figures/cogsecskills_plan_build_teach_flow.png`
- `output/figures/cogsecskills_reference_density.png`
- `output/figures/cogsecskills_harness_contract.png`
- `output/figures/cogsecskills_cover_installation.png` - canonical generated cover image
- `figures/cogsecskills_cover_installation.png` - synchronized title-page cover mirror configured in `config.yaml`

If generated Markdown or data is wrong, fix the generator under
`src/cogsecskills/artifacts/manuscript_assets/` or the source registry/skill
metadata, then regenerate.

The catalogue and verb matrix supply separate generated LaTeX and HTML table
payloads. The PDF and web manuscript retain the same 100 skill rows, exact
identifiers, evidence fields, and group-level verb counts. Keep both payloads
current when changing table layout or source fields.

## Citations And Provenance

`references.bib` contains verified manuscript-level references only. Use Pandoc
citation syntax such as `[@sandve2013reproducible]` only after the key exists in
that file. External scholarship may motivate the problem, positioning, and
interface design, but it must not be worded as evidence of CogSecSkills field
effectiveness. Per-skill `refs` counts in generated supplements are skill
metadata; they are not the rendered manuscript bibliography.

`S02_release_manifest.md` records the repository URL, version, license, source
revision descriptor, environment versions, lockfile presence, generated figure
inventory, and final gate results for the local manuscript snapshot. DOI fields
are declarations in source metadata; local gates do not check archive
resolution, DOI/version identity, or deposition of the current revision. Verify
the external record before describing this snapshot as archived.

The current software concept is `10.5281/zenodo.21513316`. The separate
historical v1.0.0 manuscript archive remains under concept
`10.5281/zenodo.20804585`, version `10.5281/zenodo.20804586`; it does not
identify the current software release chain.

## Verification

From the project root:

```bash
uv run python -m cogsecskills definitions --write
uv run python -m cogsecskills definitions --check
uv run python -m cogsecskills scenarios --check
uv run python -m cogsecskills examples --write
uv run python -m cogsecskills examples --check
uv run python -m cogsecskills dashboard --write
uv run python -m cogsecskills dashboard --check
uv run python -m cogsecskills manuscript-assets --write
uv run python -m cogsecskills manuscript-assets --check
uv run python -m cogsecskills validate
uv run python -m cogsecskills report
uv run python -m cogsecskills doctor
uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=99
```

For the sibling template environment, follow the explicit combined-render
invocation in [`05_reproducibility.md`](05_reproducibility.md). It uses the
public `RenderManager` APIs with this checkout's source and output paths; no
legacy template project mirror is required.
