# REPRO-09: pyproject comment claims pandas is in the figures extra; it is not

|Field|Value|
|---|---|
|Audit ID|`REPRO-09`|
|Lens|`REPRO`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/46) |

## Summary
A comment in pyproject.toml's `mypy-overrides` block says the optional `figures` extra is "(matplotlib/numpy/seaborn/pandas)", but the actual `[project.optional-dependencies].figures` list contains only matplotlib, numpy, and seaborn — no pandas. The comment implies a dependency that never installs from that extra; harmless but misleading for anyone debugging figure-rendering environments. One verification nuance: seaborn hard-depends on pandas, so pandas does arrive transitively — the comment is still wrong as written, and 'add the dep' is unnecessary. Severity stays low: stale doc comment, no functional impact.

## Evidence
- `pyproject.toml:71` (comment block under `mypy-overrides`):
  ```
  # The optional `figures` extra (matplotlib/numpy/seaborn/pandas) is needed only
  ```
- `pyproject.toml:41-44` — `figures = ["matplotlib>=3.7", "numpy>=1.24", "seaborn>=0.13"]` — no pandas.
- `uv.lock` `[package.optional-dependencies]` figures confirms only matplotlib/numpy/seaborn.
- Verifier check of the alternative hypothesis: the mypy override block (lines 81-82) lists `'pandas'`, `'pandas.*'` as skipped modules, but that only guards mypy against third-party stubs if pandas happens to be present transitively (seaborn depends on pandas in practice) — not evidence the extra declares it. No other extra declares pandas.

## Impact
Stale comment implies a dependency that never installs from the `figures` extra; misleading for anyone debugging figure-rendering environments (e.g. wondering why pandas imports fail without realizing it only arrives transitively via seaborn). No functional impact — hence low severity.

## Remediation
1. In `pyproject.toml:71`, drop 'pandas' from the comment so it reads "(matplotlib/numpy/seaborn)". Per verification, do NOT add pandas as a dependency: seaborn hard-depends on pandas, so pandas is already installed transitively when the figures extra is — adding an explicit pin would be unnecessary.

## Audit trail
- Discovered by the REPRO lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Confirmed verbatim at line 71 (comment block is under mypy-overrides, matching the finding). The [project.optional-dependencies].figures list at lines 41-44 contains only matplotlib/numpy/seaborn — no pandas. Also checked whether figure code actually imports pandas: the mypy override block (lines 81-82) lists 'pandas', 'pandas.*' as skipped modules, but that is only to guard mypy against third-party stubs if pandas happens to be present transitively (seaborn depends on pandas in practice), not evidence the extra declares it. Did not find any other extra declaring pandas; uv.lock per finding confirms the figures extra lacks pandas. One nuance for the fix: seaborn hard-depends on pandas, so pandas IS installed transitively when the figures extra is — the comment is still wrong as written (pandas is not part of the extra and is never declared), but 'or add the dep' is unnecessary. Severity low is honest: stale doc comment, no functional impact.
<!-- PR and issue links are added to the Tracking field after filing. -->