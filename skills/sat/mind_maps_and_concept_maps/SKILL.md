---
name: sat.mind_maps_and_concept_maps
description: Externalize a problem's concepts and relationships as a navigable graph.
---

# Mind Maps & Concept Maps

Mind maps and concept maps externalize the structure of a complex problem as a navigable node-link graph, making implicit conceptual relationships visible and shareable. Mind maps radiate from a central topic in a hierarchical tree; concept maps allow labeled, directional links between any pair of nodes (following Novak's knowledge-representation theory). Both techniques combat working-memory overload, surface hidden assumptions, and expose gaps or tangled chains of reasoning that prose analysis obscures.

## When to use

- the problem involves many interacting concepts and verbal analysis keeps losing track of their relationships
- a team needs a shared, inspectable representation of how they understand a situation
- preparing for ACH or other hypothesis-generation techniques and wanting to inventory all relevant factors first
- detecting where an adversary's narrative is internally inconsistent or exploits a real knowledge gap in the audience

## What it produces

- a structured node-link graph with labeled directed relationships between all key concepts
- identification of orphan nodes (concepts not connected to the core topic) and missing links
- a checklist of conflicts or contradictions visible in the link structure

## Defensive boundary

Use Mind Maps & Concept Maps only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Mind Maps & Concept Maps to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Mind Maps & Concept Maps, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Mind Maps & Concept Maps, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Mind Maps & Concept Maps recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Mind Maps & Concept Maps: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Mind Maps & Concept Maps: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Mind Maps & Concept Maps: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Mind Maps & Concept Maps cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Mind Maps & Concept Maps should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Mind Maps & Concept Maps, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Mind Maps & Concept Maps, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Mind Maps & Concept Maps, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Mind Maps & Concept Maps failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Mind Maps & Concept Maps failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Mind Maps & Concept Maps failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Mind Maps & Concept Maps to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Mind Maps & Concept Maps into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Mind Maps & Concept Maps to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- name links, not just draw them — unlabeled edges carry no analytic information
- use directed arrows to record WHO acts on WHOM or WHAT causes WHAT, not mere association
- distinguish 'is a', 'causes', 'depends on', and 'contradicts' as distinct link types
- after drafting, check every leaf node: if it has no outbound links, ask whether it is truly terminal or whether reasoning stopped prematurely
