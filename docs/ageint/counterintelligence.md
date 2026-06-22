# Counterintelligence (Defensive)

Defensive counterintelligence is the practice of detecting and neutralizing deception, denial, and elicitation directed at an analyst or organization — hardening the analytic process so an adversary cannot feed it false signals or extract its reasoning. In CogSecSkills this group is the eight-skill toolkit that protects the *thinking* layer: the people, sources, and workflows that turn raw information into judgments.

## On this page

- [Why it matters for cognitive security](#why-it-matters-for-cognitive-security)
- [The four defensive problems](#the-four-defensive-problems)
- [Core concepts](#core-concepts)
- [Skills in this group](#skills-in-this-group)
- [How CogSecSkills operationalizes this](#how-cogsecskills-operationalizes-this)
- [A worked example](#a-worked-example)
- [Defensive & ethical framing](#defensive--ethical-framing)
- [Related groups](#related-groups)
- [Further study](#further-study)

## Why it matters for cognitive security

Sophisticated adversaries do not just spread noise; they tailor deception to how analysts think, exploiting our preference for coherent stories and confirming evidence. Recognizing denial (hiding the true signal) and deception (presenting a false one) protects the integrity of every judgment built on collected information. Defensive CI is cognitive security applied to the analytic pipeline itself.

The threat is specific and asymmetric. An influence campaign that merely floods a feed with falsehoods is loud and detectable. A campaign that plants one *convenient, confirming* document in a channel an analyst already trusts is quiet, cheap, and far more dangerous — because it rides the analyst's own confidence. Heuer's central finding is the uncomfortable one: deception is hardest to detect precisely when it tells you what you expected to hear, and your confidence in a conclusion is not evidence that the conclusion is correct.

## The four defensive problems

This group exists to address four recurring failure modes, each with dedicated skills:

1. **Deception detection** — the picture is too clean, too convenient, or arrived too conveniently. Did an adversary stage it?
2. **Elicitation recognition** — a conversation, message, or interview is quietly extracting more than it gives. Is this routine exchange or social-engineering collection?
3. **Analytic-process hardening** — where in our own workflow could planted evidence, anchoring, or a seeded false lead corrupt the conclusion before anyone notices?
4. **Insider-threat indicators** — do converging behavioral and access signals warrant a *referral* (never a verdict) within authorized program bounds?

Every skill below maps to one or more of these problems, and every one returns a *structured advisory for a human decision-maker* — never an autonomous determination.

## Core concepts

- **Denial & Deception (D&D) detection** — distinguishing *denial* (concealment of real activity) from *deception* (active presentation of false indicators), and watching for anomalies, too-perfect evidence, and conspicuous gaps. The signature move is to reverse the analyst's posture: instead of "what does this evidence tell us?" ask "what would a rational deceiver have had to hide or plant for us to reach this conclusion?"
- **Heuer's deception literature** — the principle that deception is hardest to detect when it confirms expectations, and that an analyst's confidence is not evidence of accuracy. A missing confirmatory signal is a flagged gap, not proof of authenticity.
- **Pherson's deception-detection checklists** — **MOM** (Motive, Opportunity, Means), **POP** (Past Opposition Practices), **MOSES** (My Own Sources Evaluation), and **EVE** (Evaluation of Evidence — consistency, accuracy, and absence of gaps/anomalies). These convert an intuitive "something seems off" into a documentable, falsifiable deception hypothesis.
- **Elicitation awareness** — recognizing conversational techniques used to draw out information (flattery, assumed knowledge, quid pro quo, feigned ignorance, and deliberate false statements that invite correction) and defending against them. A reliable tell is *re-probing after deflection*: a routine conversation drops a topic when you steer away; a collection attempt circles back to it.
- **Analytic process hardening** — diversifying sources, validating source access and reliability, and routing high-stakes judgments through challenge analysis (Devil's Advocacy, ACH) before acceptance. The goal is manipulation-resistance built into the workflow, without forcing analysts to become paranoid about every source.

## Skills in this group

The group ships eight skills under `skills/counterintelligence/`. Each one declares a defensive boundary, a misuse redirect, and an evidence-discipline contract, and each returns a structured, citable advisory.

| Skill | What it does | Primary problem |
| --- | --- | --- |
| [`denial_and_deception_detection`](../../skills/counterintelligence/denial_and_deception_detection/SKILL.md) | Builds the explicit deception scenario — what an adversary would have had to do to produce this evidence — with a plausibility rating and discriminating collection priorities. | Deception detection |
| [`indicators_of_deception_analysis`](../../skills/counterintelligence/indicators_of_deception_analysis/SKILL.md) | Runs the MOM/POP/MOSES/EVE checklists across a body of evidence, documenting null findings as explicitly as positive ones. | Deception detection |
| [`elicitation_attempt_recognition`](../../skills/counterintelligence/elicitation_attempt_recognition/SKILL.md) | Maps observed conversational moves to a taxonomy of elicitation techniques, rates composite risk, and recommends disengage / limit / redirect / report. | Elicitation recognition |
| [`analytic_process_hardening`](../../skills/counterintelligence/analytic_process_hardening/SKILL.md) | Maps each workflow node to its manipulation surface and prescribes prioritized procedural controls with an explicit residual-risk statement. | Process hardening |
| [`adversary_tradecraft_profiling`](../../skills/counterintelligence/adversary_tradecraft_profiling/SKILL.md) | Converts scattered incident data into a TTPS (Tactics, Techniques, Procedures, Signatures) behavioral model for anticipation and attribution, flagging mirror-imaging risk. | Process hardening |
| [`disinformation_attribution`](../../skills/counterintelligence/disinformation_attribution/SKILL.md) | Builds an ACH-style matrix to assign responsibility for an influence operation with calibrated confidence and an explicitly evaluated false-flag hypothesis. | Deception detection |
| [`honeypot_and_canary_design`](../../skills/counterintelligence/honeypot_and_canary_design/SKILL.md) | Designs decoy assets and canary tripwires that alert on access, strictly for detection — never entrapment — with a legal/ethical/HR-review checklist. | Process hardening |
| [`insider_threat_indicator_review`](../../skills/counterintelligence/insider_threat_indicator_review/SKILL.md) | Aggregates behavioral, technical, and contextual indicators against CPNI/NITTF frameworks to inform a referral decision within authorized, privacy-respecting bounds. | Insider-threat indicators |

## How CogSecSkills operationalizes this

Skills in this group turn the checklists above into repeatable agentic reviews: running MOM/POP/MOSES/EVE against a source or claim, flagging deception indicators and evidence anomalies, and prompting a structured denial-and-deception pass before a conclusion is locked. Outputs are structured advisories for human analysts.

Three discipline contracts are shared across the group and make the advisories auditable rather than merely plausible:

- **Evidence binding.** Every finding — each deception indicator, each elicitation technique, each insider-risk cluster — must be tied to a concrete, named item: a quoted transcript line, a specific source channel and its arrival timing, an access-log entry, or a workflow node. An unsupported intent claim is labelled speculation, not evidence.
- **Separation of layers.** Observations, derived features, assumptions, inferences, contradictions, and missing inputs are labelled separately *before* any assessment is written, so a reader can see where fact ends and inference begins.
- **Weakest-link surfacing.** Before recommending any action, a skill names the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check — so the judgment stays falsifiable.

These contracts pair naturally: a `denial_and_deception_detection` scenario tells you *what to look for*, `indicators_of_deception_analysis` *scores it* against MOM/POP/MOSES/EVE, and `analytic_process_hardening` closes the *door it came through* so the same channel cannot be exploited twice.

## A worked example

A single high-value source suddenly produces an unusually clean, fully confirming report. The defensive sequence:

1. `indicators_of_deception_analysis` runs MOM/POP/MOSES/EVE: the adversary has motive and opportunity (MOM), the report is *too* convenient and lacks the usual rough edges (POP anomaly), and EVE flags an absent confirmatory signal as a gap rather than a green light.
2. `denial_and_deception_detection` constructs the explicit deception scenario — which sources the adversary would need to control and conceal — rates its plausibility against capability/motive/opportunity *together*, and lists the collection that would best discriminate a genuine picture from a managed one.
3. `analytic_process_hardening` traces the channel the report arrived through, maps it as a manipulation surface, and prescribes a control (independent corroboration before this source can anchor a high-stakes judgment) with an explicit residual-risk note.

The output is a human-readable advisory recommending a discriminating check — not an autonomous "this is deception" verdict.

## Defensive & ethical framing

This material is strictly defensive — detecting deception and protecting an organization's own analysis and information. It is not a guide to running deception, elicitation, or covert operations against others. All use is accountable, lawful, and under human oversight.

Two skills carry extra guardrails worth naming explicitly. `honeypot_and_canary_design` is for *detection only*: a triggered canary is evidence of access, never of identity, until corroborating evidence is named, and every design ships with a legal, ethical, and HR-review checklist addressing jurisdiction and entrapment concerns. `insider_threat_indicator_review` produces a *referral input*, never a determination of guilt; it requires a competing benign explanation for every indicator cluster and uses only evidence obtainable within the program's legal monitoring authorities, respecting privacy, civil liberties, and due process throughout. Every skill in the group also declares a misuse redirect: a request to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft is refused and redirected to the safe defensive form.

## Related groups

- **Structured analytic techniques** (`structured-analytic-techniques.md`) — ACH and Devil's Advocacy are the challenge-analysis backbone that several skills here route high-stakes judgments through.
- **OSINT integrity** (`osint-integrity.md`) — disinformation attribution draws on open-source investigation methodology and shares its provenance discipline.
- **Information environment** (`information-environment.md`) — campaign-level influence detection complements the per-source deception checks here.

## Further study

- AGEINT curriculum — github.com/docxology/AGEINT, concept DOI 10.5281/zenodo.20732274.
- Richards J. Heuer Jr., *Psychology of Intelligence Analysis* (1999), chapters on deception.
- Randolph H. Pherson & Richards J. Heuer Jr., *Structured Analytic Techniques for Intelligence Analysis* (deception-detection techniques: MOM/POP/MOSES/EVE).
- Roy Godson & James J. Wirtz (eds.), *Strategic Denial and Deception* (2002), on the systematic logic of D&D operations.
- CPNI and NITTF insider-threat indicator frameworks (referenced by `insider_threat_indicator_review`).
