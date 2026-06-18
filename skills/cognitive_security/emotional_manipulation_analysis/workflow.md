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

## Anti-criteria (must NOT happen)
- Do not conflate all emotional content with manipulation — legitimate journalism and advocacy use emotion; the test is whether emotion tracks evidence
- Do not produce output that could serve as a how-to guide for running influence operations; all output must be oriented toward recognition and defense
- Do not render severity verdicts without specifying the target audience — the same lever has different potency across populations
- Do not omit labeling the specific cognitive shortcut being exploited — generic 'emotional' labels are analytically useless

## AGEINT upstream
`docs/ageint/cognitive-security.md`
