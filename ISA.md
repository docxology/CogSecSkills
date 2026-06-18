---
project: CogSecSkills
task: Build and verify the CogSecSkills multiharness skill library — framework, 100-area taxonomy, 100 implemented skills, AGEINT upstream
effort: E4
phase: verify
progress: 100/100 skills fully implemented + multiharness-conforming; runner coverage gate passing
mode: algorithm
started: 2026-06-18
updated: 2026-06-18
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
skill: a single `skill.yaml` that an agent on *any* supported harness can load
and execute identically, backed by an educational upstream (AGEINT) that explains
*why*, a registry that enumerates the whole landscape, and a test suite that
proves every skill is well-formed and multiharness. Euphoric surprise: "the same
100-technique catalogue runs on Claude, Codex, or Hermes, and a test fails the
moment a skill drifts."

## Out of Scope

- Offensive influence-operation tooling or manipulation how-tos. The library is
  strictly defensive, educational, and accountable (inherited from AGEINT).
- Live external API integrations for OSINT collection (skills declare the
  capability; wiring real connectors is downstream).
- Turning the manuscript scaffold into a publication-ready paper in this pass.
  The manuscript is a documentation surface for the skills system until its
  claims, citations, figures, and render are separately verified.
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
quality linting, and (5) proves — via a passing test suite — that every on-disk
skill loads, validates, and conforms to Claude Code, Codex, and Hermes.

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
- [x] ISC-15: All 100 areas FULLY IMPLEMENTED (registry status_counts → implemented:100, stub:0, planned:0); the 92 non-exemplar skills authored in parallel as structured definitions and rendered deterministically via `cogsecskills author` (adapters bind every declared verb by construction).
- [x] ISC-16: A deterministic authoring path (`author.py` + `author`/`author-batch` CLI) renders conforming skills from structured definitions; covered by regression tests incl. malformed-input handling.

## Test Strategy

| isc | type | check | threshold | tool |
|-----|------|-------|-----------|------|
| ISC-1 | unit | registry length == 100 | exact | pytest |
| ISC-5 | integration | `validate_library(ROOT).ok` | 0 errors | pytest + CLI |
| ISC-6 | parametrized | `check_conformance` per skill | all harnesses ok | pytest |
| ISC-7 | coverage | `--cov=src/cogsecskills` | ≥90% | pytest-cov |
| ISC-8 | unit | scaffolded skill validates | ok | pytest |

## Features

| name | satisfies | depends_on | parallelizable |
|------|-----------|------------|----------------|
| runner package (spec/loader/registry/harness/validate/cli/scaffold) | ISC-5..8 | — | no |
| registry of 100 areas + 7 groups | ISC-1,2 | — | no |
| 100 implemented skills | ISC-3,4,10,14,15 | runner | yes (per skill) |
| AGEINT upstream (index + 7 primers) | ISC-9,12 | — | yes (per primer) |
| conformance + coverage test suite | ISC-5,6,7 | runner, skills | no |

## Decisions

- 2026-06-18: Kept the inherited template numerical scaffold rather than ripping
  it out — removing it risks the parent pipeline's project contract; documented as
  out-of-scope vestigial. Revisit in a later session if the project is trimmed.
- 2026-06-18: Built the reference seed skills via parallel agents against a strict file contract;
  one agent mis-nested its output under `src/` — relocated to `skills/` and verified.
- 2026-06-18: `effort_source: classifier returned E3 (on a timeout fail-safe); executor
  treated as E4` given new-project + 100-area architecture scope.
- 2026-06-18: Promoted from an exemplar library to a complete catalogue: all 100
  areas are implemented on disk, validation/report are green, and CLI insight
  affordances (`route`, `stats`, `catalogue`, `doctor`) are tested.

## Changelog

- conjecture: a harness-neutral `skill.yaml` + per-harness adapter files is enough
  to make a skill portable. learned: yes, provided a *closed* tool-verb vocabulary
  and a conformance check that asserts each harness realizes every verb a skill uses
  and that each adapter file explicitly binds those verbs.

## Verification

- ISC-1: `len(load_registry('.')) == 100` — CLI report `"registry_total": 100`.
- ISC-5: `python -m cogsecskills validate` → `0 error(s), 0 warning(s)`.
- ISC-6/7: `PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py --cov=src/cogsecskills --cov-report=term-missing` → `325 passed`, `Total coverage: 97.07%`.
- ISC-13: Forge audit returned 7 findings (2 HIGH, 3 MEDIUM, 2 LOW); all fixed and covered by regression tests; verb-axis vacuity closed by the adapter-verb-binding check + a narrowed-support non-vacuity test.
- ISC-15: `report` → `status_counts {implemented: 100, stub: 0, planned: 0}`; `validate` → `0 error(s)`; 92 skills authored via a 25-agent `/workflows` fan-out (1.05M tokens, 0 skipped) → `author-batch` rendered 92, 0 failed.
- ISC-16: `cogsecskills author`/`author-batch` + `test_cogsecskills_author.py` (render conforms, adapters bind verbs, malformed-input reported, promote flips registry).
