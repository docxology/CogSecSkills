# Workflow — Narrative Competition Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Collect and enumerate competing narratives (read, search)
Gather a representative sample of content about the topic from relevant platforms and outlets. Identify distinct narrative threads by clustering content on shared core claim, attribution (who is blamed or credited), and proposed meaning. Search for additional examples of each identified narrative across platforms to assess breadth.

## Step 2 — Characterize each narrative using framing analysis (reason)
For each narrative, document: core claim (what it asserts happened), causal attribution (why it happened and who is responsible), moral evaluation (what the situation means normatively), and proposed remedy (what should be done). Identify the dominant emotional frame (fear, outrage, hope, contempt) and the primary rhetorical devices used (anecdote, statistic misuse, false equivalence, authority appeal). Identify the target audience and primary propagation channels.

## Step 3 — Assess salience, resilience, and competition dynamics (reason)
Estimate relative salience using engagement metrics, search trend data, or media mention frequency. Assess resilience: does the narrative actively incorporate rebuttals? Does it have a loyal core audience insulated from counter-evidence? Analyze competition dynamics: are the narratives directly refuting each other, or competing for attention on parallel tracks? Identify which narrative currently holds frame advantage and why.

## Step 4 — Produce the competition map and assessment report (write)
Write the narrative competition map table and the full assessment report. The report should cover: narrative characterizations, salience comparison, resilience analysis, competition dynamics, identified rhetorical vulnerabilities in false narratives, and recommendations for monitoring cadence or protective communication strategy. Clearly separate analytical findings from any recommended communications actions.

## Evidence requirements
- For Narrative Competition Analysis, bind each finding to a labeled source — platform observations, narrative movement, automation signals, and provenance data, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Narrative Competition Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Narrative Competition Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Narrative Competition Analysis: independent lines of platform observations, narrative movement, automation signals, and provenance data converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Narrative Competition Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Narrative Competition Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Narrative Competition Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Narrative Competition Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Narrative Competition Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Narrative Competition Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Narrative Competition Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Narrative Competition Analysis failure: treating engagement volume as proof of authenticity or coordinated intent.
- Narrative Competition Analysis failure: producing guidance that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Narrative Competition Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Narrative Competition Analysis to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Narrative Competition Analysis into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Narrative Competition Analysis to map supplied narratives, automation signals, or platform affordance risks for defensive review' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate narrative salience with truth value — a highly salient narrative may be false, and a low-salience narrative may be accurate
- Do not design counter-narrative messaging within this analytical workflow; this technique produces analysis, not communications products
- Do not use audience characterizations to demean or stereotype the people who hold a narrative — the goal is understanding, not contempt
- Do not treat narrative competition as zero-sum; sometimes the goal is to raise information quality across the ecosystem, not to 'win' for one side

## AGEINT upstream
`docs/ageint/information-environment.md`
