# Workflow — Indicators Validation

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest the candidate set and scenarios (read)
Read the full candidate indicator list alongside the complete scenario or hypothesis set. Understand the claimed scenario association for each indicator before applying any tests.

## Step 2 — Apply the diagnosticity test to each indicator (reason)
For each indicator, run the counterfactual: 'Under which of the other scenarios would this indicator also appear?' If an indicator appears under all scenarios, it is non-diagnostic. If it appears under several, it is low-diagnostic. Score each indicator: High (unique to one scenario), Medium (favors one over others with clear asymmetry), Low (consistent with two or more without clear weight), Invalid (consistent with all).

## Step 3 — Identify false-diagnostic and overlap traps (reason)
Flag 'confirmatory traps' — indicators that analysts would naturally report as positive evidence but that carry no real diagnostic power. Check for indicator overlap: pairs that measure the same underlying event and provide no independent evidence. Note base-rate issues: indicators that are so common in the environment that their presence carries no signal.

## Step 4 — Check scenario coverage (reason)
For each scenario in the set, count how many high- or medium-diagnostic indicators it has. A scenario with zero or one high-diagnostic indicator is a coverage gap — warn that it may go undetected even if it unfolds. Propose collection guidance to address gaps.

## Step 5 — Produce validated matrix and report (write)
Output the revised indicators matrix with each item's diagnostic weight, disposition (retain/revise/drop), and a brief rationale. Write a validation narrative covering systemic weaknesses found, coverage gaps by scenario, and priority recommendations for the revised monitoring regime.

## Evidence requirements
- For Indicators Validation, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Indicators Validation, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Indicators Validation recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Indicators Validation: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Indicators Validation: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Indicators Validation: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Indicators Validation cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Indicators Validation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Indicators Validation, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Indicators Validation, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Indicators Validation, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Indicators Validation failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Indicators Validation failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Indicators Validation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Indicators Validation to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Indicators Validation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Indicators Validation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not retain an indicator that appears under all scenarios — it cannot discriminate and will only generate false confidence
- do not judge an indicator by whether analysts expect to see it, but by whether its presence genuinely shifts the probability of one scenario relative to others
- do not skip the scenario coverage check — validating individual indicators without checking aggregate coverage can leave entire scenarios unmonitored
- do not treat validation as a one-time event — indicator sets decay as actors learn to suppress or spoof them

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
