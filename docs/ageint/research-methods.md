# Research Methods for Analysis

Research methods for analysis are the structured practices for gathering, grading, and synthesizing evidence and for expressing judgments with calibrated, communicable confidence. In the CogSecSkills library this is the `research_methods` group: five mature, defensively-bounded skills that together turn raw sources into a reviewable analytic product where every judgment carries its evidence, its confidence, and the conditions that would change it.

This primer maps the concepts to the actual skills under `skills/research_methods/`, then walks one end-to-end example so the pipeline — grade, estimate, assess confidence, synthesize, report — is concrete rather than abstract.

## Why it matters for cognitive security

An analytic product is only as trustworthy as the method behind it. Ungraded evidence, uncalibrated confidence, and vague language let bias and adversarial framing slip through unchecked: a single well-placed source gets counted as corroboration, a hunch gets written up as "highly likely," and a buried caveat never reaches the decision-maker. Structured synthesis and calibrated estimation make analysis reproducible and its uncertainty honest — so a reader knows not just *what* is claimed but *how strongly*, *on what basis*, and *what would overturn it*.

This is the defensive core of cognitive security. The same disciplines that make an analyst's own work checkable also make manipulation visible: when every statement traces to a graded source, an injected or laundered claim has nowhere to hide, and when confidence is a separate, justified dimension, an attacker cannot smuggle certainty in through confident prose.

## The five skills at a glance

The group is small by design and composes into a pipeline. Each skill is independently invokable, but they are strongest in sequence — grade the inputs, estimate the unknowns, assess how far to trust the result, synthesize across the corpus, and report it so the bottom line is unmissable.

| Skill (`research_methods/…`) | What it produces | Reach for it when |
| --- | --- | --- |
| [`evidence_grading`](../../skills/research_methods/evidence_grading/SKILL.md) | A graded evidence table (quality × relevance) and a weight-of-evidence narrative | Heterogeneous sources of varying rigor and directness must be weighed |
| [`calibrated_estimation`](../../skills/research_methods/calibrated_estimation/SKILL.md) | A numeric estimate with reference class, base rate, 80% interval, and resolution criteria | A decision needs a probability for an uncertain outcome |
| [`analytic_confidence_assessment`](../../skills/research_methods/analytic_confidence_assessment/SKILL.md) | A justified confidence tier with sub-dimension scores and tier-change conditions | A judgment will drive a decision and its reliability limits must be explicit |
| [`structured_literature_synthesis`](../../skills/research_methods/structured_literature_synthesis/SKILL.md) | A BLUF synthesis briefing, a per-claim evidence table, and a gap inventory | A body of sources must become one gap-aware, traceable briefing |
| [`structured_reporting_and_bluf`](../../skills/research_methods/structured_reporting_and_bluf/SKILL.md) | A report leading with the key judgment + confidence, with traceable body and caveats | Any product must reach a decision-maker who may not read past paragraph one |

## Core concepts

### Evidence grading — two axes, never one

Evidence is graded on two *independent* axes: **quality** (methodological rigor, source reliability, internal validity) and **relevance** (how directly it speaks to the question at hand). Keeping them separate stops two classic failures — a rigorous study that doesn't actually address the question inflating confidence, and a perfectly on-point but flimsy source anchoring the conclusion. The standard rubrics are the **Admiralty Code / NATO source-reliability and information-credibility scale** (source A–F × information 1–6) for intelligence reporting, and **GRADE** (high/moderate/low/very-low certainty) for scientific evidence. The CogSecSkills `evidence_grading` skill combines the two grades *multiplicatively*, so low quality is never offset by high relevance, and records gaps and contradictions as their own rows.

### Calibrated estimation — outside view first

Calibrated estimation follows the forecasting literature (Tetlock, Kahneman, and the prediction-tournament tradition): produce a numeric probability, anchor it in an explicitly chosen **reference class** and its **base rate**, then make case-specific adjustments that are each individually justified. The output always carries an **80% confidence interval** and **resolution criteria** specific enough that the forecast can later be scored against reality — the feedback loop (Brier-style track records) that calibration actually depends on. Moving off the base rate without supporting evidence is treated as inside-view bias, not insight.

### Analytic confidence — likelihood is not confidence

Confidence is a *separate dimension* from likelihood. "70% likely" says how probable the outcome is; "moderate confidence" says how much to trust that 70%. The `analytic_confidence_assessment` skill assigns a tier (high/moderate/low) from three sub-dimensions — **source quality, degree of corroboration, and assumption load** — following intelligence-community standards (ICD 203). Corroboration only counts when it comes from genuinely independent sources, not a common reporting chain, and the tier holds to a conservative weakest-dimension rule. Crucially, it also lists the conditions that would *change* the tier, so confidence is falsifiable rather than impressionistic.

### Structured literature & evidence synthesis — traceable, gap-aware

Synthesis is a documented review, not convenience sampling: define a synthesis question with inclusion/exclusion criteria, gather and **deduplicate** sources (so mirrored reporting is not counted as independent agreement), extract graded claims with citations, cluster by theme, and surface agreements, conflicts, *and* gaps. The `structured_literature_synthesis` skill produces a BLUF briefing where every statement traces to a graded source and an explicit **gap inventory** of questions no source in the corpus answers — uncited statements become labelled gaps, never quiet findings.

### BLUF reporting and estimative language

**BLUF** (Bottom Line Up Front) places the key judgment and its confidence in the first sentence or paragraph, then supports it in descending order of importance with a caveats section and audience-tailored implications. Codified in intelligence tradecraft (ICD 203, ODNI), it defeats the failure mode where the decisive caveat is buried where no one reads it. Paired with **estimative language** — standardized probability words ("likely," "probable") mapped to numeric ranges — it removes the ambiguity of verbal hedging. The `structured_reporting_and_bluf` skill enforces that every body claim is traceable to a cited source or an explicitly stated assumption.

## A worked example: one claim through the pipeline

Suppose the analytic question is: *"Is a coordinated inauthentic-behavior campaign amplifying narrative X on platform Y?"* The five skills compose like this.

1. **Grade the inputs** (`evidence_grading`). Three sources arrive: a platform transparency report (high quality, high relevance), a vendor blog post reposting the same dataset (deduplicated — it is *not* independent corroboration), and an academic network-analysis preprint (high quality, moderate relevance). The table records grades, justifications, and a gap row: no independent telemetry on account creation dates.
2. **Estimate the unknowns** (`calibrated_estimation`). Reference class: prior confirmed coordination cases on comparable platforms. Base rate of "coordination confirmed given these signals" ≈ 30%; case-specific signals (synchronized posting windows) adjust upward to a point estimate of 55% with an 80% interval of 35–70% and a stated resolution event.
3. **Assess confidence** (`analytic_confidence_assessment`). Source quality is good, but corroboration is thin once the duplicate is removed and assumption load is high (the synchrony metric assumes honest timestamps). Weakest-dimension rule → **moderate confidence**, with the tier-raising condition named: independent account-provenance data.
4. **Synthesize** (`structured_literature_synthesis`). The corpus becomes a BLUF briefing: agreements (synchrony is real), conflicts (preprint's clustering threshold differs from the platform's), and the gap inventory carried forward.
5. **Report** (`structured_reporting_and_bluf`). The product opens: *"We assess it is roughly even-to-likely (≈55%, moderate confidence) that narrative X is being amplified by coordinated inauthentic behavior on platform Y."* Then evidence, the explicit caveat about timestamp integrity, and the single check that would move the judgment.

The result is a chain a second analyst can reproduce from the same inputs — and an adversary cannot quietly tilt, because every step is bound to graded evidence.

## How CogSecSkills operationalizes this

Skills in this group encode the concepts above as repeatable, harness-neutral agentic steps (each `workflow.md` names the tool verbs — `read`, `reason`, `write` — that a harness adapter binds). They tag sources with Admiralty/GRADE ratings, structure a synthesis with an audit trail, elicit calibrated probability estimates with explicit confidence, and format findings in BLUF. Every skill carries the same enforced disciplines, visible in its `SKILL.md`:

- **Evidence discipline** — each grade, score, and estimate binds to concrete evidence; observations, assumptions, inferences, contradictions, and missing inputs are labelled *separately* before the product is written.
- **Confidence and uncertainty** — explicit High / Medium / Low criteria for the product itself, plus a standing requirement to state what cannot be determined and to name the next discriminating check.
- **Negative controls and failure modes** — each `workflow.md` enumerates how the method fails (volume substituting for rigor, double-counting a shared reporting chain, dropping disconfirming evidence) so reviewers can probe for exactly those.

Each skill yields a structured, reviewable product — a graded table, a scored estimate, a BLUF briefing — never an unsourced assertion.

## Defensive & ethical framing

These methods serve transparency and accountability — every judgment carries its evidence grade, confidence, and assumptions so it can be checked and challenged. The skills are explicitly bounded: each `SKILL.md` declares a **defensive boundary** and a **misuse redirect** that refuse requests to cherry-pick sources, fabricate citations, or overstate certainty, redirecting instead to honest synthesis of authorized sources with explicit uncertainty. Person-level detail is minimized in favor of aggregate, role-, or case-level summaries, and the skills do not infer protected traits, identity, or intent beyond the supplied and authorized evidence. Use is bounded by intellectual honesty and human oversight, not advocacy or persuasion.

## Where this connects

- [Structured analytic techniques](structured-analytic-techniques.md) — the reasoning structures (ACH, key-assumptions checks) that feed graded evidence and confidence into these methods.
- [Adversarial assurance](adversarial-assurance.md) — the severity-vs-confidence and verify-the-verifier disciplines that stress-test a finished analytic product.
- [Cognitive security](cognitive-security.md) — the threat context these methods defend against.

## Further study

- AGEINT curriculum — github.com/docxology/AGEINT, concept DOI 10.5281/zenodo.20732274.
- Philip E. Tetlock & Dan Gardner, *Superforecasting: The Art and Science of Prediction* (2015).
- Richards J. Heuer Jr., *Psychology of Intelligence Analysis* (CIA Center for the Study of Intelligence, 1999); ODNI Intelligence Community Directive **ICD 203**, *Analytic Standards*.
- GRADE Working Group, *GRADE Handbook* (gradeworkinggroup.org); NATO Admiralty source-grading scale.
