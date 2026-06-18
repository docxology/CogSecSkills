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

## Anti-criteria (must NOT happen)
- do not label an account inauthentic from a single indicator — high posting volume, new account age, or a stock-looking profile photo each have innocent explanations in isolation
- do not conflate automation (bot) with inauthenticity (sock puppet) — a bot can post for an authentic person, and a sock puppet can post manually
- do not use this technique to suppress legitimate political speech — the standard is coordinated inauthentic behavior, not simply unpopular or adversarial viewpoints
- do not publish attribution to a specific operator without corroborating intelligence beyond behavioral OSINT — account signals support a hypothesis, not a definitive identification

## AGEINT upstream
`docs/ageint/osint-integrity.md`
