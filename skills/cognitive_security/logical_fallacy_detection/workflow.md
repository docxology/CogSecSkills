# Workflow — Logical Fallacy Detection

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Segment the argument into claims and inferences (read)
Parse the text into: (a) explicit premises/assertions, (b) implicit premises, (c) inferential steps ('therefore', 'because', 'this shows that'), and (d) the conclusion(s). Number each element for reference in the catalogue.

## Step 2 — Check formal validity of each inferential step (reason)
Examine each inference for formal fallacies: affirming the consequent, denying the antecedent, undistributed middle, illicit conversion, equivocation on a term used in two steps. Record each finding with the claim numbers involved and the standard name of the fallacy.

## Step 3 — Scan premises and appeals for informal fallacies (reason)
Review each premise and rhetorical move against the taxonomy of informal fallacies: relevance fallacies (ad hominem, ad verecundiam, ad populum, red herring, straw man), presumption fallacies (false dilemma, begging the question, hasty generalization, post hoc ergo propter hoc, slippery slope), and clarity fallacies (equivocation, amphiboly, accent). Note the text passage, fallacy name, and why the move is fallacious in this instance.

## Step 4 — Rate severity and assess what survives (reason)
For each identified fallacy, rate severity: FATAL (the conclusion does not follow without this move), WEAKENS (the argument is less compelling but other premises still partially support the conclusion), or MINOR (local sub-claim is unsupported but does not affect the main argument). Identify which, if any, conclusions remain supported by the non-fallacious portions of the argument.

## Step 5 — Emit fallacy catalogue and argument assessment (write)
Produce the fallacy table with location, name, category, explanation, and severity. Write the argument assessment narrative: overall logical validity verdict, which moves are purely rhetorical (persuasive but not warranting), which conclusions survive scrutiny, and the argument's persuasive-vs-epistemic gap.

## Anti-criteria (must NOT happen)
- Do not treat the presence of any fallacy as automatic proof the conclusion is false — clearly state that a fallacy means the argument does not establish the conclusion, not that the conclusion is wrong
- Do not use vague labels like 'emotional manipulation' without mapping to a specific named fallacy (e.g., appeal to fear, appeal to pity) — precision is the analytic standard
- Do not overlook implicit premises — many informal fallacies hide in what the argument assumes rather than what it states
- Do not conflate bad rhetoric with bad faith — fallacious arguments are often made by people who genuinely hold the conclusion; intent is separate from logical assessment

## AGEINT upstream
`docs/ageint/cognitive-security.md`
