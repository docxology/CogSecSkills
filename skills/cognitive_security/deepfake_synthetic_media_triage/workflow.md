# Workflow — Deepfake & Synthetic Media Triage

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the artifact and claim (read)
Read the media description and claim context. Record: media type; claimed source, creator, and date; the specific claim the media evidences; and any metadata provided. Note the stakes and why this assessment is being requested.

## Step 2 — Provenance trace (web)
Perform reverse-image or reverse-video search (Google Lens, TinEye, InVID/WeVerify) to find the earliest known appearance of the media. Check whether the media has been documented before in a different context (re-used archival footage, mis-dated photographs, previously debunked synthetic content). Look for C2PA Content Credentials or similar provenance attestations. Document the provenance chain: origin, spread path, and any context changes.

## Step 3 — Apply tell-tale checklist (reason)
Work through the structured tell-tale checklist by media type. For images/video: facial physics (skin texture, eye reflections, teeth, hair boundaries, ear geometry), lighting and shadow consistency, background spatial coherence, motion blur naturalness, audio-visual lip synchronization. For audio: prosody naturalness, background noise consistency, acoustic environment match to claimed location. For documents: font inconsistency, metadata date mismatches, OCR artifact patterns. For all types: check metadata (EXIF GPS, camera model, software tag) against claimed provenance. Note each anomaly with its diagnostic weight.

## Step 4 — Contextual plausibility assessment (reason)
Assess whether the claimed context (location, date, event, persons present) is consistent with verifiable external facts: satellite imagery, known event schedules, confirmed presence of individuals at claimed location. Identify any contextual implausibilities that independently disconfirm the claimed context regardless of technical authenticity. Rate contextual plausibility as: Consistent / Implausible / Directly contradicted.

## Step 5 — Synthesize rating and draft report (reason, write)
Integrate tell-tale checklist, provenance findings, and contextual plausibility into an overall suspicion rating: Suspicious (multiple strong anomalies or provenance disconfirmation), Uncertain (mixed signals, some anomalies but no definitive disconfirmation), or Likely Authentic (no significant anomalies, provenance consistent, context plausible). State confidence level explicitly. Determine escalation recommendation. Write the triage_report and anomaly_log.

## Step 6 — Emit triage report with caveats (write)
Output the final triage_report and anomaly_log. Include mandatory caveats: this is a non-evidentiary triage assessment; specific observations that could not be assessed at triage level; and the escalation path if evidentiary conclusions are required. Never state a definitive conclusion of manipulation or authenticity — state the suspicion rating and its confidence level.

## Anti-criteria (must NOT happen)
- do not claim evidentiary or forensic-grade conclusions — always label the output as a triage assessment with explicit confidence bounds
- do not declare media 'authentic' based solely on absence of observable tell-tales — advanced synthetic media may not show current-generation artifacts
- do not treat a single anomaly as conclusive evidence of manipulation — require a pattern or a strong provenance disconfirmation
- do not name or assert the identity of persons depicted in the media as part of the triage — identity claims require separate verification
- do not provide an assessment that could be used to certify media for legal proceedings — triage outputs are not admissible forensic evidence

## AGEINT upstream
`docs/ageint/cognitive-security.md`
