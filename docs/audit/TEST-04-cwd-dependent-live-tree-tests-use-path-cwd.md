# TEST-04: CWD-dependent live-tree tests use Path.cwd() — order/environment-sensitive

|Field|Value|
|---|---|
|Audit ID|`TEST-04`|
|Lens|`TEST`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/50) |

## Summary
Two live-tree tests anchor the repository root via `Path.cwd()` instead of the `PROJECT_ROOT = Path(__file__).resolve().parents[2]` convention used by 15+ sibling test files, so they silently depend on pytest being invoked from the project root. Running from a subdirectory, an IDE with a different working dir, or a per-file invocation makes them fail or — worse — pass vacuously on an empty row set. The verifier confirmed the mechanism precisely: src/cogsecskills/core/registry.py:28-30 uses the passed root verbatim when non-None, so `Path.cwd()` bypasses the `_project_root()` sentinel walk-up that would otherwise find the real root.

## Evidence
- tests/artifacts/test_cogsecskills_manuscript_assets.py:200

```python
rows = collect_skill_rows(Path.cwd())
```

  :201-202 — `groups = {row.group for row in rows}` / `assert groups <= set(GROUP_COLORS)`.
- tests/artifacts/test_cogsecskills_scenarios.py:436 — `registry = load_registry(Path.cwd())`; :438 — `scenarios = load_scenarios(Path.cwd())`; :449 — `assert check_scenarios(Path.cwd()) == []` (test spans 435-449).
- src/cogsecskills/core/registry.py:28-30 — `registry_path` uses the passed root verbatim: `base = Path(root) if root is not None else _project_root()`; no fallback for non-None roots.

## Impact
These "repository-wide" tests fail under subdirectory/IDE/per-file pytest invocation, and the palette test `test_live_group_palette_covers_registry_groups` passes vacuously on an empty row set (`groups <= set(GROUP_COLORS)` is trivially true when `groups` is empty); the scenarios assertions (0 == 0, `all()` over empty) are also vacuous, though `load_registry` typically raises `FileNotFoundError` first in broken-cwd cases. pyproject.toml:105 `testpaths=["tests"]` only protects bare pytest at root and does not cover subdir/IDE/per-file invocation. No shipped artifact is affected — the failure mode is test flakiness and false-green under nonstandard invocation — which is why severity medium is appropriate.

## Remediation
1. Replace `Path.cwd()` with the existing `PROJECT_ROOT = Path(__file__).resolve().parents[2]` convention in tests/artifacts/test_cogsecskills_manuscript_assets.py:200 and tests/artifacts/test_cogsecskills_scenarios.py:436, 438, 449 — matching 15+ sibling files (e.g. test_cogsecskills_examples.py:27 `load_examples(PROJECT_ROOT)`, test_cogsecskills_figures.py:389/416 `collect_skill_rows(PROJECT_ROOT)`).
2. For `test_live_group_palette_covers_registry_groups`, additionally assert `groups` is non-empty so it cannot pass vacuously on an empty tree.
3. Consider asserting the scenarios tree non-empty too (e.g. `assert scenarios` before the `all()` checks) to remove the vacuous-pass mode.

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Re-derived independently. (1) Quotes verified at cited lines; scenarios test spans 435-449 as claimed. (2) No mitigation elsewhere: src/cogsecskills/core/registry.py:28-30 `registry_path` uses the passed root verbatim — `base = Path(root) if root is not None else _project_root()` — so passing Path.cwd() explicitly bypasses the _project_root() sentinel walk-up that would otherwise find the real root; no fallback for non-None roots. (3) Vacuous-pass claim real: palette test `groups <= set(GROUP_COLORS)` trivially true on empty rows; scenarios assertions (0==0, all() over empty) also vacuous, though load_registry typically raises FileNotFound first in broken-cwd cases. (4) Inconsistent convention confirmed: 15+ sibling test files define `PROJECT_ROOT = Path(__file__).resolve().parents[2]` (e.g. test_cogsecskills_examples.py:27 uses load_examples(PROJECT_ROOT) for the analogous live-tree test; test_cogsecskills_figures.py:389/416 calls the same collect_skill_rows(PROJECT_ROOT)). (5) pyproject.toml:105 testpaths=["tests"] only helps bare pytest at root; does not protect subdir/IDE/per-file invocation. Not critical/high: no shipped artifact affected; failure mode is test flakiness/false-green under nonstandard invocation. Proposed fix (switch to PROJECT_ROOT; add non-empty assertion for groups) is correct and matches existing convention.
<!-- PR and issue links are added to the Tracking field after filing. -->
