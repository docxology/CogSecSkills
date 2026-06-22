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
- `S01_source_surface.md`
- `S02_release_manifest.md`
- `S10_skill_catalogue.md` - generated; do not edit by hand
- `S11_skill_metadata_matrix.md` - generated; do not edit by hand
- `98_symbols_glossary.md`
- `99_references.md`
- `AGENTS.md`
- `README.md`
- `SYNTAX.md`

Generated figures are written under `../output/figures/` and referenced by the
main manuscript. The title-page cover is also mirrored to `../figures/` because
the shared PDF renderer resolves configured cover images from `manuscript/` but
XeLaTeX compiles from `output/pdf`. Generated catalogue, worked-example, and
quality-dashboard data are written under `../output/data/`.

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
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --write
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check
```

`--write` updates:

- `manuscript/S10_skill_catalogue.md`
- `manuscript/S11_skill_metadata_matrix.md`
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

If generated Markdown or data is wrong, fix `src/cogsecskills/artifacts/manuscript_assets/__init__.py`
or the source registry/skill metadata, then regenerate.

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
remain unavailable unless a real archive DOI exists.

## Verification

From the project root:

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills scenarios --check
PYTHONPATH="src:." python -m cogsecskills examples --write
PYTHONPATH="src:." python -m cogsecskills examples --check
PYTHONPATH="src:." python -m cogsecskills dashboard --write
PYTHONPATH="src:." python -m cogsecskills dashboard --check
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --write
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check
PYTHONPATH="src:." python -m cogsecskills validate
PYTHONPATH="src:." python -m cogsecskills report
PYTHONPATH="src:." python -m cogsecskills doctor
PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py --cov=src/cogsecskills --cov-report=term-missing
```

From the sibling template checkout:

```bash
uv run python -m infrastructure.validation.cli markdown projects/working/CogSecSkills/manuscript/
uv run python scripts/03_render_pdf.py --project working/CogSecSkills
```
