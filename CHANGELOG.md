# Changelog

All notable changes to CogSecSkills are documented here. The format is loosely
based on [Keep a Changelog](https://keepachangelog.com/), and the project aims to
follow semantic versioning.

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
- Test suite with no mocks (real temp dirs + real YAML), ≥90% coverage gate, and
  a live conformance test that validates the real `skills/` tree.

### Notes

- The library is strictly defensive, educational, and accountable.
