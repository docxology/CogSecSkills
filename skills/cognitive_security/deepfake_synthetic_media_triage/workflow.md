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

## Evidence requirements
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

## Failure modes
- Deepfake & Synthetic Media Triage: declaring media authentic from the mere absence of current-generation artifacts, treating one anomaly as conclusive, skipping the provenance trace, or stating a definitive forensic verdict, so a triage-level judgment is mistaken for an evidentiary conclusion that advanced synthetic media could defeat.
- Deepfake & Synthetic Media Triage: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Deepfake & Synthetic Media Triage: reporting the triage report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Deepfake & Synthetic Media Triage outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the triage report from Deepfake & Synthetic Media Triage into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Deepfake & Synthetic Media Triage to assess supplied material for manipulation indicators and recommend resilience measures with media artifact, claim context, and available metadata' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not claim evidentiary or forensic-grade conclusions — always label the output as a triage assessment with explicit confidence bounds
- do not declare media 'authentic' based solely on absence of observable tell-tales — advanced synthetic media may not show current-generation artifacts
- do not treat a single anomaly as conclusive evidence of manipulation — require a pattern or a strong provenance disconfirmation
- do not name or assert the identity of persons depicted in the media as part of the triage — identity claims require separate verification
- do not provide an assessment that could be used to certify media for legal proceedings — triage outputs are not admissible forensic evidence

## AGEINT upstream
`docs/ageint/cognitive-security.md`
