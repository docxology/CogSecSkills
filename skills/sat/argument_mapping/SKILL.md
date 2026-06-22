---
name: sat.argument_mapping
description: Diagram claims, premises, and inferential links to expose logical structure and gaps.
---

# Argument Mapping

Argument Mapping (also called argument diagramming or claim-premise visualization) represents the logical structure of a complex argument as a directed graph of claims, sub-claims, premises, evidence nodes, and inferential connectors — showing which conclusions depend on which premises and where inferential gaps, circular reasoning, or unsupported leaps occur. Originating in informal logic and philosophy of reasoning (van Eemeren, Toulmin), it was adapted for intelligence analysis by Pherson and applied in cognitive-security contexts to expose the structural vulnerabilities of narratives and the load-bearing assumptions that, if undermined, collapse the whole argument. It is the diagnostic complement to Red Team critique.

## When to use

- An analytic product, policy argument, or adversary narrative must be examined for logical soundness before it is accepted or acted on
- A complex, multi-layered argument is hard to critique in prose because its structure is not explicit
- Cognitive-security assessment of an influence narrative requires identifying which premises, if refuted, would undermine the narrative's persuasive power
- Peer review of an intelligence assessment reveals disagreement about the conclusion, and the source of disagreement needs to be localized to a specific premise or inference

## What it produces

- A visual or structured representation of the argument's logical anatomy that separates claims from evidence from inference
- An explicit list of implicit assumptions embedded in inferential connectors that were previously hidden in prose
- A ranked map of argument vulnerabilities showing which nodes are most brittle and which are most load-bearing
- A reusable diagnostic artifact that can inform Red Team design, counter-narrative strategy, or analytic revision

## Defensive boundary

Use Argument Mapping only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Argument Mapping to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Argument Mapping, bind each mapped claim, inferential connector, and ranked load-bearing assumption to a specific excerpt from the argument source or a named missing premise as its evidence, and mark any node with no supporting evidence as an undefended assertion rather than an established step.
- For Argument Mapping, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the argument map.
- Before recommending any Argument Mapping action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Argument Mapping: every claim in the map traces to an evidence leaf or an explicitly marked assumption, the descriptive mapping faithfully represents the source argument, the ranked load-bearing assumptions are corroborated independently, and no unresolved contradiction would change which nodes are judged most brittle.
- Medium for Argument Mapping: the argument map is plausible, but one important argument source source, comparison case, or alternative explanation remains incomplete.
- Low for Argument Mapping: the argument map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Argument Mapping cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Argument Mapping, use only authorized argument source, and focal claim, public or source-approved records, and caller-provided context needed for the defensive task.
- For Argument Mapping, minimize person-level detail in the argument map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Argument Mapping, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Argument Mapping: conflating faithful mapping with refutation or omitting the implicit premises hidden inside inferential connectors, so the diagram either becomes a straw-man of the source or declares the structure sound while its most dangerous unstated leaps go unexamined.
- Argument Mapping: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Argument Mapping: reporting the argument map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Argument Mapping outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the argument map from Argument Mapping into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Argument Mapping to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with argument source, and focal claim' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Separate the descriptive task (mapping the argument as stated) from the evaluative task (assessing whether each step holds) — map first, critique second
- Inferential connectors are often the weakest nodes; the word 'therefore' in prose frequently hides an unstated premise that must be surfaced
- An argument map is complete only when every claim traces to an evidence leaf or is explicitly marked as an undefended assumption
- In cognitive-security contexts, identify not just logical weaknesses but rhetorical load-bearing structures: claims that would be embarrassing to rebut publicly even if logically weak
