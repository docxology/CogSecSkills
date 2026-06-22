# Workflow — Key Assumptions Check

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Recover the analytic line and list assumptions (read, reason)
Read the judgment and the reasoning that produced it. Write down **every**
assumption it depends on — both the ones the author stated and, critically, the
**unstated** ones the argument silently requires (about actors' intentions,
continuity of current conditions, reliability of sources, absence of deception,
that the past predicts the future, etc.). Aim for completeness over politeness;
an unstated assumption left off the list cannot be examined.

## Step 2 — Interrogate each assumption (reason)
For each assumption, answer three questions:
- **Why do we believe this?** State the actual basis, not a restatement.
- **What evidence supports it?** Cite it; "everyone knows" is not evidence.
- **Under what conditions would it NOT hold?** Name the concrete circumstances,
  events, or adversary choices that would falsify it. If you cannot imagine any,
  you have probably not understood the assumption.

## Step 3 — Classify confidence (reason)
Assign each assumption to one class:
- **Solid** — well-supported by evidence; unlikely to be wrong.
- **Caveated** — generally holds but with known exceptions or limits.
- **Unsupported** — believed but with little or no evidence behind it.
- **Key uncertainty** — could plausibly be wrong, and we do not know whether it is.

Do not award "solid" to an assumption merely because it is familiar or
comfortable — solidity must be earned with evidence.

## Step 4 — Flag the key assumptions (reason)
For each assumption, ask: **is it load-bearing?** — i.e., if it were false, would
the judgment change? Cross load-bearing against confidence. The assumptions that
are **both load-bearing AND uncertain** (unsupported or key uncertainty) are the
**key assumptions**. For each, run the collapse test: *if this assumption is
wrong, does the conclusion collapse, weaken, or survive?* State the answer
explicitly.

## Step 5 — Identify what would test them (reason)
For each key assumption, name the **new collection, research, or observation**
that would confirm or break it. This converts a vulnerability into a concrete,
testable requirement rather than leaving it as a worry.

## Step 6 — Rewrite the judgment and report (write)
Emit:
- the **assumptions table** (assumption · stated/unstated · rationale · contrary
  conditions · confidence class · load-bearing?),
- the **key assumptions** with their collapse analysis,
- the **collection** that would test each key assumption,
- a **revised judgment** that states the conclusion *together with* the
  assumptions it depends on (e.g. "X is likely, **provided** Y holds; if Y
  fails, the assessment reverses").

## Evidence requirements
- For Key Assumptions Check, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Key Assumptions Check, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Key Assumptions Check recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Key Assumptions Check: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Key Assumptions Check: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Key Assumptions Check: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Key Assumptions Check cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Key Assumptions Check should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Key Assumptions Check, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Key Assumptions Check, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Key Assumptions Check, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Key Assumptions Check failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Key Assumptions Check failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Key Assumptions Check failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Key Assumptions Check to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Key Assumptions Check into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Key Assumptions Check to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Letting an unstated assumption pass unexamined because no one named it.
- Marking a comfortable or convenient assumption "solid" without evidence.
- Flagging every assumption as "key" — the value is in discriminating the few
- Reporting the original judgment unchanged, hiding its dependence on assumptions.

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
