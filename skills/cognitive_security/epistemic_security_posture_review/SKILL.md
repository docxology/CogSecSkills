---
name: cognitive_security.epistemic_security_posture_review
description: Assess an organization's defenses for the integrity of how it knows what it knows.
---

# Epistemic Security Posture Review

Epistemic Security Posture Review assesses the structural integrity of how an organization forms, updates, and protects its beliefs about the world — evaluating whether its knowledge-acquisition and decision-support processes are resistant to manipulation, capture, and degradation. Drawing on epistemology, organizational learning theory, and cognitive-security frameworks (Benkler et al., Allenby & Garreau), it examines information sourcing, analytic culture, feedback mechanisms, and adversarial exposure. The output is a posture scorecard and remediation roadmap identifying the epistemic attack surfaces most likely to be exploited.

## When to use

- Before or after an organization has been targeted by disinformation or influence operations and needs a systematic vulnerability inventory
- During strategic planning cycles to assess whether epistemic infrastructure is adequate for the threat environment
- When leadership suspects analytic groupthink, source monoculture, or suppression of dissent is degrading decision quality
- As part of a broader organizational resilience audit for entities operating in high-adversarial-information environments
- When onboarding a new analytic team or restructuring intelligence/communications functions

## What it produces

- A multi-dimension posture scorecard rating current maturity on source diversity, analytic culture, feedback integrity, adversarial awareness, and training
- A ranked inventory of epistemic attack surfaces with concrete exploitation scenarios for each
- A prioritized remediation roadmap linking each vulnerability to a specific structural fix with implementation guidance
- Baseline metrics that can be re-administered periodically to track posture improvement

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Epistemic security is structural, not individual — the unit of analysis is the organization's knowledge-formation process, not any one person's beliefs
- Distinguish closed epistemic loops (feedback tells the organization what it already believes) from open ones (evidence can overturn prior belief)
- An attack surface is an exploitable dependency: any single point of information supply, any suppressed dissent channel, any unverified source chain
- Rate vulnerability by adversarial incentive x exploitability x impact on decisions — not just by theoretical weakness
