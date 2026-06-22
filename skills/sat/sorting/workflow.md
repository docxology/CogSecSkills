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
- For Sorting, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Sorting, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Sorting recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Sorting: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Sorting: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Sorting: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Sorting cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Sorting should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Sorting, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Sorting, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Sorting, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Sorting failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Sorting failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Sorting failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Sorting to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Sorting into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Sorting to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not select sort dimensions after viewing the data in a way that guarantees the preferred hypothesis dominates — dimension selection must precede sorting
- do not discard outliers without written justification; unexplained outliers are the technique's most valuable output
- do not collapse all items into a single undifferentiated list if multiple meaningful dimensions exist

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
