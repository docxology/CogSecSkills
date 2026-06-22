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
- For Epistemic Security Posture Review, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Epistemic Security Posture Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Epistemic Security Posture Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Epistemic Security Posture Review: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Epistemic Security Posture Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Epistemic Security Posture Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Epistemic Security Posture Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Epistemic Security Posture Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Epistemic Security Posture Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Epistemic Security Posture Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Epistemic Security Posture Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Epistemic Security Posture Review failure: mistaking persuasive resonance for verified harm or intent.
- Epistemic Security Posture Review failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Epistemic Security Posture Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Epistemic Security Posture Review to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Epistemic Security Posture Review into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Epistemic Security Posture Review to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not reduce epistemic security to media literacy training for individuals — the review must assess structural and organizational factors
- Do not score dimensions without evidence; if information is unavailable, mark the gap explicitly rather than assuming baseline competence
- Do not produce a roadmap that only addresses the most visible problem — single-point fixes in complex epistemic systems often shift the attack surface rather than reducing it
- Do not conflate information security (CIA triad for data) with epistemic security — they overlap but the core threats and mitigations differ substantially

## AGEINT upstream
`docs/ageint/cognitive-security.md`
