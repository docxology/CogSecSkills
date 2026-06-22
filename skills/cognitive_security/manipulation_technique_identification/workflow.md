# Workflow — Manipulation Technique Identification

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the content and context (read)
Identify the medium, source, apparent target audience, and stated purpose of the content. Note structural features (length, emotional register, calls to action, visual/aural elements if described). Establish the baseline: what is the content overtly trying to achieve?

## Step 2 — Scan for influence principles and social-psychology techniques (reason)
Examine the content against Cialdini's six influence principles (reciprocity, commitment/consistency, social proof, authority, liking, scarcity) and their exploitation variants. Note each instantiation: the specific passage, how the principle is invoked, and whether it is used transparently (legitimate) or deceptively (manipulative — e.g., fake scarcity, manufactured social proof).

## Step 3 — Scan for propaganda and disinformation techniques (reason)
Examine against recognized propaganda device taxonomies (name-calling, glittering generalities, transfer, testimonial, plain folks, card stacking, bandwagon) and modern disinformation TTPs (AMITT/DISARM categories: fear appeals, moral outrage activation, identity-group wedging, firehose repetition, false balance, astroturfing signals, decontextualization). Note each finding with the relevant taxonomy label and supporting passage.

## Step 4 — Map targeted vulnerabilities and technique interactions (reason)
For each identified technique, name the cognitive bias, heuristic, or social dynamic it exploits (e.g., availability heuristic, in-group/out-group bias, authority heuristic, loss aversion). Assess how techniques combine: do they prime each other (fear appeal → tribal identity → false dilemma), and does the combination create an effect greater than any single technique?

## Step 5 — Emit catalogue and defensive narrative (write)
Produce the technique table with name, category, passage, targeted vulnerability, potency, and evidence confidence. Write the narrative: overall manipulation strategy, technique synergies, most vulnerable audience segments, and defensive recommendations (inoculation messaging, pre-bunking the specific techniques, questions a reader can ask to trigger rational evaluation).

## Evidence requirements
- For Manipulation Technique Identification, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Manipulation Technique Identification, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Manipulation Technique Identification recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Manipulation Technique Identification: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Manipulation Technique Identification: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Manipulation Technique Identification: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Manipulation Technique Identification cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Manipulation Technique Identification should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Manipulation Technique Identification, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Manipulation Technique Identification, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Manipulation Technique Identification, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Manipulation Technique Identification failure: mistaking persuasive resonance for verified harm or intent.
- Manipulation Technique Identification failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Manipulation Technique Identification failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Manipulation Technique Identification to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Manipulation Technique Identification into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Manipulation Technique Identification to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not label content as manipulative based solely on its conclusion being false or contested — manipulation is about method (bypassing rational agency), not just about content truthfulness
- Do not use vague descriptors ('emotionally manipulative', 'propaganda') without specifying the precise named technique and the passage that instantiates it
- Do not produce this analysis as an operational playbook for deploying the identified techniques — outputs must be framed exclusively for recognition and defense
- Do not omit confidence ratings on technique identifications — some techniques are unmistakable; others are ambiguous and must be labeled as 'possible' to maintain analytical honesty

## AGEINT upstream
`docs/ageint/cognitive-security.md`
