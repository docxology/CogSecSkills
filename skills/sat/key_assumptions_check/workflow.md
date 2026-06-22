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
- For Key Assumptions Check, tie each assumption, its confidence class, and its collapse analysis to concrete evidence from the judgment and analytic line, stating the actual basis for belief and the conditions that would falsify it; an assumption rated solid without supporting evidence is unsupported and must be reclassified rather than waved through.
- For Key Assumptions Check, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the assumptions table.
- Before recommending any Key Assumptions Check action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Key Assumptions Check: the unstated as well as stated assumptions have been recovered, each is classified by genuine evidentiary support rather than familiarity, the load-bearing-and-uncertain ones carry an explicit collapse analysis, and no unresolved contradiction would change which assumptions are key or how the revised judgment depends on them.
- Medium for Key Assumptions Check: the assumptions table is plausible, but one important judgment source, comparison case, or alternative explanation remains incomplete.
- Low for Key Assumptions Check: the assumptions table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Key Assumptions Check cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Key Assumptions Check, use only authorized judgment, analytic line, and stated assumptions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Key Assumptions Check, minimize person-level detail in the assumptions table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Key Assumptions Check, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Key Assumptions Check: treating the analysis as done when the silent unstated assumptions the argument requires were never surfaced, or when a comfortable assumption was marked solid without evidence, so the rewritten judgment still hides the dependence that could make the conclusion collapse.
- Key Assumptions Check: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Key Assumptions Check: reporting the assumptions table without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Key Assumptions Check outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the assumptions table from Key Assumptions Check into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Key Assumptions Check to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with judgment, analytic line, and stated assumptions' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Letting an unstated assumption pass unexamined because no one named it.
- Marking a comfortable or convenient assumption "solid" without evidence.
- Flagging every assumption as "key" — the value is in discriminating the few
- Reporting the original judgment unchanged, hiding its dependence on assumptions.

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
