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

## Anti-criteria (must NOT happen)
- do not retain an indicator that appears under all scenarios — it cannot discriminate and will only generate false confidence
- do not judge an indicator by whether analysts expect to see it, but by whether its presence genuinely shifts the probability of one scenario relative to others
- do not skip the scenario coverage check — validating individual indicators without checking aggregate coverage can leave entire scenarios unmonitored
- do not treat validation as a one-time event — indicator sets decay as actors learn to suppress or spoof them

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
