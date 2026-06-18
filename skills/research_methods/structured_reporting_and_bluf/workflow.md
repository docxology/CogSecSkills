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

## Anti-criteria (must NOT happen)
- do not bury the main judgment at the end of the report in a narrative-reveal structure — the BLUF must appear first
- do not state confidence verbally (e.g., 'we believe') without a standardized confidence tier label (High/Moderate/Low)
- do not omit countervailing evidence to protect the main judgment — selective omission is an analytic integrity violation
- do not make claims in the body that are not traceable to a cited source or explicitly labeled assumption

## AGEINT upstream
`docs/ageint/research-methods.md`
