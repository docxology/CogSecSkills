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
- For Manipulation Technique Identification, bind every named technique, potency estimate, and targeted-vulnerability claim to concrete evidence — a specific passage or described element of the content — and assign a certain, probable, or possible confidence label so an ambiguous reading is never presented as established.
- For Manipulation Technique Identification, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the technique catalogue.
- Before recommending any Manipulation Technique Identification action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Manipulation Technique Identification: each technique in the catalogue is named from a recognized taxonomy and tied to the passage that instantiates it and the cognitive or social vulnerability it targets, the read of how techniques combine is corroborated against the content and audience context, and no unresolved contradiction would change the defensive recommendations.
- Medium for Manipulation Technique Identification: the technique catalogue is plausible, but one important content source, comparison case, or alternative explanation remains incomplete.
- Low for Manipulation Technique Identification: the technique catalogue rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Manipulation Technique Identification cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Manipulation Technique Identification, use only authorized content, target audience, and distribution context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Manipulation Technique Identification, minimize person-level detail in the technique catalogue; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Manipulation Technique Identification, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Manipulation Technique Identification: labelling content manipulative merely because its conclusion is contested rather than because its method bypasses rational agency, or using vague descriptors instead of a named technique and passage, so legitimate persuasion is misclassified and audience-specific vulnerabilities are missed.
- Manipulation Technique Identification: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Manipulation Technique Identification: reporting the technique catalogue without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Manipulation Technique Identification outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the technique catalogue from Manipulation Technique Identification into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Manipulation Technique Identification to assess supplied material for manipulation indicators and recommend resilience measures with content, target audience, and distribution context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not label content as manipulative based solely on its conclusion being false or contested — manipulation is about method (bypassing rational agency), not just about content truthfulness
- Do not use vague descriptors ('emotionally manipulative', 'propaganda') without specifying the precise named technique and the passage that instantiates it
- Do not produce this analysis as an operational playbook for deploying the identified techniques — outputs must be framed exclusively for recognition and defense
- Do not omit confidence ratings on technique identifications — some techniques are unmistakable; others are ambiguous and must be labeled as 'possible' to maintain analytical honesty

## AGEINT upstream
`docs/ageint/cognitive-security.md`
