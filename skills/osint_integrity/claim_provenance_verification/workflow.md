# Workflow — Claim Provenance Verification

Trace a public claim to its primary source, corroborate it independently, and
issue a graded verdict. Work the steps in order. Each step is tagged with the
neutral tool verb(s) it uses; consult the harness adapter for your runtime to
map each verb to a concrete tool.

1. **State the claim atomically.** `[read] [reason]` Strip editorializing,
   loaded adjectives, and framing. Reduce the claim to a single precise,
   falsifiable proposition with explicit scope (who, what, when, where, how
   much). Record both the claim as encountered and the atomic restatement — the
   gap between them is itself evidence.

2. **Anchor the point of encounter.** `[read]` Note exactly where the requester
   met the claim (URL, outlet, date) and what that source cites, if anything.
   This is the bottom of the chain, not the top.

3. **Trace citations upstream to the origin.** `[search] [web]` Follow each
   "according to / as reported by / per a study" reference one hop at a time
   toward earlier instances. Continue until you reach a **primary source** (the
   original document, dataset, statement, or eyewitness) or a **dead end**
   (a source that cites nothing further, or the chain loops). Record every hop.

4. **Detect circular reporting.** `[reason]` Collapse the traced chain to its
   distinct origins. If many outlets ultimately cite one another and converge on
   a single unverified point, that is circular reporting — flag it explicitly.
   Repetition count is not evidence; one origin repeated N times is one source.

5. **Assess the primary source directly.** `[web] [read] [reason]` Open the
   origin and check: does it actually state the claim? Is the scope the same, or
   has the claim widened in retelling? Were caveats, error bars, sample limits,
   or conditional language dropped on the way down the chain? Note every
   divergence.

6. **Seek independent corroboration.** `[search] [web] [reason]` Look for
   sources that do **not** derive from the same origin — a separate primary
   document, a separate measurement, a separate eyewitness. Two outlets sharing
   one wire story or one press release are not independent. Count only distinct,
   non-derivative origins.

7. **Record the provenance chain.** `[write]` Write the ordered chain from
   point-of-encounter back to origin with links and timestamps, plus a
   chain-of-custody note describing how each link cites the next and where the
   chain branches or loops.

8. **Issue the verdict.** `[reason] [write]` Grade the claim on the scale below,
   state a confidence level, and name the **single weakest link** — the one hop
   or gap most responsible for any remaining uncertainty.

## Verdict scale

- **verified** — claim traces to a sound primary source at matching scope, with
  at least one genuinely independent corroboration.
- **partially verified** — primary source supports a narrower or qualified
  version of the claim; scope or caveat drift is present and flagged.
- **unverified** — no reachable primary source and/or no independent
  corroboration; the claim rests on repetition or circular reporting.
- **false** — the primary source contradicts the claim, or the claim
  misrepresents what the source says.
- **unverifiable** — the chain dead-ends at an inaccessible, anonymous, or
  destroyed origin that cannot in principle be checked.

## Anti-criteria (must NOT happen)

- **Do not treat volume of repetition as corroboration.** N outlets citing one
  origin is one source, never N.
- **Do not stop at a secondary source that merely cites another secondary.**
  Keep tracing until a primary source or a genuine dead end.
- **Do not collapse scope silently.** If the claim drifted from the primary
  source's scope, flag it; never report a widened claim as verified.
- **Do not count derivative sources as independent.** Shared wire copy, shared
  press release, or shared origin is one source.
- **Do not issue a verdict without naming the single weakest link.**

## AGEINT upstream

Upstream domain doctrine for this skill lives under
`docs/ageint/osint-integrity/` (topic: `osint-integrity`) — provenance, source,
date, and location verification practice in the First Draft / Bellingcat
tradition. Defer to that doctrine where this workflow and the AGEINT topic
disagree, and feed verification findings back upstream.
