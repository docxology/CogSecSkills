# Workflow — Logical Coherence Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract and segment (read)
Read the full argument text. Identify the main conclusion(s). Segment the text into distinct claim units. Note the explicit premises offered in support of each conclusion.

## Step 2 — Build argument map and surface hidden premises (reason)
Construct the argument map using Toulmin structure (Claim / Data / Warrant / Backing / Qualifier / Rebuttal) or a simpler premise-conclusion schema. Identify every inferential step and make hidden premises explicit — state what must be true for each step to hold that the author did not state.

## Step 3 — Check validity and classify fallacies (reason)
For each inferential step, test formal validity: does the conclusion form follow necessarily from the premises? If not, name the formal fallacy (e.g., affirming the consequent, undistributed middle). Then check for informal fallacies in evidence use and rhetorical moves (ad hominem, strawman, false dilemma, slippery slope, appeal to authority, begging the question, equivocation). Assess severity: does this fallacy alone defeat the argument, or weaken it?

## Step 4 — Assess coherence and produce verdict (reason, write)
Synthesize: does the conclusion follow from the stated premises under valid inference? State the conditions under which the argument would hold and what would have to change. Assign an overall coherence rating (Valid / Valid-with-caveats / Invalid-but-restorable / Invalid). Write specific recommendations: premises to strengthen, inferences to make explicit, or a rejection justification.

## Step 5 — Produce fallacy register and annotated output (write)
Compile the fallacy register table with type, text location, description, and severity. Finalize the argument map with annotations. Write the coherence verdict narrative. If the artifact is a disinformation narrative, note which logical breaks are most rebuttable and most likely to resonate with target audiences.

## Anti-criteria (must NOT happen)
- do not conflate the argument being false with it being logically invalid — a valid argument can have false premises, and a sound conclusion can be reached by bad inference
- do not list rhetorical weaknesses as formal fallacies — distinguish formal invalidity from persuasive weaknesses
- do not assess logical coherence while simultaneously adjudicating the truth of the premises — keep those steps separate
- do not declare an argument incoherent solely because it conflicts with the reviewer's prior beliefs

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
