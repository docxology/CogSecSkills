---
name: cognitive_security.emotional_manipulation_analysis
description: Identify affective levers (fear, outrage, tribal belonging) a message exploits.
---

# Emotional Manipulation Analysis

Emotional Manipulation Analysis identifies the specific affective levers — fear, outrage, disgust, in-group loyalty, grief, hope — that a message, campaign, or artifact deliberately exploits to bypass deliberative reasoning. Rooted in the dual-process literature (Kahneman) and influence-operation research (Wardle & Derakhshan), it deconstructs persuasion technique by technique, distinguishing legitimate pathos from weaponized emotion. The output is a structured threat map that analysts and communicators can use to recognize manipulation in real time and design inoculation or counter-messaging responses.

## When to use

- Assessing a piece of suspected disinformation or propaganda for manipulation techniques before amplifying or responding
- Training analysts to recognize affective exploitation patterns across message formats
- Designing inoculation content that pre-exposes audiences to manipulation techniques before harmful narratives arrive
- Auditing organizational communications to ensure persuasion is legitimate pathos, not weaponized emotion
- Conducting post-incident analysis of how an influence operation achieved virality through emotional resonance

## What it produces

- A technique-labeled inventory of every affective lever the content activates (e.g., fear appeal, moral outrage, in-group/out-group contrast, disgust evocation, false urgency)
- Severity ratings indicating how strongly each lever is likely to bypass deliberative evaluation in the target audience
- A diagnosis of which System 1 shortcuts (availability heuristic, confirmation bias, identity-protective cognition) are being exploited
- Concrete inoculation and counter-messaging recommendations tied to each identified lever

## Defensive boundary

Use Emotional Manipulation Analysis only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Emotional Manipulation Analysis to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

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

## Failure modes and negative controls

- Emotional Manipulation Analysis failure: mistaking persuasive resonance for verified harm or intent.
- Emotional Manipulation Analysis failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Emotional Manipulation Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Emotional Manipulation Analysis to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Emotional Manipulation Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Emotional Manipulation Analysis to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Separate description from condemnation — label the technique precisely before judging intent, to preserve analytic rigor
- Map emotion to cognitive shortcut: every affective lever works by routing around a specific deliberative faculty — name which one
- Distinguish legitimate emotional appeal (accurate pathos) from manipulation (emotion decoupled from or contradicting evidence)
- Assess audience fit: the same lever may be inert for one demographic and highly effective for another — always specify target population
