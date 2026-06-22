---
name: cognitive_security.manipulation_technique_identification
description: Name the specific persuasion/manipulation techniques in a message or campaign.
---

# Manipulation Technique Identification

Manipulation technique identification names the specific persuasion and psychological manipulation techniques present in a message, campaign, or piece of content — distinguishing legitimate persuasion from techniques that bypass rational agency by exploiting cognitive biases, social dynamics, or emotional vulnerabilities. The skill draws on the social psychology literature (Cialdini's influence principles, dark-pattern persuasion taxonomies), the disinformation research taxonomy (AMITT, EU DisinfoLab, Renée DiResta's influence operations frameworks), and cognitive-security threat modeling. It is a defensive recognition skill: the output is a named catalogue that helps analysts, educators, and defenders recognize patterns before being affected by them.

## When to use

- Evaluating a specific message or piece of content suspected of using psychological manipulation rather than legitimate argumentation
- Analyzing a coordinated influence campaign to understand its operational technique set for threat intelligence or counter-messaging
- Educating audiences about specific manipulation techniques so they can recognize them in future encounters (inoculation)
- Pre-publication review of communications to ensure they do not inadvertently employ manipulative techniques in advocacy or public information campaigns

## What it produces

- A technique-by-technique catalogue naming each manipulation tactic, the specific passage exhibiting it, and the cognitive or social vulnerability it targets
- An assessment of how techniques combine into a coherent manipulation strategy and which audiences are most exposed
- Defensive awareness guidance: what to watch for in similar content and how inoculation or pre-bunking might reduce susceptibility

## Defensive boundary

Use Manipulation Technique Identification only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Manipulation Technique Identification to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Manipulation Technique Identification, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Manipulation Technique Identification, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Manipulation Technique Identification recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Manipulation Technique Identification: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Manipulation Technique Identification: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Manipulation Technique Identification: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Manipulation Technique Identification cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Manipulation Technique Identification should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Manipulation Technique Identification, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Manipulation Technique Identification, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Manipulation Technique Identification, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Manipulation Technique Identification failure: mistaking persuasive resonance for verified harm or intent.
- Manipulation Technique Identification failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Manipulation Technique Identification failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Manipulation Technique Identification to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Manipulation Technique Identification into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Manipulation Technique Identification to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Name techniques precisely using recognized taxonomies (Cialdini principles, AMITT TTPs, propaganda device names) — vague labels like 'emotional manipulation' do not build transferable recognition skills
- Distinguish manipulation from legitimate persuasion: legitimate persuasion relies on accurate evidence, valid inference, and transparent intent; manipulation bypasses rational agency by exploiting bias, social pressure, or deception
- Assess the targeted vulnerability, not just the technique — the same technique (appeal to social proof) exploits different vulnerabilities in different audiences; audience-specificity is analytically meaningful
- Maintain the defensive frame: the output is a recognition and defense tool, not a how-to for deploying manipulation
