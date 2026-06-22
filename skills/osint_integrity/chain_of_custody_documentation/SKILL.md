---
name: osint_integrity.chain_of_custody_documentation
description: Document collection, handling, and hashing so evidence integrity is auditable.
---

# Chain-of-Custody Documentation

Chain-of-custody documentation records every step in the collection, transfer, and analysis of OSINT evidence — capturing who handled each item, when, by what method, and what cryptographic hashes confirm it remained unaltered. The technique adapts law-enforcement chain-of-custody principles to open-source intelligence so that findings can withstand legal, journalistic, or organizational scrutiny. Without it, adversaries and skeptics can challenge whether evidence was fabricated, tampered, or misidentified. A complete chain anchors findings in verifiable, time-stamped, hash-confirmed records.

## When to use

- Before sharing OSINT findings with legal, journalistic, or institutional decision-makers who may face adversarial challenge
- When evidence could be subpoenaed or used in formal proceedings
- After collecting from volatile sources (social media, live websites) where content may disappear or be altered
- When multiple analysts or teams handle the same artifacts across time

## What it produces

- A row-per-artifact custody table with hash, timestamps, collector identity, and tool used
- A completeness assessment flagging any gaps where handling is undocumented
- A hash manifest that allows third-party verification that files have not been altered since collection

## Defensive boundary

Use Chain-of-Custody Documentation only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Chain-of-Custody Documentation to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

- For Chain-of-Custody Documentation, bind every custody-log row and integrity-summary statement to concrete evidence — the actual collection timestamp, source identifier, computed hash, or persistent-archive record for that specific artifact — and where a handling step is undocumented, label it an explicit gap rather than presenting an unsupported entry as verified custody.
- For Chain-of-Custody Documentation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the custody log.
- Before recommending any Chain-of-Custody Documentation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Chain-of-Custody Documentation: every artifact carries an original-capture SHA-256 hash a third party can independently re-verify, each handling event is logged as its own row with collector and timestamp, and no unresolved gap or contradiction would change the conclusion that the chain is unbroken.
- Medium for Chain-of-Custody Documentation: the custody log is plausible, but one important evidence items source, comparison case, or alternative explanation remains incomplete.
- Low for Chain-of-Custody Documentation: the custody log rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Chain-of-Custody Documentation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Chain-of-Custody Documentation, use only authorized evidence items, collection context, and prior custody log, public or source-approved records, and caller-provided context needed for the defensive task.
- For Chain-of-Custody Documentation, minimize person-level detail in the custody log; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Chain-of-Custody Documentation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Chain-of-Custody Documentation: declaring custody complete when hashes were backfilled after files were processed rather than computed at capture, when transfer events were omitted as routine, or when undocumented time gaps were never acknowledged, so the log certifies integrity it cannot actually establish.
- Chain-of-Custody Documentation: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Chain-of-Custody Documentation: reporting the custody log without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Chain-of-Custody Documentation outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the custody log from Chain-of-Custody Documentation into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Chain-of-Custody Documentation to verify supplied claims, media, sources, or datasets with documented public-source methods with evidence items, collection context, and prior custody log' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Hash at the moment of collection — post-hoc hashing only proves integrity from that later moment, not from capture
- Each transfer event (person A to person B, local to cloud storage) must be logged as its own row
- Volatile web content must be archived to a persistent store (Wayback Machine, local WARC) before any hash is considered meaningful
- A gap in custody is not automatically disqualifying but must be explicitly acknowledged and explained
