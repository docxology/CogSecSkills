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
- For Diagnostic Reasoning, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Diagnostic Reasoning, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Diagnostic Reasoning recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Diagnostic Reasoning: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Diagnostic Reasoning: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Diagnostic Reasoning: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Diagnostic Reasoning cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Diagnostic Reasoning should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Diagnostic Reasoning, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Diagnostic Reasoning, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Diagnostic Reasoning, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Diagnostic Reasoning failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Diagnostic Reasoning failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Diagnostic Reasoning failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Diagnostic Reasoning to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Diagnostic Reasoning into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Diagnostic Reasoning to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat evidence as confirming simply because it is consistent with the favored hypothesis — consistency without a high likelihood ratio is not confirmation
- do not process multiple data items simultaneously in one diagnostic assessment — each datum must be evaluated in isolation to preserve the logic
- do not allow the qualitative likelihood labels to substitute for explicit comparative reasoning across hypotheses — the ratio is the finding, not the label in isolation

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
