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
- For Disinformation Campaign Analysis, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Disinformation Campaign Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Disinformation Campaign Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Disinformation Campaign Analysis: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Disinformation Campaign Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Disinformation Campaign Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Disinformation Campaign Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Disinformation Campaign Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Disinformation Campaign Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Disinformation Campaign Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Disinformation Campaign Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Disinformation Campaign Analysis failure: mistaking persuasive resonance for verified harm or intent.
- Disinformation Campaign Analysis failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Disinformation Campaign Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Disinformation Campaign Analysis to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Disinformation Campaign Analysis into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Disinformation Campaign Analysis to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not attribute a campaign to a specific state or actor without evidence rising to at least Moderate confidence — false attribution of influence operations is itself an information hazard
- do not conflate organic viral misinformation with coordinated inauthentic behavior — require explicit coordination signals before characterizing as a 'campaign'
- do not produce a narrative taxonomy that is simply a list of false claims — the model must identify the unifying master narrative frame and why these claims work together
- do not map TTPs in this analysis as a how-to guide — describe what was observed for defensive and counter-strategy purposes only
- do not omit the alternative-hypothesis section — acknowledging what could explain the observations without assuming coordination is essential to analytical integrity

## AGEINT upstream
`docs/ageint/cognitive-security.md`
