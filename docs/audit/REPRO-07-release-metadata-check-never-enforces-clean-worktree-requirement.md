# REPRO-07: release-metadata --check never enforces the clean-worktree requirement in CI

|Field|Value|
|---|---|
|Audit ID|`REPRO-07`|
|Lens|`REPRO`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/44) |

## Summary
`release_metadata.py`'s `_findings()` appends "{mode} mode requires a clean git worktree" when mode is `release-candidate`/`public-archive` and the worktree is dirty — but CI runs `release-metadata --check` with the CLI's default `--mode local`, so the dirty-worktree and git-availability findings are unreachable from CI. The payload's `release_candidate_requires_clean_worktree: True` claim is policy text only; no automated path ever enforces it. Verdict was adjusted (severity confirmed low) because this is a missing policy-enforcement hook rather than a wrong output: metadata content is still generated and drift-checked, and the enforcement gap only matters at release time.

## Evidence
- `src/cogsecskills/artifacts/release_metadata.py:234-235` (in `_findings`, function defined at :209):
  ```
  if mode in {"release-candidate", "public-archive"} and runtime_git.get("dirty"):
      findings.append(f"{mode} mode requires a clean git worktree")
  ```
- `cli.py:664-667` — `--mode` `choices=("local", "release-candidate", "public-archive")`, `default="local"`.
- `.github/workflows/ci.yml:55` — `uv run cogsecskills release-metadata --check` (no `--mode` flag).
- Payload claim at `release_metadata.py:175` — `"release_candidate_requires_clean_worktree": True` is policy text with no automated enforcement.
- Only workflow in `.github/workflows/` is ci.yml, so no tagged-build path ever runs `--mode release-candidate`.
- Unit behavior is covered (per CHANGELOG, a release-candidate dirty-worktree test exists), but that only proves the branch logic, not CI wiring.

## Impact
A dirty-worktree release-candidate run emits no findings unless someone manually passes `--mode`; the documented clean-worktree policy is unenforced. Scope of harm (verified): metadata content is still generated and drift-checked locally-mode, so nothing wrong ships through CI — the gap is that the release-time guarantee the payload advertises is never actually checked by any automated path, leaving the clean-worktree requirement to manual discipline at release time.

## Remediation
1. Have the CI gate (or a dedicated release workflow) run `uv run cogsecskills release-metadata --check --mode release-candidate` on tagged builds, so the dirty-worktree and git-availability findings actually fire on tagged builds.
2. Alternatively, wire a release workflow (none exists today — `.github/workflows/` contains only ci.yml) that enforces the mode-gated checks at release time.

## Audit trail
- Discovered by the REPRO lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Mechanism fully confirmed: dirty-worktree findings only fire when mode != 'local' (:232-235); CI gate calls --check with the default mode='local' (ci.yml line is 55, not 34 as cited — quote text otherwise accurate). Only workflow in .github/workflows/ is ci.yml, so no tagged-build path ever runs --mode release-candidate; the payload's `release_candidate_requires_clean_worktree: True` is policy text with no automated enforcement. Tests cover the branch (per CHANGELOG, release-candidate dirty-worktree test exists) but that only proves unit behavior, not CI wiring. Corrections: ci.yml line number 34 -> 55, and _findings is the function name at :209. Severity 'low' is fair: this is a missing policy-enforcement hook, not a wrong output — metadata content is still generated and drift-checked; enforcement gap only matters at release time and is documented as a manual --mode step.
<!-- PR and issue links are added to the Tracking field after filing. -->