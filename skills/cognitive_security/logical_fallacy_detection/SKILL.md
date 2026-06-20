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

- For Logical Fallacy Detection, tie each fallacy catalogue, and argument assessment claim to concrete evidence from the specific argument text, and context item, source excerpt, observation, or command result that supports it.
- For Logical Fallacy Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the fallacy catalogue.
- Before recommending any Logical Fallacy Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Logical Fallacy Detection: the fallacy catalogue is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; segment the argument into claims and inferences and check formal validity of each inferential step checks agree, and no unresolved contradiction would change the result.
- Medium for Logical Fallacy Detection: the fallacy catalogue is plausible, but one important argument text source, comparison case, or alternative explanation remains incomplete.
- Low for Logical Fallacy Detection: the fallacy catalogue rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Logical Fallacy Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Logical Fallacy Detection, use only authorized argument text, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Logical Fallacy Detection, minimize person-level detail in the fallacy catalogue; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Logical Fallacy Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Logical Fallacy Detection: treating argument text as complete when segment the argument into claims and inferences and check formal validity of each inferential step checks or contradictory evidence are missing.
- Logical Fallacy Detection: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Logical Fallacy Detection: reporting the fallacy catalogue without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Logical Fallacy Detection outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the fallacy catalogue from Logical Fallacy Detection into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Logical Fallacy Detection to assess supplied material for manipulation indicators and recommend resilience measures with argument text, and context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Separate detecting a fallacy from refuting the conclusion — the presence of a fallacy means the argument does not establish the conclusion, not necessarily that the conclusion is false
- Name fallacies precisely using their recognized taxonomy (not just 'bad reasoning') — precision enables the person being briefed to recognize the pattern elsewhere
- Assess severity: a fatal fallacy undermines the whole argument; a minor one weakens one sub-claim — over-calling everything 'fatal' destroys calibration
- Distinguish formal fallacies (invalid logical form regardless of content) from informal fallacies (invalid due to content, context, or relevance), as the remedies differ
