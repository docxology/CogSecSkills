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
- For Indicators Validation, support each diagnosticity score and disposition with concrete evidence from the candidate indicators, the scenario set, and known base rates, and record the counterfactual reasoning that justifies it; a retained indicator whose cross-scenario behaviour was never tested against evidence is unvalidated and must be flagged, not certified.
- For Indicators Validation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the validated indicators matrix.
- Before recommending any Indicators Validation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Indicators Validation: each indicator's diagnosticity was tested by the counterfactual of whether it would appear when its target scenario is not unfolding, base-rate and overlap traps were checked rather than assumed away, every scenario has adequate high-diagnosticity coverage, and no unresolved contradiction would change a retain, revise, or drop disposition.
- Medium for Indicators Validation: the validated indicators matrix is plausible, but one important candidate indicators source, comparison case, or alternative explanation remains incomplete.
- Low for Indicators Validation: the validated indicators matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Indicators Validation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Indicators Validation, use only authorized candidate indicators, scenarios or hypotheses, and base rate context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Indicators Validation, minimize person-level detail in the validated indicators matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Indicators Validation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Indicators Validation: passing a set as validated when individual indicators were scored without auditing aggregate scenario coverage or when confirmatory traps that fire under all outcomes were retained, leaving a scenario effectively unmonitored while the matrix looks rigorous.
- Indicators Validation: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Indicators Validation: reporting the validated indicators matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Indicators Validation outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the validated indicators matrix from Indicators Validation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Indicators Validation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with candidate indicators, scenarios or hypotheses, and base rate context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not retain an indicator that appears under all scenarios — it cannot discriminate and will only generate false confidence
- do not judge an indicator by whether analysts expect to see it, but by whether its presence genuinely shifts the probability of one scenario relative to others
- do not skip the scenario coverage check — validating individual indicators without checking aggregate coverage can leave entire scenarios unmonitored
- do not treat validation as a one-time event — indicator sets decay as actors learn to suppress or spoof them

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
