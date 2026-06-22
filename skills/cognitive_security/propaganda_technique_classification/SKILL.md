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

- For Propaganda Technique Classification, bind every labelled technique to concrete evidence — a verbatim excerpt and the cognitive lever it exploits — and separate evidential technique identification from inferential intent attribution, labelling any intent claim that lacks supporting evidence as inference rather than classification.
- For Propaganda Technique Classification, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the technique classification table.
- Before recommending any Propaganda Technique Classification action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Propaganda Technique Classification: each labelled technique is anchored to a verbatim content excerpt and a consistently applied IPA or SemEval category, the identified technique mix is corroborated across passes and the context metadata, and no unresolved contradiction would change the analytical interpretation of strategic intent.
- Medium for Propaganda Technique Classification: the technique classification table is plausible, but one important content source, comparison case, or alternative explanation remains incomplete.
- Low for Propaganda Technique Classification: the technique classification table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Propaganda Technique Classification cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Propaganda Technique Classification, use only authorized content, context metadata, and taxonomy scope, public or source-approved records, and caller-provided context needed for the defensive task.
- For Propaganda Technique Classification, minimize person-level detail in the technique classification table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Propaganda Technique Classification, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Propaganda Technique Classification: declaring content classified when techniques were attributed at the whole-text level without verbatim excerpts, the extended-taxonomy pass was skipped, or inferred intent was reported with the same confidence as evidential technique identification.
- Propaganda Technique Classification: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Propaganda Technique Classification: reporting the technique classification table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Propaganda Technique Classification outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the technique classification table from Propaganda Technique Classification into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Propaganda Technique Classification to assess supplied material for manipulation indicators and recommend resilience measures with content, context metadata, and taxonomy scope' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- map each identified technique to a verbatim excerpt — vague whole-text attribution is not classification
- distinguish technique identification (what rhetorical move is this) from intent attribution (who made this and why) — the former is evidential, the latter is inferential and must be labeled as such
- note co-deployed technique interactions: bandwagon amplifies name-calling; glittering generalities prime transfer — the combination is more potent than the sum
- apply the IPA/SEMEVAL taxonomy consistently before adding idiosyncratic labels — interoperability across analysts requires shared vocabulary
