# TEST-05: chmod-000 permission test is root-unsafe and environment-dependent

|Field|Value|
|---|---|
|Audit ID|`TEST-05`|
|Lens|`TEST`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
tests/quality/test_cogsecskills_validate_coverage.py:46-53 exercises the OSError path of `validate_skill` by chmod-000ing `claude.md`, then asserting an "unreadable" error appears. As root — common in container CI — chmod 000 does not block reads, so `read_text` succeeds, no OSError fires, and the assertion fails loudly: a false failure, not silent wrong results. The verifier confirmed the mechanism (src/cogsecskills/quality/validate.py:156-157 catches OSError and emits the "unreadable" error) and that no root-conditional skip or pytest marker exists anywhere in the repo, so the test runs unguarded as root.

## Evidence
tests/quality/test_cogsecskills_validate_coverage.py:46-53 (the finding's cited range 44-53 is off by ~2 lines — chmod at :48, assert at :51 — but the content is verbatim):

```python
# Make claude.md unreadable (chmod 000)
claude.chmod(0o000)
result = validate_skill(spec, skills_dir)
assert any("unreadable" in i.message for i in result.errors)
finally: claude.chmod(0o644)
```

Mechanism under test — src/cogsecskills/quality/validate.py:156-157 catches `OSError` and emits the "unreadable" error. Repo-wide search for `geteuid`/`skipif` found no root-conditional skip or pytest marker, so the test runs unguarded as root.

## Impact
In root-CI environments the test always fails loudly — a false failure that blocks CI despite the error path being correct — and the test cannot distinguish "error path works" from "permissions are ignored on this platform". One correction to the original analysis: as root it always fails (never vacuously exercises the happy path), because the assert is unconditional. This is a CI reliability defect, not a correctness one, hence medium rather than high.

## Remediation
Pick one of the two verified-viable alternatives:

1. Skip when running as root or when the platform ignores chmod: guard with `pytest.mark.skipif(os.geteuid() == 0, ...)` or skip after probing that a chmod-000 scratch file is actually unreadable.
2. Preferred (monkeypatch-free and portable): point the spec at a path that is a directory — `read_text` on a directory raises `OSError` on all platforms regardless of privilege — so the OSError handler at src/cogsecskills/quality/validate.py:156-157 is exercised deterministically.

Option 2 is more portable because it removes the root/platform sensitivity entirely rather than skipping the coverage.

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified quote exists; finding's cited range 44-53 is off by ~2 lines (chmod at :48, assert at :51) but content is verbatim. Mechanism confirmed: src/cogsecskills/quality/validate.py:156-157 catches OSError and emits 'unreadable' error — the path under test. Repo-wide grep for geteuid/skipif found no root-conditional skip or pytest marker, so the test runs unguarded as root. As root, chmod 000 does not block reads: read_text succeeds, no OSError, no 'unreadable' error, assert fails loudly — a false failure in root-CI, not silent wrong results, so medium (not high) is right. Correction to the finding's 'why': it suggests the test could 'vacuously exercise the happy path'; in fact it always fails as root, never vacuously. Suggested fixes (euid skip or directory-path OSError probe) are sound; directory probe is more portable.
<!-- PR and issue links are added to the Tracking field after filing. -->