# AGENTS.md — CogSecSkills

Guidance for AI agents working in this project. See [`README.md`](README.md) for
the overview and [`ISA.md`](ISA.md) for the ideal-state articulation.

## What this project is

CogSecSkills is a **library of multiharness agentic skills** for Cognitive
Security and analytic tradecraft. The deliverable is the skills system:
registry, canonical definitions, on-disk skills, AGEINT docs, runner package,
scenario fixtures, tests, generated catalogue, generated manuscript supplements,
and figures that document those source surfaces.

## The source surfaces you must keep coherent

1. **`registry/skills.yaml`** — the catalogue of all 100 skill areas (the plan).
2. **`definitions/<group>/<slug>.yaml`** — the canonical skill substance.
3. **`skills/<group>/<slug>/`** — the rendered on-disk skill implementations.
4. **`docs/ageint/`** — the AGEINT educational upstream (the teach).
5. **`scenarios/defensive_readiness.yaml`** — curated defensive safe-use and
   unsafe-redirect probes (the scenario check).
6. **`examples/skill-worked-examples.yaml`** — one deterministic worked example
   source row per implemented skill.
7. **`evals/local_output_review.yaml`** — offline reviewed output fixtures
   linked to deterministic scenarios.
8. **`docs/quality-dashboard.md`**, **`docs/quality-dashboard.html`**,
   **`docs/evaluation-readiness.md`**,
   **`docs/release-claim-matrix.md`**, and **`manuscript/S10*`/`S11*`** —
   generated documentation mirrors, not hand-authored sources.

The manuscript under `manuscript/` is a documentation surface for the skills
system. Keep it evidence-bound: it may describe the registry, skills, runner,
tests, generated supplements, figures, and validation results, but it must not
invent publication claims, citations, or benchmarks.

After any change to skills, registry, scenarios, generated documentation, or
manuscript assets, run the relevant gate:

```bash
PYTHONPATH="src:." python -m cogsecskills validate   # must report 0 errors
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills scenarios --check
PYTHONPATH="src:." python -m cogsecskills examples --write
PYTHONPATH="src:." python -m cogsecskills examples --check
PYTHONPATH="src:." python -m cogsecskills evals --write
PYTHONPATH="src:." python -m cogsecskills evals --check
PYTHONPATH="src:." python -m cogsecskills dashboard --write
PYTHONPATH="src:." python -m cogsecskills dashboard --check
PYTHONPATH="src:." python -m cogsecskills release-metadata --write
PYTHONPATH="src:." python -m cogsecskills release-metadata --check
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --write
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check
```

Use [`DESIGN.md`](DESIGN.md) as the visual contract for generated figures, the
cover image, the HTML dashboard, and manuscript table density.

## Local AGENTS hierarchy

Use the nearest `AGENTS.md` when it exists:

- `src/cogsecskills/AGENTS.md` — Python runner, generators, validators, and CLI.
- `definitions/AGENTS.md` — canonical skill-substance authoring rules.
- `skills/AGENTS.md` — rendered skill tree rules; do not hand-edit definition-owned skills.
- `registry/AGENTS.md` — registry, group vocabulary, and optional harness profile metadata.
- `scenarios/AGENTS.md` — deterministic defensive scenario fixtures and expected answers.
- `docs/AGENTS.md` — public docs, generated dashboard, and claim-boundary wording.
- `manuscript/AGENTS.md` — manuscript source, generated supplements, figures, citations, and render gates.
- `tests/AGENTS.md` — test style, no-mock rule, and contract-test ownership.

## How to add a skill

1. Add a row to `registry/skills.yaml` (status `planned`), group must exist in
   `registry/groups.yaml`. If the catalogue size changes, update the README
   group-count table and `test_registry_enumerates_one_hundred_areas` in
   `tests/test_skill_library_conformance.py`.
2. Author it deterministically: create or update
   `definitions/<group>/<slug>.yaml`, then run
   `python -m cogsecskills definitions --write`. The renderer writes all
   conforming skill files and adapters bind every declared verb by construction.
   `python -m cogsecskills author <def>.json|yaml` remains available for one-off
   rendering; `author-batch` remains as a compatibility path for `_def.json`.
   Alternatively, `scaffold <group>.<slug>` for a hand-edited skeleton.
3. Run `python -m cogsecskills definitions --check`, `validate`, `doctor`,
   `scenarios --check`, `examples --check`, and the conformance tests.

All 100 catalogued areas are currently `implemented` and owned by canonical YAML
definitions rendered into the skill tree.

## Skill contract (enforced by `src/cogsecskills/validate.py`)

- Every skill dir has `skill.yaml`, `SKILL.md`, `workflow.md`, and one
  `harness/<h>.md` per configured harness, all declared in the spec's
  `harness:` map. The default configured set is `claude`, `codex`, `hermes`.
- Every harness adapter must include a Markdown binding table whose first column
  lists every neutral tool verb declared in `skill.yaml`.
- Tool verbs are a **closed set**: `read, search, write, exec, reason, web,
  delegate, ask`. Inventing a verb fails parsing.
- A skill marked `implemented` (registry or spec) must exist on disk and declare
  >=1 tool. A `planned` area with no folder is normal — not an error.
- Directory layout is `skills/<group>/<slug>/`; the parent dir name must equal the
  spec's `group`, and the leaf folder must equal the slug in `id: <group>.<slug>`.

## Operational rules

- All logic lives in `src/cogsecskills/`; definitions and skills are declarative
  data; the CLI remains a thin orchestrator over module functions.
- No mocks in tests — real `tmp_path` dirs and real YAML.
- Coverage gate >=90% on `src/`; verify the current value with the test command
  below rather than copying stale numbers into prose.
- Optional harness profiles are documentation metadata until their ids are added
  to `cogsecskills.yaml`, adapters are regenerated, and validation passes.
- **Defensive only.** Skills recognize, assess, and defend against cognitive
  attack. Never author manipulation, influence-op playbooks, or offensive how-tos —
  this is inherited from AGEINT and enforced by review, not by code.

## Tests

```bash
PYTHONPATH="src:." python -m pytest \
  tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py \
  --cov=src/cogsecskills --cov-report=term-missing
```
