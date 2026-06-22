---
name: osint_integrity.geolocation_verification
description: Confirm where imagery was taken using corroborating geographic features (defensive OSINT).
---

# Geolocation Verification

Geolocation verification cross-references visual and contextual clues in imagery — terrain, vegetation, architecture, shadows, signage, infrastructure — against authoritative mapping data to confirm or refute a claimed location. It is a defensive OSINT discipline used to detect context-collapsed or fabricated imagery before it is treated as evidence. The technique draws on sun-angle computation, map comparison, satellite imagery, and street-level reference data. It provides an independently verifiable anchor for where and when a visual was plausibly captured.

## When to use

- an image or video is being considered as evidence of a specific event at a specific place
- there is a claim that footage shows a location that it may not depict
- context collapse is suspected — older or unrelated imagery being circulated with a new narrative
- a media organization or analyst needs to independently confirm a visual's provenance before publication

## What it produces

- a probable location fix with latitude/longitude estimate or named area, plus a confidence tier (confirmed / likely / inconclusive / contradicted)
- a list of corroborating features used (terrain shape, building style, road markings, vegetation, signage)
- a note on any features that contradict the claimed location
- a shadow-angle cross-check result where the sun position can be computed from the claimed date/time

## Defensive boundary

Use Geolocation Verification only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Geolocation Verification to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

- For Geolocation Verification, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Geolocation Verification, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Geolocation Verification recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Geolocation Verification: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Geolocation Verification: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Geolocation Verification: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Geolocation Verification cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Geolocation Verification should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Geolocation Verification, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Geolocation Verification, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Geolocation Verification, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Geolocation Verification failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Geolocation Verification failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Geolocation Verification failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Geolocation Verification to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Geolocation Verification into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Geolocation Verification to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- build from fixed landmarks outward — unique terrain, infrastructure, or signage constrains the search space before general landscape features
- never anchor to the claimed location first; start landmark-agnostic and let features converge
- shadow angle and vegetation season are independent physical constraints — a mismatched shadow falsifies the claimed date as strongly as it falsifies the location
- document every reference source and feature match so the conclusion is reproducible
