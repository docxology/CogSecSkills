# Workflow — Issue Redefinition

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Document the original framing (read)
Write out the original question exactly as posed. Identify any explicit scope constraints in the tasking. Note what the question takes for granted — actors, time horizon, unit of analysis, success metric — before generating alternatives.

## Step 2 — Generate restatements using reframing levers (reason)
Apply at least six reframing levers in sequence, generating one or more restatements per lever: (1) Broaden — expand the scope or population. (2) Narrow — restrict the scope. (3) Invert — reframe as the opposite question. (4) Shift actor — change who the question is about. (5) Shift time horizon — ask it earlier or later. (6) Change unit of analysis — restate at a different level (individual / group / system). (7) Change success criterion — alter what a good answer would look like. Record all outputs without evaluating yet.

## Step 3 — Annotate assumptions and solution spaces (reason)
For each restatement, record: the core assumption it makes or removes relative to the original, and the solution space it opens or forecloses. Identify which restatements are genuinely distinct versus paraphrases. Flag any restatement that exposes an assumption in the original that had gone unexamined.

## Step 4 — Evaluate and select a preferred framing (reason)
Review all restatements against the consumer's actual decision need. Select the framing that best matches what the consumer can act on, is most tractable given available evidence, and minimizes unexamined embedded assumptions. If no single framing is clearly superior, propose keeping two framings in parallel and noting where they diverge.

## Step 5 — Produce the restatements register and preferred framing (write)
Write the full restatements register with all annotations. State the preferred framing clearly and explain why it was chosen. Document rejected framings and the reasons they were set aside — this record is part of the analytic transparency chain.

## Anti-criteria (must NOT happen)
- do not evaluate restatements while generating them — premature convergence defeats the purpose of the technique
- do not return only paraphrases of the original question; each restatement must use a distinct lever that changes the assumption set or solution space
- do not select a preferred framing simply because it matches the original question — if the original framing survives the exercise it should survive on its merits, with documented rationale
- do not skip documenting rejected framings — the record of alternatives considered is part of the analytic audit trail and cognitive-security transparency

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
