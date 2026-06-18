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

## Anti-criteria (must NOT happen)
- do not generate indicators that are consistent with all scenarios — they have no diagnostic value
- do not list desired evidence as indicators — indicators are derived from actor logic and necessary preconditions, not from what would be convenient to find
- do not omit the 'undermining' column — an indicator that only confirms never disconfirms and enables confirmation bias
- do not retain uncollectable indicators in the active monitoring matrix without flagging them as aspirational

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
