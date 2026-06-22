---
name: counterintelligence.denial_and_deception_detection
description: Detect adversary denial and deception by testing for what a deceiver would hide or plant.
---

# Denial & Deception Detection

Denial and Deception (D&D) detection applies counterintelligence logic to assess whether an adversary is actively withholding information (denial) or fabricating/staging evidence to mislead analysis (deception). The technique reverses the analyst's natural posture — instead of asking 'what does the evidence tell us?', it asks 'what would a rational deceiver need to hide or plant for us to reach this conclusion?' Introduced systematically by Godson and Wirtz and codified by Heuer, it is the foundational check against being manipulated through sources the analyst believes are reliable.

## When to use

- a high-stakes assessment rests on evidence that an adversary had both motive and opportunity to manipulate
- evidence is unusually consistent or convenient — too clean a picture can be a signature of staging
- a prior analytic conclusion is later suspected of having been built on planted information
- intelligence arrives through channels the adversary is known to have penetrated or controlled

## What it produces

- an explicit deception scenario — what the adversary would have had to do to produce this evidence — with a plausibility rating
- a set of observable deception indicators and their current confirmed/unconfirmed/absent status
- targeted collection priorities that would most effectively discriminate a genuine picture from a managed one

## Defensive boundary

Use Denial & Deception Detection only for counterintelligence and analytic-process defense: recognize, assess, document, or defend analytic teams, collection processes, and institutional trust boundaries. Do not use this skill to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.

## Misuse redirect

If a request asks Denial & Deception Detection to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft, refuse that path and redirect to the safe defensive form: review supplied interactions or processes for deception, elicitation, or insider-risk indicators.

## Evidence discipline

- For Denial & Deception Detection, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Denial & Deception Detection, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Denial & Deception Detection recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Denial & Deception Detection: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Denial & Deception Detection: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Denial & Deception Detection: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Denial & Deception Detection cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Denial & Deception Detection should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Denial & Deception Detection, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Denial & Deception Detection, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Denial & Deception Detection, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Denial & Deception Detection failure: turning defensive tradecraft recognition into operational evasion advice.
- Denial & Deception Detection failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Denial & Deception Detection failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Denial & Deception Detection to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Denial & Deception Detection into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Denial & Deception Detection to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- ask 'what would I see if this were deception?' before asking 'is this deception?' — absence of deception indicators is not evidence of their absence, only evidence you haven't looked
- deception requires capability, motive, and opportunity; assess all three before rating plausibility
- the most dangerous deception scenarios are those where the deceived party has already acted and is invested in the conclusion — look especially hard when the evidence confirms a strongly held prior
