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

## Failure modes and negative controls

- Chain-of-Custody Documentation failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Chain-of-Custody Documentation failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Chain-of-Custody Documentation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Chain-of-Custody Documentation to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Chain-of-Custody Documentation into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Chain-of-Custody Documentation to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Hash at the moment of collection — post-hoc hashing only proves integrity from that later moment, not from capture
- Each transfer event (person A to person B, local to cloud storage) must be logged as its own row
- Volatile web content must be archived to a persistent store (Wayback Machine, local WARC) before any hash is considered meaningful
- A gap in custody is not automatically disqualifying but must be explicitly acknowledged and explained
