---
name: cognitive_security.propaganda_technique_classification
description: Classify content against the canonical propaganda techniques (IPA and successors).
---

# Propaganda Technique Classification

Propaganda Technique Classification systematically identifies and labels the specific rhetorical devices in content against the canonical taxonomy established by the Institute for Propaganda Analysis (IPA, 1937) and extended by Jowett & O'Donnell, Bernays, and contemporary computational SEMEVAL frameworks. The skill maps content to techniques including transfer, glittering generalities, plain folks, card stacking, bandwagon, name-calling, and testimonial, then assesses persuasive intent and likely audience impact. It is a defensive, recognition-oriented skill that enables analysts and educators to name and explain manipulation rather than fall prey to it.

## When to use

- analyzing suspected propaganda content for an intelligence, policy, or research audience
- building a training dataset or educational example set for a media-literacy curriculum
- evaluating political advertising, public health messaging, or corporate communications for manipulative technique use
- providing annotated examples to support inoculation content design or counter-messaging strategy

## What it produces

- a technique classification table mapping each excerpt to its canonical IPA/SEMEVAL label, mechanism, and cognitive lever
- an analytical interpretation of the overall technique mix, strategic intent, and countermeasures

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- map each identified technique to a verbatim excerpt — vague whole-text attribution is not classification
- distinguish technique identification (what rhetorical move is this) from intent attribution (who made this and why) — the former is evidential, the latter is inferential and must be labeled as such
- note co-deployed technique interactions: bandwagon amplifies name-calling; glittering generalities prime transfer — the combination is more potent than the sum
- apply the IPA/SEMEVAL taxonomy consistently before adding idiosyncratic labels — interoperability across analysts requires shared vocabulary
