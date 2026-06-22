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

- For Image & Media Forensics Triage, tie every line of the triage report to concrete evidence — the reverse-image hit and its date, the specific compression or cloning artifact observed, and the contextual feature that matches or contradicts the claimed time and place — and label a clean triage as no-red-flags-found rather than authenticated, because triage is a filter and unsupported escalation or acceptance is a judgment, not a finding.
- For Image & Media Forensics Triage, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the triage report.
- Before recommending any Image & Media Forensics Triage action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Image & Media Forensics Triage: the reuse verdict rests on reverse-image and archive results that pin earlier or unrelated appearances, editing red flags are interpreted against the media's re-encoding history rather than in isolation, the context-collapse check confirms the visual is plausible for the claimed time and place, and no unresolved anomaly would change the recommended disposition.
- Medium for Image & Media Forensics Triage: the triage report is plausible, but one important media item source, comparison case, or alternative explanation remains incomplete.
- Low for Image & Media Forensics Triage: the triage report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Image & Media Forensics Triage cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Image & Media Forensics Triage, use only authorized media item, accompanying claim, and source account, public or source-approved records, and caller-provided context needed for the defensive task.
- For Image & Media Forensics Triage, minimize person-level detail in the triage report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Image & Media Forensics Triage, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Image & Media Forensics Triage: treating a single clean reverse-image result as proof of authenticity when the file may simply be unindexed, reading ELA artifacts in isolation from platform re-compression, or skipping the context-collapse check so recycled authentic media passes as original, mistaking the absence of found red flags for verified authenticity.
- Image & Media Forensics Triage: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Image & Media Forensics Triage: reporting the triage report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Image & Media Forensics Triage outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the triage report from Image & Media Forensics Triage into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Image & Media Forensics Triage to verify supplied claims, media, sources, or datasets with documented public-source methods with media item, accompanying claim, and source account' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- triage is a filter, not a proof — a clean triage result means no red flags found, not that the media is authentic
- reverse-image search is the highest-yield first step: reuse is far more common than fabrication
- error-level analysis surfaces compression inconsistencies but produces false positives with social-media re-encoding — interpret cautiously
- context collapse is cognitively harder to detect than pixel manipulation — invest time in whether the claim matches what the image physically shows
