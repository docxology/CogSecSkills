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
- For Customer (AIMS) Checklist, ground each resolved Audience, Issue, Message, and Storyline value in evidence from the tasking directive, draft, or stated consumer context, label any inferred parameter with its basis, and raise targeted clarifying questions for parameters the available evidence cannot settle.
- For Customer (AIMS) Checklist, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the aims worksheet.
- Before recommending any Customer (AIMS) Checklist action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Customer (AIMS) Checklist: the Audience names a specific decision-making role, the Issue is narrow enough to answer in this product, the Message is a single actionable declarative assertion, the Storyline is derived from that Message and Audience, and no unresolved ambiguity in the tasking would change the worksheet.
- Medium for Customer (AIMS) Checklist: the aims worksheet is plausible, but one important product or outline source, comparison case, or alternative explanation remains incomplete.
- Low for Customer (AIMS) Checklist: the aims worksheet rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Customer (AIMS) Checklist cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Customer (AIMS) Checklist, use only authorized product or outline, and consumer context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Customer (AIMS) Checklist, minimize person-level detail in the aims worksheet; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Customer (AIMS) Checklist, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Customer (AIMS) Checklist: passing a product as customer-ready when the Message is still a topic sentence rather than an assertive conclusion, the Audience is an organization rather than a decision role, or the Storyline was skipped, so analytically correct work is delivered in a form the consumer cannot act on.
- Customer (AIMS) Checklist: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Customer (AIMS) Checklist: reporting the aims worksheet without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Customer (AIMS) Checklist outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the aims worksheet from Customer (AIMS) Checklist into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Customer (AIMS) Checklist to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with product or outline, and consumer context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow the Message field to be a topic sentence ('this paper discusses X') — it must be an assertive conclusion ('we assess X because Y')
- do not conflate the Issue (the precise question) with the Audience's broader area of responsibility
- do not skip the Storyline parameter — 'accurate analysis in the wrong order' is a common and costly failure mode

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
