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

## Defensive boundary

Use Logical Fallacy Detection only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Logical Fallacy Detection to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Logical Fallacy Detection, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Logical Fallacy Detection, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Logical Fallacy Detection recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Logical Fallacy Detection: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Logical Fallacy Detection: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Logical Fallacy Detection: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Logical Fallacy Detection cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Logical Fallacy Detection should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Logical Fallacy Detection, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Logical Fallacy Detection, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Logical Fallacy Detection, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Logical Fallacy Detection failure: mistaking persuasive resonance for verified harm or intent.
- Logical Fallacy Detection failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Logical Fallacy Detection failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Logical Fallacy Detection to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Logical Fallacy Detection into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Logical Fallacy Detection to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Separate detecting a fallacy from refuting the conclusion — the presence of a fallacy means the argument does not establish the conclusion, not necessarily that the conclusion is false
- Name fallacies precisely using their recognized taxonomy (not just 'bad reasoning') — precision enables the person being briefed to recognize the pattern elsewhere
- Assess severity: a fatal fallacy undermines the whole argument; a minor one weakens one sub-claim — over-calling everything 'fatal' destroys calibration
- Distinguish formal fallacies (invalid logical form regardless of content) from informal fallacies (invalid due to content, context, or relevance), as the remedies differ
