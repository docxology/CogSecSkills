# Workflow — Getting Started Checklist

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Capture the tasking (read, ask)
Read the analytic request and any background material. If the consumer's actual decision need is unclear, ask targeted clarifying questions. Resist beginning substantive research until the question is explicit.

## Step 2 — Articulate the primary question and subordinate questions (reason)
Restate the primary analytic question in one precise, answerable sentence. Break it into subordinate questions that, when answered, will resolve the primary. Identify the time horizon and the relevant actor or domain.

## Step 3 — Identify key drivers (reason)
List the variables whose values most determine the answer. For each driver, note its current estimated state and the direction of change that would shift the analytic outcome most significantly.

## Step 4 — Surface assumptions (reason)
Enumerate assumptions — things being treated as true without verification. Rate each assumption for confidence (high/medium/low) and note what evidence would challenge it. Flag any assumption whose failure would overturn the analysis.

## Step 5 — Log prior judgments (reason)
Record any prior analytic judgments — published or informal — about the topic. Note who held them, on what evidence, and how strongly. These are anchors to be tested, not necessarily adopted.

## Step 6 — Produce the baseline checklist (write)
Compile the above into a structured baseline document: primary question, subordinate questions, drivers, assumptions register, prior judgments log, and a gaps list. This document is the analytic contract for the work that follows.

## Evidence requirements
- For Getting Started Checklist, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Getting Started Checklist, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Getting Started Checklist recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Getting Started Checklist: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Getting Started Checklist: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Getting Started Checklist: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Getting Started Checklist cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Getting Started Checklist should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Getting Started Checklist, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Getting Started Checklist, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Getting Started Checklist, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Getting Started Checklist failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Getting Started Checklist failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Getting Started Checklist failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Getting Started Checklist to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Getting Started Checklist into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Getting Started Checklist to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not begin substantive research or drafting before the primary question is written down in one sentence
- do not treat prior judgments as authoritative starting points — log them as potential anchors
- do not skip the assumptions register when the problem feels straightforward — that intuition is itself an assumption
- do not conflate drivers (variables to be tracked) with assumptions (claims accepted without current verification)

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
