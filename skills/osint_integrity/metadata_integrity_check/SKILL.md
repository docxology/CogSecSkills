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

## Failure modes and negative controls

- Metadata Integrity Check: treating a single field such as a GPS coordinate or timestamp as definitive when all such fields are trivially editable, reading absent metadata as proof of tampering despite routine platform stripping, or reporting a clean check as authentication when it is only a necessary but insufficient condition for genuine evidence.
- Metadata Integrity Check: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Metadata Integrity Check: reporting the metadata assessment without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Metadata Integrity Check outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the metadata assessment from Metadata Integrity Check into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Metadata Integrity Check to verify supplied claims, media, sources, or datasets with documented public-source methods with media file or post, and claimed provenance' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- metadata absence is informative — platform stripping on upload is routine, but deliberate pre-upload stripping is a manipulation signal; explain why fields are missing
- cross-check multiple independent fields: a spoofed GPS coordinate rarely matches an authentic device model firmware timestamp
- platform-assigned timestamps are more tamper-resistant than embedded EXIF but are still imperfect — both must be examined
- internal consistency across metadata fields is evidence of authenticity; any single field in isolation is insufficient
