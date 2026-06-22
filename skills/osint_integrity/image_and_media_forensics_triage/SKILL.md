---
name: osint_integrity.image_and_media_forensics_triage
description: Triage media for reuse, editing, and context-collapse before treating it as evidence.
---

# Image & Media Forensics Triage

Image and media forensics triage is a rapid, systematic workflow for assessing whether a photograph, video, or audio clip has been re-used from an unrelated context, digitally edited, or stripped of the context needed to interpret it honestly. It applies reverse-image search, error-level analysis (ELA), metadata inspection, and contextual plausibility checks before any piece of media is admitted as evidence in an analysis. The goal is to surface red flags quickly — a full forensic examination is triggered only when triage finds anomalies.

## When to use

- a piece of media is being considered as evidence before publishing, citing, or acting on a claim
- social media sharing volume is anomalously high and there is a strong emotional valence — conditions that correlate with recycled or manipulated content
- the source is unknown or has low prior credibility
- the claimed date and location are significant to the narrative and need independent corroboration
- analysts suspect context collapse — real media taken from a different event or location

## What it produces

- a reuse verdict: whether the image appears in earlier, unrelated contexts via reverse-image search
- a list of editing red flags: inconsistent noise patterns, compression artifacts, lighting discontinuities, or cloning signatures
- a context-collapse assessment: whether the visual content is plausible for the claimed time and place
- a recommended disposition: accept as candidate evidence, escalate to deep forensic review, or reject

## Defensive boundary

Use Image & Media Forensics Triage only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Image & Media Forensics Triage to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

- For Image & Media Forensics Triage, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Image & Media Forensics Triage, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Image & Media Forensics Triage recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Image & Media Forensics Triage: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Image & Media Forensics Triage: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Image & Media Forensics Triage: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Image & Media Forensics Triage cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Image & Media Forensics Triage should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Image & Media Forensics Triage, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Image & Media Forensics Triage, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Image & Media Forensics Triage, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Image & Media Forensics Triage failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Image & Media Forensics Triage failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Image & Media Forensics Triage failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Image & Media Forensics Triage to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Image & Media Forensics Triage into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Image & Media Forensics Triage to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- triage is a filter, not a proof — a clean triage result means no red flags found, not that the media is authentic
- reverse-image search is the highest-yield first step: reuse is far more common than fabrication
- error-level analysis surfaces compression inconsistencies but produces false positives with social-media re-encoding — interpret cautiously
- context collapse is cognitively harder to detect than pixel manipulation — invest time in whether the claim matches what the image physically shows
