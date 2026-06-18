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

## Anti-criteria (must NOT happen)
- do not treat a single clean reverse-image result as proof of authenticity — the image may simply not be indexed yet
- do not interpret ELA red flags in isolation from re-encoding history — social media platforms re-compress on upload, creating artifacts that mimic editing signatures
- do not skip the context-collapse check in favor of pixel-level analysis — recycled authentic images are the dominant manipulation tactic, not fabricated deepfakes
- do not accept media as evidence without documenting which triage steps were completed and what each found

## AGEINT upstream
`docs/ageint/osint-integrity.md`
