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

- For Diagnostic Reasoning, bind every entry in the diagnostic table and every shift in the updated ranking to concrete evidence drawn from the specific new datum and the stated priors, naming the comparative likelihood that justifies it; a ranking change unsupported by an explicit likelihood-ratio judgment is an assertion, not a diagnostic finding.
- For Diagnostic Reasoning, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the diagnostic table.
- Before recommending any Diagnostic Reasoning action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Diagnostic Reasoning: each hypothesis's likelihood ratio is grounded in the specific datum rather than mere consistency, multiple independent considerations corroborate the same update direction, the revised ranking stays stable under reasonable reweighting, and no unresolved contradiction would change which hypothesis the datum best supports.
- Medium for Diagnostic Reasoning: the diagnostic table is plausible, but one important new datum source, comparison case, or alternative explanation remains incomplete.
- Low for Diagnostic Reasoning: the diagnostic table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Diagnostic Reasoning cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Diagnostic Reasoning, use only authorized new datum, competing hypotheses, and prior assessments, public or source-approved records, and caller-provided context needed for the defensive task.
- For Diagnostic Reasoning, minimize person-level detail in the diagnostic table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Diagnostic Reasoning, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Diagnostic Reasoning: declaring the assessment complete when the datum's likelihood under each rival hypothesis was never genuinely compared, so evidence merely consistent with the favored hypothesis is mistaken for strong support and contradictory readings of the datum go unexamined.
- Diagnostic Reasoning: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Diagnostic Reasoning: reporting the diagnostic table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Diagnostic Reasoning outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the diagnostic table from Diagnostic Reasoning into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Diagnostic Reasoning to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with new datum, competing hypotheses, and prior assessments' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- the key question is NOT 'is this consistent with H?' but 'how much more likely is this datum if H is true versus if H is false?' — the ratio is what matters
- evaluate each hypothesis against the datum independently before comparing across hypotheses — avoid holistic pattern-matching
- non-diagnostic evidence (equally likely under all hypotheses) should not change the ranking, no matter how striking it seems
