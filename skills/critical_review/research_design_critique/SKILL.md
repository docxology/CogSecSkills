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

- For Research Design Critique, bind each validity threat and severity rating to concrete evidence quoted from the study's design and report the narrowest defensible claim that evidence actually supports, distinguishing a merely theoretical threat from one for which the study shows positive evidence of bias.
- For Research Design Critique, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the validity critique.
- Before recommending any Research Design Critique action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Research Design Critique: each validity threat is tied to specific design evidence from the study's methods, sampling frame, and measures, the assessments across internal, external, construct, and statistical-conclusion validity are made independently, and no unresolved contradiction would change the narrowed claim the design is judged to actually support.
- Medium for Research Design Critique: the validity critique is plausible, but one important study text source, comparison case, or alternative explanation remains incomplete.
- Low for Research Design Critique: the validity critique rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Research Design Critique cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Research Design Critique, use only authorized study text, and claim under review, public or source-approved records, and caller-provided context needed for the defensive task.
- For Research Design Critique, minimize person-level detail in the validity critique; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Research Design Critique, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Research Design Critique: accepting a study's stated conclusion when confounds, selection bias, construct mismatch, or underpowered statistics were never traced against its design, so an inferential leap from a measured outcome to a broad causal claim the design cannot license is mistaken for a finding the evidence supports.
- Research Design Critique: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Research Design Critique: reporting the validity critique without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Research Design Critique outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the validity critique from Research Design Critique into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Research Design Critique to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with study text, and claim under review' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- separate the four validity dimensions — internal, external, construct, and statistical conclusion — and assess each independently before forming an overall judgment
- identify what the design cannot rule out, not just what it claims to demonstrate
- distinguish between threats that are theoretical and threats for which the study provides positive evidence of bias
- state the narrowest defensible claim the design supports; resist upgrading it to the author's preferred conclusion
