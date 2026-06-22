# Workflow — Metadata Integrity Check

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract all metadata fields (read)
Extract the full metadata payload using appropriate tooling (ExifTool for files; platform API or third-party inspection tools for posts). Capture embedded fields (EXIF DateTimeOriginal, GPS coordinates, CameraModel, Software, Author, ModifyDate) and platform-assigned fields (upload timestamp, account creation date, server-generated ID). Record which fields are present, which are absent, and which were added by the platform rather than the originating device.

## Step 2 — Assess internal and external consistency (reason)
Check for internal consistency: do DateTimeOriginal, GPS timestamp, and file ModifyDate tell the same story? Does the CameraModel match the software version? Does the GPS coordinate match the claimed location? Then check external consistency against the claimed provenance: does the embedded date match when the event is alleged to have occurred? Flag any field that contradicts the claim or another field. Assess each inconsistency for whether it is better explained by legitimate causes (platform re-encoding, timezone conversion error, device clock drift) or by manipulation.

## Step 3 — Assign confidence ratings and verdict (reason, write)
For each key metadata field, assign a confidence rating: corroborates claim, neutral (consistent but not distinctive), contradicts claim, or absent (stripped or never present). Assess the overall spoofing risk: single-field edits are common; coherent multi-field spoofing is harder and rarer. Render an overall integrity verdict — consistent, inconsistent, or insufficient — with a plain-language narrative explaining what the metadata establishes and what additional corroboration is required before evidential use.

## Evidence requirements
- For Metadata Integrity Check, bind every field rating and the overall verdict to concrete evidence — the extracted EXIF, XMP, or platform value, its source as embedded versus platform-assigned, and the specific cross-field or external comparison that supports or contradicts the claim — and where a field is absent, document the most plausible cause rather than presenting an unexplained gap as either authenticity or tampering.
- For Metadata Integrity Check, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the metadata assessment.
- Before recommending any Metadata Integrity Check action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Metadata Integrity Check: multiple independent fields such as DateTimeOriginal, GPS, device model, and platform timestamp cohere internally and match the claimed provenance, any absence is explained by routine platform stripping rather than deliberate manipulation, and no unresolved field-level contradiction would change the integrity verdict.
- Medium for Metadata Integrity Check: the metadata assessment is plausible, but one important media file or post source, comparison case, or alternative explanation remains incomplete.
- Low for Metadata Integrity Check: the metadata assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Metadata Integrity Check cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Metadata Integrity Check, use only authorized media file or post, and claimed provenance, public or source-approved records, and caller-provided context needed for the defensive task.
- For Metadata Integrity Check, minimize person-level detail in the metadata assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Metadata Integrity Check, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Metadata Integrity Check: treating a single field such as a GPS coordinate or timestamp as definitive when all such fields are trivially editable, reading absent metadata as proof of tampering despite routine platform stripping, or reporting a clean check as authentication when it is only a necessary but insufficient condition for genuine evidence.
- Metadata Integrity Check: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Metadata Integrity Check: reporting the metadata assessment without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Metadata Integrity Check outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the metadata assessment from Metadata Integrity Check into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Metadata Integrity Check to verify supplied claims, media, sources, or datasets with documented public-source methods with media file or post, and claimed provenance' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat any single metadata field as definitive — GPS coordinates, timestamps, and author fields are all trivially editable
- do not treat absent metadata as proof of tampering — routine platform stripping removes EXIF from virtually all social media uploads
- do not skip the external consistency check: internally coherent metadata can still contradict external evidence about when or where an event occurred
- do not report a clean metadata check as authentication — it is a necessary but insufficient condition for accepting a file as genuine evidence

## AGEINT upstream
`docs/ageint/osint-integrity.md`
