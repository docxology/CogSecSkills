---
name: osint_integrity.metadata_integrity_check
description: Use and sanity-check file/post metadata while accounting for stripping and spoofing.
---

# Metadata Integrity Check

Metadata integrity check extracts and critically evaluates embedded file and post metadata — EXIF, XMP, IPTC, platform timestamps, author fields, device identifiers — while explicitly accounting for the fact that metadata can be stripped, altered, or spoofed. The technique treats metadata as a corroborating signal rather than ground truth: consistent metadata raises confidence, but inconsistent or absent metadata must be explained before any evidential use. It is routinely applied in OSINT, legal discovery, and journalism verification workflows.

## When to use

- a file or image is submitted as evidence and its origin, date, or authorship needs verification
- a document is suspected of having been altered or back-dated
- forensic chain-of-custody requirements mandate metadata provenance documentation
- metadata has been stripped or is absent and the reason for absence must be assessed
- platform-assigned metadata (tweet timestamp, upload date) needs cross-referencing against embedded file metadata

## What it produces

- a field-by-field breakdown of all recoverable metadata with source (embedded vs. platform-assigned)
- an internal consistency check: do date, GPS, device model, software version, and author fields cohere?
- an external consistency check: does the metadata match the claimed provenance?
- a spoofing and stripping risk assessment for each key field
- an overall integrity verdict: consistent, inconsistent, or insufficient data

## Defensive boundary

Use Metadata Integrity Check only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Metadata Integrity Check to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

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

## Failure modes and negative controls

- Metadata Integrity Check failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Metadata Integrity Check failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Metadata Integrity Check failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Metadata Integrity Check to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Metadata Integrity Check into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Metadata Integrity Check to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- metadata absence is informative — platform stripping on upload is routine, but deliberate pre-upload stripping is a manipulation signal; explain why fields are missing
- cross-check multiple independent fields: a spoofed GPS coordinate rarely matches an authentic device model firmware timestamp
- platform-assigned timestamps are more tamper-resistant than embedded EXIF but are still imperfect — both must be examined
- internal consistency across metadata fields is evidence of authenticity; any single field in isolation is insufficient
