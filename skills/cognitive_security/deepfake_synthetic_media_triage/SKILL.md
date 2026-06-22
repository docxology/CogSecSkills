---
name: cognitive_security.deepfake_synthetic_media_triage
description: Triage suspected synthetic media for tell-tales and provenance signals (defensive, non-forensic).
---

# Deepfake & Synthetic Media Triage

Deepfake and Synthetic Media Triage is a structured first-pass assessment procedure for suspected AI-generated, manipulated, or misrepresented media — images, video, audio, and documents. It applies a layered checklist of observable tell-tales, provenance signals, and contextual inconsistencies to rapidly determine whether a piece of media warrants escalation to full forensic analysis or can be assessed with sufficient confidence at triage level. The technique is explicitly non-forensic: it does not claim evidentiary-grade conclusions but instead produces a calibrated suspicion rating, a prioritized list of anomaly observations, and a provenance chain reconstruction using open-source signals. It is defensive and educational, designed for analysts, journalists, educators, and information-environment practitioners who need to triage at volume without laboratory tools.

## When to use

- when a piece of media is being used to support an important factual claim and its authenticity is in question
- when operating at volume in an information environment where full forensic analysis of every item is not feasible
- when advising a newsroom, analyst, or policy-maker who needs a rapid credibility assessment before acting on media-evidenced claims
- when training analysts or journalists to recognize synthetic media tell-tales as part of a media literacy program
- when a suspected deepfake has surfaced in a high-stakes context (election, conflict, public health) and a rapid triage is needed before escalation decisions

## What it produces

- a structured tell-tale checklist assessment covering: facial/body physics anomalies (for images/video), audio-visual synchronization, background and shadow consistency, EXIF and metadata integrity, provenance chain (where did this originate and how did it travel)
- a reverse-search provenance trace identifying earliest known appearances of the media
- contextual plausibility assessment: does the media's claimed context (location, time, event) cohere with verifiable external facts
- a calibrated suspicion rating — Suspicious / Uncertain / Likely Authentic — with an explicit confidence level and the specific observations driving it
- a clear escalation recommendation: whether laboratory forensic analysis, platform reporting, or expert consultation is warranted

## Defensive boundary

Use Deepfake & Synthetic Media Triage only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Deepfake & Synthetic Media Triage to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Deepfake & Synthetic Media Triage, tie the suspicion rating to concrete evidence — specific tell-tale observations with diagnostic weight, reverse-search provenance findings, metadata checks, and contextual cross-references against verifiable external facts — and state explicitly what could not be assessed at triage level and what escalation an evidentiary conclusion would require.
- For Deepfake & Synthetic Media Triage, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the triage report.
- Before recommending any Deepfake & Synthetic Media Triage action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Deepfake & Synthetic Media Triage: the suspicion rating rests on a pattern of independently observed anomalies or a strong provenance disconfirmation rather than any single tell-tale, the reverse-search trace and contextual plausibility assessment corroborate the rating, and no unresolved contradiction would change the escalation recommendation — while the output remains explicitly non-evidentiary.
- Medium for Deepfake & Synthetic Media Triage: the triage report is plausible, but one important media artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Deepfake & Synthetic Media Triage: the triage report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Deepfake & Synthetic Media Triage cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Deepfake & Synthetic Media Triage, use only authorized media artifact, claim context, and available metadata, public or source-approved records, and caller-provided context needed for the defensive task.
- For Deepfake & Synthetic Media Triage, minimize person-level detail in the triage report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Deepfake & Synthetic Media Triage, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Deepfake & Synthetic Media Triage: declaring media authentic from the mere absence of current-generation artifacts, treating one anomaly as conclusive, skipping the provenance trace, or stating a definitive forensic verdict, so a triage-level judgment is mistaken for an evidentiary conclusion that advanced synthetic media could defeat.
- Deepfake & Synthetic Media Triage: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Deepfake & Synthetic Media Triage: reporting the triage report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Deepfake & Synthetic Media Triage outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the triage report from Deepfake & Synthetic Media Triage into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Deepfake & Synthetic Media Triage to assess supplied material for manipulation indicators and recommend resilience measures with media artifact, claim context, and available metadata' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- triage is not forensics: always state that this is a non-evidentiary assessment and label confidence accurately
- no single tell-tale is conclusive — a suspicion rating requires a pattern of anomalies or a strong provenance disconfirmation
- provenance is often more diagnostic than visual tell-tales — where and when the media first appeared often exposes synthetic origin faster than pixel-level analysis
- contextual implausibility (the event couldn't have happened this way) can be more reliable than technical tell-tales that improve with each model generation
- absence of tell-tales does not establish authenticity — state explicitly what cannot be ruled out at triage level
- the C2PA/Content Credentials ecosystem is the emergent positive-provenance standard; check for it but do not treat absence as manipulation evidence
