---
name: osint_integrity.collection_plan_design
description: Plan ethical, scoped collection tied to specific intelligence requirements.
---

# Collection Plan Design

Collection plan design translates intelligence requirements into a disciplined, scoped, and ethically bounded OSINT collection strategy before any data is gathered. The plan specifies what information is needed and why, which open sources are in scope, what collection methods are lawful and proportionate, how data will be stored and protected, and what review checkpoints govern the effort. Establishing these parameters in advance prevents scope creep, reduces legal exposure, and ensures that collected material remains relevant to the stated analytic question. It is the upstream governance document for all subsequent OSINT work.

## When to use

- At the start of any OSINT investigation before collecting any data
- When an existing investigation risks expanding beyond its original mandate
- When the legal or ethical basis for collection is unclear or contested
- When multiple analysts or teams will contribute to a single collection effort and coordination is needed

## What it produces

- A written collection plan that can be reviewed for compliance and approved before collection begins
- A source priority matrix that guides analyst effort toward highest-yield, lowest-risk sources first
- Explicit documentation of what is out of scope, reducing later scope creep disputes

## Defensive boundary

Use Collection Plan Design only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Collection Plan Design to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

- For Collection Plan Design, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Collection Plan Design, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Collection Plan Design recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Collection Plan Design: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Collection Plan Design: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Collection Plan Design: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Collection Plan Design cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Collection Plan Design should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Collection Plan Design, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Collection Plan Design, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Collection Plan Design, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Collection Plan Design failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Collection Plan Design failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Collection Plan Design failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Collection Plan Design to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Collection Plan Design into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Collection Plan Design to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Start from the intelligence requirement, not from the available tools — collection that cannot answer the requirement wastes resources and creates liability
- State legal basis explicitly: passive observation, publicly available data, and active elicitation each carry different legal and ethical burdens
- Scope exclusions are as important as inclusions — what you will not collect defines the ethical boundary
- Build in review checkpoints so that scope can be reassessed if the analytic question evolves
