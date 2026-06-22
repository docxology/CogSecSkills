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

## Evidence requirements
- For Argument Mapping, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Argument Mapping, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Argument Mapping recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Argument Mapping: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Argument Mapping: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Argument Mapping: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Argument Mapping cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Argument Mapping should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Argument Mapping, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Argument Mapping, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Argument Mapping, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Argument Mapping failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Argument Mapping failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Argument Mapping failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Argument Mapping to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Argument Mapping into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Argument Mapping to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate mapping (describing the structure) with refutation (claiming the argument is wrong) — the map must accurately represent the argument even if the analyst disagrees with it
- Do not omit implicit premises because they are unstated; the most dangerous logical gaps are the ones the original author did not notice
- Do not allow the argument map to be used to construct a straw-man version of the opponent's position — accuracy to the source text is non-negotiable
- Do not produce a map so complex that no human can navigate it; prune to the most significant nodes and aggregate minor supporting evidence into summary nodes

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
