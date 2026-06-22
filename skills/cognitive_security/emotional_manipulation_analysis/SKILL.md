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

- For Emotional Manipulation Analysis, tie every identified lever and severity rating to concrete evidence — the quoted trigger phrase, the segment it appears in, and the System 1 shortcut it routes around — specify the target population for which the rating holds, and distinguish emotion that tracks the evidence from emotion decoupled from or contradicting it.
- For Emotional Manipulation Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the emotional lever map.
- Before recommending any Emotional Manipulation Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Emotional Manipulation Analysis: each affective lever in the map is anchored to the exact trigger phrase or device that activates it, mapped to the specific deliberative faculty it bypasses, and rated for severity against a named target population, with corroboration across content segments and no unresolved contradiction that would change the defensive brief.
- Medium for Emotional Manipulation Analysis: the emotional lever map is plausible, but one important content source, comparison case, or alternative explanation remains incomplete.
- Low for Emotional Manipulation Analysis: the emotional lever map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Emotional Manipulation Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Emotional Manipulation Analysis, use only authorized content, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Emotional Manipulation Analysis, minimize person-level detail in the emotional lever map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Emotional Manipulation Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Emotional Manipulation Analysis: conflating legitimate evidence-tracking pathos with weaponized emotion, rendering a severity verdict without specifying the target audience, or omitting the cognitive shortcut a lever exploits, so the map either over-flags honest advocacy or produces analytically useless generic emotion labels.
- Emotional Manipulation Analysis: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Emotional Manipulation Analysis: reporting the emotional lever map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Emotional Manipulation Analysis outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the emotional lever map from Emotional Manipulation Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Emotional Manipulation Analysis to assess supplied material for manipulation indicators and recommend resilience measures with content, and context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Separate description from condemnation — label the technique precisely before judging intent, to preserve analytic rigor
- Map emotion to cognitive shortcut: every affective lever works by routing around a specific deliberative faculty — name which one
- Distinguish legitimate emotional appeal (accurate pathos) from manipulation (emotion decoupled from or contradicting evidence)
- Assess audience fit: the same lever may be inert for one demographic and highly effective for another — always specify target population
