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
- For Analysis of Competing Hypotheses (ACH), tie every consistency rating and the final ranking to specific evidence items with their source and reliability, treat absence of expected evidence as evidence in its own right, and flag any row that is consistent with all hypotheses as non-diagnostic rather than as support.
- For Analysis of Competing Hypotheses (ACH), label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the matrix.
- Before recommending any Analysis of Competing Hypotheses (ACH) action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Analysis of Competing Hypotheses (ACH): the hypothesis set is complete and mutually exclusive, the inconsistency ranking is driven by diagnostic evidence that survives the sensitivity check on its one or two load-bearing items, multiple independent sources corroborate those items, and no unresolved contradiction would reorder the least-disconfirmed hypothesis.
- Medium for Analysis of Competing Hypotheses (ACH): the matrix is plausible, but one important question source, comparison case, or alternative explanation remains incomplete.
- Low for Analysis of Competing Hypotheses (ACH): the matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Analysis of Competing Hypotheses (ACH) cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Analysis of Competing Hypotheses (ACH), use only authorized question, hypotheses, and evidence, public or source-approved records, and caller-provided context needed for the defensive task.
- For Analysis of Competing Hypotheses (ACH), minimize person-level detail in the matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Analysis of Competing Hypotheses (ACH), do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Analysis of Competing Hypotheses (ACH): ranking the hypothesis with the most confirming marks as strongest instead of the least disconfirmed, or omitting the deception and residual hypotheses, so an unfalsified favourite survives because rival explanations were never seriously tested.
- Analysis of Competing Hypotheses (ACH): producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Analysis of Competing Hypotheses (ACH): reporting the matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Analysis of Competing Hypotheses (ACH) outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the matrix from Analysis of Competing Hypotheses (ACH) into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Analysis of Competing Hypotheses (ACH) to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with question, hypotheses, and evidence' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Ranking by weight of confirming evidence instead of by least inconsistency.
- Dropping a hypothesis because it is unpopular rather than because evidence
- Treating non-diagnostic evidence as support.

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
