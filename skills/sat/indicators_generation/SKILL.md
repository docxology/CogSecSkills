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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- a good indicator is observable, specific, and diagnostic — it must distinguish between at least two outcomes
- derive indicators from actor logic and necessary preconditions, not just from what you hope to see
- pair each indicator with at least one scenario it would undermine, not just one it confirms — avoid confirmation-only lists
- assess collectability: an indicator that cannot be observed serves no monitoring function
