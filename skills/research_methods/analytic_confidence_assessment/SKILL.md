---
name: research_methods.analytic_confidence_assessment
description: Assign and justify confidence using source quality, corroboration, and assumption load.
---

# Analytic Confidence Assessment

Analytic Confidence Assessment is a structured technique for assigning an explicit confidence level to an analytic judgment by systematically evaluating source quality, degree of corroboration, and the load of unstated assumptions underlying the conclusion. It draws on intelligence community standards (ICD 203) and structured analytic technique literature to ensure that confidence labels such as 'high,' 'moderate,' or 'low' are operationally defined and traceable rather than impressionistic. The technique prevents both overconfidence from thin evidence and false modesty that obscures genuine signal.

## When to use

- before publishing or briefing an analytic conclusion that will drive decisions
- when evidence is sparse, mixed, or derived from single sources
- when assumption load is high and unstated assumptions may be doing most of the analytic work
- when stakeholders need to understand the reliability limits of a finding

## What it produces

- an explicit confidence tier (high/moderate/low) with sub-dimension scores
- a plain-language narrative explaining why confidence is not higher or lower
- a list of the conditions that would change the confidence tier

## Defensive boundary

Use Analytic Confidence Assessment only for research-methods and synthesis integrity: recognize, assess, document, or defend reproducibility, calibrated confidence, and transparent synthesis. Do not use this skill to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.

## Misuse redirect

If a request asks Analytic Confidence Assessment to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence, refuse that path and redirect to the safe defensive form: synthesize supplied or authorized sources with explicit confidence and uncertainty labels.

## Evidence discipline

- For Analytic Confidence Assessment, bind each sub-dimension score and the overall tier to concrete evidence — a specific source with its reliability history, an observed corroboration or contradiction, or a named load-bearing assumption — so a second analyst can reproduce the same tier from the same inputs rather than accept an impressionistic rating.
- For Analytic Confidence Assessment, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the confidence assessment.
- Before recommending any Analytic Confidence Assessment action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Analytic Confidence Assessment: the assigned confidence tier is justified by strong sub-scores on source quality, corroboration, and assumption load, the corroboration comes from genuinely independent sources rather than a common reporting chain, the tier holds under the conservative weakest-dimension rule, and no unresolved contradiction in the evidence chain would change it.
- Medium for Analytic Confidence Assessment: the confidence assessment is plausible, but one important judgment source, comparison case, or alternative explanation remains incomplete.
- Low for Analytic Confidence Assessment: the confidence assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Analytic Confidence Assessment cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating research_methods evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Analytic Confidence Assessment, use only authorized judgment, evidence set, and key assumptions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Analytic Confidence Assessment, minimize person-level detail in the confidence assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Analytic Confidence Assessment, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Analytic Confidence Assessment: assigning a tier from how comfortable the analyst feels rather than from scored dimensions, treating common-origin sources as independent corroboration, or leaving high-impact unstated assumptions untested, so a confident-looking label masks thin evidence rather than a defensible judgment.
- Analytic Confidence Assessment: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Analytic Confidence Assessment: reporting the confidence assessment without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Analytic Confidence Assessment outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the confidence assessment from Analytic Confidence Assessment into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Analytic Confidence Assessment to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with judgment, evidence set, and key assumptions' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- confidence in the judgment and confidence in individual sources are distinct — assess both separately
- corroboration from independent sources raises confidence; from correlated sources it does not
- every unstated assumption that the conclusion requires is a confidence-reducing liability
- confidence labels must be operationally defined so two analysts reach the same tier from the same inputs
