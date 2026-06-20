# Workflow — What-If Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Posit the scenario as fact (read)
State the scenario in the past tense or as an accomplished fact: 'X has occurred.' Read the current context and baseline assumptions to understand what this scenario contradicts. Do not evaluate plausibility at this stage — accept the posit as given.

## Step 2 — Reason backward to preconditions and pathways (reason)
Working from the assumed-true scenario, identify: (a) what conditions would have had to pre-exist for this to happen — political, technical, organizational, informational; (b) what causal pathways could have led from the current baseline to this event; (c) which of these pathways are most plausible given existing evidence. Then reason forward to map the immediate and second-order implications of the scenario: what happens next, who is affected, what decisions are forced.

## Step 3 — Derive indicators and revise probability (reason, write)
Identify the observable indicators that would be visible if the scenario is developing or has occurred — what signals should collectors or analysts watch for. Reassess the probability of the scenario in light of the precondition and pathway analysis: has working through the scenario revealed it is more or less plausible than initially assessed? Write the what_if_report covering all sections.

## Evidence requirements
- For What-If Analysis, tie each what if report claim to concrete evidence from the specific scenario posit, current context, and time horizon item, source excerpt, observation, or command result that supports it.
- For What-If Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the what if report.
- Before recommending any What-If Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for What-If Analysis: the what if report is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; posit the scenario as fact and reason backward to preconditions and pathways checks agree, and no unresolved contradiction would change the result.
- Medium for What-If Analysis: the what if report is plausible, but one important scenario posit source, comparison case, or alternative explanation remains incomplete.
- Low for What-If Analysis: the what if report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what What-If Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For What-If Analysis, use only authorized scenario posit, current context, and time horizon, public or source-approved records, and caller-provided context needed for the defensive task.
- For What-If Analysis, minimize person-level detail in the what if report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For What-If Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- What-If Analysis: treating scenario posit as complete when posit the scenario as fact and reason backward to preconditions and pathways checks or contradictory evidence are missing.
- What-If Analysis: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- What-If Analysis: reporting the what if report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use What-If Analysis outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the what if report from What-If Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use What-If Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with scenario posit, current context, and time horizon' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not soften the posit to 'what if this might happen' — the scenario must be stated as fact to activate the backward-reasoning discipline
- do not skip the precondition step and jump directly to implications — the preconditions are the primary product for surfacing hidden assumptions
- do not allow the analyst to immediately explain why the scenario is implausible before completing the exercise — disbelief suspension is required through the generative phase
- do not omit observable indicators — a what-if report without warning indicators produces no actionable guidance for collection or monitoring

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
