---
name: cognitive_security.source_credibility_evaluation
description: Grade a source on reliability and a claim on credibility using the Admiralty/NATO scale.
---

# Source Credibility Evaluation

Evaluate an information source and a specific claim along two independent axes using the NATO/Admiralty Code: source reliability (A–F) based on proximity, track record, motive, and independence; and information credibility (1–6) based on independent confirmation, plausibility, and consistency with known facts. Produce a justified two-part grade (e.g. B2) and state how that grade should bound downstream use of the information.

## When to use

- Someone asks "how reliable is this source?" or "can I trust this report?"
- A claim needs a defensible, auditable credibility rating before it is acted on.
- You need to distinguish a trustworthy outlet carrying an uncorroborated rumor

## What it produces

- A **source-reliability letter (A–F)** with justification grounded in
- An **information-credibility number (1–6)** with justification grounded in
- A combined grade (e.g. `B2`) and an explicit statement of how that grade

## Defensive boundary

Use Source Credibility Evaluation only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Source Credibility Evaluation to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Source Credibility Evaluation, tie each reliability grade, credibility grade, and usage bound claim to concrete evidence from the specific source, claim, and corroboration item, source excerpt, observation, or command result that supports it.
- For Source Credibility Evaluation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the reliability grade.
- Before recommending any Source Credibility Evaluation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Source Credibility Evaluation: the reliability grade is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; identify the source and its proximity and assess track record, motive, and independence checks agree, and no unresolved contradiction would change the result.
- Medium for Source Credibility Evaluation: the reliability grade is plausible, but one important source source, comparison case, or alternative explanation remains incomplete.
- Low for Source Credibility Evaluation: the reliability grade rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Source Credibility Evaluation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Source Credibility Evaluation, use only authorized source, claim, and corroboration, public or source-approved records, and caller-provided context needed for the defensive task.
- For Source Credibility Evaluation, minimize person-level detail in the reliability grade; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Source Credibility Evaluation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Source Credibility Evaluation: treating source as complete when identify the source and its proximity and assess track record, motive, and independence checks or contradictory evidence are missing.
- Source Credibility Evaluation: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Source Credibility Evaluation: reporting the reliability grade without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Source Credibility Evaluation outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the reliability grade from Source Credibility Evaluation into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Source Credibility Evaluation to assess supplied material for manipulation indicators and recommend resilience measures with source, claim, and corroboration' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- The **letter** judges the *source* — its history, position, and incentives —
- The **number** judges *this specific claim* — whether independent evidence
