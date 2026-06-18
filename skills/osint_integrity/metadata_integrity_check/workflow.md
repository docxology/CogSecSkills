# Workflow — Metadata Integrity Check

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract all metadata fields (read)
Extract the full metadata payload using appropriate tooling (ExifTool for files; platform API or third-party inspection tools for posts). Capture embedded fields (EXIF DateTimeOriginal, GPS coordinates, CameraModel, Software, Author, ModifyDate) and platform-assigned fields (upload timestamp, account creation date, server-generated ID). Record which fields are present, which are absent, and which were added by the platform rather than the originating device.

## Step 2 — Assess internal and external consistency (reason)
Check for internal consistency: do DateTimeOriginal, GPS timestamp, and file ModifyDate tell the same story? Does the CameraModel match the software version? Does the GPS coordinate match the claimed location? Then check external consistency against the claimed provenance: does the embedded date match when the event is alleged to have occurred? Flag any field that contradicts the claim or another field. Assess each inconsistency for whether it is better explained by legitimate causes (platform re-encoding, timezone conversion error, device clock drift) or by manipulation.

## Step 3 — Assign confidence ratings and verdict (reason, write)
For each key metadata field, assign a confidence rating: corroborates claim, neutral (consistent but not distinctive), contradicts claim, or absent (stripped or never present). Assess the overall spoofing risk: single-field edits are common; coherent multi-field spoofing is harder and rarer. Render an overall integrity verdict — consistent, inconsistent, or insufficient — with a plain-language narrative explaining what the metadata establishes and what additional corroboration is required before evidential use.

## Anti-criteria (must NOT happen)
- do not treat any single metadata field as definitive — GPS coordinates, timestamps, and author fields are all trivially editable
- do not treat absent metadata as proof of tampering — routine platform stripping removes EXIF from virtually all social media uploads
- do not skip the external consistency check: internally coherent metadata can still contradict external evidence about when or where an event occurred
- do not report a clean metadata check as authentication — it is a necessary but insufficient condition for accepting a file as genuine evidence

## AGEINT upstream
`docs/ageint/osint-integrity.md`
