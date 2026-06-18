# Workflow — Influence Operation Mapping

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory evidence and scope operation (read)
Read and catalog all available evidence. Note platforms covered, time range, content types, account count, and any prior platform or researcher findings. Define the operation boundary: what is in scope for this map vs. what is out of scope or requires further collection.

## Step 2 — Decompose Actors (reason)
Identify and cluster accounts by behavioral similarity: posting cadence, template use, network co-behavior, account age, follower patterns, and automation indicators. Distinguish likely principals (controllers), proxies (witting or unwitting amplifiers), and compromised/hijacked accounts. Note infrastructure overlaps: shared IP ranges, creation batch timing, cross-platform identifiers.

## Step 3 — Decompose Behaviors (reason)
Catalog coordinated inauthentic behaviors: coordinated amplification (synchronized sharing spikes), sock-puppet cross-promotion, astroturfing (manufacturing false consensus), brigading, platform manipulation (trending exploitation, mass reporting), and impersonation. For each behavior, note the frequency, scale, and evidence basis.

## Step 4 — Decompose Content and Distribution (search, reason)
Map the narrative themes, content formats, and seeding vs. amplification patterns. Trace how content moves: which accounts seed, which amplify, and where organic uptake begins. Search open sources and prior reporting to identify content re-use, translation pipelines, or borrowed narratives from known actors. Map platform pathways and cross-platform laundering sequences.

## Step 5 — Assess attribution and alternative hypotheses (reason)
Synthesize the ABCD map into an attribution assessment. Name the most plausible actor hypothesis and the key evidence supporting it. Explicitly state two or more alternative explanations and what evidence would favor or rule out each. Rate overall confidence (low: behavioral indicators only; medium: infrastructure + behavioral; high: infrastructure + behavioral + content fingerprint aligned to a known actor's prior campaigns).

## Step 6 — Produce map and defensive brief (write)
Write the ABCD operation map table. Write the attribution assessment with confidence tier and alternative hypotheses. Write the counter-operation brief: recommended platform reporting actions (with what evidence to include), public disclosure options with risk assessment, narrative counter-strategies matched to the operation's content themes, and monitoring indicators to detect if the operation continues or reconstitutes.

## Anti-criteria (must NOT happen)
- Do not attribute solely on the basis of content alignment with a known actor's known positions — many independent actors share narratives; attribution requires behavioral and infrastructure evidence
- Do not produce output structured as operational guidance for running influence operations; all output must be oriented toward detection, attribution, and defense
- Do not conflate amplification by real users with coordinated inauthentic behavior — distinguish organic uptake from coordinated promotion with explicit evidence
- Do not omit alternative attribution hypotheses; a single-hypothesis attribution assessment is not analytically defensible

## AGEINT upstream
`docs/ageint/cognitive-security.md`
