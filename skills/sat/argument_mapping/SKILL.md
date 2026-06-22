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

- For Argument Mapping, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Argument Mapping, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Argument Mapping recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Argument Mapping: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Argument Mapping: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Argument Mapping: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Argument Mapping cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Argument Mapping should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Argument Mapping, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Argument Mapping, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Argument Mapping, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Argument Mapping failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Argument Mapping failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Argument Mapping failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Argument Mapping to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Argument Mapping into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Argument Mapping to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Separate the descriptive task (mapping the argument as stated) from the evaluative task (assessing whether each step holds) — map first, critique second
- Inferential connectors are often the weakest nodes; the word 'therefore' in prose frequently hides an unstated premise that must be surfaced
- An argument map is complete only when every claim traces to an evidence leaf or is explicitly marked as an undefended assumption
- In cognitive-security contexts, identify not just logical weaknesses but rhetorical load-bearing structures: claims that would be embarrassing to rebut publicly even if logically weak
