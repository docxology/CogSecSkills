# TEST-10: Coverage gaps: negative-path tests missing for registry/config edge interactions exercised only via happy path in live conformance

|Field|Value|
|---|---|
|Audit ID|`TEST-10`|
|Lens|`TEST`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
The conformance suite's quality-control test asserts only substring presence (`"unsafe" in negative`, `"inference" in evidence`), and `ALLOWED_SHARED_QUALITY_ITEMS` — the whitelist deciding which shared quality items may repeat across skills — has zero behavioral test: only set-key equality and a subset check exist, with whitelist semantics exercised only via real-corpus fixtures. There is also no dedicated test for `--root` pointing at a nonexistent directory. Red team verdict ADJUSTED: the original "unsafe unsafe unsafe passes" example is refuted (the suite additionally rejects `GENERIC_NEGATIVE_CONTROL_PHRASES` and requires skill-name/slug/specificity tokens), and the whitelist is currently a latent mechanism (all three values are empty sets at quality_constants.py:52-55), so blast radius is minimal; the narrower claims — weak keyword assertions, untested whitelist semantics, missing `--root` error path — survive, and severity stays low.

## Evidence
- tests/conformance/test_skill_library_conformance.py:85-98 — `assert "unsafe" in negative ... assert "inference" in evidence` (substring-only assertions confirmed), but the same test at :96-113 also asserts `not any(phrase in negative for phrase in GENERIC_NEGATIVE_CONTROL_PHRASES)` and `assert (specificity overlap ...), f"{skill_id}: negative controls are not skill- or group-specific"` (in `test_canonical_definitions_have_specific_quality_controls`).
- tests/core/test_cogsecskills_locate_and_constants.py:78-79

```python
def test_allowed_shared_quality_items_keys_match_reused():
    assert set(ALLOWED_SHARED_QUALITY_ITEMS) == set(REUSED_QUALITY_FIELDS)
```

  (only key-set equality, plus a subset check at :74-75; no value/whitelist-semantics test)
- Whitelist values: quality_constants.py:52-55 — all three `ALLOWED_SHARED_QUALITY_ITEMS` sets currently empty.
- No dedicated test for `--root` pointing at a nonexistent directory (repo-wide search; only missing-registry/data paths are covered).

## Impact
The corpus-wide anti-boilerplate gate is the project's central quality claim, but keyword assertions alone are weak: a degenerate entry padded with skill-name/slug tokens could slip past the substring checks (though not past the `GENERIC_NEGATIVE_CONTROL_PHRASES`/specificity assertions). A bug in `ALLOWED_SHARED_QUALITY_ITEMS` semantics would silently permit cross-skill copy-paste; today it is a latent mechanism (empty sets), which keeps blast radius minimal but leaves the whitelist semantics unguarded for when it activates.

## Remediation
1. Add a conformance-side unit test with a hand-built definition whose quality controls include (a) a whitelisted shared item — must pass — and (b) a non-whitelisted duplicate — must fail; this pins the whitelist semantics of `ALLOWED_SHARED_QUALITY_ITEMS` (src/cogsecskills quality_constants.py:52-55, exercised at definitions.py:341-343 and insights.py:315-317) so the latent mechanism has a behavioral test before it activates.
2. Add a CLI test for a nonexistent `--root` asserting the error message and exit code — the error path is currently touched only indirectly via validate_library missing-registry.
3. Optionally strengthen the keyword assertions in tests/conformance/test_skill_library_conformance.py:85-98 by asserting the negative control mentions the skill's own slug, which the specificity assertion already implies — unify rather than keep the substring-only checks as a separate weak convention.

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Partially refuted, partially confirmed. (a) The 'unsafe unsafe unsafe passes' example is wrong: the conformance suite additionally rejects GENERIC_NEGATIVE_CONTROL_PHRASES and requires negative controls to contain skill-name/slug/specificity tokens (test_canonical_definitions_have_specific_quality_controls, lines 85-113), so a degenerate keyword-only negative would fail the specificity assertion. The narrower claim survives: keyword assertions alone are weak, and a degenerate entry padded with skill tokens could slip past. (b) Confirmed ALLOWED_SHARED_QUALITY_ITEMS has zero behavioral test — only set-key equality (test_cogsecskills_locate_and_constants.py:78-79) and a subset check (:74-75); its whitelist semantics are exercised in definitions.py:341-343 and insights.py:315-317 only via real-corpus fixtures, with no unit test of an allowed-shared-item-pass vs non-whitelisted-duplicate-fail. Mitigating: all three whitelist values are currently empty sets (quality_constants.py:52-55), so the whitelist is a latent mechanism with no active effect today, keeping blast radius minimal. (c) Confirmed no dedicated test for `--root` pointing at a nonexistent directory (searched tests/ for nonexistent-root CLI cases; only missing-registry/data paths are covered). Severity low is correct; the fix suggestion is sensible.
<!-- PR and issue links are added to the Tracking field after filing. -->