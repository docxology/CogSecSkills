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
- For Chain-of-Custody Documentation, tie each custody log, and integrity summary claim to concrete evidence from the specific evidence items, collection context, and prior custody log item, source excerpt, observation, or command result that supports it.
- For Chain-of-Custody Documentation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the custody log.
- Before recommending any Chain-of-Custody Documentation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Chain-of-Custody Documentation: the custody log is supported by multiple independent source records, custody notes, metadata, corroborating references, and contradiction logs; inventory evidence items and compute and record hashes checks agree, and no unresolved contradiction would change the result.
- Medium for Chain-of-Custody Documentation: the custody log is plausible, but one important evidence items source, comparison case, or alternative explanation remains incomplete.
- Low for Chain-of-Custody Documentation: the custody log rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Chain-of-Custody Documentation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Chain-of-Custody Documentation, use only authorized evidence items, collection context, and prior custody log, public or source-approved records, and caller-provided context needed for the defensive task.
- For Chain-of-Custody Documentation, minimize person-level detail in the custody log; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Chain-of-Custody Documentation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Chain-of-Custody Documentation: treating evidence items as complete when inventory evidence items and compute and record hashes checks or contradictory evidence are missing.
- Chain-of-Custody Documentation: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Chain-of-Custody Documentation: reporting the custody log without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Chain-of-Custody Documentation outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the custody log from Chain-of-Custody Documentation into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Chain-of-Custody Documentation to verify supplied claims, media, sources, or datasets with documented public-source methods with evidence items, collection context, and prior custody log' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not backfill hashes after files have been processed, converted, or shared — only original-capture hashes have integrity value
- Do not omit transfer events on the assumption they are routine — every hand-off is a potential integrity break
- Do not declare custody complete when there are undocumented time gaps; acknowledge gaps explicitly in the integrity summary

## AGEINT upstream
`docs/ageint/osint-integrity.md`
