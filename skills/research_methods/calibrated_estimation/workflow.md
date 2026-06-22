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

## Failure modes
- Calibrated Estimation failure: collapsing heterogeneous evidence into an unsupported single confident conclusion.
- Calibrated Estimation failure: producing guidance that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Calibrated Estimation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Calibrated Estimation to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Calibrated Estimation into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Calibrated Estimation to synthesize supplied or authorized sources with explicit confidence and uncertainty labels' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not substitute vague verbal probability terms (likely, possible, probable) for numeric estimates — they defeat calibration
- do not skip the reference class step and reason only from inside-view case features
- do not treat a single authoritative source's estimate as the reference class — that is anchoring, not calibration
- do not omit resolution criteria; an unresolvable question cannot be used to score or improve calibration

## AGEINT upstream
`docs/ageint/research-methods.md`
