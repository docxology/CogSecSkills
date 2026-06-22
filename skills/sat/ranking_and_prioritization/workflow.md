# Workflow — Ranking & Prioritization

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish criteria and weights (read, ask)
Read the item list and decision context. Identify two to five evaluation criteria (e.g., likelihood, impact, reversibility, time-sensitivity). Assign relative weights summing to 1.0. If weights cannot be derived from context, ask the analyst or decision maker to specify them explicitly. Document the rationale for each criterion and its weight.

## Step 2 — Score each item (reason)
For each item, assign a raw score (e.g., 1–5) on each criterion using a consistent, pre-defined scale. For paired comparison: compare each item pair on each criterion and record the winner. Compute total weighted scores. Flag any item that scores near the median on all criteria — it may deserve reconsideration as a borderline case.

## Step 3 — Rank, sense-check, and emit (reason, write)
Order items by total weighted score. Identify any rank that conflicts strongly with subject-matter intuition and investigate the conflict — it is either a criterion gap or an informative analytic finding. Run a one-factor sensitivity sweep varying each top weight by ±20% to identify rank-sensitive placements. Emit the scoring matrix, ranked list, placement rationales, and sensitivity notes.

## Evidence requirements
- For Ranking & Prioritization, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Ranking & Prioritization, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Ranking & Prioritization recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Ranking & Prioritization: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Ranking & Prioritization: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Ranking & Prioritization: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Ranking & Prioritization cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Ranking & Prioritization should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Ranking & Prioritization, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Ranking & Prioritization, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Ranking & Prioritization, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Ranking & Prioritization failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Ranking & Prioritization failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Ranking & Prioritization failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Ranking & Prioritization to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Ranking & Prioritization into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Ranking & Prioritization to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not define or adjust criteria after scoring has begun — this retroactively rationalizes a pre-held ranking
- do not allow a single high-salience item to anchor the scoring scale for all others (set the scale independently)
- do not suppress the sensitivity analysis when the top-ranked item is fragile — fragility is analytically material
- do not present the ranked list without disclosing the weights and criteria that produced it

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
