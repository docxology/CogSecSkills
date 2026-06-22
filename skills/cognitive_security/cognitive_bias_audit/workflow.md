# Workflow — Cognitive Bias Audit

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Profile the analysis (read)
Read the full analysis text. Extract: the main conclusion(s), the evidence cited, the assumptions stated or implied, and the reasoning chain connecting evidence to conclusion. Note the decision type (predictive, diagnostic, evaluative), domain, stakes, and any described time or political pressures.

## Step 2 — Map against bias taxonomy (reason)
Work through a structured taxonomy of biases in order: (1) heuristic biases — availability, representativeness, anchoring, base-rate neglect; (2) confirmation family — confirmation bias, selective evidence weighting, disconfirmation resistance; (3) social/organizational biases — groupthink, authority deference, mirror-imaging; (4) motivated reasoning — politicization, wishful thinking, projection; (5) framing and ordering effects. For each category, identify whether the analysis exhibits the pattern, cite the passage(s), and estimate how much the bias could shift the conclusion.

## Step 3 — Rank by distortion magnitude (reason)
Score each identified bias on distortion magnitude: High = the conclusion would likely change if the bias were removed; Medium = the conclusion might shift in confidence or nuance; Low = the bias affects presentation but not substance. Consider domain stakes in setting thresholds. Prioritize the top 3-5 biases for detailed treatment.

## Step 4 — Draft the bias audit report (write)
For each bias in priority order: (a) name and define the bias precisely; (b) quote the text where it manifests; (c) explain the distortion mechanism — how this bias leads to a specific error in this analysis; (d) state the debiasing action — a specific technique such as 'apply Analysis of Competing Hypotheses to the evidence set' or 'solicit a red-team challenge to assumption X'. Write the priority table. Close with an overall analytic confidence adjustment given the identified bias load.

## Step 5 — Emit final product (write)
Output the structured bias_audit_report as markdown and the priority_bias_summary as a table. Flag if the aggregate bias load is severe enough to recommend re-analysis before the product is used in decisions.

## Evidence requirements
- For Cognitive Bias Audit, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Cognitive Bias Audit, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Cognitive Bias Audit recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Cognitive Bias Audit: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Cognitive Bias Audit: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Cognitive Bias Audit: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Cognitive Bias Audit cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Cognitive Bias Audit should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Cognitive Bias Audit, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Cognitive Bias Audit, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Cognitive Bias Audit, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Cognitive Bias Audit failure: mistaking persuasive resonance for verified harm or intent.
- Cognitive Bias Audit failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Cognitive Bias Audit failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Cognitive Bias Audit to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Cognitive Bias Audit into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Cognitive Bias Audit to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not produce a generic list of all known biases without grounding each one in quoted text from the analysis
- do not rate every bias as 'High' — calibrated severity distinctions are the core value of the audit
- do not conflate cognitive bias with deliberate deception, politicization, or poor sourcing — these are distinct failure modes requiring different remediation
- do not offer debiasing advice that cannot actually be implemented by the analyst (e.g. 'run an RCT' for a time-sensitive assessment)
- do not treat absence of bias evidence as confirmation of unbiased analysis — note the limits of text-based auditing and what cannot be seen without process observation

## AGEINT upstream
`docs/ageint/cognitive-security.md`
