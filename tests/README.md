# tests

Test suite for the CogSecSkills runner and skill library. CI runs the whole tree
with a coverage gate:

```bash
uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=97
```

While iterating, name a single package (e.g. `uv run pytest tests/contract`).

## Packages

| Package | Concern | Approx. test modules |
| --- | --- | --- |
| `tests/core/` | Runner data model: spec parsing, registry, loader, config, harness adapters | 5 |
| `tests/authoring/` | Authoring pipeline: `author`, `scaffold`, `definitions --write/--check` | 4 |
| `tests/quality/` | Conformance validation and quality lint (`validate`, `doctor`, insights) | 8 |
| `tests/artifacts/` | Generated views: scenarios, examples, evals, dashboard, release metadata, manuscript assets, figures | 14 |
| `tests/contract/` | CLI contract tests: exit codes, `--format json` payloads, argument handling | 3 |
| `tests/conformance/` | Whole-library invariants (e.g. 100 catalogued areas, coverage floors) | 1 |

## Conventions

- **No mocks.** Tests use real `tmp_path` directories and real YAML files; see
  `../AGENTS.md` for the no-mock rule.
- Coverage floor: 90 in `pyproject.toml`, enforced at `97` locally and in CI.
- Deterministic: no network access; figure tests use the `figures` extra
  (installed in CI via `.[dev,figures]`).
