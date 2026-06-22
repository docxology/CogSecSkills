# Changelog

All notable changes to CogSecSkills are documented here. The format is loosely
based on [Keep a Changelog](https://keepachangelog.com/), and the project aims to
follow semantic versioning.

## [Unreleased]

### Added

- `CLAUDE.md` — Claude Code session guidance (defers to `AGENTS.md`; pins the
  generated-file boundary, gate sweep, and defensive contract).
- `docs/claude-code-skills.md` — installing the library as native Claude Code
  `/` skills by flattening `skills/` into `.claude/skills/cogsec-<slug>/`; linked
  from the docs map.
- `figures` optional-dependency extra (`matplotlib`, `numpy`, `seaborn`) so
  `manuscript-assets --write` figure rendering is reproducible.

### Fixed

- Generated-file header attribution: `docs/evaluation-readiness.md` and
  `docs/skill-worked-examples.md` now correctly credit `evals --write` and
  `examples --write` (previously mislabeled `manuscript-assets --write`).
- `mypy` no longer aborts on the optional figure libraries' stubs when the
  `figures` extra is installed alongside `dev` (added a `tool.mypy` override).

### Changed

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
