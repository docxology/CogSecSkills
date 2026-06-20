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

## Evidence requirements
- For Sorting, tie each sorted table, and outlier flags claim to concrete evidence from the specific evidence set, and sort dimensions item, source excerpt, observation, or command result that supports it.
- For Sorting, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the sorted table.
- Before recommending any Sorting action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Sorting: the sorted table is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; inventory the evidence and select and apply sort dimensions checks agree, and no unresolved contradiction would change the result.
- Medium for Sorting: the sorted table is plausible, but one important evidence set source, comparison case, or alternative explanation remains incomplete.
- Low for Sorting: the sorted table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Sorting cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Sorting, use only authorized evidence set, and sort dimensions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Sorting, minimize person-level detail in the sorted table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Sorting, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Sorting: treating evidence set as complete when inventory the evidence and select and apply sort dimensions checks or contradictory evidence are missing.
- Sorting: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Sorting: reporting the sorted table without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Sorting outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the sorted table from Sorting into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Sorting to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with evidence set, and sort dimensions' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not select sort dimensions after viewing the data in a way that guarantees the preferred hypothesis dominates — dimension selection must precede sorting
- do not discard outliers without written justification; unexplained outliers are the technique's most valuable output
- do not collapse all items into a single undifferentiated list if multiple meaningful dimensions exist

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
