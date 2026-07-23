---
project: CogSecSkills
task: Build and verify the CogSecSkills multiharness skill library — framework, 100-area taxonomy, 100 implemented skills, AGEINT upstream
effort: E4
phase: complete
progress: 100/100 skills fully implemented + multiharness-conforming; v1.1.0 release — 740 tests/94.35% coverage, all gates current, DRY centralization + CLI JSON output
mode: algorithm
started: 2026-06-18
updated: 2026-07-22
---

# CogSecSkills — Ideal State Artifact

## Problem

Analytic tradecraft for **Cognitive Security** — Structured Analytic Techniques,
source verification, deception detection, critical review — exists as human
doctrine (Heuer & Pherson, the AGEINT curriculum) but not as *dependable agentic
tool-use implementations*. Agents asked to "analyze competing hypotheses" or
"critically review this project" improvise, with no repeatable procedure, no
tool-use contract, and no guarantee the same skill runs the same way under
different agent harnesses (Claude Code, Codex, Hermes).

## Vision

A library where each analytic technique is one declarative, harness-neutral
skill: a canonical YAML definition that renders into `skill.yaml`, `SKILL.md`,
`workflow.md`, and one adapter per configured harness. The library is backed by
an educational upstream (AGEINT) that explains *why*, a registry that enumerates
the whole landscape, and a test suite that proves every skill is well-formed,
multiharness, and defensively bounded. Euphoric surprise: "the same
100-technique catalogue runs on Claude, Codex, or Hermes, and a test fails the
moment a definition, rendered skill, or adapter drifts."

## Out of Scope

- Offensive influence-operation tooling or manipulation how-tos. The library is
  strictly defensive, educational, and accountable (inherited from AGEINT).
- Live external API integrations for OSINT collection (skills declare the
  capability; wiring real connectors is downstream).
- Claiming the manuscript is an externally validated or publication-ready paper.
  The manuscript is a documentation surface for the skills system; local render
  readiness is not field validation.
- Live external API integrations / real tool connectors for the OSINT and web
  skills (they declare the `web`/`search` capability; wiring real connectors is
  downstream).

## Principles

- **Plan / build / teach stay coherent.** Registry (plan), `skills/` (build),
  `docs/ageint/` (teach) are cross-checked, never allowed to silently diverge.
- **Harness-neutral by construction.** A skill names capabilities as closed-set
  tool verbs; harnesses bind verbs to concrete tools. Portability is a property
  the test suite proves, not a hope.
- **Validation asymmetry respected.** A missing *implemented* skill is a hard
  error; a *planned* area with no on-disk skill is the normal un-built state, not
  an error.
- **Thin orchestrator.** All logic lives in `src/cogsecskills/`; skills are data;
  the CLI only orchestrates.

## Constraints

- Python ≥3.10, `uv`, pytest, no mocks (real temp dirs + real YAML).
- Coverage gate ≥90% on `src/`; current measurements belong in
  [Verification](#verification), not copied into long-lived prose.
- Lives at the private sidecar `projects/working/CogSecSkills`, symlinked into the
  template repo's `projects/working/` — never committed to the public template repo.
- Closed tool-verb vocabulary: read, search, write, exec, reason, web, delegate, ask.

## Goal

Ship a CogSecSkills project that (1) enumerates 100 Cognitive-Security/SAT skill
areas in a validated registry, (2) implements all 100 as full multiharness
skills, (3) vendors AGEINT as the educational upstream under `docs/ageint/`, (4)
exposes tested CLI affordances for routing, catalogue generation, reporting, and
quality linting, (5) proves — via a passing test suite — that every on-disk
skill loads, validates, and conforms to every configured harness, with Claude
Code, Codex, and Hermes as the default harness set, and (6) generates
synchronized manuscript supplements and figures from the live library metadata.

## Criteria

- [x] ISC-1: `registry/skills.yaml` enumerates exactly 100 skill areas across 7 groups.
- [x] ISC-2: `registry/groups.yaml` defines the 7 workflow-subfolder groups; every entry's group is defined.
- [x] ISC-3: 100 implemented skills exist on disk under `skills/<group>/<slug>/`.
- [x] ISC-4: Each implemented skill has `skill.yaml`, `SKILL.md`, `workflow.md`, and `harness/{claude,codex,hermes}.md`.
- [x] ISC-5: `python -m cogsecskills validate` reports 0 errors over the real library.
- [x] ISC-6: Each on-disk skill conforms to all 3 harnesses (adapter declared + every declared verb explicitly bound).
- [x] ISC-7: Runner package coverage ≥90%.
- [x] ISC-8: A `scaffold` command generates a conforming skill folder from any registry entry.
- [x] ISC-9: `docs/ageint/` holds an index + 7 topic primers matching the `ageint_topic` slugs.
- [x] ISC-10: The user-named "project critical review" skill is implemented and multiharness-conforming.
- [x] ISC-11: Anti: no skill folder is marked `implemented` in the registry without an on-disk build (gate enforces).
- [x] ISC-12: Anti: no offensive/manipulation how-to content — skills are defensive and accountable.
- [x] ISC-13: Cross-vendor (Forge) audit complete; all 7 findings fixed (strict spec typing, guarded groups parse, non-vacuous adapter-verb-binding, undefined-group + slug + id-prefix gates, O(n) discovery, replace-on-overwrite) with regression tests.
- [x] ISC-14: All 100 catalogued areas materialized on disk as conforming multiharness skill folders, `validate` reports 0 errors over all 100.
- [x] ISC-15: All 100 areas FULLY IMPLEMENTED (registry status_counts → implemented:100, stub:0, planned:0); all 100 skills have canonical YAML definitions rendered deterministically into the harness-facing skill tree.
- [x] ISC-16: Deterministic authoring paths (`definitions --write|--check`, `author.py`, `author`, and compatibility `author-batch`) render conforming skills from structured definitions; covered by regression tests incl. malformed-input and drift handling.
- [x] ISC-17: `manuscript-assets --write|--check` generates synchronized supplemental catalogue, metadata matrix, data exports, and figures from the live registry and skill specs.

## Test Strategy

| isc | type | check | threshold | tool |
|-----|------|-------|-----------|------|
| ISC-1 | unit | registry length == 100 | exact | pytest |
| ISC-5 | integration | `validate_library(ROOT).ok` | 0 errors | pytest + CLI |
| ISC-6 | parametrized | `check_conformance` per skill | all harnesses ok | pytest |
| ISC-7 | coverage | `--cov=src/cogsecskills` | ≥90% | pytest-cov |
| ISC-8 | unit | scaffolded skill validates | ok | pytest |
| ISC-17 | integration | generated manuscript assets match live library | no drift | CLI + pytest |

## Features

| name | satisfies | depends_on | parallelizable |
|------|-----------|------------|----------------|
| runner package (spec/loader/registry/harness/validate/cli/scaffold) | ISC-5..8 | — | no |
| registry of 100 areas + 7 groups | ISC-1,2 | — | no |
| 100 implemented skills | ISC-3,4,10,14,15 | runner | yes (per skill) |
| AGEINT upstream (index + 7 primers) | ISC-9,12 | — | yes (per primer) |
| conformance + coverage test suite | ISC-5,6,7 | runner, skills | no |
| manuscript asset generator | ISC-17 | registry, skills, runner | no |

## Decisions

- 2026-06-18: Initially kept the inherited template numerical payload to avoid
  breaking the parent pipeline's project contract; this was superseded by the
  later standalone cleanup below.
- 2026-06-18: Built the reference seed skills via parallel agents against a strict file contract;
  one agent mis-nested its output under `src/` — relocated to `skills/` and verified.
- 2026-06-18: `effort_source: classifier returned E3 (on a timeout fail-safe); executor
  treated as E4` given new-project + 100-area architecture scope.
- 2026-06-18: Promoted from an exemplar library to a complete catalogue: all 100
  areas are implemented on disk, validation/report are green, and CLI insight
  affordances (`route`, `stats`, `catalogue`, `doctor`) are tested.
- 2026-06-18: Stripped the inherited optimization payload for a clean standalone
  **published** repo (`github.com/docxology/CogSecSkills`, private, Apache-2.0).
  Reversed the earlier keep-the-scaffold decision once the project gained its own
  identity and home; the suite is now self-contained (no monorepo dependency).
- 2026-06-18: Hardening pass — made harnesses + quality thresholds configurable
  (`cogsecskills.yaml`); added the `author` deterministic renderer and intelligent
  CLI affordances; added typing (`py.typed`, mypy clean), GitHub Actions CI
  (ruff + mypy + pytest + validate + doctor on 3.10–3.12), and lifted coverage
  above the 90% gate. Docs audited accurate by an independent agent.
- 2026-06-18: Expanded the manuscript into a reader-ready skills-system report
  with narrow margins, generated S10/S11 supplements, data exports, and eight
  deterministic figures from `src/cogsecskills/manuscript_assets.py`.
- 2026-06-18: Review-hardening pass added verified manuscript citations,
  portable reproducibility commands, a release/provenance manifest, formal
  contract notation, Reference Density definition, and defensive-governance
  review rules without widening the empirical claim boundary.
- 2026-06-19: Deep skill-corpus hardening pass made the canonical definitions
  group-aware for defensive boundaries, misuse redirects, evidence/inference
  labeling, uncertainty handling, failure modes, and negative controls; doctor
  and conformance tests now reject generic negative-control boilerplate and weak
  skill-specific quality language.
- 2026-06-19: RedTeam verifier hardening closed a false-certification gap by
  rejecting repeated individual negative-control examples across the corpus, not
  only reused full negative-control sets.
- 2026-06-19: Corpus refinement pass extended that uniqueness pressure to
  confidence rubrics, evidence requirements, and privacy/legal constraints, and
  the generated S10 catalogue now exposes a quality capsule for every skill.
- 2026-06-20: Evidence-ladder pass expanded scenario readiness to 28 curated
  safe-use and unsafe-redirect fixtures, added one deterministic worked example
  per skill plus `examples --write|--check`, and extended the dashboard with
  scenario coverage, worked-example coverage, and local claim-boundary status.
- 2026-06-19: TODO-completion hardening added reviewed expected-answer bodies
  for every scenario, expanded safe/unsafe harness smoke fixtures for Codex,
  Claude, Hermes, and a custom harness, and introduced `dashboard --write|--check`
  as a generated 100-skill quality and scenario-coverage drift surface.
- 2026-06-22: Full verification audit (E4) re-ran every authoritative gate on a
  clean tree post the 06-21 modularity refactor: 622 tests / 90.89% coverage,
  `validate`/`doctor` 0/0, all nine generator `--check` gates current, manuscript
  re-rendered fresh to a 72pp PDF with 8/8 figures and clean markdown validation.
  Cross-vendor Forge audit found no HIGH defects and three CLEAN categories
  (manuscript currency, workflow completeness, edge-path safety). Acted on the one
  actionable finding: the `fig:harness-contract` caption claimed the figure "proves
  structural adapter presence," but the cells count skills that *declare* a harness
  adapter (`rows.py:134` reads `spec.harness`); the file-existence + per-verb-binding
  invariant is enforced separately by `validate`/conformance. Narrowed the caption
  to match the computation. Forge's second MED note ("completely functional" =
  structural/local conformance, not live-runtime execution) is already disclosed in
  `04_artifacts_and_evidence.md` and left as honest scope, not a defect.
- 2026-06-22: Manuscript polish pass. (1) Rebuilt the cover figure
  (`_write_cover_installation`) to lead with the "CogSecSkills" wordmark + a
  one-line identity descriptor, added a live seven-group taxonomy band
  (short code + title + count, sourced from `_group_summaries`), and reflowed
  the install panel so the full clone URL fits; wired the previously-dead
  `COVER_PANEL_TITLE_SIZE`/`COVER_LABEL_SIZE` constants into the render as a
  real source of truth and retuned the readability-floor contract test to the
  new still-PDF-legible sizes (command font dropped 20.2→15.2 to fit the URL).
  (2) Rewrote the abstract as one comprehensive plaintext paragraph with no
  citations and no code spans (all nine cite keys remain used elsewhere, so the
  bibliography is unaffected). (3) Reviewed all section titles; sharpened four
  H1s (01/02/03/05) and elongated four thin H2s, preserving every `{#sec:}`
  label. Updated the H1-inventory and abstract contract tests to the new ground
  truth. Re-verified: 622 tests / 90.93%, validate+doctor 0/0, asset+definition
  gates current, fresh 72pp PDF with 8/8 figures, abstract renders as a single
  citation-free paragraph, markdown validation clean.

## Changelog

- conjecture: a harness-neutral `skill.yaml` + per-harness adapter files is enough
  to make a skill portable. learned: yes, provided a *closed* tool-verb vocabulary
  and a conformance check that asserts each harness realizes every verb a skill uses
  and that each adapter file explicitly binds those verbs.

## Verification

- 2026-06-22 v1.0.0 PUBLISHED (production): Zenodo concept DOI
  `10.5281/zenodo.20804585`, version DOI `10.5281/zenodo.20804586`
  (https://doi.org/10.5281/zenodo.20804586 resolves, record state `done`,
  combined PDF attached). Reserve-first flow stamped the concept DOI on the
  title cover and into config/CITATION.cff/codemeta.json/.zenodo.json. GitHub:
  `origin/main` at `651351a`, release `v1.0.0`
  (https://github.com/docxology/CogSecSkills/releases/tag/v1.0.0) with the
  manuscript PDF asset. Pre-publish gate: 622 tests / 91.18%, ruff clean,
  validate+doctor+all generator `--check` gates current.


- ISC-1: `len(load_registry('.')) == 100` — CLI report `"registry_total": 100`.
- ISC-5: `python -m cogsecskills validate` → `0 error(s), 0 warning(s)`.
- ISC-6/7/17: `PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py --cov=src/cogsecskills --cov-report=term-missing` -> `622 passed`, `Total coverage: 90.94%`.
- ISC-13: Forge audit returned 7 findings (2 HIGH, 3 MEDIUM, 2 LOW); all fixed and covered by regression tests; verb-axis vacuity closed by the adapter-verb-binding check + a narrowed-support non-vacuity test.
- ISC-15: `report` → `status_counts {implemented: 100, stub: 0, planned: 0}`; `validate` → `0 error(s)`; all 100 canonical definitions render into matching skill files.
- ISC-16: `cogsecskills definitions --check` → `canonical definitions are current`; `cogsecskills author`/`author-batch` + `test_cogsecskills_author.py` cover render conformance, adapter binding, malformed-input reporting, and drift detection.
- ISC-17: `python -m cogsecskills manuscript-assets --check` → `manuscript assets are current`.
- Scenario readiness: `python -m cogsecskills scenarios --check` -> `scenario readiness fixtures are current: 28 scenarios across 7 groups; 28 expected answers checked`.
- Worked examples: `python -m cogsecskills examples --check` -> `worked examples are current`.
- Quality dashboard: `python -m cogsecskills dashboard --check` -> `quality dashboard is current`; the generator owns Markdown, static HTML, and JSON views.
- Skill quality audit: `cogsecskills doctor` -> `validation: 0 error(s); quality: 0 finding(s)`; pytest verifies skill-specific negative controls, safe defensive examples, evidence/inference labels, unknown/alternative handling, workflow specificity, no reused negative-control sets, no reused individual negative-control entries, and no reused confidence/evidence/privacy quality entries.
- Manuscript render: template markdown validation -> `No issues found!`; PDF/HTML render -> 13 manuscript sections, 8/8 figures found.
- 2026-06-22 re-verification (post-refactor, clean tree): `pytest tests/ --cov=src/cogsecskills` -> `622 passed in 175.57s`, `Total coverage: 90.89%` (≥90 gate met); `validate` -> `0 error(s), 0 warning(s)`; `doctor` -> `validation: 0 error(s); quality: 0 finding(s)`; `definitions/manuscript-assets/scenarios/examples/dashboard/evals/release-metadata --check` all report "current"; fresh `03_render_pdf` -> 72pp PDF, `Found: 8/8 figures`, `Valid PDFs: 1/1`, markdown `No issues found!`; figure data tallies match live registry exactly (sat 34, cog 24, rev 12, osint 10, ci 8, info 7, method 5 = 100); 100 `workflow.md` present and conforming. Corrected `fig:harness-contract` caption verified present in rendered PDF (`pdftotext | grep "enforced separately by"` -> 1) with no broken `Figure ??` crossrefs.
- 2026-07-22 comprehensive review pass: centralized duplicated quality constants from `insights.py` + `definitions.py` into `core/quality_constants.py` (DRY); added `--format json` + `--limit N` to the CLI `list`/`groups`/`route` commands; added 80 new tests covering figures.py helpers, evals/examples/scenarios/release_metadata error paths, and CLI JSON output; cleaned `TODO.md` to forward-only; updated `CHANGELOG.md`, `README.md`, and `docs/cli.md`. `pytest` -> `722 passed`, coverage `93.9%`, validate+doctor 0/0, all generator `--check` gates current.
