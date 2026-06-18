# Workflow — Claim-Evidence Audit

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract claims and linked evidence (read)
Read the document and extract every substantive claim — factual, causal, predictive, evaluative, or policy-recommendatory. For each claim, identify what evidence the author offers at that point: data, citation, expert authority, logical inference from prior claims, or none. Record each claim-evidence pair for audit.

## Step 2 — Classify evidence type and quality (reason)
For each piece of offered evidence, classify its type (primary empirical data, replicated study, single study, expert opinion, authority citation, anecdote, rhetorical assertion) and note any quality concerns: sample size, replication status, potential conflicts of interest, recency, or generalizability limits. This classification sets the evidentiary ceiling for what the claim can legitimately assert.

## Step 3 — Assess claim-evidence sufficiency and render verdict (reason)
For each claim-evidence pair, assess whether the offered evidence is sufficient in type and strength to support the claim as stated. Assign a verdict: well-supported (evidence is sufficient and of appropriate type), adequately hedged (evidence is limited but the claim is appropriately qualified), overclaim (the claim asserts more certainty, scope, or causality than the evidence can support), underclaim (evidence clearly supports a stronger statement but the author hedges excessively), or unsupported (no evidence is offered for a substantive claim). Assign a severity rating (high / medium / low) to each non-passing verdict.

## Step 4 — Detect patterns and formulate corrections (reason, write)
Look across all verdicts for systematic patterns: consistent use of confidence language unsupported by evidence, citation of single weak studies for strong claims, omission of contradicting evidence, or use of rhetorical amplifiers. For each flagged claim, write a specific correction: how the claim should be reframed, what qualification should be added, or what evidence would be needed to support it as stated.

## Step 5 — Produce audit table and summary (write)
Compile the complete claim-evidence audit table. Write the audit summary identifying the overall integrity level of the document's evidentiary support, the most critical overclaims and unsupported assertions, any detected cherry-picking patterns, and a recommendation on whether the document's conclusions can be used as stated or must be substantially re-hedged before acting on them.

## Anti-criteria (must NOT happen)
- Do not conflate a claim being plausible or likely true with it being well-supported by the evidence offered in this document
- Do not let rhetorical confidence substitute for evidentiary strength — words like 'clearly' and 'obviously' must be treated as claims about evidence strength, not as evidence
- Do not restrict the audit to explicit claim-evidence pairs; the most dangerous overclaims are often implicit in how conclusions are framed relative to the data actually presented
- Do not apply a uniform evidentiary standard across claim types — causal claims require stronger evidence than descriptive claims; policy recommendations require stronger evidence than diagnostic claims

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
