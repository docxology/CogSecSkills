# Workflow — Diagnostic Reasoning

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — State the datum and the hypothesis set (read)
Record the new datum precisely. List all active competing hypotheses. Note the current prior assessment (relative likelihood) for each hypothesis before this datum is considered.

## Step 2 — Assess expected likelihood per hypothesis (reason)
For each hypothesis H, ask: 'If H were true, how likely would we be to see this specific datum?' Rate each on a qualitative scale (very likely / somewhat likely / roughly neutral / somewhat unlikely / very unlikely). Then ask: 'If H were false, how likely would this datum be?' The ratio of these two assessments is the likelihood ratio.

## Step 3 — Determine direction and magnitude of update (reason)
Compare the likelihood ratios across hypotheses. Hypotheses where the datum is much more likely than under alternatives gain support; those where it is much less likely lose ground. Hypotheses where the likelihood ratio is near 1 are unchanged. Note that a datum can simultaneously support one hypothesis and refute another.

## Step 4 — Assess diagnostic value (reason, write)
Determine whether this datum is highly diagnostic (large spread in likelihood ratios across hypotheses), moderately diagnostic, or low-diagnostic (all ratios near 1). If low-diagnostic, explain what evidence would be more discriminating.

## Step 5 — Produce updated ranking and table (write)
Fill the diagnostic table. Write the updated hypothesis ranking with explicit reasoning. Note if the datum warrants a significant change in the lead hypothesis or only a marginal adjustment. Flag if collection against a specific more-diagnostic indicator is recommended.

## Evidence requirements
- For Diagnostic Reasoning, tie each diagnostic table, updated ranking, and diagnostic value assessment claim to concrete evidence from the specific new datum, competing hypotheses, and prior assessments item, source excerpt, observation, or command result that supports it.
- For Diagnostic Reasoning, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the diagnostic table.
- Before recommending any Diagnostic Reasoning action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Diagnostic Reasoning: the diagnostic table is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; state the datum and the hypothesis set and assess expected likelihood per hypothesis checks agree, and no unresolved contradiction would change the result.
- Medium for Diagnostic Reasoning: the diagnostic table is plausible, but one important new datum source, comparison case, or alternative explanation remains incomplete.
- Low for Diagnostic Reasoning: the diagnostic table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Diagnostic Reasoning cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Diagnostic Reasoning, use only authorized new datum, competing hypotheses, and prior assessments, public or source-approved records, and caller-provided context needed for the defensive task.
- For Diagnostic Reasoning, minimize person-level detail in the diagnostic table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Diagnostic Reasoning, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Diagnostic Reasoning: treating new datum as complete when state the datum and the hypothesis set and assess expected likelihood per hypothesis checks or contradictory evidence are missing.
- Diagnostic Reasoning: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Diagnostic Reasoning: reporting the diagnostic table without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Diagnostic Reasoning outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the diagnostic table from Diagnostic Reasoning into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Diagnostic Reasoning to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with new datum, competing hypotheses, and prior assessments' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat evidence as confirming simply because it is consistent with the favored hypothesis — consistency without a high likelihood ratio is not confirmation
- do not process multiple data items simultaneously in one diagnostic assessment — each datum must be evaluated in isolation to preserve the logic
- do not allow the qualitative likelihood labels to substitute for explicit comparative reasoning across hypotheses — the ratio is the finding, not the label in isolation

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
