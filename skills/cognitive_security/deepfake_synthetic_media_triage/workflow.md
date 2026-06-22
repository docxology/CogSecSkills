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
- For Deepfake & Synthetic Media Triage, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Deepfake & Synthetic Media Triage, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Deepfake & Synthetic Media Triage recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Deepfake & Synthetic Media Triage: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Deepfake & Synthetic Media Triage: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Deepfake & Synthetic Media Triage: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Deepfake & Synthetic Media Triage cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Deepfake & Synthetic Media Triage should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Deepfake & Synthetic Media Triage, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Deepfake & Synthetic Media Triage, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Deepfake & Synthetic Media Triage, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Deepfake & Synthetic Media Triage failure: mistaking persuasive resonance for verified harm or intent.
- Deepfake & Synthetic Media Triage failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Deepfake & Synthetic Media Triage failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Deepfake & Synthetic Media Triage to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Deepfake & Synthetic Media Triage into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Deepfake & Synthetic Media Triage to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not claim evidentiary or forensic-grade conclusions — always label the output as a triage assessment with explicit confidence bounds
- do not declare media 'authentic' based solely on absence of observable tell-tales — advanced synthetic media may not show current-generation artifacts
- do not treat a single anomaly as conclusive evidence of manipulation — require a pattern or a strong provenance disconfirmation
- do not name or assert the identity of persons depicted in the media as part of the triage — identity claims require separate verification
- do not provide an assessment that could be used to certify media for legal proceedings — triage outputs are not admissible forensic evidence

## AGEINT upstream
`docs/ageint/cognitive-security.md`
