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
- For Multiple Hypothesis Generation, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Multiple Hypothesis Generation, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Multiple Hypothesis Generation recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Multiple Hypothesis Generation: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Multiple Hypothesis Generation: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Multiple Hypothesis Generation: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Multiple Hypothesis Generation cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Multiple Hypothesis Generation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Multiple Hypothesis Generation, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Multiple Hypothesis Generation, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Multiple Hypothesis Generation, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Multiple Hypothesis Generation failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Multiple Hypothesis Generation failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Multiple Hypothesis Generation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Multiple Hypothesis Generation to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Multiple Hypothesis Generation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Multiple Hypothesis Generation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow the perceived likelihood of a hypothesis to determine whether it is included — low-probability hypotheses belong in the set if they are logically possible given the evidence
- do not declare the hypothesis set complete without explicitly testing for a logical remainder (the space covered by none of the stated hypotheses)
- do not merge two hypotheses that lead to different action recommendations, even if their descriptions sound similar

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
