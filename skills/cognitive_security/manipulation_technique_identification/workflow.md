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

## Anti-criteria (must NOT happen)
- Do not label content as manipulative based solely on its conclusion being false or contested — manipulation is about method (bypassing rational agency), not just about content truthfulness
- Do not use vague descriptors ('emotionally manipulative', 'propaganda') without specifying the precise named technique and the passage that instantiates it
- Do not produce this analysis as an operational playbook for deploying the identified techniques — outputs must be framed exclusively for recognition and defense
- Do not omit confidence ratings on technique identifications — some techniques are unmistakable; others are ambiguous and must be labeled as 'possible' to maintain analytical honesty

## AGEINT upstream
`docs/ageint/cognitive-security.md`
