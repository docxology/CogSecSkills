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
- For Image & Media Forensics Triage, tie each triage report claim to concrete evidence from the specific media item, accompanying claim, and source account item, source excerpt, observation, or command result that supports it.
- For Image & Media Forensics Triage, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the triage report.
- Before recommending any Image & Media Forensics Triage action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Image & Media Forensics Triage: the triage report is supported by multiple independent source records, custody notes, metadata, corroborating references, and contradiction logs; capture claims and metadata and run reverse-image and archive search checks agree, and no unresolved contradiction would change the result.
- Medium for Image & Media Forensics Triage: the triage report is plausible, but one important media item source, comparison case, or alternative explanation remains incomplete.
- Low for Image & Media Forensics Triage: the triage report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Image & Media Forensics Triage cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Image & Media Forensics Triage, use only authorized media item, accompanying claim, and source account, public or source-approved records, and caller-provided context needed for the defensive task.
- For Image & Media Forensics Triage, minimize person-level detail in the triage report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Image & Media Forensics Triage, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Image & Media Forensics Triage: treating media item as complete when capture claims and metadata and run reverse-image and archive search checks or contradictory evidence are missing.
- Image & Media Forensics Triage: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Image & Media Forensics Triage: reporting the triage report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Image & Media Forensics Triage outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the triage report from Image & Media Forensics Triage into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Image & Media Forensics Triage to verify supplied claims, media, sources, or datasets with documented public-source methods with media item, accompanying claim, and source account' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat a single clean reverse-image result as proof of authenticity — the image may simply not be indexed yet
- do not interpret ELA red flags in isolation from re-encoding history — social media platforms re-compress on upload, creating artifacts that mimic editing signatures
- do not skip the context-collapse check in favor of pixel-level analysis — recycled authentic images are the dominant manipulation tactic, not fabricated deepfakes
- do not accept media as evidence without documenting which triage steps were completed and what each found

## AGEINT upstream
`docs/ageint/osint-integrity.md`
