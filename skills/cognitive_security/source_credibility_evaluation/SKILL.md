---
name: cognitive_security.source_credibility_evaluation
description: >-
  Grade an information source on reliability (A–F) and a specific claim on
  credibility (1–6) using the NATO/Admiralty Code, treating the two axes as
  independent and explaining each grade so it can bound downstream use of the
  information.
---

# Source Credibility Evaluation

Evaluate a source and a claim the way an intelligence analyst does: separate
*who is telling you* from *what they are telling you*, grade each on its own
scale, and explain the grade so a reader knows exactly how far to trust it.

## When to use

- Someone asks "how reliable is this source?" or "can I trust this report?"
- A claim needs a defensible, auditable credibility rating before it is acted on.
- You need to distinguish a trustworthy outlet carrying an uncorroborated rumor
  from a shaky outlet carrying a confirmed fact — the Admiralty Code is built
  for exactly this.

## What it produces

- A **source-reliability letter (A–F)** with justification grounded in
  proximity, track record, motive/bias, and independence.
- An **information-credibility number (1–6)** with justification grounded in
  independent confirmation, plausibility, and consistency with known facts.
- A combined grade (e.g. `B2`) and an explicit statement of how that grade
  should **bound downstream use** of the information.

## Procedure

The full step-by-step procedure lives in [workflow.md](workflow.md). In brief:
identify the source and its proximity to the information, assess track record /
motive / independence, assign the A–F letter, assess the specific claim against
independent corroboration, assign the 1–6 number, and state the usage bound.

### Reference scales

| Reliability (source) | Meaning | Credibility (information) | Meaning |
| --- | --- | --- | --- |
| A | Completely reliable | 1 | Confirmed by other independent sources |
| B | Usually reliable | 2 | Probably true |
| C | Fairly reliable | 3 | Possibly true |
| D | Not usually reliable | 4 | Doubtful |
| E | Unreliable | 5 | Improbable |
| F | Reliability cannot be judged | 6 | Truth cannot be judged |

## Key discipline

**Reliability and credibility are independent axes.** A grade is a *pair*, never
a single number, because the two questions are genuinely separate:

- The **letter** judges the *source* — its history, position, and incentives —
  and travels with that source across many claims.
- The **number** judges *this specific claim* — whether independent evidence
  confirms it — and is reassessed for every claim, even from the same source.

A usually-reliable source (B) can carry an uncorroborated claim (B3); an unknown
source (F) can carry a fact independently confirmed elsewhere (F1). Never let
prestige substitute for corroboration, and never assign **A1** without genuine
independent confirmation — A1 requires both a completely reliable source *and*
a claim verified by separate, independent sources.
