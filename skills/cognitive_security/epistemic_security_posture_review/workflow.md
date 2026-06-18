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

## Anti-criteria (must NOT happen)
- Do not reduce epistemic security to media literacy training for individuals — the review must assess structural and organizational factors
- Do not score dimensions without evidence; if information is unavailable, mark the gap explicitly rather than assuming baseline competence
- Do not produce a roadmap that only addresses the most visible problem — single-point fixes in complex epistemic systems often shift the attack surface rather than reducing it
- Do not conflate information security (CIA triad for data) with epistemic security — they overlap but the core threats and mitigations differ substantially

## AGEINT upstream
`docs/ageint/cognitive-security.md`
