# Workflow — Indicators of Deception Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish baseline and ingest evidence (read)
Read the evidence corpus and source profile in full. Articulate the baseline expectation: what would the reporting look like if no deception were occurring? Note the specific claims being evaluated and their sourcing.

## Step 2 — Apply MOM — Motive, Opportunity, Means (reason)
Assess whether an adversary plausibly has the motive to deceive on this topic (what would they gain?), the opportunity (do they have access to the collection channels being used?), and the means (resources, agents-in-place, or technical capabilities to inject false or manipulated information). Record conclusions per element with supporting evidence.

## Step 3 — Apply POP — Potential indicators of deception (reason)
Survey the evidence for anomalies against baseline: reporting that is suspiciously timely, unusually confirming of key judgments, internally consistent in ways that real intelligence rarely is, lacking supporting details that would naturally accompany genuine access, or delivered through channels the adversary could influence.

## Step 4 — Apply MOSES — Manipulation, Omission, Selective emphasis, Exaggeration (reason)
Examine the reporting for evidence that information has been deliberately manipulated (altered facts), selectively omitted (what is conspicuously absent?), selectively emphasized (what receives disproportionate weight?), or exaggerated (claims exceed what the source's access could plausibly support).

## Step 5 — Apply EVE — Evidence, Validation, Evaluation (reason)
Evaluate the evidence that exists for or against a deception hypothesis. What corroborating or contradicting information is available from independent channels? What validation checks are possible (technical, liaison, physical)? Assign an overall deception-likelihood rating: Low / Moderate / High / Inconclusive.

## Step 6 — Produce deception assessment report (write)
Write the structured report with one section per framework component, citing specific evidence for each finding. Include the composite deception-likelihood rating, a summary narrative of the proposed deception mechanism if applicable, and recommended analytic responses (caveat the intelligence, seek independent corroboration, tasked collection to test the hypothesis, or escalate to counterintelligence).

## Anti-criteria (must NOT happen)
- Do not treat anomalies alone as proof of deception — the framework requires a plausible mechanism (MOM) before elevating risk
- Do not allow a clean MOM/POP/MOSES/EVE result to produce unqualified confidence in the intelligence — the absence of detected indicators is not proof of accuracy
- Do not apply this framework to adjudicate between competing honest analysts — it is for assessing adversary-driven manipulation, not analytical disagreement
- Do not omit the EVE step in favor of stopping at anomaly identification — the evaluation step is what distinguishes a hypothesis from a conclusion

## AGEINT upstream
`docs/ageint/counterintelligence.md`
