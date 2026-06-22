# Workflow — Alternative Futures (Scenarios)

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Identify critical uncertainties (read, reason)
Review the problem statement and known drivers. Through structured brainstorming (e.g., sticky-note diverge-converge), identify the forces most likely to determine the outcome and most uncertain in direction. Select the two that are (a) most impactful and (b) most independent of each other to serve as scenario axes.

## Step 2 — Construct the scenario matrix (reason)
Place the two chosen uncertainties on perpendicular axes with their extreme poles labeled. The four quadrants define four distinct alternative futures. Name each scenario memorably (evocative label, not 'Scenario A'). Confirm each is internally coherent: does a world where axis-1 is high and axis-2 is low make logical sense?

## Step 3 — Populate scenario narratives (reason, write)
For each quadrant, write a brief (one-paragraph) narrative describing what the world looks like in that future: key actors, conditions, dynamics, and consequences for the focal question. Include a date or time horizon. Ensure each narrative is distinct — if two quadrants feel similar, the axes may not be truly independent.

## Step 4 — Derive discriminating indicators (reason, write)
For each scenario, identify 3–5 observable signals that would be present in that world but absent or weak in others. Prioritize leading indicators over lagging. Compile into a tracking table: indicator, which scenario(s) it favors, current status, and collection priority.

## Step 5 — Stress-test strategy and document (reason, write)
Evaluate the current strategy or plan against each scenario: Where does it succeed? Where does it fail? Identify robust actions (effective across all or most scenarios) and fragile actions (optimal only in the assumed-most-likely scenario). Write the final deliverable: matrix, narratives, indicator table, and strategy assessment.

## Evidence requirements
- For Alternative Futures (Scenarios), bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Alternative Futures (Scenarios), keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Alternative Futures (Scenarios) recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Alternative Futures (Scenarios): independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Alternative Futures (Scenarios): the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Alternative Futures (Scenarios): the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Alternative Futures (Scenarios) cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Alternative Futures (Scenarios) should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Alternative Futures (Scenarios), use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Alternative Futures (Scenarios), protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Alternative Futures (Scenarios), do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Alternative Futures (Scenarios) failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Alternative Futures (Scenarios) failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Alternative Futures (Scenarios) failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Alternative Futures (Scenarios) to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Alternative Futures (Scenarios) into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Alternative Futures (Scenarios) to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not construct scenarios as best-case / worst-case / most-likely — this is a disguised single-point forecast, not genuine alternatives
- Do not assign probabilities to scenarios during construction; probability assignment reintroduces the anchoring the technique is designed to defeat
- Do not let the 'most likely' scenario receive disproportionate narrative detail, as this biases consumers back toward single-outcome thinking
- Do not skip the indicator step — scenarios without discriminating signals cannot be operationally monitored

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
