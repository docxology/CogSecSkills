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
- For Morphological Analysis, tie each parameter, each enumerated value, and every pruning decision to concrete evidence from the problem statement and known constraints, recording the ruling-out reason per excluded cell; a combination removed without evidential justification is an unexamined possibility and must be reinstated or its exclusion explicitly defended.
- For Morphological Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the morphological box.
- Before recommending any Morphological Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Morphological Analysis: the chosen parameters are genuinely independent, each value set was enumerated exhaustively before any pruning, every excluded cell carries a documented logical or evidential reason, and no unresolved contradiction would change the surviving scenario inventory or which cells are flagged most-likely and most-dangerous.
- Medium for Morphological Analysis: the morphological box is plausible, but one important problem statement source, comparison case, or alternative explanation remains incomplete.
- Low for Morphological Analysis: the morphological box rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Morphological Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Morphological Analysis, use only authorized problem statement, and known constraints, public or source-approved records, and caller-provided context needed for the defensive task.
- For Morphological Analysis, minimize person-level detail in the morphological box; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Morphological Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Morphological Analysis: treating the scenario space as bounded when cells were pruned on intuition or familiarity without a documented basis, or when co-varying parameters were left un-collapsed, so the configuration where the surprise actually lives is silently excluded from the inventory.
- Morphological Analysis: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Morphological Analysis: reporting the morphological box without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Morphological Analysis outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the morphological box from Morphological Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Morphological Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with problem statement, and known constraints' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not prune cells based on intuition or familiarity before documenting the logical or evidential basis for exclusion
- do not allow the parameter list to be dominated by factors whose values are already known — the technique's value is in the under-explored dimensions
- do not report only the most-likely scenario; the most-dangerous scenario must always appear in the output even if assessed as low probability

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
