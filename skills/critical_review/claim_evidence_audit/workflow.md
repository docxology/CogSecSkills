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
- For Claim-Evidence Audit, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Claim-Evidence Audit, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Claim-Evidence Audit recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Claim-Evidence Audit: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Claim-Evidence Audit: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Claim-Evidence Audit: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Claim-Evidence Audit cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Claim-Evidence Audit should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Claim-Evidence Audit, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Claim-Evidence Audit, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Claim-Evidence Audit, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Claim-Evidence Audit failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Claim-Evidence Audit failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Claim-Evidence Audit failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Claim-Evidence Audit to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Claim-Evidence Audit into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Claim-Evidence Audit to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate a claim being plausible or likely true with it being well-supported by the evidence offered in this document
- Do not let rhetorical confidence substitute for evidentiary strength — words like 'clearly' and 'obviously' must be treated as claims about evidence strength, not as evidence
- Do not restrict the audit to explicit claim-evidence pairs; the most dangerous overclaims are often implicit in how conclusions are framed relative to the data actually presented
- Do not apply a uniform evidentiary standard across claim types — causal claims require stronger evidence than descriptive claims; policy recommendations require stronger evidence than diagnostic claims

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
