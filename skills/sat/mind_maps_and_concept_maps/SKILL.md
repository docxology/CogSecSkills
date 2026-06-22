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

- For Mind Maps & Concept Maps, bind each node and each labeled edge to concrete evidence in the source material, preserving the raw language used for provenance, and mark any link that rests on inference rather than confirmed relationship; an edge asserted without supporting evidence is a hypothesis about structure, not a documented one.
- For Mind Maps & Concept Maps, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the concept graph.
- Before recommending any Mind Maps & Concept Maps action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Mind Maps & Concept Maps: every node and labeled directed link traces to named concepts and relationships in the source material, distinct concepts are kept on separate nodes rather than conflated, the gap-and-conflict audit has been run over the whole graph, and no unresolved contradiction in the link structure would change the represented understanding.
- Medium for Mind Maps & Concept Maps: the concept graph is plausible, but one important source material source, comparison case, or alternative explanation remains incomplete.
- Low for Mind Maps & Concept Maps: the concept graph rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Mind Maps & Concept Maps cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Mind Maps & Concept Maps, use only authorized source material, central topic, and map type, public or source-approved records, and caller-provided context needed for the defensive task.
- For Mind Maps & Concept Maps, minimize person-level detail in the concept graph; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Mind Maps & Concept Maps, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Mind Maps & Concept Maps: presenting the graph as a faithful structure when edges were left unlabeled or distinct concepts were collapsed into one node to keep it tidy, so hidden conflation and uninterpretable links obscure the very relationships and contradictions the map exists to expose.
- Mind Maps & Concept Maps: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Mind Maps & Concept Maps: reporting the concept graph without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Mind Maps & Concept Maps outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the concept graph from Mind Maps & Concept Maps into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Mind Maps & Concept Maps to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with source material, central topic, and map type' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- name links, not just draw them — unlabeled edges carry no analytic information
- use directed arrows to record WHO acts on WHOM or WHAT causes WHAT, not mere association
- distinguish 'is a', 'causes', 'depends on', and 'contradicts' as distinct link types
- after drafting, check every leaf node: if it has no outbound links, ask whether it is truly terminal or whether reasoning stopped prematurely
