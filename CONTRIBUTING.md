# Contributing to CogSecSkills

Thanks for helping build a dependable, defensive Cognitive-Security skill library.

## Ground rules

- **Defensive only.** Every skill recognizes, assesses, and defends against
  cognitive attack. We do not accept operational how-tos for running manipulation,
  influence operations, or any offensive capability. Keep content educational,
  accountable, and bounded by legal and ethical constraints (inherited from
  [AGEINT](docs/ageint/README.md)).
- **The contract is enforced, not conventional.** Every skill must pass
  `python -m cogsecskills validate` (0 errors). See
  [`docs/skill-contract.md`](docs/skill-contract.md).
- **Code before prompts.** Logic lives in `src/cogsecskills/`; skills are
  declarative data; the CLI only orchestrates.
- **No mocks in tests.** Real `tmp_path` directories and real YAML.

## Setup

```bash
uv sync                      # or: pip install -e ".[dev]"
python -m cogsecskills validate
python -m pytest --cov=cogsecskills --cov-report=term-missing
```

The coverage gate is **90%** on the `cogsecskills` package; the suite uses no mocks.

## Adding or deepening a skill

The preferred path is the deterministic author command — see
[`docs/authoring-skills.md`](docs/authoring-skills.md):

```bash
# 1. (new area) add a row to registry/skills.yaml (status: planned)
# 2. write a JSON definition, then:
python -m cogsecskills author my_skill_def.json
# 3.
python -m cogsecskills validate     # 0 errors
python -m cogsecskills doctor         # quality lint
```

Use only the closed tool-verb vocabulary: `read, search, write, exec, reason,
web, delegate, ask`.

## Before opening a PR

1. `python -m cogsecskills validate` → 0 errors.
2. `python -m cogsecskills doctor` → no quality findings (or justify them).
3. `python -m pytest` → green, coverage ≥ 90%.
4. `ruff check src/cogsecskills tests/` and `ruff format` → clean.
5. If you changed the catalogue size, regenerate `docs/catalogue.md`
   (`python -m cogsecskills catalogue > docs/catalogue.md`) and update the README
   group-count table and the conformance test's expected total.

## Project layout

See [`docs/architecture.md`](docs/architecture.md) and [`AGENTS.md`](AGENTS.md).
