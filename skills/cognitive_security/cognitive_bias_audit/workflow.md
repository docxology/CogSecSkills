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

## Anti-criteria (must NOT happen)
- do not produce a generic list of all known biases without grounding each one in quoted text from the analysis
- do not rate every bias as 'High' — calibrated severity distinctions are the core value of the audit
- do not conflate cognitive bias with deliberate deception, politicization, or poor sourcing — these are distinct failure modes requiring different remediation
- do not offer debiasing advice that cannot actually be implemented by the analyst (e.g. 'run an RCT' for a time-sensitive assessment)
- do not treat absence of bias evidence as confirmation of unbiased analysis — note the limits of text-based auditing and what cannot be seen without process observation

## AGEINT upstream
`docs/ageint/cognitive-security.md`
