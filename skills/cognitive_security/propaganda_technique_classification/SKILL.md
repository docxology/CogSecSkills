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

## Defensive boundary

Use Propaganda Technique Classification only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Propaganda Technique Classification to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Propaganda Technique Classification, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Propaganda Technique Classification, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Propaganda Technique Classification recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Propaganda Technique Classification: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Propaganda Technique Classification: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Propaganda Technique Classification: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Propaganda Technique Classification cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Propaganda Technique Classification should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Propaganda Technique Classification, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Propaganda Technique Classification, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Propaganda Technique Classification, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Propaganda Technique Classification failure: mistaking persuasive resonance for verified harm or intent.
- Propaganda Technique Classification failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Propaganda Technique Classification failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Propaganda Technique Classification to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Propaganda Technique Classification into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Propaganda Technique Classification to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- map each identified technique to a verbatim excerpt — vague whole-text attribution is not classification
- distinguish technique identification (what rhetorical move is this) from intent attribution (who made this and why) — the former is evidential, the latter is inferential and must be labeled as such
- note co-deployed technique interactions: bandwagon amplifies name-calling; glittering generalities prime transfer — the combination is more potent than the sum
- apply the IPA/SEMEVAL taxonomy consistently before adding idiosyncratic labels — interoperability across analysts requires shared vocabulary
