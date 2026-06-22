# Workflow — Image & Media Forensics Triage

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Capture claims and metadata (read)
Record the precise claim the media is being used to support: what event, where, and when. Extract any available metadata (EXIF, platform-assigned creation date). Note the publishing account and platform. These baseline facts anchor the triage so each check has a specific claim to test against.

## Step 2 — Run reverse-image and archive search (web)
Submit the image or keyframes to reverse-image search engines (Google Images, TinEye, Yandex Images) and media-specific databases (InVID/WeVerify, PimEyes if person-centric). Record all earlier appearances. If the image predates the claimed event or appears in a clearly different context, flag as likely reuse or context collapse.

## Step 3 — Apply editing and context triage (reason)
Assess editing artifacts: examine compression consistency across image regions (ELA heuristic), look for cloning, inconsistent shadow direction or lighting, mismatched depth of field, or inconsistent noise grain. For video, check for frame-rate anomalies or audio sync errors. Separately assess plausibility: does the vegetation, weather, building style, or crowd clothing match the claimed time and place? Flag any inconsistency as a red flag.

## Step 4 — Assign triage verdict and disposition (reason, write)
Synthesize all findings: reuse result, editing red flags, and context-plausibility assessment. Assign a triage confidence tier and recommend a disposition: (1) Accept as candidate — no red flags found, treat as provisional evidence subject to corroboration; (2) Escalate — anomalies detected, refer for deep forensic analysis before any evidentiary use; (3) Reject — confirmed earlier appearance in unrelated context, or physical inconsistencies that cannot be reconciled with the claim. Document findings in the triage report.

## Evidence requirements
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

## Failure modes
- Image & Media Forensics Triage failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Image & Media Forensics Triage failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Image & Media Forensics Triage failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Image & Media Forensics Triage to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Image & Media Forensics Triage into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Image & Media Forensics Triage to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat a single clean reverse-image result as proof of authenticity — the image may simply not be indexed yet
- do not interpret ELA red flags in isolation from re-encoding history — social media platforms re-compress on upload, creating artifacts that mimic editing signatures
- do not skip the context-collapse check in favor of pixel-level analysis — recycled authentic images are the dominant manipulation tactic, not fabricated deepfakes
- do not accept media as evidence without documenting which triage steps were completed and what each found

## AGEINT upstream
`docs/ageint/osint-integrity.md`
