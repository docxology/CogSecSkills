# Workflow — Analytic Matrices

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Define matrix dimensions (read, reason)
Identify what will occupy rows versus columns based on the analytic question. Common configurations: hypotheses × evidence items (for ACH-style analysis); actors × capabilities or behaviors (for threat or influence-operation mapping); options × evaluation criteria (for decision support). Confirm the two axes are genuinely independent dimensions, not restatements of each other.

## Step 2 — Establish the rating scheme (reason)
Before populating cells, define the rating scale. For evidence-consistency matrices: C (consistent), I (inconsistent), N/A (not applicable), ? (unknown). For capability matrices: H/M/L or a numeric score. Record the legend explicitly. Never let the scale drift during population.

## Step 3 — Populate the matrix (read, reason)
Working systematically row by row, evaluate each cell against the defined scale using available evidence. Record the rating and a brief source citation or rationale. Flag cells that are ambiguous or where evidence conflicts. Do not skip cells — a deliberate N/A is different from a blank.

## Step 4 — Identify patterns and anomalies (reason, write)
Scan completed rows for dominance (one hypothesis/option consistently rates better), scan columns for diagnostic value (some evidence items discriminate strongly while others do not), and flag any row or column that is entirely blank or entirely consistent (the former is a gap; the latter may indicate a non-discriminating dimension). Note conflicting cells and determine whether they reflect source conflict or genuine ambiguity.

## Step 5 — Produce summary and implications (write)
Write a pattern summary: which row(s) are best supported, which evidence is most diagnostic, what the key gaps are, and what the matrix implies for the analytic question. Include the matrix itself and the legend as the core deliverable. Note any cells where the analyst's confidence is low and additional collection would be highest value.

## Evidence requirements
- For Analytic Matrices, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Analytic Matrices, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Analytic Matrices recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Analytic Matrices: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Analytic Matrices: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Analytic Matrices: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Analytic Matrices cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Analytic Matrices should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Analytic Matrices, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Analytic Matrices, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Analytic Matrices, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Analytic Matrices failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Analytic Matrices failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Analytic Matrices failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Analytic Matrices to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Analytic Matrices into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Analytic Matrices to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not define the rating scale after populating cells — post-hoc scale design is a form of motivated reasoning
- Do not treat a matrix with many blank cells as complete — blanks must be explicitly acknowledged as gaps or N/A judgments
- Do not collapse the matrix into a single 'winning' row without showing the full pattern, as this hides the reasoning that reviewers need to audit
- Do not use the matrix as a score-sheet that mechanically outputs an answer; it is a reasoning aid, and the analyst must interpret the patterns

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
