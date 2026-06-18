# Workflow — Trust & Credibility Modeling

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Map the actor set and environment (read)
Read all available information about the information environment and its actors: who produces content, who intermediates it (editors, aggregators, influencers, algorithms), and who consumes it. Document observable credibility signals already in use — verification badges, institutional affiliations, track records, endorsement chains. Note which credibility signals are easily mimicked versus which require genuine institutional standing.

## Step 2 — Establish credibility histories and threat precedents (search)
Search for prior credibility assessments, fact-check records, and institutional track records for key actors. Look up known influence-operation tactics that have targeted similar information environments — which trust pathways have adversaries previously exploited, and with what success. Cross-reference actor affiliations against known front-organization patterns or credential-laundering networks.

## Step 3 — Build the trust model (reason)
Apply the three-component trust framework to each key actor: rate Competence (expertise signals, track record accuracy, domain authority), Benevolence (alignment of actor's interests with the audience's wellbeing), and Integrity (consistency between stated values and actions, transparency about methods and funding). Map trust-transfer pathways — which high-trust anchors are endorsing or being cited by which lower-trust actors, and in which direction credibility is flowing. Identify the heuristics the audience actually uses (as opposed to what they say they use) by examining what content achieves high engagement and what sources they repeatedly cite.

## Step 4 — Identify exploitation vectors (reason)
For each trust pathway in the model, identify the corresponding exploitation technique: (1) Credential mimicry — logos, titles, domain names that echo legitimate institutions; (2) Authority cascade — using one genuine citation to build a laundered credibility chain; (3) Parasocial trust manufacture — long-running engagement strategies that build felt relationship without reciprocal accountability; (4) Competence-benevolence split attacks — establishing competence through accurate early content, then exploiting accumulated credibility for false claims; (5) Integrity theater — performative transparency that signals honesty while concealing actual conflicts. Rate each vector by attack feasibility and potential impact.

## Step 5 — Audit vulnerabilities and write recommendations (reason, write)
Rank the identified trust vulnerabilities by combined criticality score (pathway centrality × exploitation feasibility × impact). Write the structured trust model document and exploitation vulnerability audit table. For each high-priority vulnerability, specify a concrete hardening measure — provenance labeling, cross-source triangulation requirements, transparency disclosures, or audience inoculation messaging. Note which hardening measures require institutional action versus which can be implemented by individual analysts or communicators. Explicitly bound the model's confidence and note actors or pathways where data was insufficient for reliable assessment.

## Anti-criteria (must NOT happen)
- do not conflate credibility with accuracy — high-credibility sources can disseminate false information and low-credibility sources can be accidentally correct; model them as distinct properties
- do not treat institutional affiliation as a reliable credibility proxy without independently verifying that affiliation is genuine and that the institution's credibility extends to the specific claim domain
- do not limit the model to formal source relationships — parasocial, peer-network, and algorithmic-recommendation trust pathways are often the primary exploitation vectors and must be included
- do not produce a static trust model without noting the conditions under which it would change — trust architecture shifts rapidly during crises, scandals, or coordinated attacks on anchor institutions
- do not recommend audience education alone as the primary hardening measure — literacy interventions are necessary but insufficient; structural fixes to credibility signals and platform architecture are required for durable protection

## AGEINT upstream
`docs/ageint/cognitive-security.md`
