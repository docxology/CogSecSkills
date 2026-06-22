---
name: critical_review.research_design_critique
description: Critique a study's design for validity threats, confounds, and inferential reach.
---

# Research Design Critique

Research Design Critique applies the canonical framework of internal validity, external validity, construct validity, and statistical conclusion validity to systematically identify flaws in a study's design before accepting its conclusions. The technique surfaces confounds, selection biases, demand characteristics, measurement problems, and unjustified inferential leaps that weaken a claim's epistemic weight. It is grounded in Cook and Campbell's validity typology and is standard practice in intelligence analysis, scientific peer review, and cognitive-security assessments of research used to justify policy or belief updates.

## When to use

- a study or report is cited to justify a consequential decision or belief update
- a research claim is used to discredit or bolster a policy position
- you need to assess whether a finding generalizes beyond its original sample or context
- a study is presented as definitive but the design is observational or weakly controlled
- a cognitive-security assessment requires evaluating the evidence base behind a narrative

## What it produces

- a structured table mapping each validity dimension to specific threats found in the design
- a severity rating for each threat (high/medium/low) with textual evidence from the study
- a narrowed claim statement: the conclusion the evidence actually supports vs. what was stated
- recommended caveats that any honest consumer of the research should apply

## Defensive boundary

Use Research Design Critique only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Research Design Critique to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Research Design Critique, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Research Design Critique, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Research Design Critique recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Research Design Critique: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Research Design Critique: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Research Design Critique: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Research Design Critique cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Research Design Critique should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Research Design Critique, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Research Design Critique, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Research Design Critique, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Research Design Critique failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Research Design Critique failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Research Design Critique failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Research Design Critique to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Research Design Critique into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Research Design Critique to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- separate the four validity dimensions — internal, external, construct, and statistical conclusion — and assess each independently before forming an overall judgment
- identify what the design cannot rule out, not just what it claims to demonstrate
- distinguish between threats that are theoretical and threats for which the study provides positive evidence of bias
- state the narrowest defensible claim the design supports; resist upgrading it to the author's preferred conclusion
