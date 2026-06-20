# Workflow — Emotional Manipulation Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest and segment content (read)
Read the full content to be analyzed. Segment it into units (headline, lead paragraph, image caption, call-to-action, etc.) that can each be independently evaluated for emotional loading.

## Step 2 — Identify and label affective levers (reason)
For each segment, identify the primary emotion being targeted (fear, outrage, disgust, nostalgia, hope, tribal belonging, shame, grief). Label the specific persuasion technique in use (fear appeal, guilt trip, in-group solidarity trigger, moral outrage bait, false urgency, etc.). Note the exact phrase or device that triggers the emotion.

## Step 3 — Map emotion to bypassed cognition (reason)
For each identified lever, name the deliberative faculty it bypasses or short-circuits (e.g., evidence evaluation, source verification, proportionality judgment, identity-protective cognition). Rate severity (low/medium/high) based on how completely the lever disconnects affect from deliberation in the likely audience.

## Step 4 — Assess audience amplification factors (reason)
Consider contextual factors that amplify lever effectiveness: pre-existing fears, recent trauma or crisis, in-group vs. out-group salience, platform affordances that reward emotional content, and audience demographics associated with higher susceptibility to each technique.

## Step 5 — Produce lever map and defensive brief (write)
Compile the emotional lever map as a structured table. Write a defensive brief summarizing the overall manipulation strategy, the most dangerous levers, and specific inoculation or counter-messaging recommendations for each high-severity lever. Distinguish legitimate emotional appeals from weaponized ones explicitly.

## Evidence requirements
- For Emotional Manipulation Analysis, tie each emotional lever map, and defensive brief claim to concrete evidence from the specific content, and context item, source excerpt, observation, or command result that supports it.
- For Emotional Manipulation Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the emotional lever map.
- Before recommending any Emotional Manipulation Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Emotional Manipulation Analysis: the emotional lever map is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; ingest and segment content and identify and label affective levers checks agree, and no unresolved contradiction would change the result.
- Medium for Emotional Manipulation Analysis: the emotional lever map is plausible, but one important content source, comparison case, or alternative explanation remains incomplete.
- Low for Emotional Manipulation Analysis: the emotional lever map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Emotional Manipulation Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Emotional Manipulation Analysis, use only authorized content, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Emotional Manipulation Analysis, minimize person-level detail in the emotional lever map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Emotional Manipulation Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Emotional Manipulation Analysis: treating content as complete when ingest and segment content and identify and label affective levers checks or contradictory evidence are missing.
- Emotional Manipulation Analysis: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Emotional Manipulation Analysis: reporting the emotional lever map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Emotional Manipulation Analysis outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the emotional lever map from Emotional Manipulation Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Emotional Manipulation Analysis to assess supplied material for manipulation indicators and recommend resilience measures with content, and context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate all emotional content with manipulation — legitimate journalism and advocacy use emotion; the test is whether emotion tracks evidence
- Do not produce output that could serve as a how-to guide for running influence operations; all output must be oriented toward recognition and defense
- Do not render severity verdicts without specifying the target audience — the same lever has different potency across populations
- Do not omit labeling the specific cognitive shortcut being exploited — generic 'emotional' labels are analytically useless

## AGEINT upstream
`docs/ageint/cognitive-security.md`
