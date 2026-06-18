# AGENTS.md — CogSecSkills

Guidance for AI agents working in this project. See [`README.md`](README.md) for
the overview and [`ISA.md`](ISA.md) for the ideal-state articulation.

## What this project is

CogSecSkills is a **library of multiharness agentic skills** for Cognitive
Security and analytic tradecraft. The deliverable is the skills system:
registry, on-disk skills, AGEINT docs, runner package, tests, generated
catalogue, and a manuscript scaffold that documents those source surfaces.

## The three artifacts you must keep coherent

1. **`registry/skills.yaml`** — the catalogue of all 100 skill areas (the plan).
2. **`skills/<group>/<slug>/`** — the on-disk skill implementations (the build).
3. **`docs/ageint/`** — the AGEINT educational upstream (the teach).

The manuscript scaffold under `manuscript/` is a documentation surface for the
skills system. Keep it evidence-bound: it may describe the registry, skills,
runner, tests, and validation results, but it must not invent publication
claims, citations, figures, or benchmarks.

After any change to skills or the registry, run the gate:

```bash
PYTHONPATH="src:." python -m cogsecskills validate   # must report 0 errors
```

## How to add a skill

1. Add a row to `registry/skills.yaml` (status `planned`), group must exist in
   `registry/groups.yaml`. If the catalogue size changes, update the README
   group-count table and `test_registry_enumerates_one_hundred_areas` in
   `tests/test_skill_library_conformance.py`.
2. Author it deterministically (preferred): write a JSON definition (see
   `src/cogsecskills/author.py` docstring for the schema) and run
   `python -m cogsecskills author <def>.json` — the renderer writes all six
   conforming files (adapters bind every declared verb by construction) and sets
   status `implemented`. For many at once, drop a `_def.json` in each skill folder
   and run `python -m cogsecskills author-batch` (renders + promotes the registry).
   Alternatively, `scaffold <group>.<slug>` for a hand-edited skeleton.
3. `python -m cogsecskills validate` (0 errors) and run the conformance tests.

All 100 catalogued areas are currently `implemented`. The 92 non-exemplar skills
were authored in parallel as structured definitions and rendered via `author`.

## Skill contract (enforced by `src/cogsecskills/validate.py`)

- Every skill dir has `skill.yaml`, `SKILL.md`, `workflow.md`, and one
  `harness/<h>.md` per harness (`claude`, `codex`, `hermes`), all declared in the
  spec's `harness:` map.
- Every harness adapter must include a Markdown binding table whose first column
  lists every neutral tool verb declared in `skill.yaml`.
- Tool verbs are a **closed set**: `read, search, write, exec, reason, web,
  delegate, ask`. Inventing a verb fails parsing.
- A skill marked `implemented` (registry or spec) must exist on disk and declare
  >=1 tool. A `planned` area with no folder is normal — not an error.
- Directory layout is `skills/<group>/<slug>/`; the parent dir name must equal the
  spec's `group`, and the leaf folder must equal the slug in `id: <group>.<slug>`.

## Operational rules

- All logic lives in `src/cogsecskills/`; skills are declarative data; the CLI and
  scripts only orchestrate (thin-orchestrator pattern).
- No mocks in tests — real `tmp_path` dirs and real YAML.
- Coverage gate >=90% on `src/`; verify the current value with the test command
  below rather than copying stale numbers into prose.
- **Defensive only.** Skills recognize, assess, and defend against cognitive
  attack. Never author manipulation, influence-op playbooks, or offensive how-tos —
  this is inherited from AGEINT and enforced by review, not by code.

## Tests

```bash
PYTHONPATH="src:." python -m pytest \
  tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py \
  --cov=src/cogsecskills --cov-report=term-missing
```
