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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Name techniques precisely using recognized taxonomies (Cialdini principles, AMITT TTPs, propaganda device names) — vague labels like 'emotional manipulation' do not build transferable recognition skills
- Distinguish manipulation from legitimate persuasion: legitimate persuasion relies on accurate evidence, valid inference, and transparent intent; manipulation bypasses rational agency by exploiting bias, social pressure, or deception
- Assess the targeted vulnerability, not just the technique — the same technique (appeal to social proof) exploits different vulnerabilities in different audiences; audience-specificity is analytically meaningful
- Maintain the defensive frame: the output is a recognition and defense tool, not a how-to for deploying manipulation
