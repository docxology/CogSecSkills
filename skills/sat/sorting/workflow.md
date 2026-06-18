# Workflow — Sorting

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory the evidence (read)
Read the full evidence set and list every item. Note which attributes are consistently available across items (date, source, geography, reliability rating, significance estimate, content type, etc.).

## Step 2 — Select and apply sort dimensions (reason)
Choose one primary and at least one secondary sort dimension. Assign each evidence item to its position in the resulting structure. Where an item fits multiple clusters equally, flag it as ambiguous.

## Step 3 — Identify clusters and outliers (reason, write)
Name each dominant cluster and characterize what it represents analytically. Identify items that fall outside every cluster. For each outlier, write a brief note explaining what hypothesis could account for its anomalous position (e.g., deception artifact, measurement error, genuine surprise).

## Step 4 — Produce sorted table and outlier flags (write)
Emit the sorted table with cluster labels and the outlier-flag list. Record which dimensions were used and invite re-sorting on alternatives.

## Anti-criteria (must NOT happen)
- do not select sort dimensions after viewing the data in a way that guarantees the preferred hypothesis dominates — dimension selection must precede sorting
- do not discard outliers without written justification; unexplained outliers are the technique's most valuable output
- do not collapse all items into a single undifferentiated list if multiple meaningful dimensions exist

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
