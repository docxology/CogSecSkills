# Workflow — Multiple Hypothesis Generation

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory the evidence and initial frame (read)
Read each evidence item and record what state of the world it is consistent with. Read any initial hypotheses already on the table. Note the framing assumptions embedded in those hypotheses — these are the most common source of artificial narrowing.

## Step 2 — Generate a candidate hypothesis set (reason)
Apply structured brainstorming: consider actor-based alternatives (different who), mechanism-based alternatives (different how), and intent-based alternatives (different why). Use devil's advocacy and red-team perspectives to ensure hypotheses hostile to the prevailing view are represented. Aim for at least three non-trivial hypotheses before considering the set draft-complete.

## Step 3 — Apply MECE discipline (reason)
Test each pair for mutual exclusivity: if both can simultaneously be true, either merge them into one hypothesis or add a conditional variable that makes them distinct. Test the full set for collective exhaustiveness: identify any remaining logical space not covered by any hypothesis and either add a new hypothesis or add a residual catch-all. Document every merge, split, and gap identified.

## Step 4 — Emit labeled hypothesis set and completeness audit (write)
Output each hypothesis with a label (H1–Hn), a description of its key distinguishing claim, a brief statement of what evidence pattern would most support or refute it, and any diagnostic collection requirement implied. Append the completeness audit documenting the MECE test results and any residual space.

## Anti-criteria (must NOT happen)
- do not allow the perceived likelihood of a hypothesis to determine whether it is included — low-probability hypotheses belong in the set if they are logically possible given the evidence
- do not declare the hypothesis set complete without explicitly testing for a logical remainder (the space covered by none of the stated hypotheses)
- do not merge two hypotheses that lead to different action recommendations, even if their descriptions sound similar

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
