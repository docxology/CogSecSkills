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

## Anti-criteria (must NOT happen)
- do not substitute vague verbal probability terms (likely, possible, probable) for numeric estimates — they defeat calibration
- do not skip the reference class step and reason only from inside-view case features
- do not treat a single authoritative source's estimate as the reference class — that is anchoring, not calibration
- do not omit resolution criteria; an unresolvable question cannot be used to score or improve calibration

## AGEINT upstream
`docs/ageint/research-methods.md`
