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

## Anti-criteria (must NOT happen)
- Do not define the rating scale after populating cells — post-hoc scale design is a form of motivated reasoning
- Do not treat a matrix with many blank cells as complete — blanks must be explicitly acknowledged as gaps or N/A judgments
- Do not collapse the matrix into a single 'winning' row without showing the full pattern, as this hides the reasoning that reviewers need to audit
- Do not use the matrix as a score-sheet that mechanically outputs an answer; it is a reasoning aid, and the analyst must interpret the patterns

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
