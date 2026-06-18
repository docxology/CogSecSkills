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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- ask 'what would I see if this were deception?' before asking 'is this deception?' — absence of deception indicators is not evidence of their absence, only evidence you haven't looked
- deception requires capability, motive, and opportunity; assess all three before rating plausibility
- the most dangerous deception scenarios are those where the deceived party has already acted and is invested in the conclusion — look especially hard when the evidence confirms a strongly held prior
