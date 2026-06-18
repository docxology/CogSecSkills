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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- triage is a filter, not a proof — a clean triage result means no red flags found, not that the media is authentic
- reverse-image search is the highest-yield first step: reuse is far more common than fabrication
- error-level analysis surfaces compression inconsistencies but produces false positives with social-media re-encoding — interpret cautiously
- context collapse is cognitively harder to detect than pixel manipulation — invest time in whether the claim matches what the image physically shows
