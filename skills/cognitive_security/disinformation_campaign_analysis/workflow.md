# Workflow — Disinformation Campaign Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory and characterize artifacts (read)
Read all provided campaign artifacts. Build a structured inventory: content type, platform, account/channel identifier, timestamp, engagement signals, language/geography indicators, and thematic coding. Note any content that appears in multiple places with identical or slightly varied text (a signal of coordinated inauthentic behavior). Establish the campaign's observed timeline.

## Step 2 — Cross-reference with prior documentation (web, search)
Search OSINT databases (EUvsDisinfo, DFRLab, Stanford Internet Observatory reports), platform transparency reports, and academic literature for prior documentation of: these accounts/channels, these narratives, this infrastructure, or this actor fingerprint. Check DISARM framework for matching TTP patterns. Document whether this appears to be a new campaign or connected to a previously characterized operation.

## Step 3 — Reconstruct narrative architecture (reason)
Identify the master narrative: the central false or misleading frame that all observed content serves. Below it, map supporting sub-narratives that reinforce the master narrative from different angles or for different audience segments. Characterize each narrative's emotional register (fear, outrage, ridicule, false hope), its factual grounding (fabrication, decontextualization, selective emphasis, impersonation), and its apparent target audience.

## Step 4 — Model actor network and amplification structure (reason)
Map the observed actor network: identify seed accounts (first posters), amplifier accounts (retransmitters), and bridge accounts (that carry content across communities or platforms). Look for coordination signals: posting time clusters, text similarity beyond coincidence, cross-platform seeding. Characterize amplification infrastructure: automated behavior signals, coordinated inauthentic account networks, exploitation of algorithmic amplification mechanisms. Assess attribution: what can be said about who operates this network and with what confidence.

## Step 5 — Enumerate TTPs against DISARM or equivalent framework (reason)
Map each observed tactic and technique to a recognized TTP taxonomy, preferably DISARM. For each TTP: identify the technique (e.g. 'Create fake personas', 'Use hashtag hijacking', 'Cultivate useful idiots'), describe how it specifically manifests in this campaign, and note its diagnostic indicators. Assess which TTPs are most central to the campaign's design versus opportunistic.

## Step 6 — Synthesize campaign model and draft report (reason, write)
Integrate narrative architecture, actor network, TTP inventory, and amplification structure into a unified campaign model. Assess overall campaign objectives with confidence rating. Identify what the campaign is designed to do to its target audiences (polarize, confuse, suppress, delegitimize). Draft the campaign_analysis_report, narrative_taxonomy_table, and ttp_inventory_table. Explicitly state alternative hypotheses (could this be spontaneous rather than coordinated?) and what evidence would distinguish them.

## Step 7 — Emit final analysis with confidence labeling (write)
Output all three products. Every attribution claim must carry an explicit confidence label (Low/Moderate/High) and the specific evidence basis. Every inference must be distinguished from direct observation. Include a 'limitations' section noting what could not be assessed from available artifacts and what additional data would improve confidence.

## Evidence requirements
- For Disinformation Campaign Analysis, bind every narrative, TTP, and attribution claim to concrete evidence — collected artifacts, timing and content-synchronization signals, or prior OSINT reporting — keep direct observation distinct from inference and from rated attribution, and state what could not be assessed from the available artifacts.
- For Disinformation Campaign Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the campaign analysis report.
- Before recommending any Disinformation Campaign Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Disinformation Campaign Analysis: the campaign model's objectives, narrative hierarchy, actor network, and DISARM-aligned TTP inventory are each corroborated by artifacts and prior documentation, coordination signals distinguish the campaign from spontaneous virality, attribution carries an explicitly rated confidence with stated basis, and no unresolved contradiction would change the assessment.
- Medium for Disinformation Campaign Analysis: the campaign analysis report is plausible, but one important campaign artifacts source, comparison case, or alternative explanation remains incomplete.
- Low for Disinformation Campaign Analysis: the campaign analysis report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Disinformation Campaign Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Disinformation Campaign Analysis, use only authorized campaign artifacts, known context, and target audience indicators, public or source-approved records, and caller-provided context needed for the defensive task.
- For Disinformation Campaign Analysis, minimize person-level detail in the campaign analysis report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Disinformation Campaign Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Disinformation Campaign Analysis: asserting attribution to a state or actor below moderate confidence, characterizing spontaneous viral misinformation as a coordinated campaign without coordination signals, or omitting the alternative-hypothesis section, so the model itself becomes an information hazard rather than a defensible characterization.
- Disinformation Campaign Analysis: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Disinformation Campaign Analysis: reporting the campaign analysis report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Disinformation Campaign Analysis outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the campaign analysis report from Disinformation Campaign Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Disinformation Campaign Analysis to assess supplied material for manipulation indicators and recommend resilience measures with campaign artifacts, known context, and target audience indicators' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not attribute a campaign to a specific state or actor without evidence rising to at least Moderate confidence — false attribution of influence operations is itself an information hazard
- do not conflate organic viral misinformation with coordinated inauthentic behavior — require explicit coordination signals before characterizing as a 'campaign'
- do not produce a narrative taxonomy that is simply a list of false claims — the model must identify the unifying master narrative frame and why these claims work together
- do not map TTPs in this analysis as a how-to guide — describe what was observed for defensive and counter-strategy purposes only
- do not omit the alternative-hypothesis section — acknowledging what could explain the observations without assuming coordination is essential to analytical integrity

## AGEINT upstream
`docs/ageint/cognitive-security.md`
