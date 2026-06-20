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

- For Collection Plan Design, tie each collection plan, and source priority matrix claim to concrete evidence from the specific intelligence requirement, legal and policy constraints, and available resources item, source excerpt, observation, or command result that supports it.
- For Collection Plan Design, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the collection plan.
- Before recommending any Collection Plan Design action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Collection Plan Design: the collection plan is supported by multiple independent source records, custody notes, metadata, corroborating references, and contradiction logs; clarify the intelligence requirement and derive scope, sources, and ethical boundaries checks agree, and no unresolved contradiction would change the result.
- Medium for Collection Plan Design: the collection plan is plausible, but one important intelligence requirement source, comparison case, or alternative explanation remains incomplete.
- Low for Collection Plan Design: the collection plan rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Collection Plan Design cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Collection Plan Design, use only authorized intelligence requirement, legal and policy constraints, and available resources, public or source-approved records, and caller-provided context needed for the defensive task.
- For Collection Plan Design, minimize person-level detail in the collection plan; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Collection Plan Design, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Collection Plan Design: treating intelligence requirement as complete when clarify the intelligence requirement and derive scope, sources, and ethical boundaries checks or contradictory evidence are missing.
- Collection Plan Design: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Collection Plan Design: reporting the collection plan without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Collection Plan Design outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the collection plan from Collection Plan Design into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Collection Plan Design to verify supplied claims, media, sources, or datasets with documented public-source methods with intelligence requirement, legal and policy constraints, and available resources' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Start from the intelligence requirement, not from the available tools — collection that cannot answer the requirement wastes resources and creates liability
- State legal basis explicitly: passive observation, publicly available data, and active elicitation each carry different legal and ethical burdens
- Scope exclusions are as important as inclusions — what you will not collect defines the ethical boundary
- Build in review checkpoints so that scope can be reassessed if the analytic question evolves
