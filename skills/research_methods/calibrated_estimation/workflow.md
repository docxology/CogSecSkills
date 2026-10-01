# Workflow — Calibrated Estimation

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Define the question and find the reference class (read, search)
Make the question specific and resolvable: what outcome, by what date, adjudicated how? Search for or recall a reference class — a population of similar past cases — and extract its base rate frequency.

## Step 2 — Apply inside-view adjustments (reason)
Identify two or three case-specific factors that genuinely distinguish this situation from the reference class average. Adjust the base rate incrementally for each factor; resist moving far from the base rate without strong independent evidence. Note that the inside view systematically underestimates variance.

## Step 3 — Match uncertainty and scoring to the forecast (reason)
For an event forecast, report a probability and any justified uncertainty about that estimate; assess calibration across resolved comparable forecasts using observed frequencies and a declared accuracy score such as the Brier score. For a numeric outcome forecast, an 80% prediction interval can be checked for outcome coverage over many comparable cases. Label an interval around an estimated probability separately and explain its method. If no feedback history exists, state that calibration is unverified. Identify the assumption most likely to shift the estimate.

## Step 4 — Document and communicate the estimate (write)
Write the calibrated estimate report: the numeric probability, the reference class and base rate, adjustment narrative, forecast type and uncertainty method, resolution criteria, scoring plan, and the evidence that would trigger an update. Save a timestamped forecast before the outcome is known.

## Evidence requirements
- For Calibrated Estimation, tie the point estimate, the base rate, and every adjustment to concrete evidence — the historical frequencies defining the reference class and the case-specific factors that warrant departing from it — and treat any move from the base rate without supporting evidence as an unjustified inside-view bias.
- For Calibrated Estimation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the calibrated estimate.
- Before recommending any Calibrated Estimation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Calibrated Estimation: the probability estimate is anchored in an explicitly chosen reference class with a documented base rate, the inside-view adjustments are justified, the uncertainty method matches the forecast type, a documented history of comparable resolved forecasts supports the calibration claim, and the resolution criteria and scoring convention are explicit.
- Medium for Calibrated Estimation: the calibrated estimate is plausible, but one important question source, comparison case, or alternative explanation remains incomplete.
- Low for Calibrated Estimation: the calibrated estimate rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Calibrated Estimation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Calibrated Estimation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Calibrated Estimation, use only authorized question, evidence, prior estimate, public or source-approved records, and caller-provided context needed for the defensive task.
- For Calibrated Estimation, minimize person-level detail in the calibrated estimate; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Calibrated Estimation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Calibrated Estimation: scoring a probability interval against a binary outcome, confusing confidence with event probability, or calling a single untested estimate calibrated without a recorded history of resolved forecasts.
- Calibrated Estimation: skipping the reference class and reasoning only from inside-view case features, anchoring on a single source's number, stating vague verbal probabilities instead of a numeric estimate, or omitting resolution criteria, so the forecast cannot be scored and overconfidence goes uncorrected.
- Calibrated Estimation: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Calibrated Estimation: reporting the calibrated estimate without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Calibrated Estimation outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the calibrated estimate from Calibrated Estimation into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Calibrated Estimation to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with question, evidence, and prior estimate' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not substitute vague verbal probability terms (likely, possible, probable) for numeric estimates — they defeat calibration
- do not skip the reference class step and reason only from inside-view case features
- do not treat a single authoritative source's estimate as the reference class — that is anchoring, not calibration
- do not omit resolution criteria; an unresolvable question cannot be used to score or improve calibration
- do not confuse outcome prediction intervals with confidence or credible intervals for estimated probabilities, or claim calibration from one forecast

## AGEINT upstream
`docs/ageint/research-methods.md`
