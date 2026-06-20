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
- For Narrative Competition Analysis, tie each narrative competition map, and competition assessment report claim to concrete evidence from the specific narrative corpus, topic definition, and engagement metrics item, source excerpt, observation, or command result that supports it.
- For Narrative Competition Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the narrative competition map.
- Before recommending any Narrative Competition Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Narrative Competition Analysis: the narrative competition map is supported by multiple independent platform observations, narrative movement, automation signals, and provenance data; collect and enumerate competing narratives and characterize each narrative using framing analysis checks agree, and no unresolved contradiction would change the result.
- Medium for Narrative Competition Analysis: the narrative competition map is plausible, but one important narrative corpus source, comparison case, or alternative explanation remains incomplete.
- Low for Narrative Competition Analysis: the narrative competition map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Narrative Competition Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating information_environment evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Narrative Competition Analysis, use only authorized narrative corpus, topic definition, and engagement metrics, public or source-approved records, and caller-provided context needed for the defensive task.
- For Narrative Competition Analysis, minimize person-level detail in the narrative competition map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Narrative Competition Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Narrative Competition Analysis: treating narrative corpus as complete when collect and enumerate competing narratives and characterize each narrative using framing analysis checks or contradictory evidence are missing.
- Narrative Competition Analysis: producing advice that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Narrative Competition Analysis: reporting the narrative competition map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Narrative Competition Analysis outputs to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the narrative competition map from Narrative Competition Analysis into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Narrative Competition Analysis to map supplied narratives, automation signals, or platform affordance risks for defensive review with narrative corpus, topic definition, and engagement metrics' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate narrative salience with truth value — a highly salient narrative may be false, and a low-salience narrative may be accurate
- Do not design counter-narrative messaging within this analytical workflow; this technique produces analysis, not communications products
- Do not use audience characterizations to demean or stereotype the people who hold a narrative — the goal is understanding, not contempt
- Do not treat narrative competition as zero-sum; sometimes the goal is to raise information quality across the ecosystem, not to 'win' for one side

## AGEINT upstream
`docs/ageint/information-environment.md`
