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

- For Epistemic Security Posture Review, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Epistemic Security Posture Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Epistemic Security Posture Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Epistemic Security Posture Review: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Epistemic Security Posture Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Epistemic Security Posture Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Epistemic Security Posture Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Epistemic Security Posture Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Epistemic Security Posture Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Epistemic Security Posture Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Epistemic Security Posture Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Epistemic Security Posture Review failure: mistaking persuasive resonance for verified harm or intent.
- Epistemic Security Posture Review failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Epistemic Security Posture Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Epistemic Security Posture Review to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Epistemic Security Posture Review into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Epistemic Security Posture Review to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Epistemic security is structural, not individual — the unit of analysis is the organization's knowledge-formation process, not any one person's beliefs
- Distinguish closed epistemic loops (feedback tells the organization what it already believes) from open ones (evidence can overturn prior belief)
- An attack surface is an exploitable dependency: any single point of information supply, any suppressed dissent channel, any unverified source chain
- Rate vulnerability by adversarial incentive x exploitability x impact on decisions — not just by theoretical weakness
