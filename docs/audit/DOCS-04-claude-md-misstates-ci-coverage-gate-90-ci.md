# DOCS-04: CLAUDE.md misstates the CI coverage gate as >=90% when CI enforces 97

|Field|Value|
|---|---|
|Audit ID|`DOCS-04`|
|Lens|`DOCS`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
CLAUDE.md presents `uv run pytest --cov=cogsecskills --cov-report=term-missing   # coverage gate >=90%` inside its CI commands block, but .github/workflows/ci.yml actually enforces `--cov-fail-under=97`. A contributor trusting CLAUDE.md's 90% bar would be surprised when CI fails a 93%-coverage branch. Both README.md and AGENTS.md correctly state 97, making CLAUDE.md the sole stale doc.

## Evidence
CLAUDE.md:66 (in the block of commands CI enforces, lines ~63-66):

```
uv run pytest --cov=cogsecskills --cov-report=term-missing   # coverage gate >=90%
```

.github/workflows/ci.yml:40 (what CI actually runs):

```
uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=97
```

README.md:224 and AGENTS.md:110-111/126 both correctly state the CI gate is 97 (AGENTS.md additionally explains that pyproject sets `fail_under=90` locally while CI enforces 97). No mitigating note exists in CLAUDE.md itself; the mismatch is real.

## Impact
Documentation-only defect: no wrong results are shipped, but a contributor following CLAUDE.md believes 90% is the CI bar. A regression dropping coverage to 93% passes CLAUDE.md's stated gate yet fails CI, wasting a CI round-trip and undermining trust in the contributor docs. The doc also contradicts two sibling docs (README.md, AGENTS.md).

## Remediation
Update CLAUDE.md:66 so the CI commands block reads `uv run pytest --cov=cogsecskills --cov-report=term-missing --cov-fail-under=97` (or reference AGENTS.md's note that pyproject sets 90 locally while CI enforces 97).

## Audit trail
- Discovered by the DOCS lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Confirmed all three citations. CLAUDE.md:66 sits in a block explicitly presenting commands CI enforces (lines ~63-66) and annotates the pytest line 'coverage gate >=90%'; ci.yml:40 actually enforces --cov-fail-under=97. README.md:224 and AGENTS.md:110-111/126 both correctly state 97 (AGENTS.md even explains pyproject sets fail_under=90 locally while CI enforces 97), so CLAUDE.md is the sole stale doc. Re-derived reasoning holds: a contributor trusting CLAUDE.md's 90% bar would be surprised when CI fails at 93% coverage. Checked mitigations: none in CLAUDE.md itself; the mismatch is real. Severity medium is appropriate — documentation-only defect, no wrong results shipped, but it misleads contributors and contradicts two sibling docs.
<!-- PR and issue links are added to the Tracking field after filing. -->