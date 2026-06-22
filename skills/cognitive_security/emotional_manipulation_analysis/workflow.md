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
- For Emotional Manipulation Analysis, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Emotional Manipulation Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Emotional Manipulation Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Emotional Manipulation Analysis: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Emotional Manipulation Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Emotional Manipulation Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Emotional Manipulation Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Emotional Manipulation Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Emotional Manipulation Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Emotional Manipulation Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Emotional Manipulation Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Emotional Manipulation Analysis failure: mistaking persuasive resonance for verified harm or intent.
- Emotional Manipulation Analysis failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Emotional Manipulation Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Emotional Manipulation Analysis to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Emotional Manipulation Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Emotional Manipulation Analysis to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate all emotional content with manipulation — legitimate journalism and advocacy use emotion; the test is whether emotion tracks evidence
- Do not produce output that could serve as a how-to guide for running influence operations; all output must be oriented toward recognition and defense
- Do not render severity verdicts without specifying the target audience — the same lever has different potency across populations
- Do not omit labeling the specific cognitive shortcut being exploited — generic 'emotional' labels are analytically useless

## AGEINT upstream
`docs/ageint/cognitive-security.md`
