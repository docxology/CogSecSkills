# Workflow — Structured Brainstorming

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Frame the problem and set aside prior framing (read)
Read the problem statement. If prior analytic framing exists, note it explicitly and declare it suspended for the divergence phase. Doing so acknowledges the anchor without being constrained by it.

## Step 2 — Diverge: unconstrained idea generation (reason, ask)
Generate every plausible idea, hypothesis, threat vector, or option, including low-probability ones. Defer all judgment. If idea flow is drying up early, ask the analyst: 'What would an adversary want us not to think of here?' and 'What assumption would have to be wrong for a completely different hypothesis to be correct?'

## Step 3 — Cluster and apply convergence criteria (reason)
Group ideas by theme or type. Apply the convergence criteria to rank clusters and individual ideas. Explicitly flag ideas that are novel but low-probability — they belong in the output even if not in the shortlist.

## Step 4 — Produce raw inventory and ranked shortlist (write)
Emit the complete raw idea inventory (divergence output) and the ranked shortlist table (convergence output). For every idea excluded from the shortlist, write a one-line reason. Note any idea suppressed by social or hierarchical pressure that re-emerged during the structured process.

## Anti-criteria (must NOT happen)
- do not allow criticism, ranking, or comparative judgment during the divergence phase — even implicit facial reactions that signal 'that is a bad idea' violate the technique
- do not allow the prior dominant hypothesis to appear first in the divergence list; it anchors generation — introduce it mid-list or randomize order
- do not omit discarded ideas from the written output; they must appear with explicit rejection rationale so reviewers can challenge the convergence step

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
