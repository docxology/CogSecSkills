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

## Evidence requirements
- For Claim-Evidence Audit, bind each claim's verdict to concrete evidence by recording exactly what the document offers in support and classifying its type, and treat confidence language such as 'clearly' or 'obviously' as a claim about evidence strength to be evaluated, never as the evidence itself.
- For Claim-Evidence Audit, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the claim evidence table.
- Before recommending any Claim-Evidence Audit action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Claim-Evidence Audit: each substantive claim's sufficiency verdict is anchored to the specific evidence the document actually offers for it, the evidence-type classification and overclaim or unsupported ratings remain stable when any single claim-evidence pair is re-examined, and no unresolved contradiction would change the overall judgment of whether the conclusions can be trusted as stated.
- Medium for Claim-Evidence Audit: the claim evidence table is plausible, but one important document source, comparison case, or alternative explanation remains incomplete.
- Low for Claim-Evidence Audit: the claim evidence table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Claim-Evidence Audit cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Claim-Evidence Audit, use only authorized document, and claim taxonomy, public or source-approved records, and caller-provided context needed for the defensive task.
- For Claim-Evidence Audit, minimize person-level detail in the claim evidence table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Claim-Evidence Audit, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Claim-Evidence Audit: declaring the document sound when substantive claims were never separated from the evidence offered for them, so cherry-picked data, rhetorical confidence words, and implicit overclaims in how conclusions are framed pass unexamined and an unsupported assertion is mistaken for a well-supported finding.
- Claim-Evidence Audit: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Claim-Evidence Audit: reporting the claim evidence table without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Claim-Evidence Audit outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the claim evidence table from Claim-Evidence Audit into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Claim-Evidence Audit to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with document, and claim taxonomy' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate a claim being plausible or likely true with it being well-supported by the evidence offered in this document
- Do not let rhetorical confidence substitute for evidentiary strength — words like 'clearly' and 'obviously' must be treated as claims about evidence strength, not as evidence
- Do not restrict the audit to explicit claim-evidence pairs; the most dangerous overclaims are often implicit in how conclusions are framed relative to the data actually presented
- Do not apply a uniform evidentiary standard across claim types — causal claims require stronger evidence than descriptive claims; policy recommendations require stronger evidence than diagnostic claims

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
