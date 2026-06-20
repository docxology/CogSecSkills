---
name: sat.analysis_of_competing_hypotheses
description: Score evidence by diagnosticity across a full hypothesis set to find the least-disconfirmed explanation.
---

# Analysis of Competing Hypotheses (ACH)

ACH (Heuer, CIA) forces the analyst to evaluate ALL plausible hypotheses against ALL evidence simultaneously, rather than building a case for the first satisfactory explanation. The decisive move is to seek evidence that DISCONFIRMS hypotheses: the surviving hypothesis is the one with the least diagnostic evidence against it, not the one with the most evidence for it. This skill drives the full eight-step ACH procedure as an agentic loop.

## When to use

- Multiple competing explanations for an event, attribution, or trend.
- You suspect you (or the source) have anchored on a first impression.
- A high-stakes judgment where confirmation bias would be costly.

## What it produces

- hypotheses x evidence with C/I/N and diagnosticity weights
- hypotheses ordered by inconsistency score, least-disconfirmed first
- future observations that would shift the ranking

## Defensive boundary

Use Analysis of Competing Hypotheses (ACH) only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Analysis of Competing Hypotheses (ACH) to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Analysis of Competing Hypotheses (ACH), tie each matrix, ranking, and indicators claim to concrete evidence from the specific question, hypotheses, and evidence item, source excerpt, observation, or command result that supports it.
- For Analysis of Competing Hypotheses (ACH), label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the matrix.
- Before recommending any Analysis of Competing Hypotheses (ACH) action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Analysis of Competing Hypotheses (ACH): the matrix is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; enumerate hypotheses and list evidence and arguments checks agree, and no unresolved contradiction would change the result.
- Medium for Analysis of Competing Hypotheses (ACH): the matrix is plausible, but one important question source, comparison case, or alternative explanation remains incomplete.
- Low for Analysis of Competing Hypotheses (ACH): the matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Analysis of Competing Hypotheses (ACH) cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Analysis of Competing Hypotheses (ACH), use only authorized question, hypotheses, and evidence, public or source-approved records, and caller-provided context needed for the defensive task.
- For Analysis of Competing Hypotheses (ACH), minimize person-level detail in the matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Analysis of Competing Hypotheses (ACH), do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Analysis of Competing Hypotheses (ACH): treating question as complete when enumerate hypotheses and list evidence and arguments checks or contradictory evidence are missing.
- Analysis of Competing Hypotheses (ACH): producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Analysis of Competing Hypotheses (ACH): reporting the matrix without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Analysis of Competing Hypotheses (ACH) outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the matrix from Analysis of Competing Hypotheses (ACH) into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Analysis of Competing Hypotheses (ACH) to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with question, hypotheses, and evidence' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Diagnosticity over weight of evidence.** Evidence consistent with *every*
- **Disconfirm, don't confirm.** Rank by inconsistency, not consistency.
- **Absence of evidence is evidence.** A missing observation a hypothesis
- **Sensitivity check.** Identify which one or two items, if wrong, flip the
