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
- For Cognitive Bias Audit, bind each identified bias to concrete evidence — a quoted passage, a stated assumption, or a described organizational pressure — pair it with a debiasing action the analyst can actually implement, and note explicitly what text-based auditing cannot reveal without observing the analytic process itself.
- For Cognitive Bias Audit, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the bias audit report.
- Before recommending any Cognitive Bias Audit action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Cognitive Bias Audit: each flagged bias is anchored to a quoted passage from the analysis under review, its distortion magnitude is calibrated against domain stakes and logical path-dependence rather than asserted uniformly, the prioritized ranking is stable across the bias taxonomy, and no unresolved contradiction would change the recommended debiasing actions.
- Medium for Cognitive Bias Audit: the bias audit report is plausible, but one important analysis or decision source, comparison case, or alternative explanation remains incomplete.
- Low for Cognitive Bias Audit: the bias audit report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Cognitive Bias Audit cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Cognitive Bias Audit, use only authorized analysis or decision, domain context, and known pressures, public or source-approved records, and caller-provided context needed for the defensive task.
- For Cognitive Bias Audit, minimize person-level detail in the bias audit report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Cognitive Bias Audit, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Cognitive Bias Audit: asserting a bias without quoting the text that shows it, rating every bias as high severity, or conflating cognitive bias with deliberate deception, so the catalogue lectures abstractly instead of making specific, calibrated, actionable bias intrusions visible to the analyst.
- Cognitive Bias Audit: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Cognitive Bias Audit: reporting the bias audit report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Cognitive Bias Audit outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the bias audit report from Cognitive Bias Audit into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Cognitive Bias Audit to assess supplied material for manipulation indicators and recommend resilience measures with analysis or decision, domain context, and known pressures' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not produce a generic list of all known biases without grounding each one in quoted text from the analysis
- do not rate every bias as 'High' — calibrated severity distinctions are the core value of the audit
- do not conflate cognitive bias with deliberate deception, politicization, or poor sourcing — these are distinct failure modes requiring different remediation
- do not offer debiasing advice that cannot actually be implemented by the analyst (e.g. 'run an RCT' for a time-sensitive assessment)
- do not treat absence of bias evidence as confirmation of unbiased analysis — note the limits of text-based auditing and what cannot be seen without process observation

## AGEINT upstream
`docs/ageint/cognitive-security.md`
