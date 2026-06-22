# Workflow — Issue Redefinition

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Document the original framing (read)
Write out the original question exactly as posed. Identify any explicit scope constraints in the tasking. Note what the question takes for granted — actors, time horizon, unit of analysis, success metric — before generating alternatives.

## Step 2 — Generate restatements using reframing levers (reason)
Apply at least six reframing levers in sequence, generating one or more restatements per lever: (1) Broaden — expand the scope or population. (2) Narrow — restrict the scope. (3) Invert — reframe as the opposite question. (4) Shift actor — change who the question is about. (5) Shift time horizon — ask it earlier or later. (6) Change unit of analysis — restate at a different level (individual / group / system). (7) Change success criterion — alter what a good answer would look like. Record all outputs without evaluating yet.

## Step 3 — Annotate assumptions and solution spaces (reason)
For each restatement, record: the core assumption it makes or removes relative to the original, and the solution space it opens or forecloses. Identify which restatements are genuinely distinct versus paraphrases. Flag any restatement that exposes an assumption in the original that had gone unexamined.

## Step 4 — Evaluate and select a preferred framing (reason)
Review all restatements against the consumer's actual decision need. Select the framing that best matches what the consumer can act on, is most tractable given available evidence, and minimizes unexamined embedded assumptions. If no single framing is clearly superior, propose keeping two framings in parallel and noting where they diverge.

## Step 5 — Produce the restatements register and preferred framing (write)
Write the full restatements register with all annotations. State the preferred framing clearly and explain why it was chosen. Document rejected framings and the reasons they were set aside — this record is part of the analytic transparency chain.

## Evidence requirements
- For Issue Redefinition, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Issue Redefinition, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Issue Redefinition recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Issue Redefinition: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Issue Redefinition: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Issue Redefinition: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Issue Redefinition cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Issue Redefinition should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Issue Redefinition, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Issue Redefinition, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Issue Redefinition, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Issue Redefinition failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Issue Redefinition failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Issue Redefinition failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Issue Redefinition to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Issue Redefinition into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Issue Redefinition to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not evaluate restatements while generating them — premature convergence defeats the purpose of the technique
- do not return only paraphrases of the original question; each restatement must use a distinct lever that changes the assumption set or solution space
- do not select a preferred framing simply because it matches the original question — if the original framing survives the exercise it should survive on its merits, with documented rationale
- do not skip documenting rejected framings — the record of alternatives considered is part of the analytic audit trail and cognitive-security transparency

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
