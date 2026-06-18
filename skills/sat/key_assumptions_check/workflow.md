# Workflow — Key Assumptions Check

Harness-neutral agentic procedure. Each step names the **tool verb** it uses
(see `skill.yaml` → `tools`). A harness adapter binds each verb to concrete
tools; the logic here is identical across harnesses.

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

## Anti-criteria (must NOT happen)
- Letting an unstated assumption pass unexamined because no one named it.
- Marking a comfortable or convenient assumption "solid" without evidence.
- Flagging every assumption as "key" — the value is in discriminating the few
  load-bearing-and-uncertain ones from the many that do not matter.
- Reporting the original judgment unchanged, hiding its dependence on assumptions.

## AGEINT upstream
`docs/ageint/` → structured-analytic-techniques (assumption-testing /
sensitivity family).
