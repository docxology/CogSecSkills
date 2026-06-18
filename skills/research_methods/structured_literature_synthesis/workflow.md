# Workflow — Structured Literature Synthesis

A deterministic procedure for turning a body of sources into a structured,
evidence-graded, gap-aware briefing. Each step names the neutral tool verb(s) it
relies on; map them to a concrete harness via the adapters in `harness/`.

1. **Define the synthesis question and scope** [reason, write].
   State the single question the synthesis must answer. Write explicit
   inclusion/exclusion criteria: source types, recency, language, relevance, and
   quality thresholds. Everything downstream is judged against this scope.

2. **Gather and deduplicate sources** [search, web, read].
   Collect candidate sources (retrieving from the web only where permitted),
   then deduplicate — same study reported twice, mirror copies, reprints — so no
   single finding is double-counted. Record what was excluded and why.

3. **Extract claims and findings per source** [read, reason].
   From each retained source, extract its concrete claims/findings. For each
   extracted claim record: the source citation, a verbatim or tight paraphrase,
   and a per-source **quality grade** (e.g., method strength, sample, peer
   review, independence). Build the evidence table here.

4. **Cluster findings by theme** [reason].
   Group the extracted claims into themes that bear on the synthesis question.
   A claim may inform more than one theme; keep its citation attached wherever
   it lands.

5. **Identify agreements, conflicts, and gaps** [reason].
   Within each theme, mark where sources agree, where they conflict, and what
   the corpus does **not** answer. Gaps are first-class output: name the
   questions no source addresses.

6. **Grade strength of evidence per theme** [reason].
   Apply the rubric below to each theme as a whole, weighing source count,
   source quality, independence, and consistency.

7. **Write the BLUF synthesis** [write].
   Bottom line up front. Then: themes with their graded evidence, conflicts
   surfaced honestly, gaps with what would resolve them, and full citations.
   Verify every synthesized statement traces back to the evidence table.

## Evidence-strength rubric

Grade each theme, not just each source.

- **Strong** — multiple independent, high-quality sources converge; no
  substantive unresolved conflict.
- **Moderate** — several sources agree but with limited independence, mixed
  quality, or minor unresolved conflict.
- **Weak** — few sources, low-quality sources, or notable conflict; the claim is
  suggestive but not dependable.
- **Insufficient** — too little evidence to grade, or the corpus does not
  address the question (record as a gap).

## Anti-criteria (must NOT happen)

- Do **not** present a single source's claim as settled consensus.
- Do **not** hide or smooth over conflicting findings.
- Do **not** synthesize beyond what the sources support.
- Do **not** drop citations — no uncited statement in the briefing.
- Do **not** double-count duplicate sources as independent agreement.

## AGEINT upstream

Upstream guidance and grading conventions for this method live under
`docs/ageint/` in the **research-methods** topic; this skill is the executable
backbone those cognitive-security research-methods skills compose on.
