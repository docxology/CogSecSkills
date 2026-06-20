# Workflow — Red Hat Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Build the adversary frame (read, reason)
Read all available adversary profile information. Construct the adversary's internal worldview: their primary goals and how they prioritize among them; their perceived constraints (resource, legal, normative, reputational); their risk tolerance inferred from past behavior; the information environment they operate in; and their organizational decision culture (centralized vs. distributed, risk-seeking vs. risk-averse). Explicitly set aside your own evaluative frame at each step.

## Step 2 — Develop adversary courses of action (reason)
From inside the adversary's frame, identify the options available to them in the current situation. For each plausible option, trace the internal decision logic: what goal it serves, what risk it carries from their perspective, and what they would need to believe for it to be their preferred choice. Identify the Most Probable COA and the Most Dangerous COA separately. Note where these diverge — divergence is analytically important.

## Step 3 — Flag mirror imaging and emit findings (reason, write)
Review the current analytic line for mirror-imaging assumptions: places where adversary behavior is being explained by reference to how we would behave. For each flag, state the assumption, the evidence for and against it, and an alternative adversary-logic explanation. Emit the adversary frame, COAs with internal reasoning, and the mirror-imaging flag list. Include indicators that would confirm or disconfirm each COA.

## Evidence requirements
- For Red Hat Analysis, tie each adversary frame, courses of action, and mirror imaging flags claim to concrete evidence from the specific adversary profile, situation context, and analytic question item, source excerpt, observation, or command result that supports it.
- For Red Hat Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the adversary frame.
- Before recommending any Red Hat Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Red Hat Analysis: the adversary frame is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; build the adversary frame and develop adversary courses of action checks agree, and no unresolved contradiction would change the result.
- Medium for Red Hat Analysis: the adversary frame is plausible, but one important adversary profile source, comparison case, or alternative explanation remains incomplete.
- Low for Red Hat Analysis: the adversary frame rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Red Hat Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Red Hat Analysis, use only authorized adversary profile, situation context, and analytic question, public or source-approved records, and caller-provided context needed for the defensive task.
- For Red Hat Analysis, minimize person-level detail in the adversary frame; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Red Hat Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Red Hat Analysis: treating adversary profile as complete when build the adversary frame and develop adversary courses of action checks or contradictory evidence are missing.
- Red Hat Analysis: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Red Hat Analysis: reporting the adversary frame without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Red Hat Analysis outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the adversary frame from Red Hat Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Red Hat Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with adversary profile, situation context, and analytic question' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not evaluate adversary options by our own values or risk calculus — an action that seems irrational from our frame may be optimal from theirs
- do not conflate the adversary's capability with their intent, or their rhetoric with their actual decision goals
- do not allow the exercise to become advocacy for the adversary's position — the purpose is understanding, not sympathy or operational planning
- do not present only the most probable COA without separately surfacing the most dangerous one

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
