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

- For Manipulation Technique Identification, bind every named technique, potency estimate, and targeted-vulnerability claim to concrete evidence — a specific passage or described element of the content — and assign a certain, probable, or possible confidence label so an ambiguous reading is never presented as established.
- For Manipulation Technique Identification, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the technique catalogue.
- Before recommending any Manipulation Technique Identification action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Manipulation Technique Identification: each technique in the catalogue is named from a recognized taxonomy and tied to the passage that instantiates it and the cognitive or social vulnerability it targets, the read of how techniques combine is corroborated against the content and audience context, and no unresolved contradiction would change the defensive recommendations.
- Medium for Manipulation Technique Identification: the technique catalogue is plausible, but one important content source, comparison case, or alternative explanation remains incomplete.
- Low for Manipulation Technique Identification: the technique catalogue rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Manipulation Technique Identification cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Manipulation Technique Identification, use only authorized content, target audience, and distribution context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Manipulation Technique Identification, minimize person-level detail in the technique catalogue; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Manipulation Technique Identification, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Manipulation Technique Identification: labelling content manipulative merely because its conclusion is contested rather than because its method bypasses rational agency, or using vague descriptors instead of a named technique and passage, so legitimate persuasion is misclassified and audience-specific vulnerabilities are missed.
- Manipulation Technique Identification: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Manipulation Technique Identification: reporting the technique catalogue without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Manipulation Technique Identification outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the technique catalogue from Manipulation Technique Identification into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Manipulation Technique Identification to assess supplied material for manipulation indicators and recommend resilience measures with content, target audience, and distribution context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Name techniques precisely using recognized taxonomies (Cialdini principles, AMITT TTPs, propaganda device names) — vague labels like 'emotional manipulation' do not build transferable recognition skills
- Distinguish manipulation from legitimate persuasion: legitimate persuasion relies on accurate evidence, valid inference, and transparent intent; manipulation bypasses rational agency by exploiting bias, social pressure, or deception
- Assess the targeted vulnerability, not just the technique — the same technique (appeal to social proof) exploits different vulnerabilities in different audiences; audience-specificity is analytically meaningful
- Maintain the defensive frame: the output is a recognition and defense tool, not a how-to for deploying manipulation
