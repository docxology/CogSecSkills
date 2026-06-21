# Supplemental Claim-Provenance Source Map {#sec:source_surface}

This supplement records the source surfaces that own manuscript claims. Use it
as the quick provenance map before editing prose, generated supplements, figures,
or verification statements.

| Surface | Role |
|---|---|
| `registry/skills.yaml` | Catalogue plan: skill ids, names, groups, status, summaries, and AGEINT topics. |
| `registry/groups.yaml` | Taxonomy plan: group ids and display titles. |
| `skills/**/skill.yaml` | Skill build contract: triggers, verbs, inputs, outputs, references, and harness paths. |
| `skills/**/SKILL.md` | Harness-facing one-skill description and "when to use" guidance. |
| `skills/**/workflow.md` | Harness-neutral step procedure and anti-criteria. |
| `skills/**/harness/*.md` | Adapter bindings for every configured harness; the default set is Claude, Codex, and Hermes. |
| `scenarios/defensive_readiness.yaml` | Curated safe-use, unsafe-redirect, expected response-shape, and expected-answer fixtures for deterministic scenario readiness. |
| `examples/skill-worked-examples.yaml` | Source-owned deterministic worked examples, one per skill. |
| `examples/` | Local non-secret harness smoke transcripts, group examples, and source worked examples; these are fixtures, not live runtime evidence. |
| `docs/skill-worked-examples.md` | Generated Markdown worked-example catalogue for all 100 skills. |
| `output/data/skill_worked_examples.json` | Generated machine-readable worked-example snapshot. |
| `docs/quality-dashboard.md` / `docs/quality-dashboard.html` | Generated Markdown and static HTML dashboard over all 100 skills, quality capsules, scenario coverage, worked-example coverage, harnesses, references, claim-boundary status, and verified-state rows. |
| `output/data/quality_dashboard.json` | Generated machine-readable dashboard snapshot used for drift review. |
| `docs/claim-boundaries.md` | Reader-facing statement of what local gates prove and do not prove. |
| `docs/connector-boundaries.md` | Optional OSINT/web connector boundaries before any live connector is wired. |
| `docs/analyst-output-review.md` | Lightweight rubric for future analyst-output review fixtures. |
| `docs/future-validation-protocols.md` | Future-only protocols for baseline comparison, analyst usability, connector readiness, and DOI/publication readiness. |
| `docs/release-checklist.md` | Release-candidate command and human-review checklist. |
| `docs/ageint/` | Educational upstream and AGEINT topic context. |
| `src/cogsecskills/` | Parser, validator, authoring, insights, scenario checker, CLI, and manuscript asset generator. |
| `tests/` | Regression evidence for contract, CLI, configuration, insights, scenarios, and generated assets. |
| `CITATION.cff` | Software citation metadata for the repository-level artifact. |
| `codemeta.json` | Machine-readable software metadata. |
| `pyproject.toml` | Package metadata, dependency declaration, and test/coverage configuration. |
| `uv.lock` | Dependency lockfile for local reproducibility. |
| `manuscript/references.bib` | Verified manuscript-level bibliography. |
| `manuscript/S02_release_manifest.md` | Release provenance and gate-result surface. |
| `output/data/` | Generated machine-readable catalogue exports. |
| `output/figures/` | Generated visualizations referenced by the manuscript. |

## Expansion Checklist

- Confirm which files are authored source and which are generated.
- Confirm which commands reproduce the current outputs.
- Confirm whether a value belongs in prose, a generated supplement, or a data export.
- Confirm which external references need verified BibTeX entries.
- Confirm all manuscript citation keys resolve in `manuscript/references.bib`.
- Confirm reproducibility instructions use `${PROJECT_ROOT}` and
  `${TEMPLATE_ROOT}` rather than author-local absolute paths.
- Confirm whether any private material must be summarized rather than quoted or copied.
