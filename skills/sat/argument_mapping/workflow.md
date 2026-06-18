# Workflow — Argument Mapping

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Identify the top-level conclusion (read)
Read the source document and identify the single main claim the argument is trying to establish. In complex documents with multiple arguments, select the focal claim and bracket the rest for separate mapping. Write the top-level claim in one sentence in declarative form.

## Step 2 — Extract claims, premises, and evidence (read, reason)
Working backward from the conclusion, identify each sub-claim that directly supports it. For each sub-claim, identify its supporting premises and any evidence citations. Distinguish claim types: empirical claims (verifiable facts), interpretive claims (pattern/meaning judgments), and value claims (normative assertions). Flag implicit premises embedded in inferential connectors ('since X is true, Y follows' — what unstated premise links X to Y?).

## Step 3 — Map inferential structure and gaps (reason)
Draw the directed support graph: arrows from evidence/premises to the claims they support; rebuttal arrows where counter-evidence is acknowledged; qualification arrows where scope is limited. Identify gaps: claims with no supporting nodes (undefended assertions), circular structures (A supports B, B supports A), and equivocations (a key term used with different meanings in different nodes).

## Step 4 — Assess load-bearing assumptions (reason, write)
For each implicit assumption surfaced in step 3, assess: (a) Is it likely true? (b) Is it testable? (c) If false, how much of the conclusion does it undermine? Rank assumptions by their load-bearing weight × confidence gap. These are the argument's cognitive-security vulnerabilities: the nodes an adversary would target to collapse the narrative or that an analyst should verify before endorsing the conclusion.

## Step 5 — Produce map and vulnerability report (write)
Write the argument map in structured indented notation or a Markdown-table-based representation (since visual graph tools are not always available). Produce the load-bearing assumption table with columns: Assumption, Basis, Falsifiability, Impact-if-False, Priority. Write the logical gap report summarizing the most significant inferential weaknesses. Include a one-paragraph synthesis noting the strongest and most vulnerable parts of the argument.

## Anti-criteria (must NOT happen)
- Do not conflate mapping (describing the structure) with refutation (claiming the argument is wrong) — the map must accurately represent the argument even if the analyst disagrees with it
- Do not omit implicit premises because they are unstated; the most dangerous logical gaps are the ones the original author did not notice
- Do not allow the argument map to be used to construct a straw-man version of the opponent's position — accuracy to the source text is non-negotiable
- Do not produce a map so complex that no human can navigate it; prune to the most significant nodes and aggregate minor supporting evidence into summary nodes

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
