# The Information Environment

The information environment is the connected system of actors, content, platforms, and audiences through which information flows — and the structure of that system shapes which narratives spread, stall, or distort. A claim's fate is rarely decided by the claim itself; it is decided by who carries it, through which platform mechanics, to which audiences, at what tempo. Reading the environment structurally is the precondition for defending it.

This primer introduces the `information_environment` group: seven skills that turn that structural reading into repeatable, reviewable analysis. Each skill is summarized below and lives under [`skills/information_environment/`](../../skills/information_environment/).

- [Why it matters for cognitive security](#why-it-matters)
- [Core concepts](#core-concepts)
- [The skills in this group](#the-skills)
- [How a defender chains them together](#chaining)
- [Defensive and ethical framing](#ethics)
- [Further study](#further-study)

## Why it matters for cognitive security {#why-it-matters}

Manipulation rarely looks like a single false post; it looks like *patterns* — coordinated timing, synthetic amplification, and narratives engineered to exploit platform mechanics. A lone false claim is a content problem, addressable with a fact-check. A manufactured consensus is an *environmental* problem: the same false claim arrives from a hundred apparently-independent voices, in synchronized bursts, routed through the platform's recommendation engine into exactly the communities primed to believe it. No single post is the attack; the structure is.

Understanding the environment structurally lets a defender do three things a content-level view cannot:

1. **Distinguish organic discourse from manufactured consensus** — the difference between a thousand people who independently care about an issue and a small cluster operating a thousand accounts.
2. **Attribute amplification to behavior, not viewpoint** — separating *how* a narrative moved (coordination, automation, paid reach) from *what* it claims, so analysis stays defensible.
3. **Locate leverage points** — the bridges, super-spreaders, and platform affordances where a measured intervention (labeling, friction, prebunking, counter-narrative placement) actually changes outcomes, instead of fighting every individual post.

## Core concepts {#core-concepts}

- **Narrative ecosystems** — how framings, memes, and claims propagate and mutate across communities, who carries them, and how competing narratives contest the same events. A narrative is treated as a living entity competing for salience, not a static string.
- **Coordinated Inauthentic Behavior (CIB)** — the platform-defined signature of deceptive coordination (the *behavior*, not the viewpoint): synchronized posting, sockpuppet clusters, content reuse, and cross-platform seeding. The defining property is concealment of the organized nature of the activity.
- **Bot and automation detection** — behavioral, temporal, network, and linguistic signals (posting cadence, account-creation bursts, content duplication, follower-graph homogeneity) that indicate automation or amplification, always weighed against the false-positive risk from high-volume legitimate users.
- **Network analysis of information flow** — graph methods (centrality, betweenness, community detection, diffusion modeling) that classify nodes by structural role: seeds, amplifiers, bridges, gatekeepers, and sinks.
- **Platform affordances** — how design features (recommendation algorithms, resharing, reply structure, group/channel topology, anonymity, ad targeting, virality incentives) shape what spreads and create exploitable attack surfaces, including cross-feature interactions that amplify risk beyond any single feature.
- **Emergence and early warning** — detecting nascent narratives and inflection points (volume spikes, velocity shifts, topology changes) *before* they reach mainstream salience, while separating organic trend formation from coordinated emergence.

## The skills in this group {#the-skills}

Each skill converts one analytical lens into an agentic procedure that emits structured, confidence-rated evidence for human interpretation — never an autonomous verdict.

| Skill | What it does | Characteristic output |
| --- | --- | --- |
| [`coordinated_inauthentic_behavior_detection`](../../skills/information_environment/coordinated_inauthentic_behavior_detection/) | Finds groups of accounts acting in concert via temporal co-occurrence, content reuse, and network clustering | Account clusters, amplification multiplier, coordination typology, confidence rating |
| [`bot_and_automation_detection`](../../skills/information_environment/bot_and_automation_detection/) | Distinguishes automated from human activity using behavioral and temporal fingerprinting | Per-account classification table with rationale, inauthentic-amplification share, false-positive caveats |
| [`information_flow_network_analysis`](../../skills/information_environment/information_flow_network_analysis/) | Models the environment as a directed graph to find amplifiers, bridges, gatekeepers, and sinks | Structural propagation map, role classifications, velocity timeline, vulnerability assessment |
| [`narrative_ecosystem_mapping`](../../skills/information_environment/narrative_ecosystem_mapping/) | Inventories competing narratives, their carriers, amplification pathways, and target audiences | Labeled narrative inventory with carrier profiles, salience scores, ecosystem vulnerabilities |
| [`narrative_competition_analysis`](../../skills/information_environment/narrative_competition_analysis/) | Examines how rival narratives compete for attention, belief, and durability | Competing-narrative map, relative salience estimates, rhetorical analysis, narrative vulnerabilities |
| [`platform_affordance_risk_assessment`](../../skills/information_environment/platform_affordance_risk_assessment/) | Maps platform features to the manipulation vectors they enable | Affordance-to-vector mapping, prioritized risk matrix, mitigation recommendations |
| [`trend_and_emergence_monitoring`](../../skills/information_environment/trend_and_emergence_monitoring/) | Detects nascent narratives and inflection points before mainstream salience | Prioritized signal log with emergence-stage classification, authenticity assessment, escalation cues |

A useful distinction: **CIB detection** asks *are these accounts coordinating?* while **bot detection** asks *is this account automated?* — coordination can run on authentic-looking human accounts, and automation can be uncoordinated. Likewise, **narrative ecosystem mapping** inventories the whole field of carriers and audiences, while **narrative competition analysis** zooms into how two or more rival framings of the *same* event win or lose ground.

## How a defender chains them together {#chaining}

The skills compose into an early-warning-to-response cycle. A representative flow:

1. **Watch.** [`trend_and_emergence_monitoring`](../../skills/information_environment/trend_and_emergence_monitoring/) runs continuously and flags an unusual velocity spike on a hashtag ahead of a high-risk event, cueing deeper analysis.
2. **Authenticate the signal.** [`bot_and_automation_detection`](../../skills/information_environment/bot_and_automation_detection/) and [`coordinated_inauthentic_behavior_detection`](../../skills/information_environment/coordinated_inauthentic_behavior_detection/) assess whether the spike reflects organic interest or manufactured amplification, and estimate the inauthentic share.
3. **Map the structure.** [`information_flow_network_analysis`](../../skills/information_environment/information_flow_network_analysis/) reconstructs who spread what to whom in what order, naming the super-spreaders and cross-community bridges.
4. **Read the narratives.** [`narrative_ecosystem_mapping`](../../skills/information_environment/narrative_ecosystem_mapping/) and [`narrative_competition_analysis`](../../skills/information_environment/narrative_competition_analysis/) characterize the competing framings, their rhetorical appeals, and their factual or logical weaknesses.
5. **Understand the terrain.** [`platform_affordance_risk_assessment`](../../skills/information_environment/platform_affordance_risk_assessment/) explains which platform features made the spread possible and which design or policy mitigations would blunt a repeat.

The output of that chain is not an enforcement action — it is a structured environmental assessment that a human analyst, trust-and-safety team, journalist, or policymaker can act on, contest, or escalate.

## Defensive and ethical framing {#ethics}

Analysis focuses on *behavior and structure*, not the legitimacy of viewpoints — the goal is protecting the information commons, not policing opinion. Every skill in this group operates under the same boundary:

- **Behavior over belief.** The unit of analysis is coordination, automation, and propagation structure — never whether a position is one the analyst agrees with.
- **Evidence, not verdicts.** Detection outputs are confidence-rated hypotheses requiring human confirmation; an account flagged as likely automated or a cluster flagged as likely coordinated is a starting point for review, not a sentence.
- **False positives taken seriously.** High-volume legitimate users, passionate organic movements, and coincidental co-activity can all mimic manipulation signatures, so every assessment carries explicit caveats about that risk.
- **Bounded by law, terms, and privacy.** Work respects platform terms of service and individual privacy, and stays within legal and ethical constraints.

These analyses describe how manipulation works so it can be detected and resisted; they are not, and must not be repurposed as, a playbook for conducting it.

## Further study {#further-study}

- AGEINT curriculum — github.com/docxology/AGEINT, concept DOI 10.5281/zenodo.20732274.
- Kate Starbird et al., research on crisis informatics and coordinated manipulation (University of Washington CIP).
- Stanford Internet Observatory and EU DisinfoLab reports on coordinated inauthentic behavior.
- Affordance theory foundations (Gibson; Norman) as applied to sociotechnical platform analysis, underpinning [`platform_affordance_risk_assessment`](../../skills/information_environment/platform_affordance_risk_assessment/).
