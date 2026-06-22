---
name: sat.structured_analogies
description: Reason from a disciplined set of comparable historical cases, not a single anecdote.
---

# Structured Analogies

Structured Analogies (also called Historical Analogy Analysis) is a structured-analytic technique that selects, evaluates, and systematically compares a set of historical precedent cases to a current situation rather than relying on a single, intuitively chosen anecdote. By making the selection criteria explicit and requiring analysis of both similarities and dissimilarities across multiple cases, it constrains the cognitive tendency to over-extend a single vivid precedent. In cognitive-security contexts it is used to assess whether a suspected influence operation or adversarial narrative campaign resembles documented historical patterns and what those precedents predict about likely trajectories and countermeasures.

## When to use

- a situation is novel enough that direct evidence is sparse but historical precedents plausibly exist
- an analyst or decision-maker is already anchored on a single analogy and needs disciplined expansion
- assessing an influence operation or adversarial campaign whose playbook may echo documented historical cases
- estimating likely outcomes or timelines when base rates from historical cases are the best available evidence

## What it produces

- a disciplined multi-case comparison table that makes the basis for analogy explicit and auditable
- an explicit mapping of where the current case is similar to and where it diverges from each precedent
- confidence-weighted lessons and predictions qualified by the degree of analogy fit

## Defensive boundary

Use Structured Analogies only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Structured Analogies to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Structured Analogies, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Structured Analogies, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Structured Analogies recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Structured Analogies: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Structured Analogies: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Structured Analogies: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Structured Analogies cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Structured Analogies should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Structured Analogies, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Structured Analogies, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Structured Analogies, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Structured Analogies failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Structured Analogies failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Analogies failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Structured Analogies to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Structured Analogies into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Structured Analogies to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- select cases using criteria stated before examining outcomes — post-hoc cherry-picking defeats the technique
- dissimilarities carry equal analytic weight to similarities; a disconfirming case must be included
- weight lessons by the number of cases supporting them and the closeness of fit, not by how vivid the single most compelling case is
