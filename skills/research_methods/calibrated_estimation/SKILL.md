---
name: research_methods.calibrated_estimation
description: Produce calibrated probability estimates with explicit reference classes and ranges.
---

# Calibrated Estimation

Calibrated Estimation is a disciplined probability-elicitation technique in which an analyst produces numeric probability estimates (or ranges) for uncertain outcomes and grounds those estimates in explicitly chosen reference classes, base rates, and adjustment logic. Developed in the forecasting literature by Tetlock, Kahneman, and others, and operationalized in prediction tournaments and intelligence training, the technique combats overconfidence and inside-view bias by requiring analysts to compare the current case against a reference class of similar past cases before applying case-specific adjustments. The output is an estimate accompanied by a reference class, a stated confidence interval, and the reasoning behind any adjustments from the base rate.

## When to use

- when a decision requires a probability estimate for a future or uncertain event
- when inside-view reasoning is dominating and base rate anchoring is needed
- when comparing multiple alternative futures and their likelihoods
- when tracking and updating beliefs as new evidence arrives (Bayesian updating context)

## What it produces

- a numeric probability estimate (or range) for the target question
- an explicit reference class and the base rate derived from it
- a documented adjustment narrative explaining why the estimate departs from the base rate
- an 80% confidence interval and stated resolution criteria

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- start outside — choose a reference class of similar cases and obtain its base rate before looking at case-specific details
- adjustments from the base rate require explicit justification and should be modest unless case-specific evidence is strong
- express uncertainty numerically; vague words like 'likely' carry idiosyncratic interpretations across recipients
- calibration is measured over many forecasts — track outcomes and score forecasts to improve future calibration
