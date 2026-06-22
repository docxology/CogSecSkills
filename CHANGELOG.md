# Changelog

All notable changes to CogSecSkills are documented here. The format is loosely
based on [Keep a Changelog](https://keepachangelog.com/), and the project aims to
follow semantic versioning.

## [1.0.0] - 2026-06-22

First archived public release.

### Added

- Archived on Zenodo with a permanent DOI. Concept DOI (all versions):
  [10.5281/zenodo.20804585](https://doi.org/10.5281/zenodo.20804585); version
  DOI (v1.0.0): [10.5281/zenodo.20804586](https://doi.org/10.5281/zenodo.20804586).
- Title-cover figure now renders the archived DOI alongside the repository URL,
  leads with the `CogSecSkills` identity wordmark, and includes a live
  seven-group taxonomy band generated from the registry.

### Changed

- Abstract rewritten as a single comprehensive plaintext paragraph (no
  citations or code spans) for clean archive and citation metadata.
- Sharpened section titles across the manuscript.

## [Unreleased]

### Added

- `CLAUDE.md` — Claude Code session guidance (defers to `AGENTS.md`; pins the
  generated-file boundary, gate sweep, and defensive contract).
- `docs/claude-code-skills.md` — installing the library as native Claude Code
  `/` skills by flattening `skills/` into `.claude/skills/cogsec-<slug>/`; linked
  from the docs map.
- `figures` optional-dependency extra (`matplotlib`, `numpy`, `seaborn`) so
  `manuscript-assets --write` figure rendering is reproducible. CI installs
  `.[dev,figures]` so the figure-asset tests run for real (no skips), and mypy
  gains a `follow_imports = skip` override for these third-party stubs so
  newer-Python stub syntax does not break the 3.10 type target.
- `manuscript/07_ethics_and_responsible_use.md` — standalone Ethics, Dual-Use,
  and Responsible-Use section (dual-use stance, defensive-by-contract-and-review,
  human-subjects scope, adopter responsibilities, and explicit non-claims).
- `manuscript/01_introduction.md` — a "Related Work and Positioning" subsection
  situating the library against the four cited literatures, grounded only in
  already-verified `references.bib` keys.
- Expanded `manuscript/98_symbols_glossary.md` from 4 to 11 terms (defensive
  boundary, misuse redirect, negative control, scenario fixture, worked example,
  reference density) and documented the `ageint_topic` crosswalk field.

### Fixed

- **CI/test suite now passes from a clean checkout.** Four artifact tests
  (`test_repository_examples_cover_all_rendered_skills`, three
  `test_release_metadata_*`) and the `examples`/`evals`/`dashboard`/
  `release-metadata`/`manuscript-assets` coherence gates assert against the
  gitignored `output/` tree, which a fresh clone lacks and nothing generated
  before pytest — so CI had been red since 2026-06-20 (4 failed / 618 passed on
  a clean runner). A session-scoped autouse fixture in `tests/conftest.py` now
  builds `output/` once when absent, making the suite self-contained; because
  pytest runs before the coherence-gate steps in the same CI job, the whole
  pipeline goes green (622 passed, all gates `current`). Idempotent — skipped
  when a populated `output/` already exists.
- Generated-file header attribution: `docs/evaluation-readiness.md` and
  `docs/skill-worked-examples.md` now correctly credit `evals --write` and
  `examples --write` (previously mislabeled `manuscript-assets --write`).
- `mypy` no longer aborts on the optional figure libraries' stubs when the
  `figures` extra is installed alongside `dev` (added a `tool.mypy` override).
- CI now enforces the full conformance contract: `.github/workflows/ci.yml`
  runs every generated-file drift gate (`definitions`, `scenarios`, `examples`,
  `evals`, `dashboard`, `release-metadata`, `manuscript-assets` `--check`), not
  just `validate`/`doctor`/`pytest`. Previously a hand-edit to a generated file
  could pass CI while failing the local gate sweep. Added a least-privilege
  `permissions: contents: read` block.

### Changed

- **Package and tests reorganized for modularity.** The flat 19-module runner is now
  grouped into cohesive subpackages along its (acyclic) dependency graph — `core/`
  (spec, registry, loader, config, harness), `authoring/` (author, scaffold, definitions),
  `quality/` (validate, insights), `artifacts/` (scenarios, examples, evals, dashboard,
  release_metadata, and the `manuscript_assets/` package) — with `cli.py` as the thin
  top-level interface. The 2,115-line `manuscript_assets.py` monolith was split into a
  package (`paths`, `rows`, `tables`, `figures`, `assets_io`) behind a façade `__init__`
  that re-exports the exact public API. Tests mirror the package layout
  (`tests/{core,authoring,quality,artifacts,contract,conformance}/`). Project-root
  discovery was centralized into `core.locate.project_root()` (a sentinel walk-up that
  fails loud), replacing 10 fragile `Path(__file__).parents[N]` magic-depths. Public CLI
  and import surfaces are unchanged; mypy/ruff clean, all validation/drift gates current.
- **Machine-stitched grammar repaired across all 100 skill definitions.** The
  `evidence_requirements`, `confidence_rubric`, `uncertainty_handling`,
  `privacy_legal_constraints`, and `failure_modes` quality fields had been generated by an
  earlier tool that spliced workflow step-titles and output/input names into sentences (e.g.
  "tie each sorted table, and outlier flags claim to concrete evidence from the specific
  evidence set, and sort dimensions item"), producing text that passed every gate but read as
  machine garble. Every definition now carries a grammatical, **skill-specific** rewrite of
  those fields, grounded in the technique's real outputs, failure modes, and evidence types
  (e.g. astroturfing cites creation-date spikes / content-hash overlap / follower-graph
  density; geolocation cites matched-terrain reference imagery and sun-angle computation),
  with per-skill uniqueness, keyword coverage, and scenario quality-term contracts preserved.
  The `author.default_quality_fields` fallback was also hardened to emit clean article-safe
  prose for any field a definition leaves unset.
- **Red-Team Review skill (`critical_review.red_team_review`) deepened and de-stitched.**
  Rewrote the canonical definition (source of truth → regenerated 6 skill files): removed the
  machine-stitched grammar that spliced workflow-step titles into the confidence rubric, failure
  modes, and evidence requirements; expanded the workflow from 5 to 6 operational steps (decomposed
  adversary model, attack-surface checklist with explicit coverage-gap flagging, assumption inversion
  + compounding attack chains, a 1–5 × 1–5 exploitability×impact scoring rubric with priority bands,
  mitigation re-testing against the adversary, and an explicit GO / NO-GO / GO-WITH-CONDITIONS call);
  grew anti-criteria from 5 to 10 (incl. a calibration guard that the scores and go/no-go are analyst
  estimates to be peer-checked, not objective measurement); distinguished Devil's Advocacy from
  structured Team A/Team B; added Shostack (2014) *Threat Modeling* and MITRE ATT&CK references.
  validate/doctor remain 0 errors / 0 findings.
- **Documentation deepened and manuscript supplements refreshed.** The 8 AGEINT educational
  primers (`docs/ageint/`) and the main explanatory docs (`architecture.md`, `authoring-skills.md`,
  `configuration.md`, `harness-cookbook.md`, `skill-contract.md`) were substantially deepened —
  each primer now maps its group to the real skills, and `adversarial-assurance.md` reflects the
  deepened red-team workflow (adversary modeling, attack-surface taxonomy, exploitability×impact
  scoring, go/no-go). All file-level documentation contracts and claim boundaries preserved.
  Generated manuscript supplements (`S10_skill_catalogue.md`, figures) and the quality dashboard
  were regenerated to reflect the cleaned skills, and the PDF/HTML manuscript was re-rendered.
- `QUICKSTART.md` documents the `figures` extra and includes
  `manuscript-assets --check` in the validation sweep.

## [0.1.0] — 2026-06-18

Initial release. A multiharness agentic skill library for Cognitive Security and
analytic tradecraft.

### Added

- **100 skill areas, all implemented** across 7 groups (Structured Analytic
  Techniques, Cognitive Security, Critical Review & Assurance, OSINT & Source
  Integrity, Counterintelligence & Deception, Information Environment, Research
  Methods), each a conforming multiharness skill folder (`SKILL.md` +
  `skill.yaml` + `workflow.md` + `harness/{claude,codex,hermes}.md`).
- **Runner package** `cogsecskills`: harness-neutral spec parser, registry,
  loader, multiharness conformance, validation gates, deterministic authoring
  renderer, scaffolder, and a thin CLI.
- **Deterministic authoring** (`author` / `author-batch`): renders conforming
  skills from a structured JSON definition; adapters bind every declared verb by
  construction.
- **Intelligent affordances**: `route` (free-text skill router), `stats`,
  `groups`, `catalogue` (generated index), `doctor` (validation + quality lint),
  `export`.
- **Configurable** via optional `cogsecskills.yaml`: target harness set (adding a
  harness needs no code change) and `doctor` quality thresholds.
- **AGEINT educational upstream** under `docs/ageint/` (index + 7 topic primers)
  and a full documentation set under `docs/`.
- Test suite with no mocks (real temp dirs + real YAML), ≥90% coverage gate (~98%
  actual), and a live conformance test that validates the real `skills/` tree.
- **Typed** package (`py.typed`, mypy-clean) and a `--version` flag.
- **GitHub Actions CI** — ruff (lint + format), mypy, pytest + coverage gate,
  `cogsecskills validate`, and `cogsecskills doctor` across Python 3.10–3.12.

### Notes

- The library is strictly defensive, educational, and accountable.
