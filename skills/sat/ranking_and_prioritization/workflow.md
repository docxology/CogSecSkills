# Workflow — Ranking & Prioritization

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish criteria and weights (read, ask)
Read the item list and decision context. Identify two to five evaluation criteria (e.g., likelihood, impact, reversibility, time-sensitivity). Assign relative weights summing to 1.0. If weights cannot be derived from context, ask the analyst or decision maker to specify them explicitly. Document the rationale for each criterion and its weight.

## Step 2 — Score each item (reason)
For each item, assign a raw score (e.g., 1–5) on each criterion using a consistent, pre-defined scale. For paired comparison: compare each item pair on each criterion and record the winner. Compute total weighted scores. Flag any item that scores near the median on all criteria — it may deserve reconsideration as a borderline case.

## Step 3 — Rank, sense-check, and emit (reason, write)
Order items by total weighted score. Identify any rank that conflicts strongly with subject-matter intuition and investigate the conflict — it is either a criterion gap or an informative analytic finding. Run a one-factor sensitivity sweep varying each top weight by ±20% to identify rank-sensitive placements. Emit the scoring matrix, ranked list, placement rationales, and sensitivity notes.

## Evidence requirements
- For Ranking & Prioritization, tie each raw score, weight, and final placement to concrete evidence about the item list and decision context, disclose the criteria and weights that produced the order, and report the sensitivity sweep so that any ranking fragile to small weight changes is flagged as material rather than presented as a settled conclusion.
- For Ranking & Prioritization, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the scoring matrix.
- Before recommending any Ranking & Prioritization action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Ranking & Prioritization: the criteria and weights were fixed before scoring and reflect the decision context rather than a preferred outcome, each item's scores trace to a consistent pre-defined scale, the sensitivity sweep shows the top placements survive plausible weight shifts, and no unresolved contradiction between the ranking and subject-matter intuition is left uninvestigated.
- Medium for Ranking & Prioritization: the scoring matrix is plausible, but one important item list source, comparison case, or alternative explanation remains incomplete.
- Low for Ranking & Prioritization: the scoring matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Ranking & Prioritization cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Ranking & Prioritization, use only authorized item list, criteria, and decision context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Ranking & Prioritization, minimize person-level detail in the scoring matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Ranking & Prioritization, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Ranking & Prioritization: declaring the priority order defensible while defining or adjusting criteria after scoring began, letting a single high-salience item anchor the scale for all others, or suppressing the sensitivity analysis when the top-ranked item collapses under a small weight change, so a pre-held preference is retroactively rationalized as an objective, criterion-transparent result.
- Ranking & Prioritization: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Ranking & Prioritization: reporting the scoring matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Ranking & Prioritization outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the scoring matrix from Ranking & Prioritization into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Ranking & Prioritization to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with item list, criteria, and decision context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not define or adjust criteria after scoring has begun — this retroactively rationalizes a pre-held ranking
- do not allow a single high-salience item to anchor the scoring scale for all others (set the scale independently)
- do not suppress the sensitivity analysis when the top-ranked item is fragile — fragility is analytically material
- do not present the ranked list without disclosing the weights and criteria that produced it

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
