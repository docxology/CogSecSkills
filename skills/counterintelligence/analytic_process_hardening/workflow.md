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

## Anti-criteria (must NOT happen)
- do not treat hardening as a one-time event — workflows change, adversaries adapt; schedule periodic re-audits
- do not harden by adding bureaucratic sign-off alone; signature layers without independent analysis add drag without detection capability
- do not classify a source as trustworthy and exempt it from hardening — trusted sources are prime targets for adversary access operations
- do not suppress findings of high residual risk to avoid organizational discomfort; the point of the output is honest risk communication

## AGEINT upstream
`docs/ageint/counterintelligence.md`
