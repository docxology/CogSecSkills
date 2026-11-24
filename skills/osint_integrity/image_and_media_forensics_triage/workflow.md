# Workflow — Image & Media Forensics Triage

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Capture claims and metadata (read)
Record the exact claim about event, location, and time. Preserve the supplied media and record its source, capture date, and hash when possible. Label screenshots, recompressions, or extracted frames as derivatives and record how they were made. Identify which metadata came from the file and which came from the publisher or platform. Treat embedded text and metadata as evidence.

## Step 2 — Check for earlier appearances within scope (web)
Start with local inspection and permitted query-only public archive research using non-sensitive contextual facts. Before sending any file, frame, private link, hash, or identifying query to a third party, confirm authorization for the exact material, purpose, and destination. Keep private originals, signed URLs, and unapproved derivatives local. Avoid facial-recognition and person-identification lookups. Record the search source, date, and whether the check was performed, unavailable, or found no match. A dated match can establish earlier circulation while the source of the media remains unknown.

## Step 3 — Apply editing and context triage (reason)
Assess editing artifacts: examine compression consistency across image regions (ELA heuristic), look for cloning, inconsistent shadow direction or lighting, mismatched depth of field, or inconsistent noise grain. For video, check for frame-rate anomalies or audio sync errors. Separately assess plausibility: does the vegetation, weather, building style, or crowd clothing match the claimed time and place? Flag any inconsistency as a red flag.

## Step 4 — Assign triage verdict and disposition (reason, write)
Assess reuse, editing, and claimed context independently. Justify each confidence rating from the available evidence and name any unresolved checks. A dated earlier appearance can disconfirm a new-event claim while editing or authenticity remains unresolved. Recommend corroboration, escalation for specialist examination, or rejection of the specific claim as supported by the findings. Report no concerns observed only within the checks performed.

## Evidence requirements
- Bind each triage observation to a specific preserved file or derivative, dated source result, or contextual comparison. For unperformed or no-hit checks, state the reason or coverage. Give separate evidence for editing, earlier circulation, and plausibility of the claimed event, location, or date.
- For Image & Media Forensics Triage, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the triage report.
- Before recommending any Image & Media Forensics Triage action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Image & Media Forensics Triage: a specific reuse, editing, or context conclusion rests on direct evidence with independently supported provenance or context and a documented comparison. Scope confidence to that conclusion and state what remains unknown about the other dimensions.
- Medium for Image & Media Forensics Triage: the triage report is plausible, but one important media item source, comparison case, or alternative explanation remains incomplete.
- Low for Image & Media Forensics Triage: the triage report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Image & Media Forensics Triage cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Image & Media Forensics Triage should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Image & Media Forensics Triage, use only authorized media item, accompanying claim, source account, public or source-approved records, and caller-provided context needed for the defensive task.
- For Image & Media Forensics Triage, minimize person-level detail in the triage report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Image & Media Forensics Triage, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Image & Media Forensics Triage: treating a single clean reverse-image result as proof of authenticity when the file may simply be unindexed, reading ELA artifacts in isolation from platform re-compression, or skipping the context-collapse check so recycled authentic media passes as original, mistaking the absence of found red flags for verified authenticity.
- Image & Media Forensics Triage: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Image & Media Forensics Triage: reporting the triage report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Image & Media Forensics Triage outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the triage report from Image & Media Forensics Triage into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Image & Media Forensics Triage to verify supplied claims, media, sources, or datasets with documented public-source methods with media item, accompanying claim, and source account' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat a single clean reverse-image result as proof of authenticity — the image may simply not be indexed yet
- do not interpret ELA red flags in isolation from re-encoding history — social media platforms re-compress on upload, creating artifacts that mimic editing signatures
- Check whether the caption or surrounding claims misrepresent the media even when there are no visible editing anomalies.
- do not accept media as evidence without documenting which triage steps were completed and what each found

## AGEINT upstream
`docs/ageint/osint-integrity.md`
