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

## Evidence requirements
- For Trust & Credibility Modeling, tie each trust model, and exploitation vulnerability audit claim to concrete evidence from the specific information environment, actor set, and threat actor context item, source excerpt, observation, or command result that supports it.
- For Trust & Credibility Modeling, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the trust model.
- Before recommending any Trust & Credibility Modeling action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Trust & Credibility Modeling: the trust model is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; map the actor set and environment and establish credibility histories and threat precedents checks agree, and no unresolved contradiction would change the result.
- Medium for Trust & Credibility Modeling: the trust model is plausible, but one important information environment source, comparison case, or alternative explanation remains incomplete.
- Low for Trust & Credibility Modeling: the trust model rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Trust & Credibility Modeling cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Trust & Credibility Modeling, use only authorized information environment, actor set, and threat actor context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Trust & Credibility Modeling, minimize person-level detail in the trust model; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Trust & Credibility Modeling, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Trust & Credibility Modeling: treating information environment as complete when map the actor set and environment and establish credibility histories and threat precedents checks or contradictory evidence are missing.
- Trust & Credibility Modeling: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Trust & Credibility Modeling: reporting the trust model without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Trust & Credibility Modeling outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the trust model from Trust & Credibility Modeling into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Trust & Credibility Modeling to assess supplied material for manipulation indicators and recommend resilience measures with information environment, actor set, and threat actor context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate credibility with accuracy — high-credibility sources can disseminate false information and low-credibility sources can be accidentally correct; model them as distinct properties
- do not treat institutional affiliation as a reliable credibility proxy without independently verifying that affiliation is genuine and that the institution's credibility extends to the specific claim domain
- do not limit the model to formal source relationships — parasocial, peer-network, and algorithmic-recommendation trust pathways are often the primary exploitation vectors and must be included
- do not produce a static trust model without noting the conditions under which it would change — trust architecture shifts rapidly during crises, scandals, or coordinated attacks on anchor institutions
- do not recommend audience education alone as the primary hardening measure — literacy interventions are necessary but insufficient; structural fixes to credibility signals and platform architecture are required for durable protection

## AGEINT upstream
`docs/ageint/cognitive-security.md`
