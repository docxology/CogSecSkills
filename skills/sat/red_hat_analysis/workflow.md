# Workflow — Red Hat Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Build the adversary frame (read, reason)
Read all available adversary profile information. Construct the adversary's internal worldview: their primary goals and how they prioritize among them; their perceived constraints (resource, legal, normative, reputational); their risk tolerance inferred from past behavior; the information environment they operate in; and their organizational decision culture (centralized vs. distributed, risk-seeking vs. risk-averse). Explicitly set aside your own evaluative frame at each step.

## Step 2 — Develop adversary courses of action (reason)
From inside the adversary's frame, identify the options available to them in the current situation. For each plausible option, trace the internal decision logic: what goal it serves, what risk it carries from their perspective, and what they would need to believe for it to be their preferred choice. Identify the Most Probable COA and the Most Dangerous COA separately. Note where these diverge — divergence is analytically important.

## Step 3 — Flag mirror imaging and emit findings (reason, write)
Review the current analytic line for mirror-imaging assumptions: places where adversary behavior is being explained by reference to how we would behave. For each flag, state the assumption, the evidence for and against it, and an alternative adversary-logic explanation. Emit the adversary frame, COAs with internal reasoning, and the mirror-imaging flag list. Include indicators that would confirm or disconfirm each COA.

## Evidence requirements
- For Red Hat Analysis, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Red Hat Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Red Hat Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Red Hat Analysis: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Red Hat Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Red Hat Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Red Hat Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Red Hat Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Red Hat Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Red Hat Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Red Hat Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Red Hat Analysis failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Red Hat Analysis failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Red Hat Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Red Hat Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Red Hat Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Red Hat Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not evaluate adversary options by our own values or risk calculus — an action that seems irrational from our frame may be optimal from theirs
- do not conflate the adversary's capability with their intent, or their rhetoric with their actual decision goals
- do not allow the exercise to become advocacy for the adversary's position — the purpose is understanding, not sympathy or operational planning
- do not present only the most probable COA without separately surfacing the most dangerous one

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
