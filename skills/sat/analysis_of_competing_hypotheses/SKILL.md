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

- For Analysis of Competing Hypotheses (ACH), bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Analysis of Competing Hypotheses (ACH), keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Analysis of Competing Hypotheses (ACH) recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Analysis of Competing Hypotheses (ACH): independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Analysis of Competing Hypotheses (ACH): the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Analysis of Competing Hypotheses (ACH): the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Analysis of Competing Hypotheses (ACH) cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Analysis of Competing Hypotheses (ACH) should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Analysis of Competing Hypotheses (ACH), use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Analysis of Competing Hypotheses (ACH), protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Analysis of Competing Hypotheses (ACH), do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Analysis of Competing Hypotheses (ACH) failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Analysis of Competing Hypotheses (ACH) failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Analysis of Competing Hypotheses (ACH) failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Analysis of Competing Hypotheses (ACH) to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Analysis of Competing Hypotheses (ACH) into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Analysis of Competing Hypotheses (ACH) to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Diagnosticity over weight of evidence.** Evidence consistent with *every*
- **Disconfirm, don't confirm.** Rank by inconsistency, not consistency.
- **Absence of evidence is evidence.** A missing observation a hypothesis
- **Sensitivity check.** Identify which one or two items, if wrong, flip the
