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

- For Denial & Deception Detection, tie each dd assessment, deception indicators, and collection recommendations claim to concrete evidence from the specific evidence body, current assessment, and adversary profile item, source excerpt, observation, or command result that supports it.
- For Denial & Deception Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the dd assessment.
- Before recommending any Denial & Deception Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Denial & Deception Detection: the dd assessment is supported by multiple independent interaction records, process artifacts, deception indicators, and alternative explanations; characterize the evidence and the beneficiary and apply the deceiver's calculus checks agree, and no unresolved contradiction would change the result.
- Medium for Denial & Deception Detection: the dd assessment is plausible, but one important evidence body source, comparison case, or alternative explanation remains incomplete.
- Low for Denial & Deception Detection: the dd assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Denial & Deception Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Denial & Deception Detection, use only authorized evidence body, current assessment, and adversary profile, public or source-approved records, and caller-provided context needed for the defensive task.
- For Denial & Deception Detection, minimize person-level detail in the dd assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Denial & Deception Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Denial & Deception Detection: treating evidence body as complete when characterize the evidence and the beneficiary and apply the deceiver's calculus checks or contradictory evidence are missing.
- Denial & Deception Detection: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Denial & Deception Detection: reporting the dd assessment without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Denial & Deception Detection outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the dd assessment from Denial & Deception Detection into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Denial & Deception Detection to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with evidence body, current assessment, and adversary profile' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- ask 'what would I see if this were deception?' before asking 'is this deception?' — absence of deception indicators is not evidence of their absence, only evidence you haven't looked
- deception requires capability, motive, and opportunity; assess all three before rating plausibility
- the most dangerous deception scenarios are those where the deceived party has already acted and is invested in the conclusion — look especially hard when the evidence confirms a strongly held prior
