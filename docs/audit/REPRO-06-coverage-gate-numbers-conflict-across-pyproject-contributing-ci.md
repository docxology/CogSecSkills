# REPRO-06: Coverage gate numbers conflict across pyproject, CONTRIBUTING, and CI

|Field|Value|
|---|---|
|Audit ID|`REPRO-06`|
|Lens|`REPRO`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/43) |

## Summary
pyproject.toml sets `fail_under = 90`, CONTRIBUTING.md tells contributors "The coverage gate is **90%**" and its PR checklist says 'coverage ≥ 90% → green', while CI actually enforces `--cov-fail-under=97`; CLAUDE.md also misstates the CI gate as >=90% directly under its CI context. A contributor passing at 90-96% locally will fail CI, contradicting the PR checklist's instruction. Verdict was adjusted (severity confirmed low) after verification: AGENTS.md:110-112 already acknowledges the two-floor split and warns against copying stale numbers, and README.md:224, TODO.md:18, dashboard artifacts, and tests/README.md all correctly say 97 — the conflict is limited to CONTRIBUTING + CLAUDE.md plus pyproject's stale floor, a docs footgun rather than broken code.

## Evidence
- `pyproject.toml:121-122` — `[tool.coverage.report]` / `fail_under = 90`.
- `CONTRIBUTING.md:27` — 'The coverage gate is **90%** on the `cogsecskills` package; the suite uses no mocks.' and `:50` — '`python -m pytest` → green, coverage ≥ 90%.'
- `.github/workflows/ci.yml:40`:
  ```
  run: uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=97
  ```
- `CLAUDE.md:66` — 'uv run pytest --cov=cogsecskills --cov-report=term-missing   # coverage gate >=90%' presented under 'CI (.github/workflows/ci.yml) additionally enforces:'.
- Context: `AGENTS.md:110-112` acknowledges the discrepancy ('CI enforces the stricter --cov-fail-under=97… rather than copying stale numbers into prose'), but CONTRIBUTING still asserts 90%. README.md:224, TODO.md:18, dashboard artifacts, and tests/README.md all correctly say 97; CHANGELOG confirms 97 is the intended floor.

## Impact
Local runs pass at 90-96% coverage while CI fails, contradicting the PR checklist's 'coverage ≥ 90% → green' instruction. Contributor footgun: wasted CI cycles and confusion about which floor is real. Verified scope: the conflict is limited to CONTRIBUTING + CLAUDE.md (+ pyproject's stale 90 floor); README, TODO, dashboard artifacts, and tests/README.md already state 97 correctly, and 97 is the intended floor per CHANGELOG.

## Remediation
1. In `pyproject.toml` `[tool.coverage.report]` (~line 122), bump `fail_under` to 97 so pyproject and CI share a single source of truth (the intended floor per CHANGELOG).
2. Fix `CONTRIBUTING.md:27` and `:50` to state the 97% gate instead of 90%.
3. Fix `CLAUDE.md:66` to state the actual CI gate (`--cov-fail-under=97`) instead of '>=90%'.

## Audit trail
- Discovered by the REPRO lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Substance fully confirmed; only cited line numbers drifted (CONTRIBUTING is :27/:50, not :16; ci.yml is :40, not :27). Verified: pyproject fail_under=90; CI --cov-fail-under=97; CONTRIBUTING tells contributors 90%; CLAUDE.md misstates the CI gate as >=90% directly under CI context. AGENTS.md:110-112 indeed acknowledges the two-floor split and says verify rather than copy numbers, but CONTRIBUTING still asserts 90% and its PR checklist says 'coverage ≥ 90% → green', so a contributor passing at 90-96% locally can fail CI. README.md:224, TODO.md:18, dashboard artifacts, and tests/README.md all correctly say 97, so the conflict is real but limited to CONTRIBUTING + CLAUDE.md (+ pyproject's stale floor). Severity low is fair: docs/footgun, not broken code; CHANGELOG confirms 97 is the intended floor. Suggested fix (bump pyproject fail_under to 97 and correct CONTRIBUTING/CLAUDE.md) is sound. Confidence high.
<!-- PR and issue links are added to the Tracking field after filing. -->