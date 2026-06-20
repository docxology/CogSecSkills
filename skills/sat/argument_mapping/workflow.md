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
- For Argument Mapping, tie each argument map, load bearing assumption list, and logical gap report claim to concrete evidence from the specific argument source, and focal claim item, source excerpt, observation, or command result that supports it.
- For Argument Mapping, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the argument map.
- Before recommending any Argument Mapping action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Argument Mapping: the argument map is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; identify the top-level conclusion and extract claims, premises, and evidence checks agree, and no unresolved contradiction would change the result.
- Medium for Argument Mapping: the argument map is plausible, but one important argument source source, comparison case, or alternative explanation remains incomplete.
- Low for Argument Mapping: the argument map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Argument Mapping cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Argument Mapping, use only authorized argument source, and focal claim, public or source-approved records, and caller-provided context needed for the defensive task.
- For Argument Mapping, minimize person-level detail in the argument map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Argument Mapping, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Argument Mapping: treating argument source as complete when identify the top-level conclusion and extract claims, premises, and evidence checks or contradictory evidence are missing.
- Argument Mapping: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Argument Mapping: reporting the argument map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Argument Mapping outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the argument map from Argument Mapping into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Argument Mapping to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with argument source, and focal claim' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not conflate mapping (describing the structure) with refutation (claiming the argument is wrong) — the map must accurately represent the argument even if the analyst disagrees with it
- Do not omit implicit premises because they are unstated; the most dangerous logical gaps are the ones the original author did not notice
- Do not allow the argument map to be used to construct a straw-man version of the opponent's position — accuracy to the source text is non-negotiable
- Do not produce a map so complex that no human can navigate it; prune to the most significant nodes and aggregate minor supporting evidence into summary nodes

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
