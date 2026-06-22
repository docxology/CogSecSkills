# Workflow — Analysis of Competing Hypotheses (ACH)

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Enumerate hypotheses (reason, search)
Generate a **complete and mutually exclusive** set of hypotheses. Include the
deception hypothesis ("someone wants me to believe H1") and a residual
"something we haven't thought of". If the user supplied a partial set, complete
it; never evaluate fewer than three.

## Step 2 — List evidence and arguments (read, search)
Assemble every relevant item: facts, arguments, assumptions, and **absence of
evidence** (things that should be present under some hypothesis but are not).
Tag each item with source and reliability (link to
`cognitive_security.source_credibility_evaluation` if grading is needed).

## Step 3 — Build the matrix (reason)
For each (evidence, hypothesis) cell, score consistency:
- **C** — consistent with the hypothesis
- **I** — inconsistent with the hypothesis
- **N** — not applicable / no bearing

## Step 4 — Assess diagnosticity (reason)
Mark each evidence ROW's diagnosticity. A row that is **C for every hypothesis**
has **no diagnostic value** — flag it and set it aside. The analysis lives in
the rows that discriminate.

## Step 5 — Refine (reason)
Delete non-diagnostic evidence and merge redundant hypotheses. Re-examine items
where everything is "C" — you may have mis-scored, or the hypotheses are not
truly distinct.

## Step 6 — Draw tentative conclusions (reason)
Rank hypotheses by **inconsistency score** (count/weight of I marks). The
hypothesis with the **fewest** inconsistencies is provisionally strongest. Do
NOT pick the one with the most "C" marks — that is the bias trap.

## Step 7 — Sensitivity analysis (reason)
Identify the one or two evidence items that, if wrong or deceptive, would change
the ranking. State how the conclusion depends on them. Re-verify those items.

## Step 8 — Report with indicators (write)
Emit:
- the matrix,
- the ranking with inconsistency scores,
- the single most diagnostic item and the single most damaging item,
- a calibrated confidence statement,
- **indicators**: future observations that would confirm or overturn the lead
  hypothesis (link to `sat.indicators_generation`).

## Evidence requirements
- For Analysis of Competing Hypotheses (ACH), bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Analysis of Competing Hypotheses (ACH), keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Analysis of Competing Hypotheses (ACH) recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Analysis of Competing Hypotheses (ACH): independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Analysis of Competing Hypotheses (ACH): the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Analysis of Competing Hypotheses (ACH): the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Analysis of Competing Hypotheses (ACH) cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Analysis of Competing Hypotheses (ACH) should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Analysis of Competing Hypotheses (ACH), use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Analysis of Competing Hypotheses (ACH), protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Analysis of Competing Hypotheses (ACH), do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Analysis of Competing Hypotheses (ACH) failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Analysis of Competing Hypotheses (ACH) failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Analysis of Competing Hypotheses (ACH) failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Analysis of Competing Hypotheses (ACH) to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Analysis of Competing Hypotheses (ACH) into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Analysis of Competing Hypotheses (ACH) to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Ranking by weight of confirming evidence instead of by least inconsistency.
- Dropping a hypothesis because it is unpopular rather than because evidence
- Treating non-diagnostic evidence as support.

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
