# Workflow — Structured Reporting & BLUF

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Assemble the inputs (read)
Read the analytic judgment (with its stated confidence level), all supporting evidence and sources, the key assumptions, and any prior confidence assessment. Note the audience and the decision the report will inform.

## Step 2 — Draft the BLUF and argument structure (reason)
Write the BLUF first: one to three sentences stating the key judgment, the confidence level in standardized language (High/Moderate/Low), and the single most important caveat. Then outline the body in descending order of importance: which evidence is strongest, which assumptions are load-bearing, what countervailing evidence exists.

## Step 3 — Check traceability and completeness (reason)
Review each claim in the draft body. Every factual assertion must link to a cited source or be flagged as an explicit assumption. Confirm that the caveats section includes the two or three conditions that would most change the judgment. Verify the BLUF accurately reflects the body — inconsistencies between headline and body are a common analytic failure mode.

## Step 4 — Produce the final structured report (write)
Write the final report with clearly labeled sections: BLUF, Key Evidence (graded if available), Key Assumptions, Argument, Caveats and Countervailing Evidence, and Implications for the decision audience. Use standardized confidence language throughout. Include a one-line 'What Would Change This Assessment' note at the end.

## Evidence requirements
- For Structured Reporting & BLUF, tie each structured report claim to concrete evidence from the specific analytic judgment, evidence and sources, and assumptions item, source excerpt, observation, or command result that supports it.
- For Structured Reporting & BLUF, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the structured report.
- Before recommending any Structured Reporting & BLUF action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Structured Reporting & BLUF: the structured report is supported by multiple independent study designs, source quality, reproducibility artifacts, and uncertainty records; assemble the inputs and draft the bluf and argument structure checks agree, and no unresolved contradiction would change the result.
- Medium for Structured Reporting & BLUF: the structured report is plausible, but one important analytic judgment source, comparison case, or alternative explanation remains incomplete.
- Low for Structured Reporting & BLUF: the structured report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Structured Reporting & BLUF cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating research_methods evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Structured Reporting & BLUF, use only authorized analytic judgment, evidence and sources, and assumptions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Structured Reporting & BLUF, minimize person-level detail in the structured report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Structured Reporting & BLUF, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Structured Reporting & BLUF: treating analytic judgment as complete when assemble the inputs and draft the bluf and argument structure checks or contradictory evidence are missing.
- Structured Reporting & BLUF: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Structured Reporting & BLUF: reporting the structured report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Structured Reporting & BLUF outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the structured report from Structured Reporting & BLUF into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Structured Reporting & BLUF to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with analytic judgment, evidence and sources, and assumptions' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not bury the main judgment at the end of the report in a narrative-reveal structure — the BLUF must appear first
- do not state confidence verbally (e.g., 'we believe') without a standardized confidence tier label (High/Moderate/Low)
- do not omit countervailing evidence to protect the main judgment — selective omission is an analytic integrity violation
- do not make claims in the body that are not traceable to a cited source or explicitly labeled assumption

## AGEINT upstream
`docs/ageint/research-methods.md`
