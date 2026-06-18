# Workflow — Red Hat Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Build the adversary frame (read, reason)
Read all available adversary profile information. Construct the adversary's internal worldview: their primary goals and how they prioritize among them; their perceived constraints (resource, legal, normative, reputational); their risk tolerance inferred from past behavior; the information environment they operate in; and their organizational decision culture (centralized vs. distributed, risk-seeking vs. risk-averse). Explicitly set aside your own evaluative frame at each step.

## Step 2 — Develop adversary courses of action (reason)
From inside the adversary's frame, identify the options available to them in the current situation. For each plausible option, trace the internal decision logic: what goal it serves, what risk it carries from their perspective, and what they would need to believe for it to be their preferred choice. Identify the Most Probable COA and the Most Dangerous COA separately. Note where these diverge — divergence is analytically important.

## Step 3 — Flag mirror imaging and emit findings (reason, write)
Review the current analytic line for mirror-imaging assumptions: places where adversary behavior is being explained by reference to how we would behave. For each flag, state the assumption, the evidence for and against it, and an alternative adversary-logic explanation. Emit the adversary frame, COAs with internal reasoning, and the mirror-imaging flag list. Include indicators that would confirm or disconfirm each COA.

## Anti-criteria (must NOT happen)
- do not evaluate adversary options by our own values or risk calculus — an action that seems irrational from our frame may be optimal from theirs
- do not conflate the adversary's capability with their intent, or their rhetoric with their actual decision goals
- do not allow the exercise to become advocacy for the adversary's position — the purpose is understanding, not sympathy or operational planning
- do not present only the most probable COA without separately surfacing the most dangerous one

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
