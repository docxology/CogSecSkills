# Workflow — Analysis of Competing Hypotheses

Harness-neutral agentic procedure. Each step names the **tool verb** it uses
(see `skill.yaml` → `tools`). A harness adapter binds each verb to concrete
tools; the logic here is identical across harnesses.

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

## Anti-criteria (must NOT happen)
- Ranking by weight of confirming evidence instead of by least inconsistency.
- Dropping a hypothesis because it is unpopular rather than because evidence
  disconfirms it.
- Treating non-diagnostic evidence as support.

## AGEINT upstream
`docs/ageint/` → structured-analytic-techniques (hypothesis testing family).
