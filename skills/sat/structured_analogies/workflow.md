# Workflow — Structured Analogies

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the current situation (read)
Read the current situation description. Identify the key attributes that any historical analogue must share: actor type, medium, intent, target, environmental conditions. These become the selection criteria.

## Step 2 — Identify and select candidate cases (search, reason)
Search for historical cases that plausibly match the stated criteria. Aim for at least three to five cases, including at least one that is widely cited (to capture the intuitive analogy) and at least one that is less obvious (to test its boundaries). Exclude cases only if they fail stated criteria, not because their outcomes are inconvenient.

## Step 3 — Map similarities and dissimilarities (reason)
For each case, systematically compare it to the current situation on every dimension. Rate each comparison as strongly similar, partially similar, or dissimilar. Record the key dissimilarity for every case — even the closest analogues will have important disanalogies.

## Step 4 — Derive lessons and bound confidence (reason, write)
Extract lessons that are supported by multiple cases and are robust to the dissimilarities. Note where a lesson rests on a single case or on a weak analogy fit, and reduce confidence accordingly. Write predicted trajectories qualified by the analogy's limitations.

## Step 5 — Produce comparison table and analytic narrative (write)
Emit the multi-case comparison table and the lessons-and-predictions narrative. Flag the single most relied-upon analogy as a potential anchor bias risk.

## Evidence requirements
- For Structured Analogies, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Structured Analogies, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Structured Analogies recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Structured Analogies: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Structured Analogies: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Structured Analogies: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Structured Analogies cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Structured Analogies should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Structured Analogies, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Structured Analogies, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Structured Analogies, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Structured Analogies failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Structured Analogies failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Analogies failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Structured Analogies to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Structured Analogies into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Structured Analogies to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not select cases after learning their outcomes in a way that biases toward cases that support the preferred conclusion
- do not treat a close similarity on salient features as confirmation — check structural and contextual dissimilarities before drawing lessons
- do not present a single historical case as 'the' analogy without showing the full comparison set and why others were excluded or downweighted

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
