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

- For Calibrated Estimation, tie each calibrated estimate claim to concrete evidence from the specific question, evidence, and prior estimate item, source excerpt, observation, or command result that supports it.
- For Calibrated Estimation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the calibrated estimate.
- Before recommending any Calibrated Estimation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Calibrated Estimation: the calibrated estimate is supported by multiple independent study designs, source quality, reproducibility artifacts, and uncertainty records; define the question and find the reference class and apply inside-view adjustments checks agree, and no unresolved contradiction would change the result.
- Medium for Calibrated Estimation: the calibrated estimate is plausible, but one important question source, comparison case, or alternative explanation remains incomplete.
- Low for Calibrated Estimation: the calibrated estimate rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Calibrated Estimation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating research_methods evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Calibrated Estimation, use only authorized question, evidence, and prior estimate, public or source-approved records, and caller-provided context needed for the defensive task.
- For Calibrated Estimation, minimize person-level detail in the calibrated estimate; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Calibrated Estimation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Calibrated Estimation: treating question as complete when define the question and find the reference class and apply inside-view adjustments checks or contradictory evidence are missing.
- Calibrated Estimation: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Calibrated Estimation: reporting the calibrated estimate without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Calibrated Estimation outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the calibrated estimate from Calibrated Estimation into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Calibrated Estimation to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with question, evidence, and prior estimate' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- start outside — choose a reference class of similar cases and obtain its base rate before looking at case-specific details
- adjustments from the base rate require explicit justification and should be modest unless case-specific evidence is strong
- express uncertainty numerically; vague words like 'likely' carry idiosyncratic interpretations across recipients
- calibration is measured over many forecasts — track outcomes and score forecasts to improve future calibration
