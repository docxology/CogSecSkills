# Workflow — Team A / Team B

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish teams and shared evidence (read, ask)
Confirm the two competing hypotheses (Team A and Team B) and the shared evidence base. If the hypotheses are ambiguous or incompletely specified, use ask to clarify before proceeding. Document the shared evidence inventory — both teams work from exactly the same raw material.

## Step 2 — Develop each team's strongest case (reason)
For Team A: construct the strongest honest argument for hypothesis A — which evidence supports it most compellingly, what assumptions it requires, and what would have to be true for it to be correct. Then do the same for Team B. Identify the key diagnostic evidence — the evidence that most clearly discriminates between the two hypotheses. Also identify what each team must concede: the evidence that cuts against its own position.

## Step 3 — Structure the debate and adjudicate (reason, write)
Present Team A's core argument and Team B's core argument in parallel. Document the key points of evidentiary disagreement. Adjudicate: which hypothesis is better supported by the diagnostic evidence? At what confidence level? What residual uncertainties remain? What new evidence would most shift the balance? Write the team_debate_summary.

## Evidence requirements
- For Team A / Team B, tie each team's core argument, every conceded weakness, and the final adjudication to concrete evidence from the shared evidence base, citing the specific item that discriminates between hypothesis A and hypothesis B, and label which points rest on assumption rather than observed evidence.
- For Team A / Team B, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the team debate summary.
- Before recommending any Team A / Team B action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Team A / Team B: each team's strongest case is built in good faith from the shared evidence base rather than a strawman, the adjudication of which hypothesis is better supported holds when the most diagnostic evidence item is reweighted, and no unresolved contradiction in that evidence would reverse the verdict.
- Medium for Team A / Team B: the team debate summary is plausible, but one important shared evidence source, comparison case, or alternative explanation remains incomplete.
- Low for Team A / Team B: the team debate summary rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Team A / Team B cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Team A / Team B, use only authorized shared evidence, hypothesis a, and hypothesis b, public or source-approved records, and caller-provided context needed for the defensive task.
- For Team A / Team B, minimize person-level detail in the team debate summary; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Team A / Team B, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Team A / Team B: declaring the debate concluded when one side was argued as a strawman, when the concession step that forces each team to acknowledge disconfirming evidence was skipped, or when the output collapsed into a split-the-difference compromise instead of an honest adjudication of which hypothesis the evidence supports.
- Team A / Team B: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Team A / Team B: reporting the team debate summary without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Team A / Team B outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the team debate summary from Team A / Team B into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Team A / Team B to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with shared evidence, hypothesis a, and hypothesis b' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow either team's case to be a strawman — each must represent the genuinely strongest available argument for its hypothesis
- do not produce a compromise or 'split the difference' conclusion — adjudicate honestly which hypothesis the evidence better supports
- do not omit the concession step — each team must acknowledge the evidence that most undermines its position
- do not conflate the two roles: Team A argues for A, Team B argues for B — the moderator/analyst adjudicates, not either team

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
