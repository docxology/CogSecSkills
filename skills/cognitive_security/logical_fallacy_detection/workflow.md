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

## Evidence requirements
- For Logical Fallacy Detection, tie every catalogued fallacy and severity rating to concrete evidence — a specific quoted passage and the numbered premise or inferential step it occupies — and state explicitly that a fallacy unsupported by such evidence is an assertion about reasoning, not a demonstrated flaw.
- For Logical Fallacy Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the fallacy catalogue.
- Before recommending any Logical Fallacy Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Logical Fallacy Detection: each catalogued fallacy is anchored to a quoted passage and a precisely named formal or informal type, the validity verdict is stable after the argument is segmented into premises and inferential steps, and no unresolved contradiction would change which conclusions survive removal of the fallacious moves.
- Medium for Logical Fallacy Detection: the fallacy catalogue is plausible, but one important argument text source, comparison case, or alternative explanation remains incomplete.
- Low for Logical Fallacy Detection: the fallacy catalogue rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Logical Fallacy Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Logical Fallacy Detection, use only authorized argument text, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Logical Fallacy Detection, minimize person-level detail in the fallacy catalogue; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Logical Fallacy Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Logical Fallacy Detection: treating the presence of a fallacy as proof the conclusion is false, or over-calling minor moves as fatal, while overlooking implicit premises where many informal fallacies hide, so the catalogue misstates the argument's true epistemic standing.
- Logical Fallacy Detection: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Logical Fallacy Detection: reporting the fallacy catalogue without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Logical Fallacy Detection outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the fallacy catalogue from Logical Fallacy Detection into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Logical Fallacy Detection to assess supplied material for manipulation indicators and recommend resilience measures with argument text, and context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat the presence of any fallacy as automatic proof the conclusion is false — clearly state that a fallacy means the argument does not establish the conclusion, not that the conclusion is wrong
- Do not use vague labels like 'emotional manipulation' without mapping to a specific named fallacy (e.g., appeal to fear, appeal to pity) — precision is the analytic standard
- Do not overlook implicit premises — many informal fallacies hide in what the argument assumes rather than what it states
- Do not conflate bad rhetoric with bad faith — fallacious arguments are often made by people who genuinely hold the conclusion; intent is separate from logical assessment

## AGEINT upstream
`docs/ageint/cognitive-security.md`
