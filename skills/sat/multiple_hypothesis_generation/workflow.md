# Workflow — Multiple Hypothesis Generation

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory the evidence and initial frame (read)
Read each evidence item and record what state of the world it is consistent with. Read any initial hypotheses already on the table. Note the framing assumptions embedded in those hypotheses — these are the most common source of artificial narrowing.

## Step 2 — Generate a candidate hypothesis set (reason)
Apply structured brainstorming: consider actor-based alternatives (different who), mechanism-based alternatives (different how), and intent-based alternatives (different why). Use devil's advocacy and red-team perspectives to ensure hypotheses hostile to the prevailing view are represented. Aim for at least three non-trivial hypotheses before considering the set draft-complete.

## Step 3 — Apply MECE discipline (reason)
Test each pair for mutual exclusivity: if both can simultaneously be true, either merge them into one hypothesis or add a conditional variable that makes them distinct. Test the full set for collective exhaustiveness: identify any remaining logical space not covered by any hypothesis and either add a new hypothesis or add a residual catch-all. Document every merge, split, and gap identified.

## Step 4 — Emit labeled hypothesis set and completeness audit (write)
Output each hypothesis with a label (H1–Hn), a description of its key distinguishing claim, a brief statement of what evidence pattern would most support or refute it, and any diagnostic collection requirement implied. Append the completeness audit documenting the MECE test results and any residual space.

## Evidence requirements
- For Multiple Hypothesis Generation, tie each hypothesis set, and completeness check claim to concrete evidence from the specific evidence set, initial hypotheses, and domain context item, source excerpt, observation, or command result that supports it.
- For Multiple Hypothesis Generation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the hypothesis set.
- Before recommending any Multiple Hypothesis Generation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Multiple Hypothesis Generation: the hypothesis set is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; inventory the evidence and initial frame and generate a candidate hypothesis set checks agree, and no unresolved contradiction would change the result.
- Medium for Multiple Hypothesis Generation: the hypothesis set is plausible, but one important evidence set source, comparison case, or alternative explanation remains incomplete.
- Low for Multiple Hypothesis Generation: the hypothesis set rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Multiple Hypothesis Generation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Multiple Hypothesis Generation, use only authorized evidence set, initial hypotheses, and domain context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Multiple Hypothesis Generation, minimize person-level detail in the hypothesis set; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Multiple Hypothesis Generation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Multiple Hypothesis Generation: treating evidence set as complete when inventory the evidence and initial frame and generate a candidate hypothesis set checks or contradictory evidence are missing.
- Multiple Hypothesis Generation: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Multiple Hypothesis Generation: reporting the hypothesis set without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Multiple Hypothesis Generation outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the hypothesis set from Multiple Hypothesis Generation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Multiple Hypothesis Generation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with evidence set, initial hypotheses, and domain context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow the perceived likelihood of a hypothesis to determine whether it is included — low-probability hypotheses belong in the set if they are logically possible given the evidence
- do not declare the hypothesis set complete without explicitly testing for a logical remainder (the space covered by none of the stated hypotheses)
- do not merge two hypotheses that lead to different action recommendations, even if their descriptions sound similar

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
