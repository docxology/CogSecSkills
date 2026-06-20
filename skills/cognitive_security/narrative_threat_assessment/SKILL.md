---
name: cognitive_security.narrative_threat_assessment
description: Characterize a narrative's intent, mechanics, reach, and harm potential as a cognitive threat.
---

# Narrative Threat Assessment

A defensive cognitive-security procedure that examines a circulating narrative to characterize it as a potential cognitive threat. It captures the narrative's claims and framing, identifies the target audience and the belief or identity levers it exploits, classifies the manipulation techniques present, assesses provenance and likely intent, estimates reach and harm potential, and recommends defensive responses such as prebunking and lateral reading. The output protects audiences; it never authors manipulation or a playbook for running an influence operation.

## When to use

- A narrative is spreading and you need to know whether it is a cognitive threat,
- You must brief a community, platform, or newsroom on a suspected influence
- You want an accountable, evidence-bound read on provenance and likely intent

## What it produces

- A **threat assessment** document covering: captured claims and framing; target
- A prioritized list of **defensive recommendations** — prebunking, lateral

## Defensive boundary

Use Narrative Threat Assessment only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Narrative Threat Assessment to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Narrative Threat Assessment, tie each threat assessment, and defensive recommendations claim to concrete evidence from the specific narrative text, and context item, source excerpt, observation, or command result that supports it.
- For Narrative Threat Assessment, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the threat assessment.
- Before recommending any Narrative Threat Assessment action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Narrative Threat Assessment: the threat assessment is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; capture the narrative precisely and identify target audience and levers checks agree, and no unresolved contradiction would change the result.
- Medium for Narrative Threat Assessment: the threat assessment is plausible, but one important narrative text source, comparison case, or alternative explanation remains incomplete.
- Low for Narrative Threat Assessment: the threat assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Narrative Threat Assessment cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Narrative Threat Assessment, use only authorized narrative text, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Narrative Threat Assessment, minimize person-level detail in the threat assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Narrative Threat Assessment, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Narrative Threat Assessment: treating narrative text as complete when capture the narrative precisely and identify target audience and levers checks or contradictory evidence are missing.
- Narrative Threat Assessment: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Narrative Threat Assessment: reporting the threat assessment without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Narrative Threat Assessment outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the threat assessment from Narrative Threat Assessment into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Narrative Threat Assessment to assess supplied material for manipulation indicators and recommend resilience measures with narrative text, and context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- bind every finding to evidence and defensive use
