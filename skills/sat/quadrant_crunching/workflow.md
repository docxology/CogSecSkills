# Workflow — Quadrant Crunching

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Select axes (read, reason)
Read the problem statement and dominant assessment. Identify the two assumptions (or variables) that are simultaneously most consequential for the outcome and most uncertain. Assign each a binary pair of poles (e.g., Actor X is capable / Actor X is not capable; Environment is permissive / Environment is restrictive). Document why these axes were chosen over alternatives.

## Step 2 — Populate the matrix (reason)
Construct an N×M table. For each cell, write a short scenario title and a one- to two-sentence narrative describing the world in which both axis poles co-occur. If a cell is internally incoherent (i.e., the two poles cannot logically co-exist), label it Incoherent and explain why. Resist the urge to pre-filter cells as 'impossible' without explicit reasoning.

## Step 3 — Rate plausibility and identify indicators (reason, write)
For each coherent cell assign a plausibility rating (High / Medium / Low) with a brief evidence citation. Identify one to three observable indicators that would confirm each scenario is unfolding. Note which cell(s) the current dominant assessment inhabits, and flag any Medium or High plausibility alternatives it ignores. Emit the matrix, narratives, and a summary of implications for the analytic question.

## Evidence requirements
- For Quadrant Crunching, anchor each cell's coherence judgment, plausibility rating, and confirming indicators to concrete evidence rather than to confidence in the base case, document the evidentiary reason any cell is labeled incoherent, and bind the neglected-cell findings to specific evidence showing the dominant assessment's blind spot rather than asserting it.
- For Quadrant Crunching, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the scenario matrix.
- Before recommending any Quadrant Crunching action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Quadrant Crunching: the two axes were chosen for maximum consequence and genuine independent uncertainty, every coherent matrix cell was examined on its own internal logic before its evidence-anchored plausibility rating, the neglected cells the dominant assessment ignores are explicitly surfaced with reasoning, and no unresolved contradiction would change which alternatives deserve attention.
- Medium for Quadrant Crunching: the scenario matrix is plausible, but one important problem statement source, comparison case, or alternative explanation remains incomplete.
- Low for Quadrant Crunching: the scenario matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Quadrant Crunching cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Quadrant Crunching, use only authorized problem statement, dominant assessment, and candidate assumptions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Quadrant Crunching, minimize person-level detail in the scenario matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Quadrant Crunching, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Quadrant Crunching: declaring the scenario space mapped while letting the dominant assessment pre-filter cells as impossible without incoherence reasoning, choosing axes that are correlated rather than independent or merely easy to enumerate, or anchoring plausibility on analyst confidence instead of evidence, so the matrix reproduces tunnel vision under the appearance of having considered all combinations.
- Quadrant Crunching: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Quadrant Crunching: reporting the scenario matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Quadrant Crunching outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the scenario matrix from Quadrant Crunching into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Quadrant Crunching to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with problem statement, dominant assessment, and candidate assumptions' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow the current dominant assessment to pre-filter cells as impossible without explicit incoherence reasoning
- do not reduce axes to variables that are actually correlated — each axis must represent an independent uncertain dimension
- do not collapse all Low-plausibility cells into a single residual 'other' bucket; each must appear explicitly
- do not let the axis selection be driven by ease of enumeration rather than consequence and uncertainty

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
