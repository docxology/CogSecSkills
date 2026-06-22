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

## Failure modes
- Research Design Critique: accepting a study's stated conclusion when confounds, selection bias, construct mismatch, or underpowered statistics were never traced against its design, so an inferential leap from a measured outcome to a broad causal claim the design cannot license is mistaken for a finding the evidence supports.
- Research Design Critique: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Research Design Critique: reporting the validity critique without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Research Design Critique outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the validity critique from Research Design Critique into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Research Design Critique to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with study text, and claim under review' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not reject a study because its conclusion is inconvenient — assess design quality independently of whether you agree with the finding
- do not conflate statistical significance with substantive validity — a well-powered null result can be as design-flawed as any other study
- do not omit the external validity dimension because the study is internally clean — a tightly controlled lab result may not transfer to real-world conditions
- do not produce only a narrative critique without specifying which validity dimension each threat belongs to

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
