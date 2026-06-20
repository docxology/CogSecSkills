# Manuscript Syntax - CogSecSkills

This manuscript uses the shared template conventions from `docs/guides/manuscript-semantics.md` in the sibling template repository.

## Section Labels

| File | H1 | Label |
|---|---|---|
| `00_abstract.md` | Abstract | `{#sec:abstract}` |
| `01_introduction.md` | Library Purpose and Reader Map | `{#sec:introduction}` |
| `02_system_context.md` | Source Boundary and Harness-Neutral Skill Contract | `{#sec:system_context}` |
| `03_methods.md` | Source-Owned Authoring and Manuscript Generation | `{#sec:methods}` |
| `04_artifacts_and_evidence.md` | Evidence Surfaces, Generated Views, and Claim Discipline | `{#sec:artifacts_evidence}` |
| `05_reproducibility.md` | Reproducibility and Render Gates | `{#sec:reproducibility}` |
| `06_limitations_and_next_steps.md` | Evidence Boundaries, Defensive Governance, and Next Steps | `{#sec:limitations_next_steps}` |
| `S01_source_surface.md` | Supplemental Claim-Provenance Source Map | `{#sec:source_surface}` |
| `S02_release_manifest.md` | Supplemental Local Release and Render Manifest | `{#sec:release_manifest}` |
| `S10_skill_catalogue.md` | Supplemental 100-Skill Catalogue | `{#sec:supplemental_skill_catalogue}` |
| `S11_skill_metadata_matrix.md` | Supplemental Skill Metadata and Figure Matrix | `{#sec:supplemental_skill_metadata_matrix}` |
| `98_symbols_glossary.md` | Symbols and Skill-System Glossary | `{#sec:symbols_glossary}` |
| `99_references.md` | References | `{#sec:references}` |

## Citations

Use Pandoc citation syntax only, for example `[@sandve2013reproducible]`. Every key must exist in `references.bib` before it appears in prose. Do not paste review-tool citation artifacts such as file-citation handles or turn IDs into manuscript Markdown.

## Figures

Generated figures live under `../output/figures/` and are referenced with labels such as:

```markdown
![Caption text.](../output/figures/example.png){#fig:example width=80%}
```

Current generated figure labels:

| Figure | Label |
| --- | --- |
| `cogsecskills_taxonomy_counts.png` | `{#fig:taxonomy-counts}` |
| `cogsecskills_skill_grid.png` | `{#fig:skill-grid}` |
| `cogsecskills_verb_heatmap.png` | `{#fig:verb-heatmap}` |
| `cogsecskills_ageint_network.png` | `{#fig:ageint-network}` |
| `cogsecskills_plan_build_teach_flow.png` | `{#fig:plan-build-teach-flow}` |
| `cogsecskills_reference_density.png` | `{#fig:reference-density}` |
| `cogsecskills_harness_contract.png` | `{#fig:harness-contract}` |

The generated title-page cover image is configured in `config.yaml` rather than
referenced as a Markdown figure:

| Cover image | Config field |
| --- | --- |
| `cogsecskills_cover_installation.png` | `paper.cover.image` |

The generator writes the canonical cover under `output/figures/` and a byte-
identical mirror under root `figures/` for the shared PDF title-page renderer.

## Generated Files

Run from the project root:

```bash
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --write
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check
```

Generated supplements must keep their generated-file header. Edit the generator
or source metadata instead of editing `S10_` or `S11_` by hand.

## Scenario Fixtures

`scenarios/defensive_readiness.yaml` is an authored local-readiness fixture set.
It supports the manuscript's Scenario Readiness claim only when this command
passes:

```bash
PYTHONPATH="src:." python -m cogsecskills scenarios --check
```

Those fixtures include expected-response metadata and reviewed expected-answer
bodies. Do not describe them as live harness runs, external model evaluations,
or field validation.

## Skill Worked Examples

`examples/skill-worked-examples.yaml` is the source-owned fixture file. The
generated reader views are:

```bash
PYTHONPATH="src:." python -m cogsecskills examples --write
PYTHONPATH="src:." python -m cogsecskills examples --check
```

`docs/skill-worked-examples.md` and
`output/data/skill_worked_examples.json` are generated. Treat them as local
expected-answer examples, not live harness transcripts or empirical validation.

## Quality Dashboard

`docs/quality-dashboard.md` and `output/data/quality_dashboard.json` are generated
drift surfaces. Regenerate and check them from the project root:

```bash
PYTHONPATH="src:." python -m cogsecskills dashboard --write
PYTHONPATH="src:." python -m cogsecskills dashboard --check
```

Do not hand-edit the generated dashboard or cite it as empirical effectiveness
evidence.

## Claims

Quantitative and publication claims need support from a source file, test,
generated artifact, or resolved citation. Local validation and render success do
not by themselves prove field efficacy or release readiness.
