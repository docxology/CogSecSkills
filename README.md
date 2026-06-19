# CogSecSkills

[![CI](https://github.com/docxology/CogSecSkills/actions/workflows/ci.yml/badge.svg)](https://github.com/docxology/CogSecSkills/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)

**Agentic tool-use skills for Cognitive Security and analytic tradecraft.**

CogSecSkills is a library of **100 analytic skills** — Structured Analytic
Techniques (SATs), cognitive-security defenses, OSINT integrity, counter-
intelligence, and critical review — each authored once as a **harness-neutral
skill** that runs identically under Claude Code, Codex, or Hermes.

New here? The [documentation map](docs/README.md) points you to the right place.

The library is strictly **defensive, educational, and accountable**. Its
educational upstream is the [AGEINT](docs/ageint/README.md) curriculum. These
skills recognize, assess, and defend against cognitive attack — they do not
author manipulation.

## The three coherent artifacts

| Artifact | Role | Where |
|----------|------|-------|
| **Teach** | the concepts (the *why*) | [`docs/ageint/`](docs/ageint/README.md) |
| **Plan** | catalogue of all 100 skill areas (the *what*) | [`registry/skills.yaml`](registry/skills.yaml) |
| **Build** | multiharness skill implementations (the *how*) | [`skills/`](skills/) |

`python -m cogsecskills validate` keeps Plan and Build coherent: every on-disk
skill must be catalogued, and every `implemented` catalogue entry must exist.

## Skill groups (workflow subfolders)

| Group | Focus | Count |
|-------|-------|-------|
| `sat` | Structured Analytic Techniques (Heuer & Pherson) | 34 |
| `cognitive_security` | Defending perception, reasoning, decision-making | 24 |
| `critical_review` | Adversarial + constructive review (incl. **project critical review**) | 12 |
| `osint_integrity` | Open-source collection with provenance discipline | 10 |
| `counterintelligence` | Denial/deception detection, process hardening | 8 |
| `information_environment` | Narratives, influence ops, coordinated behavior | 7 |
| `research_methods` | Synthesis, evidence grading, calibrated estimation | 5 |

**All 100 areas are fully implemented** as conforming, multiharness skill folders —
each with a real, technique-accurate procedure, a fitting tool plan, and adapters
that bind every declared verb under Claude Code, Codex, and Hermes.
`python -m cogsecskills report` shows the live counts (implemented: 100).

The 8 hand-authored skills below are the reference exemplars; the other 92 were
authored in parallel (one agent per technique) as structured definitions and
rendered deterministically via `cogsecskills author`, so every skill conforms by
construction.

## Anatomy of a skill

```
skills/<group>/<slug>/
  skill.yaml          # harness-neutral spec — the single source of truth
  SKILL.md            # Claude Code native entry point (frontmatter + doc)
  workflow.md         # the agentic procedure, each step tagged with a tool verb
  harness/
    claude.md         # verb -> Claude Code tools (Read/Grep/Bash/WebSearch/Write)
    codex.md          # verb -> Codex tools (shell/apply_patch/web)
    hermes.md         # verb -> Hermes function calls (fs.read/web.search/fs.write)
```

A skill declares its capabilities as **closed-set tool verbs** (`read`, `search`,
`write`, `exec`, `reason`, `web`, `delegate`, `ask`). Each harness adapter binds
those verbs to concrete tools in a Markdown binding table. The validator checks
that every declared verb is present in every adapter, so "multiharness" is a
property the test suite *proves*, not a hope.

## Usage

```bash
# List the catalogue (all 100 areas)
python -m cogsecskills list
python -m cogsecskills list --group sat --status implemented

# Inspect one skill
python -m cogsecskills show sat.analysis_of_competing_hypotheses

# Find the best skill for a free-text analytic need
python -m cogsecskills route "verify a viral claim before sharing it"

# Validate the whole library (plan <-> build coherence + multiharness conformance)
python -m cogsecskills validate

# JSON status report
python -m cogsecskills report

# Statistics, grouped catalogue, and quality lint
python -m cogsecskills stats
python -m cogsecskills catalogue --markdown --output docs/catalogue.md
python -m cogsecskills doctor

# Author a full skill deterministically from a structured JSON definition
python -m cogsecskills author path/to/_def.json          # render one
python -m cogsecskills author-batch                      # render every skills/**/_def.json + promote

# Scaffold a brand-new planned area from the registry (skeleton to deepen)
python -m cogsecskills scaffold sat.some_new_area
```

(From the project root, with `PYTHONPATH="src:."` or after `uv sync`.)

## The 8 reference exemplars

(All 100 skills are implemented; these 8 are the hand-authored references.)


| Skill | Group |
|-------|-------|
| `sat.analysis_of_competing_hypotheses` | Structured Analytic Techniques |
| `sat.key_assumptions_check` | Structured Analytic Techniques |
| `sat.devils_advocacy` | Structured Analytic Techniques |
| `cognitive_security.narrative_threat_assessment` | Cognitive Security |
| `cognitive_security.source_credibility_evaluation` | Cognitive Security |
| `critical_review.project_critical_review` | Critical Review & Assurance |
| `osint_integrity.claim_provenance_verification` | OSINT & Source Integrity |
| `research_methods.structured_literature_synthesis` | Research & Synthesis Methods |

## Testing

```bash
PYTHONPATH="src:." python -m pytest \
  tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py \
  --cov=src/cogsecskills --cov-report=term-missing
```

The live conformance test (`tests/test_skill_library_conformance.py`) runs against
the real `skills/` tree: adding a malformed skill, or an `implemented` registry
entry with no build, fails the suite.

## Provenance

- This project lives in the private `projects/working/CogSecSkills` sidecar and
  uses the sibling public docxology template only for optional manuscript/render
  validation. The **deliverable is the skills system**: registry, skills,
  AGEINT docs, runner, tests, and the manuscript scaffold that describes those
  source surfaces.
- Educational upstream: [AGEINT](https://github.com/docxology/AGEINT)
  (concept DOI [10.5281/zenodo.20732274](https://doi.org/10.5281/zenodo.20732274)).
- The skill catalogue draws on Heuer & Pherson, *Structured Analytic Techniques
  for Intelligence Analysis*, and the cognitive-security literature cited per-primer.

See [`ISA.md`](ISA.md) for the project's ideal-state articulation and acceptance
criteria.
