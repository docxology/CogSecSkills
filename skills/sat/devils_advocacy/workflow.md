# Workflow — Devil's Advocacy

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — State the consensus and its foundations (read, write)
Restate the lead judgment as a clear claim, enumerate its cited evidence, and list the explicit and implicit assumptions it rests on.

## Step 2 — Select the most vulnerable assumptions (reason)
Choose load-bearing assumptions that are unexamined, inherited from analogy, unsupported by evidence, or resting on absence of contradiction.

## Step 3 — Review the evidence base for soft spots (read, reason)
Separate evidence that genuinely supports the consensus from evidence that is assumed, ambiguous, single-sourced, missing, or contradictory.

## Step 4 — Construct the strongest alternative interpretation (reason)
Build the most credible good-faith alternative reading of the same evidence, as a capable opposing analyst would.

## Step 5 — Marshal the counter-case honestly (reason, write)
Assemble the counter-case with its supporting facts, causal logic, predictions, and its own limitations.

## Step 6 — Assess robustness and resolving collection (reason, write)
State whether the consensus survived intact, survived with caveats, or failed, then name the evidence that would resolve the dispute.

## Evidence requirements
- For Devil's Advocacy, tie each counter case, and robustness verdict claim to concrete evidence from the specific consensus judgment, and evidence base item, source excerpt, observation, or command result that supports it.
- For Devil's Advocacy, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the counter case.
- Before recommending any Devil's Advocacy action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Devil's Advocacy: the counter case is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; state the consensus and its foundations and select the most vulnerable assumptions checks agree, and no unresolved contradiction would change the result.
- Medium for Devil's Advocacy: the counter case is plausible, but one important consensus judgment source, comparison case, or alternative explanation remains incomplete.
- Low for Devil's Advocacy: the counter case rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Devil's Advocacy cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Devil's Advocacy, use only authorized consensus judgment, and evidence base, public or source-approved records, and caller-provided context needed for the defensive task.
- For Devil's Advocacy, minimize person-level detail in the counter case; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Devil's Advocacy, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Devil's Advocacy: treating consensus judgment as complete when state the consensus and its foundations and select the most vulnerable assumptions checks or contradictory evidence are missing.
- Devil's Advocacy: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Devil's Advocacy: reporting the counter case without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Devil's Advocacy outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the counter case from Devil's Advocacy into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Devil's Advocacy to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with consensus judgment, and evidence base' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- **No straw man.** The counter-case must be the strongest real case against the
- **No contrarianism for its own sake.** The exercise tests robustness; it is
- **No suppression of the result.** If the consensus fails the challenge, report
- **No collapsing of evidence categories.** Do not treat merely-assumed or

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
