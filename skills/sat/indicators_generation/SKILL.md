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

- For Indicators Generation, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Indicators Generation, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Indicators Generation recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Indicators Generation: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Indicators Generation: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Indicators Generation: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Indicators Generation cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Indicators Generation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Indicators Generation, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Indicators Generation, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Indicators Generation, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Indicators Generation failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Indicators Generation failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Indicators Generation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Indicators Generation to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Indicators Generation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Indicators Generation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- a good indicator is observable, specific, and diagnostic — it must distinguish between at least two outcomes
- derive indicators from actor logic and necessary preconditions, not just from what you hope to see
- pair each indicator with at least one scenario it would undermine, not just one it confirms — avoid confirmation-only lists
- assess collectability: an indicator that cannot be observed serves no monitoring function
