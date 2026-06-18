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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- the key question is NOT 'is this consistent with H?' but 'how much more likely is this datum if H is true versus if H is false?' — the ratio is what matters
- evaluate each hypothesis against the datum independently before comparing across hypotheses — avoid holistic pattern-matching
- non-diagnostic evidence (equally likely under all hypotheses) should not change the ranking, no matter how striking it seems
