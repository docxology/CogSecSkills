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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Separate description from condemnation — label the technique precisely before judging intent, to preserve analytic rigor
- Map emotion to cognitive shortcut: every affective lever works by routing around a specific deliberative faculty — name which one
- Distinguish legitimate emotional appeal (accurate pathos) from manipulation (emotion decoupled from or contradicting evidence)
- Assess audience fit: the same lever may be inert for one demographic and highly effective for another — always specify target population
