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
uv sync --locked --extra dev --extra figures  # or: pip install -e ".[dev,figures]"
uv run python -m cogsecskills validate
uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=99
```

The coverage gate is **99%** on the `cogsecskills` package; the suite uses no mocks.

## Adding or deepening a skill

The preferred path is the canonical definition renderer — see
[`docs/authoring-skills.md`](docs/authoring-skills.md):

```bash
# 1. (new area) add a row to registry/skills.yaml (status: planned)
# 2. create or deepen definitions/<group>/<slug>.yaml
uv run python -m cogsecskills definitions --write
uv run python -m cogsecskills definitions --check
# 3. validate structure and skill-specific quality
uv run python -m cogsecskills validate
uv run python -m cogsecskills doctor
```

Use only the closed tool-verb vocabulary: `read, search, write, exec, reason,
web, delegate, ask`.

The `figures` extra is needed for the real figure-generation tests in the full
suite. One-off `author`, `author-batch`, and `scaffold` output must be promoted
into canonical definitions before it becomes library-owned skill substance.

## Before opening a PR

1. `uv run python -m cogsecskills validate` → 0 errors.
2. `uv run python -m cogsecskills doctor` → no quality findings (or justify them).
3. `uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=99`
   → green, coverage ≥ 99%.
4. `uv run ruff check src/cogsecskills tests`,
   `uv run ruff format --check src/cogsecskills tests`, and `uv run mypy` → clean.
5. Run the generated-output gates in [`AGENTS.md`](AGENTS.md) after any skill,
   scenario, registry, example, or manuscript source change. Regenerate with
   the owning command; do not edit generated files by hand.
6. If you changed the catalogue size, regenerate `docs/catalogue.md`
   (`uv run python -m cogsecskills catalogue --markdown --output docs/catalogue.md`) and
   update the README group-count table and the conformance test's expected total.

## Project layout

See [`docs/architecture.md`](docs/architecture.md) and [`AGENTS.md`](AGENTS.md).
