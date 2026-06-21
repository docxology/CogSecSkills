# CogSecSkills

[![CI](https://github.com/docxology/CogSecSkills/actions/workflows/ci.yml/badge.svg)](https://github.com/docxology/CogSecSkills/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)

**Agentic tool-use skills for Cognitive Security and analytic tradecraft.**

CogSecSkills is a library of **100 analytic skills** — Structured Analytic
Techniques (SATs), cognitive-security defenses, OSINT integrity, counter-
intelligence, and critical review — each authored once as a **harness-neutral
skill** with default adapters for Claude Code, Codex, and Hermes, and the same
structural contract for any additional configured harness.

New here? Start with [`QUICKSTART.md`](QUICKSTART.md), then use the
[documentation map](docs/README.md). To install the public repository into an
agent harness, see [`docs/harness-installation.md`](docs/harness-installation.md)
and [`docs/harness-cookbook.md`](docs/harness-cookbook.md).

The library is strictly **defensive, educational, and accountable**. Its
educational upstream is the [AGEINT](docs/ageint/README.md) curriculum. These
skills recognize, assess, and defend against cognitive attack — they do not
author manipulation.

## The three coherent artifacts

| Artifact | Role | Where |
|----------|------|-------|
| **Teach** | the concepts (the *why*) | [`docs/ageint/`](docs/ageint/README.md) |
| **Plan** | catalogue of all 100 skill areas (the *what*) | [`registry/skills.yaml`](registry/skills.yaml) |
| **Build** | canonical definitions and rendered multiharness skill implementations (the *how*) | [`definitions/`](definitions/) and [`skills/`](skills/) |

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
that bind every declared verb under the configured harness set. The default
configured set is Claude Code, Codex, and Hermes.
`python -m cogsecskills report` shows the live counts (implemented: 100).

All 100 skills now have persistent canonical definitions under `definitions/`.
`python -m cogsecskills definitions --write` renders the full `skills/` tree
deterministically from that source layer, and `definitions --check` proves the
definitions and rendered files have not drifted.
`python -m cogsecskills scenarios --check` adds a deterministic defensive
readiness gate over curated safe-use and unsafe-redirect fixtures; it checks
routing, local skill contracts, expected response-shape metadata, and reviewed
expected-answer fixtures without calling external model runtimes.
`python -m cogsecskills examples --write` generates one worked defensive
example per skill from `examples/skill-worked-examples.yaml`.
`python -m cogsecskills evals --write` generates offline local output-review
fixtures and reports from scenario expected answers; it does not call live
models.
`python -m cogsecskills dashboard --write` generates a 100-skill quality
dashboard for navigation and drift review across scenarios, offline evals,
worked examples, quality capsules, harnesses, references, and source paths,
with Markdown, static HTML, and JSON views.
`python -m cogsecskills release-metadata --write` generates the local release
claim matrix and metadata snapshot without publishing, tagging, or archiving.
Exact git revision, branch, and dirty-state values are observed at command
runtime rather than embedded in committed generated files.

## Anatomy of a skill

```
skills/<group>/<slug>/
  skill.yaml          # generated harness-neutral spec
  SKILL.md            # Claude Code native entry point (frontmatter + doc)
  workflow.md         # the agentic procedure, each step tagged with a tool verb
  harness/
    claude.md         # default adapter: Claude Code tools
    codex.md          # default adapter: Codex tools
    hermes.md         # default adapter: Hermes function calls
    <name>.md         # optional configured harness adapter
```

A skill declares its capabilities as **closed-set tool verbs** (`read`, `search`,
`write`, `exec`, `reason`, `web`, `delegate`, `ask`). Each harness adapter binds
those verbs to concrete tools in a Markdown binding table. The validator checks
that every declared verb is present in every adapter, so "multiharness" is a
property the test suite *proves*, not a hope.

The persistent source of truth for authored skill substance is
`definitions/<group>/<slug>.yaml`; `skill.yaml` and the companion Markdown files
are the generated, harness-facing build outputs.

## Usage

```bash
# Install from GitHub and validate the library
git clone https://github.com/docxology/CogSecSkills.git
cd CogSecSkills
uv sync
PYTHONPATH="src:." python -m cogsecskills validate

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
python -m cogsecskills scenarios --check
python -m cogsecskills examples --write
python -m cogsecskills examples --check
python -m cogsecskills evals --write
python -m cogsecskills evals --check
python -m cogsecskills dashboard --write
python -m cogsecskills dashboard --check
python -m cogsecskills release-metadata --write
python -m cogsecskills release-metadata --check

# Regenerate manuscript supplements and figures from the live library
python -m cogsecskills manuscript-assets --write
python -m cogsecskills manuscript-assets --check

# Regenerate all rendered skills from canonical YAML definitions
python -m cogsecskills definitions --write
python -m cogsecskills definitions --check

# Author a full skill deterministically from a structured JSON/YAML definition
python -m cogsecskills author path/to/definition.yaml     # render one
python -m cogsecskills author-batch                      # compatibility path for skills/**/_def.json

# Scaffold a brand-new planned area from the registry (skeleton to deepen)
python -m cogsecskills scaffold sat.some_new_area
```

(From the project root, with `PYTHONPATH="src:."` or after `uv sync`.)

To connect a harness, point it at `skills/<group>/<slug>/SKILL.md`, use
`workflow.md` for the neutral procedure, and bind tools through the matching
`harness/<name>.md` adapter. The default configured set is `claude`, `codex`,
and `hermes`; add more harnesses in `cogsecskills.yaml` and regenerate adapters
with `python -m cogsecskills definitions --write`.

For bounded examples, see
[`examples/harness-smoke-transcripts.md`](examples/harness-smoke-transcripts.md)
[`examples/group-worked-examples.md`](examples/group-worked-examples.md), and
[`docs/skill-worked-examples.md`](docs/skill-worked-examples.md).
For claim discipline, see [`docs/claim-boundaries.md`](docs/claim-boundaries.md).
For the generated quality dashboard, see
[`docs/quality-dashboard.md`](docs/quality-dashboard.md) and
[`docs/quality-dashboard.html`](docs/quality-dashboard.html). Visual style rules
for generated figures, the cover image, dashboard pages, and manuscript tables
live in [`DESIGN.md`](DESIGN.md).

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

- Canonical public repository: <https://github.com/docxology/CogSecSkills>.
  Local manuscript/render validation may use the sibling docxology template, but
  the **deliverable is the skills system**: registry, skills, AGEINT docs,
  runner, tests, generated manuscript supplements, and figures that describe
  those source surfaces.
- Educational upstream: [AGEINT](https://github.com/docxology/AGEINT)
  (concept DOI [10.5281/zenodo.20732274](https://doi.org/10.5281/zenodo.20732274)).
- The skill catalogue draws on Heuer & Pherson, *Structured Analytic Techniques
  for Intelligence Analysis*, and the cognitive-security literature cited per-primer.

See [`ISA.md`](ISA.md) for the project's ideal-state articulation and acceptance
criteria.
