# Workflow — Analytic Process Hardening

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Map the workflow (read)
Document each stage of the analytic process: collection sources, how information enters the workflow, who processes it, what review gates exist, who approves the final product, and who consumes it. Include handoff points where information passes between analysts or systems.

## Step 2 — Identify manipulation surfaces (reason)
For each node, ask: (1) Can a motivated adversary introduce fabricated or misleading content here? (2) Does the workflow create anchoring — is later analysis downstream of early judgments? (3) Are there single-source choke points where one planted item cannot be cross-checked? (4) Are there cognitive pressure points — deadline, senior attention, prior investment — that suppress challenge? Map findings into a vulnerability table.

## Step 3 — Score and prioritize risks (reason)
Rate each identified surface on adversary access (how hard is it to inject?), analyst detection probability (how likely is detection?), and consequence of successful manipulation (what decision would be corrupted?). Rank by the product of these three factors. Focus hardening on the top tercile.

## Step 4 — Design targeted controls (reason, write)
For each high-priority surface, prescribe one or more controls from the hardening toolkit: source diversification (cross-check via independent channel), structured challenge (red team or devil's advocate step), blind review (reviewer sees no prior conclusion), provenance tagging (track each claim to its source so contamination can be traced), or collection gap disclosure (require explicit statement of what is unknown). Assign an owner and a verification criterion for each control.

## Step 5 — Document residual risk (write)
State explicitly what manipulation surfaces remain after controls, why they cannot be fully mitigated, and what decision-maker behavior (e.g., seeking corroboration before acting) compensates. Provide a summary hardening scorecard comparing pre- and post-control risk for each node.

## Evidence requirements
- For Analytic Process Hardening, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Analytic Process Hardening, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Analytic Process Hardening recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Analytic Process Hardening: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Analytic Process Hardening: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Analytic Process Hardening: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Analytic Process Hardening cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Analytic Process Hardening should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Analytic Process Hardening, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Analytic Process Hardening, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Analytic Process Hardening, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Analytic Process Hardening failure: turning defensive tradecraft recognition into operational evasion advice.
- Analytic Process Hardening failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Analytic Process Hardening failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Analytic Process Hardening to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Analytic Process Hardening into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Analytic Process Hardening to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat hardening as a one-time event — workflows change, adversaries adapt; schedule periodic re-audits
- do not harden by adding bureaucratic sign-off alone; signature layers without independent analysis add drag without detection capability
- do not classify a source as trustworthy and exempt it from hardening — trusted sources are prime targets for adversary access operations
- do not suppress findings of high residual risk to avoid organizational discomfort; the point of the output is honest risk communication

## AGEINT upstream
`docs/ageint/counterintelligence.md`
