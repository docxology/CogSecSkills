---
name: counterintelligence.analytic_process_hardening
description: Harden an analytic workflow against being gamed, anchored, or fed planted evidence.
---

# Analytic Process Hardening

Analytic process hardening audits an intelligence or research workflow to identify the specific points at which an adversary — or a manipulation campaign — could plant evidence, anchor judgments, seed false leads, or exploit cognitive biases to corrupt conclusions. Rooted in counterintelligence tradecraft and structured analytic technique discipline, it maps each workflow node to its manipulation surface, then prescribes procedural controls that reduce exploitability without requiring analysts to become suspicious of all sources. The output is an action-ready hardening plan with prioritized controls.

## When to use

- a high-stakes analytic workflow will inform a major decision and manipulation by an adversary is a credible threat
- a prior assessment was later found to have relied on planted or manipulated evidence
- a workflow aggregates information from sources with adversarial access or that operate in contested information environments
- an organization is designing a new analytic process and wants manipulation-resistance built in from the start

## What it produces

- a node-by-node map of manipulation surfaces in the workflow with associated detection difficulty ratings
- a prioritized set of procedural controls targeting the highest-risk nodes first
- an explicit residual-risk statement so decision-makers know what cannot be fully mitigated

## Defensive boundary

Use Analytic Process Hardening only for counterintelligence and analytic-process defense: recognize, assess, document, or defend analytic teams, collection processes, and institutional trust boundaries. Do not use this skill to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.

## Misuse redirect

If a request asks Analytic Process Hardening to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft, refuse that path and redirect to the safe defensive form: review supplied interactions or processes for deception, elicitation, or insider-risk indicators.

## Evidence discipline

- For Analytic Process Hardening, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Analytic Process Hardening, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Analytic Process Hardening recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Analytic Process Hardening: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Analytic Process Hardening: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Analytic Process Hardening: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Analytic Process Hardening cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Analytic Process Hardening should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Analytic Process Hardening, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Analytic Process Hardening, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Analytic Process Hardening, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Analytic Process Hardening failure: turning defensive tradecraft recognition into operational evasion advice.
- Analytic Process Hardening failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Analytic Process Hardening failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Analytic Process Hardening to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Analytic Process Hardening into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Analytic Process Hardening to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- map attack surfaces structurally — ask 'what would a sophisticated deceiver do at this node?' not 'do we trust our sources?'
- controls must be proportionate — hardening every node equally creates analyst fatigue and degrades legitimate throughput; prioritize by adversary capability × consequence of manipulation
- independence of review is the strongest single control: a reviewer who processed different sources and was not present during drafting catches the most
