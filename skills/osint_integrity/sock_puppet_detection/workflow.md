# Workflow — Sock-Puppet Detection

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Collect account baseline data (read)
Gather all accessible account data: creation date, name/username change history, profile image, bio, posting history (volume, times, topics), follower/following counts and growth curve, and interaction patterns (what is retweeted, who is tagged). For each field, note whether it is present and plausible. Archive the data immediately — sock puppet accounts are often deleted after detection.

## Step 2 — Run cross-platform and image lookups (web)
Reverse-image search the profile picture for use on other platforms or in stock photo databases. Search usernames and display names across platforms. Check whether the account cross-posts to other platforms with different claimed identities. Look up the account in third-party follower-audit tools that surface bot-like follower ratios. Query any available coordinated-inauthentic-behavior databases (e.g., Stanford Internet Observatory takedown archives, DFRLab datasets).

## Step 3 — Apply indicator framework (reason)
Evaluate the account against the four indicator classes: (1) Behavioral — posting pace above human sustainable rates (>100 posts/day sustained), near-zero original content, single-topic monoculture; (2) Temporal — account created shortly before the narrative it promotes became prominent, activity concentrated in non-local hours for the claimed location; (3) Network — follower-to-following ratio consistent with purchased followers, follower acquisition in unnatural discrete batches, interaction cluster that overlaps with other suspected inauthentic accounts; (4) Identity and content — profile image identified as AI-generated or stock photo, biographic details internally inconsistent, language register inconsistent with claimed nationality or profession. Record each indicator as present, absent, or unknown.

## Step 4 — Synthesize verdict and disposition (reason, write)
Assess how many indicator classes are flagged and whether the pattern is better explained by inauthenticity or by plausible authentic behavior (e.g., a political activist posting intensely during a crisis). Consider alternative explanations: a lone real person who posts obsessively is different from a coordinated network even if surface indicators overlap. Assign a confidence tier. Write the inauthenticity report documenting each flagged indicator, alternative explanations considered, the confidence verdict, and a recommended disposition (flag for platform reporting, exclude from analysis, or continue monitoring).

## Evidence requirements
- For Sock-Puppet Detection, tie each indicator assessment, and inauthenticity report claim to concrete evidence from the specific account identifier, platform, and related accounts item, source excerpt, observation, or command result that supports it.
- For Sock-Puppet Detection, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the indicator assessment.
- Before recommending any Sock-Puppet Detection action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Sock-Puppet Detection: the indicator assessment is supported by multiple independent source records, custody notes, metadata, corroborating references, and contradiction logs; collect account baseline data and run cross-platform and image lookups checks agree, and no unresolved contradiction would change the result.
- Medium for Sock-Puppet Detection: the indicator assessment is plausible, but one important account identifier source, comparison case, or alternative explanation remains incomplete.
- Low for Sock-Puppet Detection: the indicator assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Sock-Puppet Detection cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Sock-Puppet Detection, use only authorized account identifier, platform, and related accounts, public or source-approved records, and caller-provided context needed for the defensive task.
- For Sock-Puppet Detection, minimize person-level detail in the indicator assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Sock-Puppet Detection, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Sock-Puppet Detection: treating account identifier as complete when collect account baseline data and run cross-platform and image lookups checks or contradictory evidence are missing.
- Sock-Puppet Detection: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Sock-Puppet Detection: reporting the indicator assessment without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Sock-Puppet Detection outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the indicator assessment from Sock-Puppet Detection into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Sock-Puppet Detection to verify supplied claims, media, sources, or datasets with documented public-source methods with account identifier, platform, and related accounts' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not label an account inauthentic from a single indicator — high posting volume, new account age, or a stock-looking profile photo each have innocent explanations in isolation
- do not conflate automation (bot) with inauthenticity (sock puppet) — a bot can post for an authentic person, and a sock puppet can post manually
- do not use this technique to suppress legitimate political speech — the standard is coordinated inauthentic behavior, not simply unpopular or adversarial viewpoints
- do not publish attribution to a specific operator without corroborating intelligence beyond behavioral OSINT — account signals support a hypothesis, not a definitive identification

## AGEINT upstream
`docs/ageint/osint-integrity.md`
