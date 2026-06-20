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
- For Analytic Process Hardening, tie each vulnerability map, hardening plan, and residual risk statement claim to concrete evidence from the specific workflow description, adversary context, and prior incidents item, source excerpt, observation, or command result that supports it.
- For Analytic Process Hardening, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the vulnerability map.
- Before recommending any Analytic Process Hardening action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Analytic Process Hardening: the vulnerability map is supported by multiple independent interaction records, process artifacts, deception indicators, and alternative explanations; map the workflow and identify manipulation surfaces checks agree, and no unresolved contradiction would change the result.
- Medium for Analytic Process Hardening: the vulnerability map is plausible, but one important workflow description source, comparison case, or alternative explanation remains incomplete.
- Low for Analytic Process Hardening: the vulnerability map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Analytic Process Hardening cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Analytic Process Hardening, use only authorized workflow description, adversary context, and prior incidents, public or source-approved records, and caller-provided context needed for the defensive task.
- For Analytic Process Hardening, minimize person-level detail in the vulnerability map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Analytic Process Hardening, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Analytic Process Hardening: treating workflow description as complete when map the workflow and identify manipulation surfaces checks or contradictory evidence are missing.
- Analytic Process Hardening: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Analytic Process Hardening: reporting the vulnerability map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Analytic Process Hardening outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the vulnerability map from Analytic Process Hardening into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Analytic Process Hardening to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with workflow description, adversary context, and prior incidents' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat hardening as a one-time event — workflows change, adversaries adapt; schedule periodic re-audits
- do not harden by adding bureaucratic sign-off alone; signature layers without independent analysis add drag without detection capability
- do not classify a source as trustworthy and exempt it from hardening — trusted sources are prime targets for adversary access operations
- do not suppress findings of high residual risk to avoid organizational discomfort; the point of the output is honest risk communication

## AGEINT upstream
`docs/ageint/counterintelligence.md`
