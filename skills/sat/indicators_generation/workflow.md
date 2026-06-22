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
- For Indicators Generation, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Indicators Generation, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Indicators Generation recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Indicators Generation: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Indicators Generation: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Indicators Generation: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Indicators Generation cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Indicators Generation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Indicators Generation, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Indicators Generation, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Indicators Generation, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Indicators Generation failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Indicators Generation failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Indicators Generation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Indicators Generation to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Indicators Generation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Indicators Generation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not generate indicators that are consistent with all scenarios — they have no diagnostic value
- do not list desired evidence as indicators — indicators are derived from actor logic and necessary preconditions, not from what would be convenient to find
- do not omit the 'undermining' column — an indicator that only confirms never disconfirms and enables confirmation bias
- do not retain uncollectable indicators in the active monitoring matrix without flagging them as aspirational

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
