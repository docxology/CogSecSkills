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

- For Analytic Process Hardening, tie each vulnerability map, hardening plan, and residual risk statement claim to concrete evidence from the specific workflow description, adversary context, and prior incidents item, source excerpt, observation, or command result that supports it.
- For Analytic Process Hardening, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the vulnerability map.
- Before recommending any Analytic Process Hardening action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Analytic Process Hardening: the vulnerability map is supported by multiple independent interaction records, process artifacts, deception indicators, and alternative explanations; map the workflow and identify manipulation surfaces checks agree, and no unresolved contradiction would change the result.
- Medium for Analytic Process Hardening: the vulnerability map is plausible, but one important workflow description source, comparison case, or alternative explanation remains incomplete.
- Low for Analytic Process Hardening: the vulnerability map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Analytic Process Hardening cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Analytic Process Hardening, use only authorized workflow description, adversary context, and prior incidents, public or source-approved records, and caller-provided context needed for the defensive task.
- For Analytic Process Hardening, minimize person-level detail in the vulnerability map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Analytic Process Hardening, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Analytic Process Hardening: treating workflow description as complete when map the workflow and identify manipulation surfaces checks or contradictory evidence are missing.
- Analytic Process Hardening: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Analytic Process Hardening: reporting the vulnerability map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Analytic Process Hardening outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the vulnerability map from Analytic Process Hardening into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Analytic Process Hardening to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with workflow description, adversary context, and prior incidents' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- map attack surfaces structurally — ask 'what would a sophisticated deceiver do at this node?' not 'do we trust our sources?'
- controls must be proportionate — hardening every node equally creates analyst fatigue and degrades legitimate throughput; prioritize by adversary capability × consequence of manipulation
- independence of review is the strongest single control: a reviewer who processed different sources and was not present during drafting catches the most
