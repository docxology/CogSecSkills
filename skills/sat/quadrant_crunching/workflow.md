# Workflow — Quadrant Crunching

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Select axes (read, reason)
Read the problem statement and dominant assessment. Identify the two assumptions (or variables) that are simultaneously most consequential for the outcome and most uncertain. Assign each a binary pair of poles (e.g., Actor X is capable / Actor X is not capable; Environment is permissive / Environment is restrictive). Document why these axes were chosen over alternatives.

## Step 2 — Populate the matrix (reason)
Construct an N×M table. For each cell, write a short scenario title and a one- to two-sentence narrative describing the world in which both axis poles co-occur. If a cell is internally incoherent (i.e., the two poles cannot logically co-exist), label it Incoherent and explain why. Resist the urge to pre-filter cells as 'impossible' without explicit reasoning.

## Step 3 — Rate plausibility and identify indicators (reason, write)
For each coherent cell assign a plausibility rating (High / Medium / Low) with a brief evidence citation. Identify one to three observable indicators that would confirm each scenario is unfolding. Note which cell(s) the current dominant assessment inhabits, and flag any Medium or High plausibility alternatives it ignores. Emit the matrix, narratives, and a summary of implications for the analytic question.

## Evidence requirements
- For Quadrant Crunching, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Quadrant Crunching, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Quadrant Crunching recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Quadrant Crunching: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Quadrant Crunching: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Quadrant Crunching: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Quadrant Crunching cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Quadrant Crunching should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Quadrant Crunching, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Quadrant Crunching, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Quadrant Crunching, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Quadrant Crunching failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Quadrant Crunching failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Quadrant Crunching failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Quadrant Crunching to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Quadrant Crunching into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Quadrant Crunching to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow the current dominant assessment to pre-filter cells as impossible without explicit incoherence reasoning
- do not reduce axes to variables that are actually correlated — each axis must represent an independent uncertain dimension
- do not collapse all Low-plausibility cells into a single residual 'other' bucket; each must appear explicitly
- do not let the axis selection be driven by ease of enumeration rather than consequence and uncertainty

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
