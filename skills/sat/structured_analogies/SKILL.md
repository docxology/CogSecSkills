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

- For Structured Analogies, tie each case comparison table, and lessons and predictions claim to concrete evidence from the specific current situation, candidate cases, and comparison dimensions item, source excerpt, observation, or command result that supports it.
- For Structured Analogies, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the case comparison table.
- Before recommending any Structured Analogies action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Structured Analogies: the case comparison table is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; characterize the current situation and identify and select candidate cases checks agree, and no unresolved contradiction would change the result.
- Medium for Structured Analogies: the case comparison table is plausible, but one important current situation source, comparison case, or alternative explanation remains incomplete.
- Low for Structured Analogies: the case comparison table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Structured Analogies cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Structured Analogies, use only authorized current situation, candidate cases, and comparison dimensions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Structured Analogies, minimize person-level detail in the case comparison table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Structured Analogies, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Structured Analogies: treating current situation as complete when characterize the current situation and identify and select candidate cases checks or contradictory evidence are missing.
- Structured Analogies: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Analogies: reporting the case comparison table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Structured Analogies outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the case comparison table from Structured Analogies into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Structured Analogies to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with current situation, candidate cases, and comparison dimensions' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- select cases using criteria stated before examining outcomes — post-hoc cherry-picking defeats the technique
- dissimilarities carry equal analytic weight to similarities; a disconfirming case must be included
- weight lessons by the number of cases supporting them and the closeness of fit, not by how vivid the single most compelling case is
