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
- For Devil's Advocacy, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Devil's Advocacy, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Devil's Advocacy recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Devil's Advocacy: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Devil's Advocacy: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Devil's Advocacy: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Devil's Advocacy cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Devil's Advocacy should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Devil's Advocacy, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Devil's Advocacy, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Devil's Advocacy, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Devil's Advocacy failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Devil's Advocacy failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Devil's Advocacy failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Devil's Advocacy to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Devil's Advocacy into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Devil's Advocacy to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- **No straw man.** The counter-case must be the strongest real case against the
- **No contrarianism for its own sake.** The exercise tests robustness; it is
- **No suppression of the result.** If the consensus fails the challenge, report
- **No collapsing of evidence categories.** Do not treat merely-assumed or

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
