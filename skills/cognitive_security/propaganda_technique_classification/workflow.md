# Workflow — Propaganda Technique Classification

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest content and establish context (read)
Read the full content item and any context metadata. Note source, audience, platform, and any campaign context. Identify the primary rhetorical register (political, commercial, health, social) as this affects which technique sub-families are most likely to be active. Do not begin classifying until the full content has been read — early framing artifacts can bias technique detection.

## Step 2 — Apply taxonomy pass 1 — IPA seven techniques (reason)
Scan content for the seven IPA canonical techniques: (1) Name-Calling — attaching a negative label to an opponent without evidence; (2) Glittering Generalities — associating a cause with virtue words (freedom, democracy, God) without substance; (3) Transfer — borrowing authority or prestige from a respected symbol; (4) Testimonial — having a respected or disrespected person endorse or condemn an idea; (5) Plain Folks — identifying the speaker as an ordinary person; (6) Card Stacking — selecting only favorable evidence while omitting contrary evidence; (7) Bandwagon — appealing to the desire to be on the winning side. For each detected technique, record the verbatim excerpt and cognitive lever.

## Step 3 — Apply taxonomy pass 2 — extended techniques (reason)
For content warranting deeper analysis, apply the SEMEVAL 2020 extended taxonomy (18 classes), including: Appeal to Fear/Prejudice, Loaded Language, Repetition, Exaggeration/Minimisation, Doubt, Obfuscation/Intentional Vagueness, Whataboutism, Causal Oversimplification, Black-and-White Fallacy, Thought-Terminating Cliché, Red Herring, Straw Man, and Appeal to Authority. Document technique co-occurrence patterns and their interaction effects.

## Step 4 — Assess strategic intent and produce classification output (reason, write)
Interpret the overall technique mix: what emotional and cognitive state is the content designed to produce in the target audience? Which audience vulnerabilities (fear, identity threat, authority deference, in-group loyalty) does the mix exploit? Rate confidence in intent attribution separately from technique identification. Compose the classification table and the analytical interpretation narrative, including suggested countermeasures appropriate to each identified technique.

## Anti-criteria (must NOT happen)
- do not attribute intent (who made this and why) with the same confidence level as technique identification — intent is an inference, not a classification
- do not classify at the whole-content level without mapping each technique to a specific verbatim excerpt
- do not conflate persuasion with propaganda — legitimate advocacy uses emotional and rhetorical appeals; the distinguishing criterion is systematic deception or exploitation of cognitive vulnerabilities, not mere emotional engagement
- do not produce this analysis for the purpose of constructing or improving propaganda — this is a recognition and defense skill

## AGEINT upstream
`docs/ageint/cognitive-security.md`
