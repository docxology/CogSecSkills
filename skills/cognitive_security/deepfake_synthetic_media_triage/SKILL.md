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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- triage is not forensics: always state that this is a non-evidentiary assessment and label confidence accurately
- no single tell-tale is conclusive — a suspicion rating requires a pattern of anomalies or a strong provenance disconfirmation
- provenance is often more diagnostic than visual tell-tales — where and when the media first appeared often exposes synthetic origin faster than pixel-level analysis
- contextual implausibility (the event couldn't have happened this way) can be more reliable than technical tell-tales that improve with each model generation
- absence of tell-tales does not establish authenticity — state explicitly what cannot be ruled out at triage level
- the C2PA/Content Credentials ecosystem is the emergent positive-provenance standard; check for it but do not treat absence as manipulation evidence
