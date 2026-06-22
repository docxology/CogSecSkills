# Workflow — Team A / Team B

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish teams and shared evidence (read, ask)
Confirm the two competing hypotheses (Team A and Team B) and the shared evidence base. If the hypotheses are ambiguous or incompletely specified, use ask to clarify before proceeding. Document the shared evidence inventory — both teams work from exactly the same raw material.

## Step 2 — Develop each team's strongest case (reason)
For Team A: construct the strongest honest argument for hypothesis A — which evidence supports it most compellingly, what assumptions it requires, and what would have to be true for it to be correct. Then do the same for Team B. Identify the key diagnostic evidence — the evidence that most clearly discriminates between the two hypotheses. Also identify what each team must concede: the evidence that cuts against its own position.

## Step 3 — Structure the debate and adjudicate (reason, write)
Present Team A's core argument and Team B's core argument in parallel. Document the key points of evidentiary disagreement. Adjudicate: which hypothesis is better supported by the diagnostic evidence? At what confidence level? What residual uncertainties remain? What new evidence would most shift the balance? Write the team_debate_summary.

## Evidence requirements
- For Team A / Team B, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Team A / Team B, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Team A / Team B recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Team A / Team B: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Team A / Team B: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Team A / Team B: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Team A / Team B cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Team A / Team B should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Team A / Team B, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Team A / Team B, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Team A / Team B, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Team A / Team B failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Team A / Team B failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Team A / Team B failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Team A / Team B to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Team A / Team B into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Team A / Team B to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow either team's case to be a strawman — each must represent the genuinely strongest available argument for its hypothesis
- do not produce a compromise or 'split the difference' conclusion — adjudicate honestly which hypothesis the evidence better supports
- do not omit the concession step — each team must acknowledge the evidence that most undermines its position
- do not conflate the two roles: Team A argues for A, Team B argues for B — the moderator/analyst adjudicates, not either team

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
