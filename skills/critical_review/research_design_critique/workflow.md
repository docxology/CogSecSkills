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

## Anti-criteria (must NOT happen)
- do not reject a study because its conclusion is inconvenient — assess design quality independently of whether you agree with the finding
- do not conflate statistical significance with substantive validity — a well-powered null result can be as design-flawed as any other study
- do not omit the external validity dimension because the study is internally clean — a tightly controlled lab result may not transfer to real-world conditions
- do not produce only a narrative critique without specifying which validity dimension each threat belongs to

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
