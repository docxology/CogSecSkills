# Workflow — Metadata Integrity Check

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract all metadata fields (read)
Extract the full metadata payload using appropriate tooling (ExifTool for files; platform API or third-party inspection tools for posts). Capture embedded fields (EXIF DateTimeOriginal, GPS coordinates, CameraModel, Software, Author, ModifyDate) and platform-assigned fields (upload timestamp, account creation date, server-generated ID). Record which fields are present, which are absent, and which were added by the platform rather than the originating device.

## Step 2 — Assess internal and external consistency (reason)
Check for internal consistency: do DateTimeOriginal, GPS timestamp, and file ModifyDate tell the same story? Does the CameraModel match the software version? Does the GPS coordinate match the claimed location? Then check external consistency against the claimed provenance: does the embedded date match when the event is alleged to have occurred? Flag any field that contradicts the claim or another field. Assess each inconsistency for whether it is better explained by legitimate causes (platform re-encoding, timezone conversion error, device clock drift) or by manipulation.

## Step 3 — Assign confidence ratings and verdict (reason, write)
For each key metadata field, assign a confidence rating: corroborates claim, neutral (consistent but not distinctive), contradicts claim, or absent (stripped or never present). Assess the overall spoofing risk: single-field edits are common; coherent multi-field spoofing is harder and rarer. Render an overall integrity verdict — consistent, inconsistent, or insufficient — with a plain-language narrative explaining what the metadata establishes and what additional corroboration is required before evidential use.

## Evidence requirements
- For Metadata Integrity Check, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Metadata Integrity Check, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Metadata Integrity Check recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Metadata Integrity Check: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Metadata Integrity Check: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Metadata Integrity Check: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Metadata Integrity Check cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Metadata Integrity Check should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Metadata Integrity Check, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Metadata Integrity Check, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Metadata Integrity Check, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Metadata Integrity Check failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Metadata Integrity Check failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Metadata Integrity Check failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Metadata Integrity Check to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Metadata Integrity Check into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Metadata Integrity Check to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat any single metadata field as definitive — GPS coordinates, timestamps, and author fields are all trivially editable
- do not treat absent metadata as proof of tampering — routine platform stripping removes EXIF from virtually all social media uploads
- do not skip the external consistency check: internally coherent metadata can still contradict external evidence about when or where an event occurred
- do not report a clean metadata check as authentication — it is a necessary but insufficient condition for accepting a file as genuine evidence

## AGEINT upstream
`docs/ageint/osint-integrity.md`
