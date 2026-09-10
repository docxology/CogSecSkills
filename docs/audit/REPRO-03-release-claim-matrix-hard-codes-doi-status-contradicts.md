# REPRO-03: Release claim matrix hard-codes a DOI status that contradicts the files it reads

|Field|Value|
|---|---|
|Audit ID|`REPRO-03`|
|Lens|`REPRO`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | PENDING-ISSUE-LINK |

## Summary
The claim matrix built by `release_metadata.py` hard-codes the row `{"claim": "Public archive DOI", "status": "unavailable until a real archive exists", "evidence": "CITATION.cff and CodeMeta contain no DOI"}` as a static string, even though the same file's `_has_doi()` correctly detects two DOI identifiers in CITATION.cff/codemeta.json and flips `archive.status` to `available`. The generated honesty surface `docs/release-claim-matrix.md` therefore ships a permanently false claim ("contains no DOI") baked into the payload, and the check passes because both the text and the contradiction are regenerated identically. Severity stays medium: the machine-readable `archive.status` field is correct, so the defect is cosmetic-to-misleading rather than a broken execution contract.

## Evidence
- `src/cogsecskills/artifacts/release_metadata.py:196-198` (inside the static `claim_matrix` list at :184-199):
  ```
  "claim": "Public archive DOI"
  "status": "unavailable until a real archive exists"
  "evidence": "CITATION.cff and CodeMeta contain no DOI"
  ```
- `CITATION.cff:18` — `doi: 10.5281/zenodo.20804585` (identifiers block at :21-27); `codemeta.json:18` — `"identifier": "10.5281/zenodo.20804585"`.
- `release_metadata.py:101-131` — `_has_doi(cff, codemeta)` sets `doi_present`; `:165` — `"status": "unavailable" if not doi_present else "available"`. With two DOI identifiers present, `doi_present=True` and `archive.status='available'`.
- Generated proof of the internal contradiction: `output/data/release_metadata.json:2-4` shows `"archive": {"doi_present": true, "status": "available"}` while `:19-21` of the same JSON shows the claim-matrix row 'unavailable until a real archive exists / CITATION.cff and CodeMeta contain no DOI'.
- `docs/release-claim-matrix.md:25` ships the same false row verbatim.
- No mitigating gate: the mode guard at `release_metadata.py:236` (`mode == "public-archive" and not payload["archive"]["doi_present"]`) uses the correct `_has_doi` result but does nothing about the static claim-matrix text; no test asserts the claim matrix agrees with `payload['archive']`, so regeneration reproduces the contradiction identically.

## Impact
The repo's self-described honesty surface ships a factually false evidence line — "CITATION.cff and CodeMeta contain no DOI" — while a real DOI exists, and the same JSON artifact internally contradicts itself (`archive.status: available` next to a claim-matrix row asserting no DOI). Because the row is static, regeneration reproduces the contradiction identically forever, and the release-claim matrix cannot be trusted as a claim-boundary document. Wrong decisions (e.g. "no archive exists, cannot cite") can be drawn from the rendered markdown.

## Remediation
1. In `src/cogsecskills/artifacts/release_metadata.py` (~lines 184-199), replace the hard-coded DOI-row `status`/`evidence` strings with values derived from `payload["archive"]` / `_has_doi()` — e.g. status `available` with the actual DOI as evidence when `doi_present` is true, and the current "unavailable" text only when no DOI exists.
2. Regenerate `docs/release-claim-matrix.md` (and `output/data/release_metadata.json`) so the shipped surface is internally consistent.
3. Add a conformance check (test or gate) asserting the claim matrix's DOI row agrees with `payload["archive"]`, so the contradiction cannot be regenerated silently.

## Audit trail
- Discovered by the REPRO lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified all mechanisms: (1) claim_matrix rows are a static hard-coded list in _metadata_payload (release_metadata.py:184-199) — the DOI row's status/evidence strings never consult payload['archive'] or _has_doi; (2) _has_doi reads the 'identifiers' list and CITATION.cff has two DOI identifiers, so doi_present=True and archive.status='available' — confirmed in the generated release_metadata.json, which is internally contradictory (archive says available, claim matrix says no DOI exists); (3) the generated markdown docs/release-claim-matrix.md:25 renders the false row verbatim. Minor citation corrections: the cff `doi:` line is :18 (finding said :24; the identifiers block spans :21-27), and the claim matrix is at :184-199 rather than ~237-252 — mechanism unchanged. Checked for mitigating gates/tests: the mode guard at release_metadata.py:236 (`mode == "public-archive" and not payload["archive"]["doi_present"]`) uses the correct _has_doi result but does nothing about the static claim-matrix text; no test asserts the claim matrix agrees with payload['archive'], so regeneration reproduces the contradiction identically. Severity medium is fair: the self-described honesty surface ships a factually false evidence line ('contain no DOI') while a real DOI exists, but the machine-readable archive.status field is correct and the contradiction is cosmetic-to-misleading rather than a broken execution contract. The proposed fix (derive the row from payload['archive']) is consistent with the file's own architecture.
<!-- PR and issue links are added to the Tracking field after filing. -->