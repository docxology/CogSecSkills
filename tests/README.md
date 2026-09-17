# tests

Test suite for the CogSecSkills runner and skill library. CI runs the whole tree
with a coverage gate:

```bash
uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=99
```

While iterating, name a single package (e.g. `uv run pytest tests/contract`).

## Packages

| Package | Concern | Approx. test modules |
| --- | --- | --- |
| `tests/core/` | Runner data model: spec parsing, registry, loader, config, harness adapters | 7 |
| `tests/authoring/` | Authoring pipeline: `author`, `scaffold`, `definitions --write/--check` | 6 |
| `tests/quality/` | Conformance validation and quality lint (`validate`, `doctor`, insights) | 9 |
| `tests/artifacts/` | Generated views: scenarios, examples, evals, dashboard, release metadata, manuscript assets, figures | 14 |
| `tests/contract/` | Source-owned doc and artifact contracts: claim boundaries, harness profiles, manuscript surfaces, catalogue drift, CLI JSON payloads | 4 |
| `tests/conformance/` | Whole-library invariants (e.g. 100 catalogued areas, registry↔disk parity) | 1 |
| `tests/runtime/` | Live-eval runner: prompt building, transcript screening, real-subprocess harness fixtures (no network, no mocks) | 1 |

## Conventions

- **No mocks for project data.** Tests use real `tmp_path` directories and real
  YAML files; see `../AGENTS.md` for the no-mock rule.
- **Accepted `pytest.MonkeyPatch` exception:** fault injection at module seams
  to reach failure branches deterministically and permission-independently
  (e.g. raising `OSError`/`ValueError` from a loader or reader, narrowing
  `HARNESS_VERB_SUPPORT`). Project data is never faked; examples:
  `tests/quality/test_cogsecskills_validate_coverage.py`,
  `tests/quality/test_cogsecskills_lowgap_coverage.py`,
  `tests/authoring/test_cogsecskills_definitions_branches.py`,
  `tests/core/test_cogsecskills_locate_and_constants.py`,
  `tests/artifacts/test_cogsecskills_examples_branches.py`.
- Coverage floor: `99` — `pyproject.toml` `fail_under` and CI `--cov-fail-under` agree.
- Deterministic: no network access; figure tests use the `figures` extra
  (installed in CI via `.[dev,figures]`).
