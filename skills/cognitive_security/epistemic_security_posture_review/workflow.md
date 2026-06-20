# Workflow — Epistemic Security Posture Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Map the epistemic architecture (read, ask)
Ingest available documentation of information-sourcing workflows, analytic processes, editorial or intelligence review chains, and dissent mechanisms. If documentation is sparse, ask targeted questions to key stakeholders covering: Where does the organization get its information? Who can challenge a dominant interpretation? How are errors or manipulation attempts reported and processed?

## Step 2 — Score posture dimensions (reason)
Evaluate the architecture against six epistemic security dimensions: (1) Source diversity — is there single-point dependency or adversarially captureable monoculture? (2) Analytic culture — are challenge and dissent institutionally licensed? (3) Feedback integrity — do wrong beliefs get corrected or self-reinforced? (4) Adversarial awareness — does the organization model who is trying to manipulate it and how? (5) Personnel training — do staff recognize manipulation techniques and know escalation paths? (6) Boundary management — how does information from outside the organization enter and get vetted? Rate each 1–5 and flag critical gaps.

## Step 3 — Identify and rank attack surfaces (reason)
From the dimension scores, enumerate exploitable attack surfaces. For each, describe: the specific structural weakness, the adversarial technique most likely to exploit it, the plausible downstream decision impact, and the detection difficulty. Rank surfaces by (adversarial incentive) x (exploitability) x (decision impact).

## Step 4 — Produce scorecard and roadmap (write)
Write the posture scorecard as a structured table. Write the attack surface narrative for the top-ranked vulnerabilities. Write the remediation roadmap: for each vulnerability, specify the structural fix, expected posture gain, implementation complexity (low/medium/high), and recommended owner. Sequence recommendations by urgency and dependency.

## Evidence requirements
- For Epistemic Security Posture Review, tie each posture scorecard, attack surface narrative, and remediation roadmap claim to concrete evidence from the specific organizational profile, epistemic practices, and known incidents item, source excerpt, observation, or command result that supports it.
- For Epistemic Security Posture Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the posture scorecard.
- Before recommending any Epistemic Security Posture Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Epistemic Security Posture Review: the posture scorecard is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; map the epistemic architecture and score posture dimensions checks agree, and no unresolved contradiction would change the result.
- Medium for Epistemic Security Posture Review: the posture scorecard is plausible, but one important organizational profile source, comparison case, or alternative explanation remains incomplete.
- Low for Epistemic Security Posture Review: the posture scorecard rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Epistemic Security Posture Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Epistemic Security Posture Review, use only authorized organizational profile, epistemic practices, and known incidents, public or source-approved records, and caller-provided context needed for the defensive task.
- For Epistemic Security Posture Review, minimize person-level detail in the posture scorecard; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Epistemic Security Posture Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Epistemic Security Posture Review: treating organizational profile as complete when map the epistemic architecture and score posture dimensions checks or contradictory evidence are missing.
- Epistemic Security Posture Review: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Epistemic Security Posture Review: reporting the posture scorecard without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Epistemic Security Posture Review outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the posture scorecard from Epistemic Security Posture Review into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Epistemic Security Posture Review to assess supplied material for manipulation indicators and recommend resilience measures with organizational profile, epistemic practices, and known incidents' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not reduce epistemic security to media literacy training for individuals — the review must assess structural and organizational factors
- Do not score dimensions without evidence; if information is unavailable, mark the gap explicitly rather than assuming baseline competence
- Do not produce a roadmap that only addresses the most visible problem — single-point fixes in complex epistemic systems often shift the attack surface rather than reducing it
- Do not conflate information security (CIA triad for data) with epistemic security — they overlap but the core threats and mitigations differ substantially

## AGEINT upstream
`docs/ageint/cognitive-security.md`
