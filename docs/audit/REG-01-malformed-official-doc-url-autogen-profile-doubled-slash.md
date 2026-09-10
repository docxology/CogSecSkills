# REG-01: Malformed official_doc_url for autogen profile (doubled slash)

|Field|Value|
|---|---|
|Audit ID|`REG-01`|
|Lens|`REG`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
The `autogen` harness profile in the registry contains a malformed documentation URL with a doubled slash (`stable//index.html`), unlike the clean single-slash URLs used by every other profile row. Public reference metadata should be uniform and clickable. The red team confirmed the verdict at low severity: the URL still resolves on most servers (path `//` is typically tolerated), so this is cosmetic/hygiene rather than broken functionality.

## Evidence
`registry/harness_profiles.yaml:104`:

```
official_doc_url: https://microsoft.github.io/autogen/stable//index.html
```

The verifier confirmed this verbatim at line 104 and that all other 15 profiles in the file use clean single-slash URLs. Checked whether an existing gate covers it — `tests/contract/test_cogsecskills_docs_contract.py:162` only asserts:

```python
str(profile["official_doc_url"]).startswith("https://")
```

The doubled slash passes that check, so the property is NOT already enforced.

## Impact
Inconsistent, malformed public reference metadata. Any future check that assumes normalized URLs (exact-match comparisons, link canonicalization, deduplication) would treat this row differently from its peers, and the cosmetic defect erodes confidence in registry hygiene. Because the URL still resolves, there is no functional breakage today — this is a contributor-facing hygiene and consistency issue.

## Remediation
1. In `registry/harness_profiles.yaml:104`, change the autogen profile's URL to `https://microsoft.github.io/autogen/stable/index.html`.
2. Extend `tests/contract/test_cogsecskills_docs_contract.py` (which already loads all profiles) with a normalization/no-doubled-slash assertion on `official_doc_url`, so malformed URLs fail loudly in CI instead of relying on visual review.

## Audit trail
- Discovered by the REG lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Confirmed verbatim at line 104; all other 15 profiles in the file use clean single-slash URLs. Checked whether an existing gate covers it: tests/contract/test_cogsecskills_docs_contract.py:162 only asserts `str(profile["official_doc_url"]).startswith("https://")` — the doubled slash passes that check, so the property is NOT already enforced. The URL would still resolve on most servers (path // typically tolerated) so it is cosmetic/hygiene, not broken functionality; low severity is correct. Fix suggestion is sound: the contract test already loads all profiles so a normalization/no-doubled-slash assertion is a natural addition.
<!-- PR and issue links are added to the Tracking field after filing. -->