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

- For Narrative Threat Assessment, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Narrative Threat Assessment, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Narrative Threat Assessment recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Narrative Threat Assessment: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Narrative Threat Assessment: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Narrative Threat Assessment: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Narrative Threat Assessment cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Narrative Threat Assessment should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Narrative Threat Assessment, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Narrative Threat Assessment, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Narrative Threat Assessment, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Narrative Threat Assessment failure: mistaking persuasive resonance for verified harm or intent.
- Narrative Threat Assessment failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Narrative Threat Assessment failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Narrative Threat Assessment to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Narrative Threat Assessment into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Narrative Threat Assessment to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- bind every finding to evidence and defensive use
