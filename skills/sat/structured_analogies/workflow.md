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
- For Structured Analogies, tie each case comparison table, and lessons and predictions claim to concrete evidence from the specific current situation, candidate cases, and comparison dimensions item, source excerpt, observation, or command result that supports it.
- For Structured Analogies, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the case comparison table.
- Before recommending any Structured Analogies action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Structured Analogies: the case comparison table is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; characterize the current situation and identify and select candidate cases checks agree, and no unresolved contradiction would change the result.
- Medium for Structured Analogies: the case comparison table is plausible, but one important current situation source, comparison case, or alternative explanation remains incomplete.
- Low for Structured Analogies: the case comparison table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Structured Analogies cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Structured Analogies, use only authorized current situation, candidate cases, and comparison dimensions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Structured Analogies, minimize person-level detail in the case comparison table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Structured Analogies, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Structured Analogies: treating current situation as complete when characterize the current situation and identify and select candidate cases checks or contradictory evidence are missing.
- Structured Analogies: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Analogies: reporting the case comparison table without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Structured Analogies outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the case comparison table from Structured Analogies into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Structured Analogies to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with current situation, candidate cases, and comparison dimensions' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not select cases after learning their outcomes in a way that biases toward cases that support the preferred conclusion
- do not treat a close similarity on salient features as confirmation — check structural and contextual dissimilarities before drawing lessons
- do not present a single historical case as 'the' analogy without showing the full comparison set and why others were excluded or downweighted

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
