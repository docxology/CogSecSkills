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

## Defensive boundary

Use Epistemic Security Posture Review only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Epistemic Security Posture Review to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Epistemic Security Posture Review, tie each posture scorecard, attack surface narrative, and remediation roadmap claim to concrete evidence from the specific organizational profile, epistemic practices, and known incidents item, source excerpt, observation, or command result that supports it.
- For Epistemic Security Posture Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the posture scorecard.
- Before recommending any Epistemic Security Posture Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Epistemic Security Posture Review: the posture scorecard is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; map the epistemic architecture and score posture dimensions checks agree, and no unresolved contradiction would change the result.
- Medium for Epistemic Security Posture Review: the posture scorecard is plausible, but one important organizational profile source, comparison case, or alternative explanation remains incomplete.
- Low for Epistemic Security Posture Review: the posture scorecard rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Epistemic Security Posture Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Epistemic Security Posture Review, use only authorized organizational profile, epistemic practices, and known incidents, public or source-approved records, and caller-provided context needed for the defensive task.
- For Epistemic Security Posture Review, minimize person-level detail in the posture scorecard; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Epistemic Security Posture Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Epistemic Security Posture Review: treating organizational profile as complete when map the epistemic architecture and score posture dimensions checks or contradictory evidence are missing.
- Epistemic Security Posture Review: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Epistemic Security Posture Review: reporting the posture scorecard without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Epistemic Security Posture Review outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the posture scorecard from Epistemic Security Posture Review into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Epistemic Security Posture Review to assess supplied material for manipulation indicators and recommend resilience measures with organizational profile, epistemic practices, and known incidents' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Epistemic security is structural, not individual — the unit of analysis is the organization's knowledge-formation process, not any one person's beliefs
- Distinguish closed epistemic loops (feedback tells the organization what it already believes) from open ones (evidence can overturn prior belief)
- An attack surface is an exploitable dependency: any single point of information supply, any suppressed dissent channel, any unverified source chain
- Rate vulnerability by adversarial incentive x exploitability x impact on decisions — not just by theoretical weakness
