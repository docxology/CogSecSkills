# Workflow — Indicators Generation

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest scenarios and context (read)
Read the full scenario set or hypothesis list. Note the key distinctions among scenarios — what makes each unique — since indicators must exploit those distinctions. Review any available actor profile or doctrine to ground derivation.

## Step 2 — Derive candidate indicators per scenario (reason)
For each scenario, ask: what actions, preparations, communications, or observable events would necessarily or probably precede or accompany this outcome? Generate a raw list of candidate indicators per scenario, drawing on actor logic, historical precedent, and necessary preconditions.

## Step 3 — Assess diagnostic value (reason)
For each candidate indicator, assess whether it is uniquely associated with one scenario or shared across several. Assign a diagnostic weight: high (appears only under one scenario), medium (favors one over others), or low (consistent with multiple scenarios). Retain high- and medium-weight indicators; flag or drop low-weight items.

## Step 4 — Check collectability (reason)
For each retained indicator, identify the collection source (open source, signals, human, sensor, imagery, etc.). Flag indicators that are logically sound but currently uncollectable — they may inform future collection planning but cannot serve as active tripwires.

## Step 5 — Produce the indicators matrix and narrative (write)
Format all retained indicators into a matrix table: observable sign, supporting scenario, undermining scenario, diagnostic weight, collection source. Write a brief narrative covering the logic behind key indicators, diagnostic trade-offs, and collection priorities.

## Evidence requirements
- For Indicators Generation, tie each indicators matrix, and indicators narrative claim to concrete evidence from the specific scenarios or hypotheses, actor profile, and collection environment item, source excerpt, observation, or command result that supports it.
- For Indicators Generation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the indicators matrix.
- Before recommending any Indicators Generation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Indicators Generation: the indicators matrix is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; ingest scenarios and context and derive candidate indicators per scenario checks agree, and no unresolved contradiction would change the result.
- Medium for Indicators Generation: the indicators matrix is plausible, but one important scenarios or hypotheses source, comparison case, or alternative explanation remains incomplete.
- Low for Indicators Generation: the indicators matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Indicators Generation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Indicators Generation, use only authorized scenarios or hypotheses, actor profile, and collection environment, public or source-approved records, and caller-provided context needed for the defensive task.
- For Indicators Generation, minimize person-level detail in the indicators matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Indicators Generation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Indicators Generation: treating scenarios or hypotheses as complete when ingest scenarios and context and derive candidate indicators per scenario checks or contradictory evidence are missing.
- Indicators Generation: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Indicators Generation: reporting the indicators matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Indicators Generation outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the indicators matrix from Indicators Generation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Indicators Generation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with scenarios or hypotheses, actor profile, and collection environment' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not generate indicators that are consistent with all scenarios — they have no diagnostic value
- do not list desired evidence as indicators — indicators are derived from actor logic and necessary preconditions, not from what would be convenient to find
- do not omit the 'undermining' column — an indicator that only confirms never disconfirms and enables confirmation bias
- do not retain uncollectable indicators in the active monitoring matrix without flagging them as aspirational

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
