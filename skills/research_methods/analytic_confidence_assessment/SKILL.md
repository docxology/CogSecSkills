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

- For Analytic Confidence Assessment, bind each finding to a labeled source — study designs, source quality, reproducibility artifacts, and uncertainty records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Analytic Confidence Assessment, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Analytic Confidence Assessment recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Analytic Confidence Assessment: independent lines of study designs, source quality, reproducibility artifacts, and uncertainty records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Analytic Confidence Assessment: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Analytic Confidence Assessment: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Analytic Confidence Assessment cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Analytic Confidence Assessment should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Analytic Confidence Assessment, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Analytic Confidence Assessment, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Analytic Confidence Assessment, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Analytic Confidence Assessment failure: collapsing heterogeneous evidence into an unsupported single confident conclusion.
- Analytic Confidence Assessment failure: producing guidance that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Analytic Confidence Assessment failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Analytic Confidence Assessment to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Analytic Confidence Assessment into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Analytic Confidence Assessment to synthesize supplied or authorized sources with explicit confidence and uncertainty labels' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- confidence in the judgment and confidence in individual sources are distinct — assess both separately
- corroboration from independent sources raises confidence; from correlated sources it does not
- every unstated assumption that the conclusion requires is a confidence-reducing liability
- confidence labels must be operationally defined so two analysts reach the same tier from the same inputs
