# Workflow — Morphological Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Decompose into parameters (read, reason)
Read the problem statement and identify 3–7 independent parameters that together define the space of possible configurations. For each parameter, enumerate 2–5 discrete values it could take. Record parameters as rows and values as columns in the morphological box.

## Step 2 — Prune impossible combinations (reason)
Cross each parameter value against all values of every other parameter. Mark any combination that is logically impossible, physically infeasible, or ruled out by confirmed evidence. Document the ruling-out reason for every pruned cell. The surviving cells form the feasible scenario inventory.

## Step 3 — Assess surviving scenarios (reason)
For each surviving combination, assess: (a) current evidential support (supported / neutral / contradicted by available reporting), (b) likelihood given base rates and context, (c) consequence if realized, and (d) whether current collection can distinguish this scenario from its neighbors.

## Step 4 — Report findings (write)
Produce the morphological box as a table, the scenario inventory as an annotated list, and priority findings calling out the most-likely scenario, the most-dangerous scenario, and any collection gap that prevents disambiguation of high-consequence cells.

## Evidence requirements
- For Morphological Analysis, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Morphological Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Morphological Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Morphological Analysis: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Morphological Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Morphological Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Morphological Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Morphological Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Morphological Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Morphological Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Morphological Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Morphological Analysis failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Morphological Analysis failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Morphological Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Morphological Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Morphological Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Morphological Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not prune cells based on intuition or familiarity before documenting the logical or evidential basis for exclusion
- do not allow the parameter list to be dominated by factors whose values are already known — the technique's value is in the under-explored dimensions
- do not report only the most-likely scenario; the most-dangerous scenario must always appear in the output even if assessed as low probability

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
