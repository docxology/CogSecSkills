# Workflow — What-If Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Posit the scenario as fact (read)
State the scenario in the past tense or as an accomplished fact: 'X has occurred.' Read the current context and baseline assumptions to understand what this scenario contradicts. Do not evaluate plausibility at this stage — accept the posit as given.

## Step 2 — Reason backward to preconditions and pathways (reason)
Working from the assumed-true scenario, identify: (a) what conditions would have had to pre-exist for this to happen — political, technical, organizational, informational; (b) what causal pathways could have led from the current baseline to this event; (c) which of these pathways are most plausible given existing evidence. Then reason forward to map the immediate and second-order implications of the scenario: what happens next, who is affected, what decisions are forced.

## Step 3 — Derive indicators and revise probability (reason, write)
Identify the observable indicators that would be visible if the scenario is developing or has occurred — what signals should collectors or analysts watch for. Reassess the probability of the scenario in light of the precondition and pathway analysis: has working through the scenario revealed it is more or less plausible than initially assessed? Write the what_if_report covering all sections.

## Evidence requirements
- For What-If Analysis, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For What-If Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any What-If Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for What-If Analysis: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for What-If Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for What-If Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what What-If Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence What-If Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For What-If Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For What-If Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For What-If Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- What-If Analysis failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- What-If Analysis failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- What-If Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use What-If Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn What-If Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use What-If Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not soften the posit to 'what if this might happen' — the scenario must be stated as fact to activate the backward-reasoning discipline
- do not skip the precondition step and jump directly to implications — the preconditions are the primary product for surfacing hidden assumptions
- do not allow the analyst to immediately explain why the scenario is implausible before completing the exercise — disbelief suspension is required through the generative phase
- do not omit observable indicators — a what-if report without warning indicators produces no actionable guidance for collection or monitoring

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
