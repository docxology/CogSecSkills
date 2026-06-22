# Workflow — Customer (AIMS) Checklist

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest tasking and draft (read)
Read the tasking directive, the draft or outline, and any available consumer context. Note the stated purpose, the stated audience, and any explicit or implicit constraints on scope.

## Step 2 — Resolve AIMS parameters (ask, reason)
For each of the four parameters, determine whether it is explicitly stated, inferrable from context, or genuinely unknown. For unknown parameters, generate targeted clarifying questions. For inferrable ones, state the inferred value and the basis for the inference.

## Step 3 — Assess alignment between draft and AIMS (reason)
Compare the draft's actual structure, lead, and conclusions against the resolved AIMS parameters. Does the lead sentence state the Message? Does the logical flow match the Storyline? Is technical depth appropriate for the Audience? Is the Issue actually answered?

## Step 4 — Produce worksheet and revision recommendations (write)
Fill the AIMS worksheet with the four resolved parameters. Write specific, actionable revision recommendations for every misalignment found, citing the paragraph or section that needs revision and explaining why it fails the relevant parameter.

## Evidence requirements
- For Customer (AIMS) Checklist, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Customer (AIMS) Checklist, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Customer (AIMS) Checklist recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Customer (AIMS) Checklist: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Customer (AIMS) Checklist: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Customer (AIMS) Checklist: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Customer (AIMS) Checklist cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Customer (AIMS) Checklist should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Customer (AIMS) Checklist, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Customer (AIMS) Checklist, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Customer (AIMS) Checklist, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Customer (AIMS) Checklist failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Customer (AIMS) Checklist failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Customer (AIMS) Checklist failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Customer (AIMS) Checklist to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Customer (AIMS) Checklist into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Customer (AIMS) Checklist to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow the Message field to be a topic sentence ('this paper discusses X') — it must be an assertive conclusion ('we assess X because Y')
- do not conflate the Issue (the precise question) with the Audience's broader area of responsibility
- do not skip the Storyline parameter — 'accurate analysis in the wrong order' is a common and costly failure mode

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
