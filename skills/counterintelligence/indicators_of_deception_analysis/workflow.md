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

## Evidence requirements
- For Indicators of Deception Analysis, tie each deception assessment report claim to concrete evidence from the specific evidence corpus, source profile, and baseline expectations item, source excerpt, observation, or command result that supports it.
- For Indicators of Deception Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the deception assessment report.
- Before recommending any Indicators of Deception Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Indicators of Deception Analysis: the deception assessment report is supported by multiple independent interaction records, process artifacts, deception indicators, and alternative explanations; establish baseline and ingest evidence and apply mom — motive, opportunity, means checks agree, and no unresolved contradiction would change the result.
- Medium for Indicators of Deception Analysis: the deception assessment report is plausible, but one important evidence corpus source, comparison case, or alternative explanation remains incomplete.
- Low for Indicators of Deception Analysis: the deception assessment report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Indicators of Deception Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Indicators of Deception Analysis, use only authorized evidence corpus, source profile, and baseline expectations, public or source-approved records, and caller-provided context needed for the defensive task.
- For Indicators of Deception Analysis, minimize person-level detail in the deception assessment report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Indicators of Deception Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Indicators of Deception Analysis: treating evidence corpus as complete when establish baseline and ingest evidence and apply mom — motive, opportunity, means checks or contradictory evidence are missing.
- Indicators of Deception Analysis: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Indicators of Deception Analysis: reporting the deception assessment report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Indicators of Deception Analysis outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the deception assessment report from Indicators of Deception Analysis into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Indicators of Deception Analysis to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with evidence corpus, source profile, and baseline expectations' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat anomalies alone as proof of deception — the framework requires a plausible mechanism (MOM) before elevating risk
- Do not allow a clean MOM/POP/MOSES/EVE result to produce unqualified confidence in the intelligence — the absence of detected indicators is not proof of accuracy
- Do not apply this framework to adjudicate between competing honest analysts — it is for assessing adversary-driven manipulation, not analytical disagreement
- Do not omit the EVE step in favor of stopping at anomaly identification — the evaluation step is what distinguishes a hypothesis from a conclusion

## AGEINT upstream
`docs/ageint/counterintelligence.md`
