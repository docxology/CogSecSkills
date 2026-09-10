# REPRO-02: CITATION.cff uses an invalid cff-version and a version DOI mislabeled for the wrong release

|Field|Value|
|---|---|
|Audit ID|`REPRO-02`|
|Lens|`REPRO`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
`CITATION.cff` declares `cff-version: 1.7.0` — the project version was pasted into the CFF schema-version field, whose valid values are the 1.2.x line — so any CFF validator (cffconvert, GitHub's CFF check) rejects the file. The same file cites `version: 1.7.0` while its identifiers block labels 10.5281/zenodo.20804586 as "Version DOI (v1.0.0)", creating miscitation risk. No CI step or repo tool validates CITATION.cff syntax. Severity stays medium: a metadata-level defect causing validation failure and citation confusion, with no runtime/code impact.

## Evidence
- `CITATION.cff:1` — `cff-version: 1.7.0` (valid CFF schema versions are 1.2.x).
- `CITATION.cff` (~line 31) — `version: 1.7.0`.
- `CITATION.cff` identifiers block (~lines 32-37):
  ```
  value: 10.5281/zenodo.20804585
  description: Concept DOI (all versions)
  value: 10.5281/zenodo.20804586
  description: Version DOI (v1.0.0)
  ```
  The version DOI is explicitly labeled v1.0.0 while the file cites v1.7.0.
- Amplifying factor (verifier): `README.md:41` actively directs citers to 10.5281/zenodo.20804586.
- No gate: `.github/workflows/ci.yml` contains no cff/citation validation; no test or tool in the repo validates CITATION.cff.
- Partial mitigation (verifier): `TODO.md:93` — 'Update CITATION.cff and codemeta.json with new version DOI once deposited on Zenodo' — shows the DOI staleness is a known pending item, but nothing acknowledges or fixes the invalid `cff-version`, and a TODO is not a gate.

## Impact
The file will fail cffconvert/CFF validation, and anyone following the citation instructions cites the v1.0.0 DOI for what the file claims is v1.7.0 — miscitation risk amplified by README.md pointing citers at the v1.0.0 DOI. Nothing in CI catches either problem, so both persist indefinitely.

## Remediation
1. In `CITATION.cff`, set `cff-version: 1.2.0` (valid 1.2.x schema version) instead of the pasted project version.
2. Resolve the version-DOI mismatch: either drop the `Version DOI (v1.0.0)` identifier, or relabel/update it once the v1.7.0 deposit exists (per the existing TODO.md:93 item).
3. Add a CFF validation step to `.github/workflows/ci.yml` (e.g. run `cffconvert --validate` or the GitHub CFF validator action) so an invalid citation file fails CI instead of shipping.

## Audit trail
- Discovered by the REPRO lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified by reading the full file. (1) `cff-version: 1.7.0` at line 1 confirmed verbatim — this is the project version pasted into the schema-version field; valid CFF schema versions are 1.2.0 (1.2.x line), so cffconvert/GitHub's CFF validation rejects the file. (2) `version: 1.7.0` and the identifiers block confirmed: concept DOI 10.5281/zenodo.20804585, version DOI 10.5281/zenodo.20804586 explicitly labeled 'Version DOI (v1.0.0)' while the file cites v1.7.0 — a stale/possibly-wrong version DOI (miscitation risk). Note README.md:41 actively directs citers to 10.5281/zenodo.20804586, amplifying the risk. (3) No existing gate: .github/workflows/ci.yml contains no cff/citation validation; no test or tool in the repo validates CITATION.cff. (4) Partial mitigation found: TODO.md:93 ('Update CITATION.cff and codemeta.json with new version DOI once deposited on Zenodo') shows the DOI staleness is a known, documented pending item — but nothing acknowledges or fixes the invalid cff-version, and a TODO is not a gate. (5) Severity medium is right: metadata-level defect causing validation failure and citation confusion; no runtime/code impact. Exact line number of `version:` is ~31 (file has 37 lines); finding's line citations check out.
<!-- PR and issue links are added to the Tracking field after filing. -->