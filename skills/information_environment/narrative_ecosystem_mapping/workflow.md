# Workflow — Narrative Ecosystem Mapping

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Scope and collect (read, search)
Define the information space boundaries (topic, language, platform, time window). Collect or retrieve a representative sample of content—posts, articles, broadcasts—and compile any known actor lists or prior reports. Do not pre-filter content by perceived credibility at this stage.

## Step 2 — Identify and cluster narratives (reason)
Read through the collected content and inductively identify recurring narratives—coherent story lines, frames, or explanatory claims. Cluster surface-level variants under a master narrative. Name each narrative in one crisp sentence capturing its central claim and implied protagonist/antagonist. Distinguish master narratives from supporting sub-narratives.

## Step 3 — Map carriers and amplification pathways (reason)
For each narrative, identify who carries it (media outlets, influencer accounts, state actors, grassroots communities, bot networks) and how it flows—which platforms host it, which actors amplify it into new audience segments, and whether coordination appears organic or synthetic.

## Step 4 — Assess audience segments and resonance (reason)
Identify the primary audience segments each narrative targets. Assess resonance drivers: which identity concerns, prior beliefs, or grievances make each narrative sticky for its target audience. Note segments that are under-served by credible counter-narratives.

## Step 5 — Identify ecosystem vulnerabilities and produce map (reason, write)
Identify structural vulnerabilities: narrative vacuums, over-reliance on a small number of high-centrality carriers, audiences with low counter-narrative exposure. Produce the narrative inventory table and the structured ecosystem map, noting the competition dynamics and flagging the highest-priority vulnerabilities.

## Evidence requirements
- For Narrative Ecosystem Mapping, bind each finding to a labeled source — platform observations, narrative movement, automation signals, and provenance data, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Narrative Ecosystem Mapping, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Narrative Ecosystem Mapping recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Narrative Ecosystem Mapping: independent lines of platform observations, narrative movement, automation signals, and provenance data converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Narrative Ecosystem Mapping: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Narrative Ecosystem Mapping: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Narrative Ecosystem Mapping cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Narrative Ecosystem Mapping should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Narrative Ecosystem Mapping, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Narrative Ecosystem Mapping, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Narrative Ecosystem Mapping, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Narrative Ecosystem Mapping failure: treating engagement volume as proof of authenticity or coordinated intent.
- Narrative Ecosystem Mapping failure: producing guidance that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Narrative Ecosystem Mapping failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Narrative Ecosystem Mapping to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Narrative Ecosystem Mapping into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Narrative Ecosystem Mapping to map supplied narratives, automation signals, or platform affordance risks for defensive review' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate the existence of a narrative with evidence that it is coordinated or inauthentic — organic narratives can be just as harmful
- do not reduce the ecosystem map to a list of 'bad' versus 'good' narratives; the technique maps competition and dynamics, not a binary truth judgment
- do not treat salience (volume, reach) as a proxy for resonance or belief adoption without separate evidence
- do not finalize the map from a single content snapshot — information ecosystems evolve; note the temporal scope explicitly

## AGEINT upstream
`docs/ageint/information-environment.md`
