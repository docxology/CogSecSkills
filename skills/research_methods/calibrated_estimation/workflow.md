# Workflow — Calibrated Estimation

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Define the question and find the reference class (read, search)
Make the question specific and resolvable: what outcome, by what date, adjudicated how? Search for or recall a reference class — a population of similar past cases — and extract its base rate frequency.

## Step 2 — Apply inside-view adjustments (reason)
Identify two or three case-specific factors that genuinely distinguish this situation from the reference class average. Adjust the base rate incrementally for each factor; resist moving far from the base rate without strong independent evidence. Note that the inside view systematically underestimates variance.

## Step 3 — Set confidence interval and check for overconfidence (reason)
State an 80% confidence interval around the point estimate. As a calibration check, verify that past 80% intervals contain the true answer roughly 80% of the time. If intervals have been too narrow historically, widen them. Identify which assumption, if wrong, would most shift the estimate.

## Step 4 — Document and communicate the estimate (write)
Write the calibrated estimate report: the numeric probability, the reference class and base rate, a one-paragraph adjustment narrative, the confidence interval, resolution criteria, and a note on what new evidence would trigger a significant update.

## Evidence requirements
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

## Failure modes
- Calibrated Estimation: treating question as complete when define the question and find the reference class and apply inside-view adjustments checks or contradictory evidence are missing.
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

## AGEINT upstream
`docs/ageint/research-methods.md`
