---
name: sat.indicators_validation
description: Test indicators for diagnosticity: do they actually discriminate between outcomes?
---

# Indicators Validation

Indicators Validation is a quality-control technique that stress-tests a candidate indicator set to determine whether each indicator genuinely discriminates among the scenarios it is claimed to distinguish. It applies diagnosticity tests — asking whether an indicator would appear under only one outcome, under several, or under all — and prunes or restructures the indicator set accordingly. This prevents the common failure mode in which analysts collect confirmatory data against indicators that would appear regardless of which outcome is unfolding.

## When to use

- after an initial indicators generation pass, before deploying an indicator set for live monitoring
- when a monitoring regime has produced unexpected false positives or missed events
- when inherited indicator sets need a quality audit
- when indicators are being used in high-stakes warning contexts where a false negative or false positive carries significant cost

## What it produces

- a diagnosticity rating for every candidate indicator (high / medium / low / invalid)
- a disposition decision for each indicator: retain as-is, revise to increase specificity, or drop
- identification of scenario gaps — scenarios that lack a sufficient number of high-diagnosticity indicators
- a clean, validated indicators matrix ready for operational monitoring

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- the diagnosticity test: ask 'would this indicator appear even if this scenario were NOT unfolding?' — if yes, it is not diagnostic for that scenario
- apply the counterfactual: for each indicator, enumerate every scenario under which it would appear, not just the target scenario
- distinguish true-positive traps (indicators that look confirmatory but appear under all outcomes) from genuinely diagnostic signals
- coverage check: ensure every scenario has at least two high-diagnosticity indicators or flag it as a coverage gap
