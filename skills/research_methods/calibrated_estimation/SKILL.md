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

## Defensive boundary

Use Calibrated Estimation only for research-methods and synthesis integrity: recognize, assess, document, or defend reproducibility, calibrated confidence, and transparent synthesis. Do not use this skill to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.

## Misuse redirect

If a request asks Calibrated Estimation to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence, refuse that path and redirect to the safe defensive form: synthesize supplied or authorized sources with explicit confidence and uncertainty labels.

## Evidence discipline

- For Calibrated Estimation, bind each finding to a labeled source — study designs, source quality, reproducibility artifacts, and uncertainty records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Calibrated Estimation, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Calibrated Estimation recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Calibrated Estimation: independent lines of study designs, source quality, reproducibility artifacts, and uncertainty records converge, credible alternatives have been tested, and the central estimate would survive removing any single source.
- Medium confidence for Calibrated Estimation: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Calibrated Estimation: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Calibrated Estimation cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Calibrated Estimation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Calibrated Estimation, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Calibrated Estimation, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Calibrated Estimation, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Calibrated Estimation failure: collapsing heterogeneous evidence into an unsupported single confident conclusion.
- Calibrated Estimation failure: producing guidance that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Calibrated Estimation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Calibrated Estimation to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Calibrated Estimation into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Calibrated Estimation to synthesize supplied or authorized sources with explicit confidence and uncertainty labels' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- start outside — choose a reference class of similar cases and obtain its base rate before looking at case-specific details
- adjustments from the base rate require explicit justification and should be modest unless case-specific evidence is strong
- express uncertainty numerically; vague words like 'likely' carry idiosyncratic interpretations across recipients
- calibration is measured over many forecasts — track outcomes and score forecasts to improve future calibration
