---
name: cognitive_security.framing_and_priming_analysis
description: Surface the frames and primes shaping interpretation beneath a message's literal content.
---

# Framing & Priming Analysis

Framing and Priming Analysis surfaces the implicit conceptual frames — the organizing metaphors, category choices, and contextual anchors — that shape how a message is received before its literal content is processed. Drawing on Lakoff's cognitive linguistics, Kahneman's anchoring research, and Entman's framing theory, the technique examines what is foregrounded vs. backgrounded, which comparison sets or reference points are primed, and how word choice activates preloaded schema that channel interpretation. The output gives analysts and communicators a principled account of the meta-layer of persuasion that operates beneath explicit argument.

## When to use

- Auditing a news story, press release, or official statement for subtle framing choices that steer interpretation
- Comparing coverage of the same event across partisan or national sources to identify divergent dominant frames
- Preparing communicators to respond to a narrative attack without inadvertently reinforcing the attacker's frame
- Training analysts to recognize priming sequences in long-form influence operations
- Designing counter-messaging that explicitly competes at the frame level rather than only disputing surface facts

## What it produces

- A typed inventory of every active frame and prime: metaphor, category label, salience omission, comparison set anchor, or order-of-presentation prime
- An account of which cognitive schema each device activates and what interpretive conclusions it predisposes the reader toward
- Identification of what the frame systematically forecloses — the alternative framings that the dominant frame makes invisible or implausible
- Concrete alternative framings or counter-frame language that reactivate suppressed schema

## Defensive boundary

Use Framing & Priming Analysis only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Framing & Priming Analysis to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Framing & Priming Analysis, anchor every named frame, prime, and severity rating to concrete evidence in the supplied content — a specific lexical choice, metaphor, omission, or anchor — and to the audience whose pre-loaded schema that evidence would activate, rather than asserting interpretive effects in the abstract.
- For Framing & Priming Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the frame inventory.
- Before recommending any Framing & Priming Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Framing & Priming Analysis: each entry in the frame inventory ties a named device to a specific textual marker and the schema it activates, the dominant-frame reading is corroborated by contrastive comparison across alternative versions and the stated audience context, and no unresolved contradiction would change the reframing brief.
- Medium for Framing & Priming Analysis: the frame inventory is plausible, but one important content source, comparison case, or alternative explanation remains incomplete.
- Low for Framing & Priming Analysis: the frame inventory rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Framing & Priming Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Framing & Priming Analysis, use only authorized content, alternative versions, and audience context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Framing & Priming Analysis, minimize person-level detail in the frame inventory; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Framing & Priming Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Framing & Priming Analysis: declaring a frame mapped when the close-read of linguistic markers skipped the priming sequence or assessed activation without specifying the audience, treating every communicative framing as manipulation and missing what the dominant frame quietly forecloses.
- Framing & Priming Analysis: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Framing & Priming Analysis: reporting the frame inventory without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Framing & Priming Analysis outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the frame inventory from Framing & Priming Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Framing & Priming Analysis to assess supplied material for manipulation indicators and recommend resilience measures with content, alternative versions, and audience context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Frames operate pre-argumentatively — they shape what counts as evidence and what questions are askable before any explicit claim is evaluated
- Priming is cumulative and sequential — early word choices and juxtapositions load schema that interpret later content; map the sequence, not just individual items
- Identify what is absent as rigorously as what is present — the frame's power often lies in what it makes invisible
- Never correct a hostile frame by repeating it even to negate it — counter-frames must activate a competing schema, not reinforce the original one
