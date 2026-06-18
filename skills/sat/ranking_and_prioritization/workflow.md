# Workflow — Ranking & Prioritization

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish criteria and weights (read, ask)
Read the item list and decision context. Identify two to five evaluation criteria (e.g., likelihood, impact, reversibility, time-sensitivity). Assign relative weights summing to 1.0. If weights cannot be derived from context, ask the analyst or decision maker to specify them explicitly. Document the rationale for each criterion and its weight.

## Step 2 — Score each item (reason)
For each item, assign a raw score (e.g., 1–5) on each criterion using a consistent, pre-defined scale. For paired comparison: compare each item pair on each criterion and record the winner. Compute total weighted scores. Flag any item that scores near the median on all criteria — it may deserve reconsideration as a borderline case.

## Step 3 — Rank, sense-check, and emit (reason, write)
Order items by total weighted score. Identify any rank that conflicts strongly with subject-matter intuition and investigate the conflict — it is either a criterion gap or an informative analytic finding. Run a one-factor sensitivity sweep varying each top weight by ±20% to identify rank-sensitive placements. Emit the scoring matrix, ranked list, placement rationales, and sensitivity notes.

## Anti-criteria (must NOT happen)
- do not define or adjust criteria after scoring has begun — this retroactively rationalizes a pre-held ranking
- do not allow a single high-salience item to anchor the scoring scale for all others (set the scale independently)
- do not suppress the sensitivity analysis when the top-ranked item is fragile — fragility is analytically material
- do not present the ranked list without disclosing the weights and criteria that produced it

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
