# Structured Analytic Techniques (SATs)

Structured Analytic Techniques are explicit, repeatable methods that externalize an analyst's reasoning so assumptions, evidence, and inferences can be examined, challenged, and shared rather than left implicit in one expert's head.

This primer covers the `sat` group, the largest in the library — **34 techniques** under [`skills/sat/`](../../skills/sat/), spanning hypothesis generation and testing, assumption checking, challenge analysis, diagnostic reasoning, and mapping/matrix methods. It is the connective tissue for the other six groups: a sound `cognitive_security`, `critical_review`, or `counterintelligence` judgment is only as trustworthy as the analytic process that produced it, and that process is what the SATs make inspectable.

## Contents

- [Why it matters for cognitive security](#why-it-matters-for-cognitive-security)
- [The technique families](#the-technique-families)
- [Hypothesis-plural reasoning: MHG, ACH, diagnostic reasoning](#hypothesis-plural-reasoning-mhg-ach-diagnostic-reasoning)
- [Assumption checks and challenge analysis](#assumption-checks-and-challenge-analysis)
- [Premortem: turning hindsight into foresight](#premortem-turning-hindsight-into-foresight)
- [Mapping and matrices](#mapping-and-matrices)
- [How CogSecSkills operationalizes this](#how-cogsecskills-operationalizes-this)
- [Defensive and ethical framing](#defensive-and-ethical-framing)
- [Further study](#further-study)

## Why it matters for cognitive security

Cognitive security begins with the analyst's own mind: the same biases adversaries exploit in target audiences also distort the people defending against them. SATs are a discipline of debiasing — they slow fast intuition, force consideration of alternatives, and make analytic judgments auditable. Under information warfare, where deception and overload are the adversary's tools, a structured process is itself a defense against being manipulated into the wrong conclusion.

Three failure modes recur across information-environment analysis, and each SAT family is a countermeasure to one of them:

- **Anchoring on the first satisfactory story.** The analyst stops at the first explanation that fits, never building or testing rivals — so a planted narrative survives unexamined. *Counter:* hypothesis-plural reasoning (MHG, ACH).
- **Silent load-bearing assumptions.** A judgment rests on beliefs nobody stated or tested; when one fails, the conclusion collapses without warning. *Counter:* the Key Assumptions Check and challenge techniques.
- **Treating consistency as confirmation.** Evidence that fits the favored hypothesis is read as strong support even when it fits every hypothesis equally well. *Counter:* diagnosticity-aware methods (ACH, Diagnostic Reasoning).

## The technique families

The `sat` group follows the **Heuer & Pherson canon**, the standard taxonomy that organizes techniques into families: decomposition and visualization, idea generation, scenarios and indicators, hypothesis generation and testing, assessment of cause and effect, challenge analysis, and conflict management / decision support. The 34 skills map onto these families; the table below names the ones this primer goes deep on, with their skill directories.

| Family | Representative skills (`skills/sat/`) | What they buy you |
| --- | --- | --- |
| Hypothesis generation & testing | [`multiple_hypothesis_generation`](../../skills/sat/multiple_hypothesis_generation/), [`analysis_of_competing_hypotheses`](../../skills/sat/analysis_of_competing_hypotheses/), [`diagnostic_reasoning`](../../skills/sat/diagnostic_reasoning/) | A complete hypothesis set, scored by disconfirmation rather than confirmation |
| Challenge analysis | [`key_assumptions_check`](../../skills/sat/key_assumptions_check/), [`devils_advocacy`](../../skills/sat/devils_advocacy/), [`team_a_team_b`](../../skills/sat/team_a_team_b/), [`red_hat_analysis`](../../skills/sat/red_hat_analysis/), [`premortem_analysis`](../../skills/sat/premortem_analysis/), [`structured_self_critique`](../../skills/sat/structured_self_critique/) | Surfaced assumptions and licensed dissent against a near-final judgment |
| Scenarios & indicators | [`alternative_futures_scenarios`](../../skills/sat/alternative_futures_scenarios/), [`indicators_generation`](../../skills/sat/indicators_generation/), [`indicators_validation`](../../skills/sat/indicators_validation/), [`signposts_of_change`](../../skills/sat/signposts_of_change/), [`what_if_analysis`](../../skills/sat/what_if_analysis/) | Pre-committed observable markers that resist post-hoc rationalization |
| Decomposition & visualization | [`analytic_matrices`](../../skills/sat/analytic_matrices/), [`mind_maps_and_concept_maps`](../../skills/sat/mind_maps_and_concept_maps/), [`network_analysis`](../../skills/sat/network_analysis/), [`causal_flow_diagramming`](../../skills/sat/causal_flow_diagramming/), [`argument_mapping`](../../skills/sat/argument_mapping/), [`chronologies_and_timelines`](../../skills/sat/chronologies_and_timelines/) | Externalized structure that takes load off working memory and exposes gaps |
| Idea generation | [`structured_brainstorming`](../../skills/sat/structured_brainstorming/), [`nominal_group_technique`](../../skills/sat/nominal_group_technique/), [`starbursting`](../../skills/sat/starbursting/), [`outside_in_thinking`](../../skills/sat/outside_in_thinking/), [`quadrant_crunching`](../../skills/sat/quadrant_crunching/) | Breadth before commitment, suppressing premature convergence |

Each skill ships a uniform set of files — `SKILL.md`, `skill.yaml`, a step-by-step `workflow.md`, and a `harness/` binding — so the technique is a runnable procedure, not just a description.

## Hypothesis-plural reasoning: MHG, ACH, diagnostic reasoning

The central discipline of the SATs is **plurality of hypotheses**: never evaluate a single explanation in isolation. Three skills form a pipeline.

**Multiple Hypothesis Generation (MHG)** comes first. It requires a complete, **mutually exclusive and collectively exhaustive (MECE)** hypothesis set *before* any one is evaluated, because the most common failure in forecasting and threat assessment is an artificially narrow set. [`multiple_hypothesis_generation`](../../skills/sat/multiple_hypothesis_generation/) produces a MECE-tested, labeled set plus a completeness audit — which pairs overlapped, which were merged, and whether a logical remainder was left unaddressed. It is the mandated precursor to ACH: without it, the ACH matrix can be trivially incomplete.

**Analysis of Competing Hypotheses (ACH)** is the flagship. Heuer's decisive move is to **seek evidence that disconfirms** — the surviving hypothesis is the one with the *least* diagnostic evidence against it, not the one with the most evidence for it. The [`analysis_of_competing_hypotheses`](../../skills/sat/analysis_of_competing_hypotheses/) skill drives the full eight-step loop:

1. **Enumerate hypotheses** — complete and mutually exclusive, always including a *deception* hypothesis ("someone wants me to believe H1") and a *residual* ("something we haven't thought of"); never fewer than three.
2. **List evidence and arguments** — facts, assumptions, and the *absence of evidence* (an observation a hypothesis predicts but that is missing), each tagged with source and reliability.
3. **Build the matrix** — score every (evidence, hypothesis) cell **C** (consistent), **I** (inconsistent), or **N** (no bearing).
4. **Assess diagnosticity** — a row that is **C for every hypothesis** has no diagnostic value; flag it and set it aside. The analysis lives in the rows that discriminate.
5. **Refine** — drop non-diagnostic evidence, merge hypotheses that are not truly distinct.
6. **Draw tentative conclusions** — rank by **inconsistency score**; the hypothesis with the *fewest* I marks is provisionally strongest. Ranking by the most C marks is the bias trap.
7. **Sensitivity analysis** — name the one or two items that, if wrong or deceptive, would flip the ranking, and re-verify them.
8. **Report with indicators** — emit the matrix, the ranking, the single most diagnostic and most damaging items, a calibrated confidence statement, and *indicators*: future observations that would confirm or overturn the lead (handed off to [`indicators_generation`](../../skills/sat/indicators_generation/)).

A worked sketch makes the diagnosticity point concrete. Suppose an account network amplifies a divisive post and the hypotheses are H1 *coordinated influence operation*, H2 *organic outrage*, H3 *commercial engagement farming*. "The posts spiked within an hour" is **C** under all three — it is non-diagnostic and earns no hypothesis any credit. "The accounts were created in the same week and share a posting cadence" is **C** under H1 and H3 but **I** under H2 — it discriminates. The conclusion must rest on the discriminating rows, and the report names what would overturn it (e.g., evidence the accounts predate the issue would weaken H1).

**Diagnostic Reasoning** is ACH's single-datum companion. When one new piece of information arrives mid-analysis, [`diagnostic_reasoning`](../../skills/sat/diagnostic_reasoning/) asks the Bayesian question without demanding precise numbers: *how much more (or less) likely is this datum if H is true than if H is false?* Analysts assign comparative likelihoods (much more likely / somewhat more likely / equally likely / less likely) across the active hypotheses to form a qualitative likelihood ratio, then update the ranking traceably to that datum. This is the precise antidote to "consistency implies support": evidence is diagnostic only when it would be *rare* under the alternatives.

## Assumption checks and challenge analysis

A judgment can be built from impeccable logic on hidden, untested foundations. **Challenge techniques** exist to attack those foundations before a decision-maker does.

The **Key Assumptions Check** is the foundational one. [`key_assumptions_check`](../../skills/sat/key_assumptions_check/) makes explicit the *stated and unstated* beliefs an analytic line silently depends on, then interrogates each: why we believe it, what evidence supports it, and under what conditions it would *not* hold. Every assumption is sorted into one of four classes:

- **Solid** — well supported by evidence (and *only* if there is real evidence; "solid because familiar" is reclassified, never waved through).
- **Caveated** — holds under stated conditions that should be monitored.
- **Unsupported** — believed without an evidentiary basis.
- **Key uncertainty** — both load-bearing and uncertain.

The decisive test for each is: *if this assumption is wrong, does the conclusion collapse?* The assumptions that are **load-bearing × uncertain** are flagged as the "key assumptions," and the skill rewrites the judgment to expose its dependence on them and names the collection that would test it. It pairs naturally upstream of ACH — a hypothesis set built on an unexamined assumption inherits that assumption's fragility.

The other challenge skills attack from different angles: [`devils_advocacy`](../../skills/sat/devils_advocacy/) assigns someone to argue the contrary case; [`team_a_team_b`](../../skills/sat/team_a_team_b/) pits two structured analyses against each other; [`red_hat_analysis`](../../skills/sat/red_hat_analysis/) models how an adversary would perceive and decide; and [`structured_self_critique`](../../skills/sat/structured_self_critique/) turns the lens inward on a single analyst's own draft. All of them serve one purpose — manufacturing the dissent that consensus, authority bias, and sunk-cost pressure would otherwise suppress.

## Premortem: turning hindsight into foresight

The **premortem** (Klein) deserves its own treatment because it inverts the usual review stance. Instead of asking "what could go wrong," participants are told the plan *has already failed* and asked to explain why. Adopting the cognitive stance that failure is a settled fact bypasses the social pressure to defend a committed plan and licenses critiques a prospective review suppresses.

[`premortem_analysis`](../../skills/sat/premortem_analysis/) is most valuable when a conclusion is near commitment and overconfidence or groupthink is likely, when a prior review produced only mild, socially constrained critique, or when a team has worked an issue long enough that loss-aversion frames honest dissent as disloyalty. Its output is a ranked list of failure causes — each with a plausibility × impact estimate, a leading indicator, and a mitigation — plus the assumption breaks that would be most dangerous, recorded as a documented dissent that can be revisited if the prediction later fails. In a cognitive-security setting it stress-tests an analytic conclusion *before* it reaches a decision-maker, and the leading indicators it produces feed directly into the scenarios-and-indicators family.

## Mapping and matrices

Several techniques externalize structure so the analyst is not holding it all in working memory. **Analytic Matrices** are the most general: [`analytic_matrices`](../../skills/sat/analytic_matrices/) cross-tabulates variables — hypotheses, actors, drivers, criteria — as rows and columns, then populates each cell with evidence, ratings, or judgments. The grid does three things narrative cannot: it makes the analyst's logic explicit and independently reviewable, it surfaces **blank cells** (missing evidence) and **conflicting cells** (contradictory evidence), and it gives a pattern-level view of the problem. The ACH matrix is a specialized instance; analytic matrices also serve option analysis and influence-operation assessment (actors × capabilities × behaviors).

The visualization skills complement the grid. [`mind_maps_and_concept_maps`](../../skills/sat/mind_maps_and_concept_maps/) lay out the conceptual terrain; [`network_analysis`](../../skills/sat/network_analysis/) maps relationships among actors and accounts; [`causal_flow_diagramming`](../../skills/sat/causal_flow_diagramming/) and [`argument_mapping`](../../skills/sat/argument_mapping/) make cause-and-effect and inferential chains explicit; and [`chronologies_and_timelines`](../../skills/sat/chronologies_and_timelines/) order events so temporal anomalies (impossible sequences, suspicious synchrony) become visible. Each produces a reusable artifact that can be updated as evidence arrives without rewriting prose.

## How CogSecSkills operationalizes this

The skills in this group turn each technique into a bounded agentic procedure with a uniform contract. An ACH skill builds an evidence-by-hypothesis matrix and flags the least-disconfirmed hypothesis; a Key Assumptions Check extracts and interrogates a brief's implicit premises and classifies each; a premortem runner produces a ranked, mitigated dissent record. Every skill carries the same de-stitched, domain-specific quality scaffolding — a defensive boundary, a misuse redirect, evidence discipline, calibrated confidence and uncertainty classes, privacy/legal/harm constraints, and explicit failure modes with negative controls — so the discipline is enforced, not assumed.

Two contracts are worth calling out because they make the outputs trustworthy:

- **Calibrated confidence is mandatory.** Each skill states High / Medium / Low against concrete conditions (e.g., for ACH, *High* requires a complete, mutually exclusive hypothesis set whose ranking survives the sensitivity check on its load-bearing items with independent corroboration) and must state what the technique *cannot* determine and what remains unknown.
- **Labeling before judgment.** Observations, derived features, assumptions, inferences, contradictions, and missing inputs are labeled *separately* before any matrix or table is written, so an inference is never silently promoted to an observation.

Each skill produces a structured, inspectable artifact — a matrix, an assumptions table, a ranked failure list — rather than an opaque verdict, so the reasoning remains reviewable and the result can be revised when evidence changes.

## Defensive and ethical framing

SATs are applied to the analyst's *own* judgments to improve rigor and calibration, not to engineer persuasion. Every `sat` skill encodes this as an explicit boundary: it refuses requests to force a preferred conclusion, hide uncertainty, or rationalize manipulation, and redirects to the safe defensive form — applying the structured technique to supplied evidence while preserving alternatives and uncertainty. The privacy constraints minimize person-level detail (preferring aggregate, artifact-, role-, or case-level summaries) and forbid inferring protected traits, private identity, intent, or culpability beyond the authorized evidence. Outputs are accountable artifacts subject to human review and revision; the goal is sounder defensive analysis, never weaponized conviction.

## Further study

- AGEINT curriculum — github.com/docxology/AGEINT, concept DOI 10.5281/zenodo.20732274 (Daniel Ari Friedman, Active Inference Institute).
- The 34 runnable techniques in this group: [`skills/sat/`](../../skills/sat/) — each with a `SKILL.md`, `workflow.md`, and harness binding.
- Richards J. Heuer Jr., *Psychology of Intelligence Analysis* (CIA Center for the Study of Intelligence, 1999).
- Richards J. Heuer Jr. & Randolph H. Pherson, *Structured Analytic Techniques for Intelligence Analysis* (CQ Press; 2nd ed. 2014, 3rd ed. 2020).
- Gary Klein, "Performing a Project Premortem," *Harvard Business Review* (2007) — the premortem method.
