---
name: sat.diagnostic_reasoning
description: Apply Bayesian-style updating of a single new datum against competing explanations.
---

# Diagnostic Reasoning

Diagnostic Reasoning is a structured Bayesian-style technique for evaluating the evidentiary weight of a single new datum against a set of competing hypotheses, asking explicitly: how much more (or less) likely is this datum if hypothesis H is true than if H is false? The technique operationalizes Bayes's theorem without requiring precise probabilities: analysts assign comparative likelihoods (much more likely / somewhat more likely / equally likely / less likely) across all active hypotheses and use the pattern to update which hypothesis is best supported. This prevents the common cognitive error of treating consistent evidence as confirming evidence — evidence is truly diagnostic only when it would be rare under the alternative.

## When to use

- a new piece of information arrives and the analyst needs to determine how it changes the relative standing of active hypotheses
- an analyst is at risk of confirmation bias — treating evidence consistent with the favored hypothesis as strongly supporting it
- preparing a quantified or semi-quantified update to an analytic line for a senior reviewer or customer
- teaching analytic tradecraft — diagnostic reasoning makes the Bayesian update logic transparent and auditable

## What it produces

- an explicit comparison of how likely the datum is under each hypothesis, preventing the assumption that consistency implies strong support
- a likelihood ratio (qualitative) for each hypothesis — the core of the Bayesian update
- an updated relative ranking of hypotheses that is traceable to the specific datum just evaluated
- an assessment of the datum's actual diagnostic value and a pointer toward more diagnostic collection

## Defensive boundary

Use Diagnostic Reasoning only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Diagnostic Reasoning to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Diagnostic Reasoning, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Diagnostic Reasoning, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Diagnostic Reasoning recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Diagnostic Reasoning: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Diagnostic Reasoning: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Diagnostic Reasoning: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Diagnostic Reasoning cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Diagnostic Reasoning should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Diagnostic Reasoning, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Diagnostic Reasoning, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Diagnostic Reasoning, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Diagnostic Reasoning failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Diagnostic Reasoning failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Diagnostic Reasoning failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Diagnostic Reasoning to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Diagnostic Reasoning into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Diagnostic Reasoning to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- the key question is NOT 'is this consistent with H?' but 'how much more likely is this datum if H is true versus if H is false?' — the ratio is what matters
- evaluate each hypothesis against the datum independently before comparing across hypotheses — avoid holistic pattern-matching
- non-diagnostic evidence (equally likely under all hypotheses) should not change the ranking, no matter how striking it seems
