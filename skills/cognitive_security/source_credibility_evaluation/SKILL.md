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

- For Source Credibility Evaluation, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Source Credibility Evaluation, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Source Credibility Evaluation recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Source Credibility Evaluation: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Source Credibility Evaluation: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Source Credibility Evaluation: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Source Credibility Evaluation cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Source Credibility Evaluation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Source Credibility Evaluation, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Source Credibility Evaluation, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Source Credibility Evaluation, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Source Credibility Evaluation failure: mistaking persuasive resonance for verified harm or intent.
- Source Credibility Evaluation failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Source Credibility Evaluation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Source Credibility Evaluation to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Source Credibility Evaluation into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Source Credibility Evaluation to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- The **letter** judges the *source* — its history, position, and incentives —
- The **number** judges *this specific claim* — whether independent evidence
