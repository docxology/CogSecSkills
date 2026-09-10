# REPRO-01: .zenodo.json version (1.0.0) drifts from the 1.7.0 declared everywhere else, and the drift gate cannot see it

|Field|Value|
|---|---|
|Audit ID|`REPRO-01`|
|Lens|`REPRO`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/38) |

## Summary
`.zenodo.json` pins `"version": "1.0.0"` while pyproject.toml, CITATION.cff, codemeta.json, `src/cogsecskills/__init__.py`, and CHANGELOG.md all declare 1.7.0. The repo's own coherence gate (`cogsecskills release-metadata --check`, run in CI as "Coherence gates (no generated-file drift)") cannot see this drift because its code path never loads `.zenodo.json`. Red team adjusted severity from high to medium because the 1.0.0 value matches the actually-published Zenodo deposit (v1.0.0 version DOI) and no wrong results ship through the repo's own gates; the residual blast radius is a future Zenodo re-upload silently stamping 1.0.0 metadata on a 1.7.0 deposit.

## Evidence
- `.zenodo.json:16` — `"version": "1.0.0"` vs `pyproject.toml:9` `version = "1.7.0"` (also codemeta.json `"version": "1.7.0"`, CITATION.cff `version: 1.7.0`, `src/cogsecskills/__init__.py` `__version__ = "1.7.0"`, CHANGELOG.md top entry `## [1.7.0] - 2026-07-22`).
- `src/cogsecskills/artifacts/release_metadata.py:139-141` — `_metadata_payload` reads only:
  ```
  _read_toml(base / "pyproject.toml")
  _read_yaml(base / "CITATION.cff")
  _read_json(base / "codemeta.json")
  ```
  `.zenodo.json` is never loaded.
- `_findings()` version check compares `payload['version'] = {pyproject, citation_cff, codemeta}` only, so its 'version mismatch across pyproject, CITATION.cff, and CodeMeta' check structurally excludes `.zenodo.json`.
- `.github/workflows/ci.yml:48-55` — the 'Coherence gates (no generated-file drift)' step runs `release-metadata --check` and therefore passes despite the drift.

## Impact
The coherence gate claims "no generated-file drift" yet a citation metadata file sits a full major version behind every other version declaration. Anyone archiving the repo to Zenodo uploads v1.0.0 deposit metadata for a 1.7.0 release. Context from verification: `.zenodo.json` is deposit metadata consumed by Zenodo at upload time, and the 1.0.0 value matches the actually-published archive (v1.0.0 version DOI 10.5281/zenodo.20804586 per CITATION.cff, README, ISA.md, and docs/manuscript/S02_release_manifest.md, which explicitly notes the v1.7.0 version DOI was unavailable in that snapshot) — so the file is arguably a stale snapshot of the real 1.0.0 deposit rather than a misleading live claim. The defect remains genuine: the check should cover the file.

## Remediation
1. In `src/cogsecskills/artifacts/release_metadata.py`, extend `_metadata_payload` (~lines 139-141) to also load `.zenodo.json` (e.g. `_read_json(base / ".zenodo.json")`) and expose its version in the payload.
2. Add the Zenodo version to the cross-file version comparison in `_findings()` so 'version mismatch across pyproject, CITATION.cff, and CodeMeta' becomes '... and .zenodo.json'.
3. Bump `.zenodo.json:16` to `"version": "1.7.0"` at the next Zenodo deposit (or whenever the deposit metadata is refreshed).
4. Regenerate the release-metadata artifacts and confirm `cogsecskills release-metadata --check` still passes; the new comparison should now actually be able to fail on Zenodo version drift.

## Audit trail
- Discovered by the REPRO lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: All quoted facts confirmed: .zenodo.json pins 1.0.0 while pyproject/CITATION.cff/codemeta/__init__.py/CHANGELOG all say 1.7.0; the drift-check code path structurally excludes .zenodo.json (verified by reading _metadata_payload and _findings in full), so the gate passes despite drift. Severity downgraded from high to medium for two reasons found in context: (1) .zenodo.json is the deposit metadata consumed by Zenodo at upload time — the 1.0.0 value matches the actually-published Zenodo archive (v1.0.0 version DOI 10.5281/zenodo.20804586 per CITATION.cff, README, ISA.md, and docs/manuscript/S02_release_manifest.md which explicitly notes 'v1.7.0 version DOI unavailable in this snapshot'), so the file is arguably a stale snapshot of the real 1.0.0 deposit rather than a misleading live claim; blast radius is limited to a future Zenodo re-upload silently stamping 1.0.0 metadata on a 1.7.0 deposit. (2) No wrong results ship through the repo's own gates — the coherence gate is not lying about what it checks (its docs/generated surfaces never include .zenodo.json). Still a genuine defect: the check should cover the file, and the fix proposed (load .zenodo.json in _metadata_payload, add to version comparison, bump to 1.7.0 on next deposit) is sound. Real defect, limited blast radius → medium.
<!-- PR and issue links are added to the Tracking field after filing. -->