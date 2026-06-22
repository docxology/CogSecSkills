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
- For Logical Fallacy Detection, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Logical Fallacy Detection, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Logical Fallacy Detection recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Logical Fallacy Detection: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Logical Fallacy Detection: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Logical Fallacy Detection: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Logical Fallacy Detection cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Logical Fallacy Detection should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Logical Fallacy Detection, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Logical Fallacy Detection, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Logical Fallacy Detection, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Logical Fallacy Detection failure: mistaking persuasive resonance for verified harm or intent.
- Logical Fallacy Detection failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Logical Fallacy Detection failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Logical Fallacy Detection to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Logical Fallacy Detection into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Logical Fallacy Detection to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat the presence of any fallacy as automatic proof the conclusion is false — clearly state that a fallacy means the argument does not establish the conclusion, not that the conclusion is wrong
- Do not use vague labels like 'emotional manipulation' without mapping to a specific named fallacy (e.g., appeal to fear, appeal to pity) — precision is the analytic standard
- Do not overlook implicit premises — many informal fallacies hide in what the argument assumes rather than what it states
- Do not conflate bad rhetoric with bad faith — fallacious arguments are often made by people who genuinely hold the conclusion; intent is separate from logical assessment

## AGEINT upstream
`docs/ageint/cognitive-security.md`
