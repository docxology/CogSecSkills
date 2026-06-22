---
name: sat.indicators_generation
description: Define observable signs that would reveal which scenario or hypothesis is unfolding.
---

# Indicators Generation

Indicators Generation is a structured analytic technique for deriving a set of observable, measurable signs that would signal which of several competing scenarios, hypotheses, or courses of action is actually unfolding. Each indicator is paired with the scenario it would support or undermine, producing a diagnostic matrix that focuses collection and monitoring. The technique is foundational to warning analysis and adversarial scenario tracking in both intelligence and cognitive-security contexts.

## When to use

- when analysts need to monitor for a specific scenario or adversarial course of action in advance
- when collection resources must be allocated across competing monitoring priorities
- when an analysis of competing hypotheses (ACH) has identified scenarios whose distinction depends on observable events
- when building a warning tripwire set for a rapidly evolving situation

## What it produces

- a structured indicators matrix with each sign linked to the scenario it supports or undermines
- diagnostic weight ratings showing which indicators best discriminate among scenarios
- a collection and monitoring priority list tied to available sources
- a foundation for ongoing indicators monitoring and update cycles

## Defensive boundary

Use Indicators Generation only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Indicators Generation to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Indicators Generation, ground each indicator and its diagnostic weight in concrete evidence about the scenarios, the actor profile, and the available collection sources, and name the source that would actually observe it; an indicator with no collectable evidence path is aspirational and must be labelled as such rather than counted as active coverage.
- For Indicators Generation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the indicators matrix.
- Before recommending any Indicators Generation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Indicators Generation: each indicator is derived from the actors' necessary preconditions rather than from hoped-for observations, every indicator is paired with both a scenario it supports and one it would undermine, the diagnostic-weight assignments hold across the scenario set, and no unresolved contradiction would change which signs warrant collection priority.
- Medium for Indicators Generation: the indicators matrix is plausible, but one important scenarios or hypotheses source, comparison case, or alternative explanation remains incomplete.
- Low for Indicators Generation: the indicators matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Indicators Generation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Indicators Generation, use only authorized scenarios or hypotheses, actor profile, and collection environment, public or source-approved records, and caller-provided context needed for the defensive task.
- For Indicators Generation, minimize person-level detail in the indicators matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Indicators Generation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Indicators Generation: declaring the warning set ready when indicators consistent with every scenario were retained or the undermining pairing was skipped, so a confirmation-only list masquerades as diagnostic monitoring and uncollectable signs are treated as live tripwires.
- Indicators Generation: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Indicators Generation: reporting the indicators matrix without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Indicators Generation outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the indicators matrix from Indicators Generation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Indicators Generation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with scenarios or hypotheses, actor profile, and collection environment' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- a good indicator is observable, specific, and diagnostic — it must distinguish between at least two outcomes
- derive indicators from actor logic and necessary preconditions, not just from what you hope to see
- pair each indicator with at least one scenario it would undermine, not just one it confirms — avoid confirmation-only lists
- assess collectability: an indicator that cannot be observed serves no monitoring function
