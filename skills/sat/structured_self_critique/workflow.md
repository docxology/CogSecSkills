# Workflow — Structured Self-Critique

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest and inventory (read)
Read the full analysis draft and extract: the key judgments (what is asserted), the evidence cited in support, the assumptions made explicit or implicit, and any alternative hypotheses mentioned. List them in a working inventory.

## Step 2 — Apply the challenge checklist (reason)
Work through the standard structured self-critique checklist sequentially: (1) What are my key assumptions and could they be wrong? (2) Is the evidence reliable, current, and source-diverse? (3) What alternative explanations exist and why were they rejected? (4) Could the evidence be explained by deception or deliberate manipulation? (5) Is my confidence language calibrated to the actual evidence quality? (6) What would change my judgment — and is that indicator being monitored? (7) What has been left out because it was inconvenient or hard to collect? Document an honest answer to each.

## Step 3 — Flag weaknesses and draft revisions (reason, write)
For each challenge question that revealed a weakness, write a specific annotation: what the weakness is, how it affects the key judgment, and what revision or caveat is needed. Produce the critique_report with all annotations, alternative framings, and a prioritized revision list.

## Evidence requirements
- For Structured Self-Critique, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Structured Self-Critique, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Structured Self-Critique recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Structured Self-Critique: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Structured Self-Critique: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Structured Self-Critique: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Structured Self-Critique cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Structured Self-Critique should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Structured Self-Critique, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Structured Self-Critique, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Structured Self-Critique, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Structured Self-Critique failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Structured Self-Critique failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Self-Critique failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Structured Self-Critique to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Structured Self-Critique into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Structured Self-Critique to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat the checklist as a formality — each question must receive a genuine answer, not a reflexive 'no issues found'
- do not dismiss alternative explanations without stating the specific evidence that rules them out
- do not allow confidence language to remain uncalibrated — vague hedges ('might', 'could') must be resolved to an explicit likelihood tier
- do not omit inconvenient gaps in evidence — the report must name what is unknown, not only what is known

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
