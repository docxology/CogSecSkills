# Workflow — Structured Self-Critique

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest and inventory (read)
Read the full analysis draft and extract: the key judgments (what is asserted), the evidence cited in support, the assumptions made explicit or implicit, and any alternative hypotheses mentioned. List them in a working inventory.

## Step 2 — Apply the challenge checklist (reason)
Work through the standard structured self-critique checklist sequentially: (1) What are my key assumptions and could they be wrong? (2) Is the evidence reliable, current, and source-diverse? (3) What alternative explanations exist and why were they rejected? (4) Could the evidence be explained by deception or deliberate manipulation? (5) Is my confidence language calibrated to the actual evidence quality? (6) What would change my judgment — and is that indicator being monitored? (7) What has been left out because it was inconvenient or hard to collect? Document an honest answer to each.

## Step 3 — Flag weaknesses and draft revisions (reason, write)
For each challenge question that revealed a weakness, write a specific annotation: what the weakness is, how it affects the key judgment, and what revision or caveat is needed. Produce the critique_report with all annotations, alternative framings, and a prioritized revision list.

## Evidence requirements
- For Structured Self-Critique, tie each critique report claim to concrete evidence from the specific analysis draft, key judgments, and supporting evidence item, source excerpt, observation, or command result that supports it.
- For Structured Self-Critique, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the critique report.
- Before recommending any Structured Self-Critique action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Structured Self-Critique: the critique report is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; ingest and inventory and apply the challenge checklist checks agree, and no unresolved contradiction would change the result.
- Medium for Structured Self-Critique: the critique report is plausible, but one important analysis draft source, comparison case, or alternative explanation remains incomplete.
- Low for Structured Self-Critique: the critique report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Structured Self-Critique cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Structured Self-Critique, use only authorized analysis draft, key judgments, and supporting evidence, public or source-approved records, and caller-provided context needed for the defensive task.
- For Structured Self-Critique, minimize person-level detail in the critique report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Structured Self-Critique, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Structured Self-Critique: treating analysis draft as complete when ingest and inventory and apply the challenge checklist checks or contradictory evidence are missing.
- Structured Self-Critique: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Self-Critique: reporting the critique report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Structured Self-Critique outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the critique report from Structured Self-Critique into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Structured Self-Critique to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with analysis draft, key judgments, and supporting evidence' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat the checklist as a formality — each question must receive a genuine answer, not a reflexive 'no issues found'
- do not dismiss alternative explanations without stating the specific evidence that rules them out
- do not allow confidence language to remain uncalibrated — vague hedges ('might', 'could') must be resolved to an explicit likelihood tier
- do not omit inconvenient gaps in evidence — the report must name what is unknown, not only what is known

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
