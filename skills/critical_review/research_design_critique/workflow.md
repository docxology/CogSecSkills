# Workflow — Research Design Critique

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract design parameters (read)
Read the methods section carefully. Record: study type (RCT, quasi-experiment, observational, survey, case study), sample size and selection method, comparison condition if any, outcome measures and how they were operationalized, and the stated causal or descriptive claim.

## Step 2 — Apply the four-validity typology (reason)
For internal validity: identify confounds, selection bias, attrition, maturation, history effects, and testing effects. For external validity: assess population, setting, and temporal generalizability. For construct validity: check whether measures actually capture the constructs claimed and whether demand characteristics or mono-operation bias apply. For statistical conclusion validity: note underpowered tests, inflated Type I error from multiple comparisons, violated assumptions, and fishing.

## Step 3 — Assess inferential reach (reason)
Compare the study's stated conclusions to what the design can actually support. Identify inferential leaps — places where the authors move from their measured outcome to a broader or causal claim the design does not license. Rate each threat high/medium/low for its likely impact on the primary conclusion.

## Step 4 — Produce the critique and narrowed claim (write)
Write the validity-threat table with columns: dimension, threat name, evidence from study, severity. Then write the inferential reach assessment as a narrative: state what narrower claim the design does support and what caveats a responsible consumer must apply. Flag any threats severe enough to recommend the conclusion be withheld or substantially qualified.

## Evidence requirements
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

## Failure modes
- Research Design Critique failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Research Design Critique failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Research Design Critique failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Research Design Critique to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Research Design Critique into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Research Design Critique to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not reject a study because its conclusion is inconvenient — assess design quality independently of whether you agree with the finding
- do not conflate statistical significance with substantive validity — a well-powered null result can be as design-flawed as any other study
- do not omit the external validity dimension because the study is internally clean — a tightly controlled lab result may not transfer to real-world conditions
- do not produce only a narrative critique without specifying which validity dimension each threat belongs to

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
