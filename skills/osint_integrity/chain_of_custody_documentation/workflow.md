# Workflow — Chain-of-Custody Documentation

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory evidence items (read)
List every artifact to be documented — files, screenshots, archived pages, raw URLs. Record the original collection timestamp, source URL, and the identity of the collector for each item.

## Step 2 — Compute and record hashes (exec)
Generate a SHA-256 (or SHA-3) hash of each file or archived page at the point of collection or at the earliest available moment. Log the hash alongside the timestamp in the custody table. For web captures, archive to a persistent store first.

## Step 3 — Identify gaps and anomalies (reason)
Review the chain for missing handling events, undocumented transfers, or time gaps where tampering could have occurred. Flag any item where the hash cannot be verified against the original collection moment.

## Step 4 — Produce custody log and integrity summary (write)
Write the structured custody table and a narrative summary that acknowledges gaps, explains their cause, and recommends remediation steps (re-collection, additional archiving, or explicit uncertainty disclosure).

## Evidence requirements
- For Chain-of-Custody Documentation, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Chain-of-Custody Documentation, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Chain-of-Custody Documentation recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Chain-of-Custody Documentation: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Chain-of-Custody Documentation: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Chain-of-Custody Documentation: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Chain-of-Custody Documentation cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Chain-of-Custody Documentation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Chain-of-Custody Documentation, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Chain-of-Custody Documentation, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Chain-of-Custody Documentation, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Chain-of-Custody Documentation failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Chain-of-Custody Documentation failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Chain-of-Custody Documentation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Chain-of-Custody Documentation to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Chain-of-Custody Documentation into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Chain-of-Custody Documentation to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not backfill hashes after files have been processed, converted, or shared — only original-capture hashes have integrity value
- Do not omit transfer events on the assumption they are routine — every hand-off is a potential integrity break
- Do not declare custody complete when there are undocumented time gaps; acknowledge gaps explicitly in the integrity summary

## AGEINT upstream
`docs/ageint/osint-integrity.md`
