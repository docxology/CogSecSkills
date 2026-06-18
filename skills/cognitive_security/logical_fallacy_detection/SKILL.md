---
name: cognitive_security.logical_fallacy_detection
description: Catalogue the formal and informal fallacies in an argument or persuasive piece.
---

# Logical Fallacy Detection

Logical fallacy detection systematically catalogues the formal and informal fallacies present in an argument, persuasive message, or piece of content — distinguishing valid reasoning from rhetorically effective but logically invalid moves. The technique draws on classical logic (formal fallacies: affirming the consequent, denying the antecedent) and the tradition of informal logic catalogued by Hamblin, Walton, and others (ad hominem, appeal to authority, straw man, false dilemma, slippery slope, etc.). In cognitive-security contexts it serves as a first-pass defensive filter that separates persuasive force from epistemic warrant.

## When to use

- Evaluating the epistemic quality of persuasive content — political messaging, advocacy documents, op-eds, or viral social media posts
- Defensive analysis of content that feels rhetorically compelling but whose conclusions seem suspect
- Teaching or briefing on cognitive-security threats that exploit informal fallacies (appeal to fear, false dilemma, ad hominem attacks on credible sources)
- Pre-publication review of analytic documents to remove fallacious reasoning from official products

## What it produces

- A line-by-line or claim-by-claim catalogue of fallacies with formal names, explanations, and severity ratings
- An overall verdict on whether the argument is valid (structure) and/or sound (premises + structure), and which conclusions are genuinely supported by non-fallacious moves

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Separate detecting a fallacy from refuting the conclusion — the presence of a fallacy means the argument does not establish the conclusion, not necessarily that the conclusion is false
- Name fallacies precisely using their recognized taxonomy (not just 'bad reasoning') — precision enables the person being briefed to recognize the pattern elsewhere
- Assess severity: a fatal fallacy undermines the whole argument; a minor one weakens one sub-claim — over-calling everything 'fatal' destroys calibration
- Distinguish formal fallacies (invalid logical form regardless of content) from informal fallacies (invalid due to content, context, or relevance), as the remedies differ
