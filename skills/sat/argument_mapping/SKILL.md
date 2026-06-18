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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Separate the descriptive task (mapping the argument as stated) from the evaluative task (assessing whether each step holds) — map first, critique second
- Inferential connectors are often the weakest nodes; the word 'therefore' in prose frequently hides an unstated premise that must be surfaced
- An argument map is complete only when every claim traces to an evidence leaf or is explicitly marked as an undefended assumption
- In cognitive-security contexts, identify not just logical weaknesses but rhetorical load-bearing structures: claims that would be embarrassing to rebut publicly even if logically weak
