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
- For Analytic Matrices, anchor each cell rating and the pattern summary to a cited source excerpt or rationale, record blank cells as explicit collection gaps rather than silent omissions, and present the full grid as evidence so a reviewer can audit the reasoning instead of trusting a collapsed single answer.
- For Analytic Matrices, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the analytic matrix.
- Before recommending any Analytic Matrices action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Analytic Matrices: the row and column axes capture a genuinely independent, decidable relationship, every cell is rated against a scheme fixed before population, blank and conflicting cells are explicitly adjudicated, the dominant pattern is corroborated by multiple sources, and no unresolved contradiction would overturn the leading row.
- Medium for Analytic Matrices: the analytic matrix is plausible, but one important analytic question source, comparison case, or alternative explanation remains incomplete.
- Low for Analytic Matrices: the analytic matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Analytic Matrices cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Analytic Matrices, use only authorized analytic question, variables or hypotheses, and evidence or criteria, public or source-approved records, and caller-provided context needed for the defensive task.
- For Analytic Matrices, minimize person-level detail in the analytic matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Analytic Matrices, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Analytic Matrices: treating a grid riddled with blank cells as a finished analysis or letting the rating scale drift during population, so unexamined gaps and post-hoc scoring quietly manufacture a winning row that the underlying evidence never earned.
- Analytic Matrices: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Analytic Matrices: reporting the analytic matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Analytic Matrices outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the analytic matrix from Analytic Matrices into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Analytic Matrices to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with analytic question, variables or hypotheses, and evidence or criteria' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not define the rating scale after populating cells — post-hoc scale design is a form of motivated reasoning
- Do not treat a matrix with many blank cells as complete — blanks must be explicitly acknowledged as gaps or N/A judgments
- Do not collapse the matrix into a single 'winning' row without showing the full pattern, as this hides the reasoning that reviewers need to audit
- Do not use the matrix as a score-sheet that mechanically outputs an answer; it is a reasoning aid, and the analyst must interpret the patterns

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
