# Cognitive Security

Cognitive security is the practice of protecting human perception, cognition, and decision-making from adversarial manipulation — defending the "wetware" layer of the information ecosystem the way infosec defends networks and devices. This primer orients you to the `cognitive_security` group: the threat model it addresses, the defensive concepts it operationalizes, and the 24 skills it ships under `skills/cognitive_security/`.

## Contents

- [Why it matters](#why-it-matters)
- [The defensive lifecycle](#the-defensive-lifecycle)
- [Core concepts](#core-concepts)
- [Skills in this group](#skills-in-this-group)
- [How CogSecSkills operationalizes this](#how-cogsecskills-operationalizes-this)
- [Defensive & ethical framing](#defensive--ethical-framing)
- [Further study](#further-study)

## Why it matters

Influence operations target beliefs and behavior, not servers. When perception is compromised, every downstream decision — by analysts, institutions, and publics — is compromised too. Unlike a breached database, a manipulated belief leaves no log entry, propagates through trusted social channels, and resists correction once it has fused with identity.

A defensive posture therefore cannot wait for an incident. It requires recognizing manipulation techniques while they are still recognizable as techniques, understanding the cognitive biases they exploit, and building population-level resilience *before* exposure — because corrections after the fact rarely undo the damage. The illusory-truth effect (repetition breeds belief) and the continued-influence effect (a retracted claim keeps shaping judgment) both mean that the cheapest, most effective intervention point is upstream of the attack, not downstream of it.

## The defensive lifecycle

The skills in this group map onto a recognizable defend-detect-respond-measure cycle. Reading them as a lifecycle (rather than a flat list) clarifies which skill answers which question:

| Phase | Question it answers | Representative skills |
| --- | --- | --- |
| **Map the terrain** | Who is exposed, and how do they know what they know? | `audience_vulnerability_segmentation`, `epistemic_security_posture_review`, `attack_surface_of_belief_mapping` |
| **Detect** | Is this content/campaign manipulative, and how? | `manipulation_technique_identification`, `propaganda_technique_classification`, `logical_fallacy_detection`, `emotional_manipulation_analysis`, `framing_and_priming_analysis`, `disinformation_campaign_analysis`, `narrative_threat_assessment` |
| **Inoculate (pre-bunk)** | How do we build resistance before the attack lands? | `prebunking_inoculation_design`, `media_literacy_assessment` |
| **Respond (de-bunk)** | How do we correct without amplifying the lie? | `counter_messaging_strategy` |
| **Measure** | Is the information ecosystem getting more resilient? | `resilience_metrics_design`, `trust_and_credibility_modeling` |

The cycle is deliberately weighted toward the left: cognitive security treats prevention and recognition as primary, and after-the-fact correction as the fallback.

## Core concepts

- **Influence operations & propaganda techniques** — recognizing classic devices (cherry-picking, false dichotomy, appeal to fear, astroturfing, flooding / firehose-of-falsehood) and emotional framing as manipulation signatures. The `propaganda_technique_classification` and `manipulation_technique_identification` skills name these against established taxonomies (Cialdini's influence principles, dark-pattern persuasion catalogues, the disinformation-research literature) so an analyst can distinguish legitimate persuasion from techniques that bypass rational agency.
- **Analytic frameworks** — the **ABCDE** framework (Actor, Behavior, Content, Degree, Effect) for characterizing operations, and the **DISARM** framework (the open red/blue tactics-and-techniques matrix for disinformation, modeled on MITRE ATT&CK) for mapping and countering campaigns. `disinformation_campaign_analysis` and `influence_operation_mapping` apply these to a corpus of suspected coordinated activity.
- **Inoculation / prebunking theory** — McGuire's inoculation theory and van der Linden's prebunking research: exposing people to a weakened, clearly-labeled dose of a manipulation technique builds psychological resistance. `prebunking_inoculation_design` turns this into concrete inoculation content — an explicit warning, a weakened-dose example, a named refutation, an audience call-to-action, and efficacy-check items — drawing on Banas & Rains (2010) and field assets such as Bad News, Go Viral, and Cranky Uncle.
- **Cognitive biases** — confirmation bias, availability and anchoring effects, the illusory-truth effect, and motivated reasoning are the attack surface manipulators exploit. `cognitive_bias_audit` surfaces which biases a given message is engineered to trigger, and `framing_and_priming_analysis` examines how presentation choices steer interpretation before reasoning begins.
- **Narrative and emotion** — affect, identity, and group dynamics are leveraged to bypass deliberate reasoning. `narrative_threat_assessment` characterizes a circulating narrative's claims, the belief or identity levers it pulls, its provenance and likely intent, and its reach and harm potential — producing a defensive brief, not a playbook. `emotional_manipulation_analysis` isolates the affective machinery specifically.

## Skills in this group

The group ships 24 skills under `skills/cognitive_security/`. A few load-bearing examples, by the question they answer:

- **`narrative_threat_assessment`** — given a spreading narrative, produces an evidence-bound threat assessment (captured claims and framing, target audience and levers, technique classification, provenance, estimated reach and harm) plus a prioritized list of defensive recommendations. Use it to brief a community, platform, or newsroom.
- **`prebunking_inoculation_design`** — given a manipulation technique likely to be deployed against an audience, designs an inoculation message or module with a warning, weakened-dose example, named refutation, call-to-action, and resistance-transfer test items.
- **`counter_messaging_strategy`** — given a falsehood already circulating, selects pre-bunk vs. de-bunk vs. narrative-replacement and designs a correction using the "truth sandwich," explicitly avoiding the amplification paradox (repeating a lie to refute it) and the backfire trap. It centers the accurate narrative and flags the *technique* rather than restating the false claim.
- **`audience_vulnerability_segmentation`** — partitions a population by susceptibility to specific manipulation vectors using psychological, behavioral, and information-environment variables (not demographic proxies), so defenders can route prebunking, media-literacy resources, and trusted-messenger programs to where they yield the most protection.
- **`epistemic_security_posture_review`** — assesses how an organization forms, updates, and protects its beliefs, scoring source diversity, analytic culture, feedback integrity, adversarial awareness, and training, then prioritizing remediation against the epistemic attack surfaces most likely to be exploited.
- **`resilience_metrics_design`** — operationalizes abstract resilience (source diversity, correction uptake, narrative elasticity, trust calibration) into a trackable indicator schema with measurement protocol and stated validity limitations, drawing on RAND, EDMO, and the NATO StratCom COE measurement guidance.

The remaining skills round out the lifecycle: detection (`logical_fallacy_detection`, `manipulation_technique_identification`, `propaganda_technique_classification`, `framing_and_priming_analysis`, `emotional_manipulation_analysis`, `astroturfing_detection`, `deepfake_synthetic_media_triage`, `disinformation_campaign_analysis`, `influence_operation_mapping`, `cognitive_attack_kill_chain`, `rumor_and_virality_assessment`), provenance and trust (`information_provenance_tracing`, `information_laundering_tracing`, `source_credibility_evaluation`, `trust_and_credibility_modeling`), terrain mapping (`attack_surface_of_belief_mapping`, `cognitive_bias_audit`), and capability-building (`media_literacy_assessment`).

## How CogSecSkills operationalizes this

Skills in this group convert these frameworks into repeatable agentic procedures: classifying a suspected operation against ABCDE / DISARM, detecting propaganda-technique signatures in a text corpus, mapping audience exposure, drafting technique-based prebunks, and defining resilience indicators. Each produces a **structured, source-grounded assessment for human analysts** — a threat document, a posture scorecard, an inoculation module, an indicator schema — rather than an autonomous judgment or an action taken without review. The deliverables are designed to compose: a `narrative_threat_assessment` feeds `prebunking_inoculation_design`, which is targeted by `audience_vulnerability_segmentation`, and the whole intervention is tracked over time by `resilience_metrics_design`.

## Defensive & ethical framing

Every skill here is for *recognition and resilience* — naming manipulation and inoculating audiences — never for producing persuasive or manipulative content. The asymmetry is deliberate and built in: a skill that classifies propaganda techniques will not author them; a skill that designs prebunks works only against a named technique, with the manipulation labeled in the open; counter-messaging centers truth and refuses to restate the lie for reach.

Use is accountable, transparent, and bounded by legal and ethical constraints, with human oversight at every decision point. The outputs are aids to human judgment under review, not substitutes for it — and nothing in this group should be read as a measure of operational effectiveness in the field. Claims are bounded to what the source material supports.

## Further study

- AGEINT curriculum — github.com/docxology/AGEINT, concept DOI 10.5281/zenodo.20732274.
- Sander van der Linden, *Foolproof: Why Misinformation Infects Our Minds and How to Build Immunity* (2023); William J. McGuire's foundational inoculation-theory papers (1960s); Banas & Rains (2010), meta-analysis of inoculation research.
- The DISARM Framework (disarmframework.com) — open-source disinformation TTP matrix.
- RAND, the EU Digital Media Observatory (EDMO), and the NATO Strategic Communications Centre of Excellence — information-environment resilience measurement methodologies underpinning `resilience_metrics_design`.
