# Workflow — Resilience Metrics Design

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Define the ecosystem and decision context (read)
Ingest the ecosystem definition and stakeholder goals. Clarify: what counts as a manipulation event in this ecosystem; who the legitimate and illegitimate actors are; what the decision cadence is (weekly dashboard, quarterly assessment, crisis-triggered review); and what data is already available vs. must be newly instrumented. Document known threat vectors as the basis for metric coverage.

## Step 2 — Map resilience dimensions and candidate indicators (reason)
Decompose ecosystem resilience into four primary dimensions and generate candidate indicators for each. (1) Source diversity: number of independent high-reach outlets; Herfindahl-Hirschman Index of audience attention concentration; share of traffic reaching single-owner domain clusters. (2) Correction uptake: ratio of correction engagement to original misinformation engagement; proportion of false claims receiving timely fact-check coverage; recirculation rate of debunked content. (3) Narrative elasticity: time for manipulative narratives to achieve tipping-point spread; proportion of viral narratives originating from low-credibility sources. (4) Trust calibration: correlation between audience source trust ratings and independent credibility assessments; percentage of audience that can identify the funder of a news outlet. For each candidate, document: data source, collection feasibility, validity threats, and manipulation-resistance (can a bad actor game this metric cheaply).

## Step 3 — Select, validate, and tier the indicator set (reason)
Select a tractable set of indicators (recommend 8–15 for an ongoing monitoring program; more is not better). Tier them: Tier 1 — core indicators that must be tracked at every reporting cycle; Tier 2 — supplementary indicators for deep-dive assessments; Tier 3 — aspirational indicators pending data availability. For qualitative indicators, design inter-rater reliability protocols. For each metric, set a baseline range, an alert threshold (degradation signal), and a target range (successful intervention outcome). Flag any indicators where collection would require platform API access or survey fieldwork that may not be feasible.

## Step 4 — Author the indicator schema, measurement protocol, and implementation guidance (write)
Compose the indicator schema as a structured table. Write the measurement protocol, covering: data collection schedule, normalization procedures (especially across platforms with different base rates), missing data handling, and inter-rater calibration for qualitative indicators. Write implementation guidance covering dashboard design (which indicators to surface at a glance vs. drill-down), alert thresholds and escalation procedures, reporting cadence and stakeholder communication, and a review cycle for revisiting and updating the metric set as the threat landscape evolves.

## Anti-criteria (must NOT happen)
- do not define metrics that are easy for adversaries to game — a metric whose gaming is cheap and undetectable is a liability, not a measure
- do not use only lagging indicators — if all metrics confirm damage after it has occurred, the monitoring system cannot enable timely intervention
- do not set absolute numerical thresholds without establishing ecosystem-specific baselines — 'X% correction uptake is good' is meaningless without a reference ecosystem and pre-intervention baseline
- do not conflate quantity metrics (volume of fact-checks published) with quality/impact metrics (proportion of misinformed audience reached by a correction)

## AGEINT upstream
`docs/ageint/cognitive-security.md`
