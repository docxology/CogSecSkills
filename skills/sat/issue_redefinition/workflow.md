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
- For Issue Redefinition, anchor each restatement and the recommended framing in concrete evidence from the original question and its tasking context, documenting the specific assumption each lever exposes and recording the rejected framings; a preferred framing asserted without evidence that it better serves the decision is a preference, not a reasoned reframing.
- For Issue Redefinition, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the restatements register.
- Before recommending any Issue Redefinition action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Issue Redefinition: each restatement applies a genuinely distinct reframing lever rather than paraphrasing the original, the assumption removed or added by each is articulated explicitly, the recommended framing is justified against the consumer's actual decision need, and no unresolved tension among the alternatives would overturn that choice.
- Medium for Issue Redefinition: the restatements register is plausible, but one important original question source, comparison case, or alternative explanation remains incomplete.
- Low for Issue Redefinition: the restatements register rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Issue Redefinition cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Issue Redefinition, use only authorized original question, and tasking context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Issue Redefinition, minimize person-level detail in the restatements register; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Issue Redefinition, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Issue Redefinition: declaring the question reframed when the restatements are only paraphrases that change wording without changing the embedded assumptions, or when a preferred framing was selected before the full set was generated, so the original anchoring quietly survives the exercise.
- Issue Redefinition: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Issue Redefinition: reporting the restatements register without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Issue Redefinition outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the restatements register from Issue Redefinition into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Issue Redefinition to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with original question, and tasking context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not evaluate restatements while generating them — premature convergence defeats the purpose of the technique
- do not return only paraphrases of the original question; each restatement must use a distinct lever that changes the assumption set or solution space
- do not select a preferred framing simply because it matches the original question — if the original framing survives the exercise it should survive on its merits, with documented rationale
- do not skip documenting rejected framings — the record of alternatives considered is part of the analytic audit trail and cognitive-security transparency

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
