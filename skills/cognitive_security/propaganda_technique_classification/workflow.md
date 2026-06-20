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

## Evidence requirements
- For Propaganda Technique Classification, tie each technique classification table, and analytical interpretation claim to concrete evidence from the specific content, context metadata, and taxonomy scope item, source excerpt, observation, or command result that supports it.
- For Propaganda Technique Classification, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the technique classification table.
- Before recommending any Propaganda Technique Classification action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Propaganda Technique Classification: the technique classification table is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; ingest content and establish context and apply taxonomy pass 1 — ipa seven techniques checks agree, and no unresolved contradiction would change the result.
- Medium for Propaganda Technique Classification: the technique classification table is plausible, but one important content source, comparison case, or alternative explanation remains incomplete.
- Low for Propaganda Technique Classification: the technique classification table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Propaganda Technique Classification cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Propaganda Technique Classification, use only authorized content, context metadata, and taxonomy scope, public or source-approved records, and caller-provided context needed for the defensive task.
- For Propaganda Technique Classification, minimize person-level detail in the technique classification table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Propaganda Technique Classification, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Propaganda Technique Classification: treating content as complete when ingest content and establish context and apply taxonomy pass 1 — ipa seven techniques checks or contradictory evidence are missing.
- Propaganda Technique Classification: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Propaganda Technique Classification: reporting the technique classification table without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Propaganda Technique Classification outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the technique classification table from Propaganda Technique Classification into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Propaganda Technique Classification to assess supplied material for manipulation indicators and recommend resilience measures with content, context metadata, and taxonomy scope' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not attribute intent (who made this and why) with the same confidence level as technique identification — intent is an inference, not a classification
- do not classify at the whole-content level without mapping each technique to a specific verbatim excerpt
- do not conflate persuasion with propaganda — legitimate advocacy uses emotional and rhetorical appeals; the distinguishing criterion is systematic deception or exploitation of cognitive vulnerabilities, not mere emotional engagement
- do not produce this analysis for the purpose of constructing or improving propaganda — this is a recognition and defense skill

## AGEINT upstream
`docs/ageint/cognitive-security.md`
