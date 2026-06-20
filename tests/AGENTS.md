# AGENTS.md - Tests

Tests are contract oracles for the real repository shape.

## Rules

- No mocks for project data. Use real `tmp_path` repositories, real YAML, and the
  same public functions the CLI uses.
- Do not weaken or delete failing tests to make gates pass.
- Maintain contract-test ownership. Add focused tests when introducing a new
  source-owned surface, generated file, CLI command, or claim-boundary rule.
- Keep broad library tests pointed at the real `registry/`, `definitions/`, and
  `skills/` tree.

## Common Gates

```bash
PYTHONPATH="src:." python -m pytest tests/test_cogsecskills_*.py tests/test_skill_library_conformance.py --cov=src/cogsecskills --cov-report=term-missing
uv run ruff check src/cogsecskills tests
uv run ruff format --check src/cogsecskills tests
uv run mypy
```
