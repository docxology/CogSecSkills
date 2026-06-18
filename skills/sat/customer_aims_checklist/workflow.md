# Workflow — Customer (AIMS) Checklist

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest tasking and draft (read)
Read the tasking directive, the draft or outline, and any available consumer context. Note the stated purpose, the stated audience, and any explicit or implicit constraints on scope.

## Step 2 — Resolve AIMS parameters (ask, reason)
For each of the four parameters, determine whether it is explicitly stated, inferrable from context, or genuinely unknown. For unknown parameters, generate targeted clarifying questions. For inferrable ones, state the inferred value and the basis for the inference.

## Step 3 — Assess alignment between draft and AIMS (reason)
Compare the draft's actual structure, lead, and conclusions against the resolved AIMS parameters. Does the lead sentence state the Message? Does the logical flow match the Storyline? Is technical depth appropriate for the Audience? Is the Issue actually answered?

## Step 4 — Produce worksheet and revision recommendations (write)
Fill the AIMS worksheet with the four resolved parameters. Write specific, actionable revision recommendations for every misalignment found, citing the paragraph or section that needs revision and explaining why it fails the relevant parameter.

## Anti-criteria (must NOT happen)
- do not allow the Message field to be a topic sentence ('this paper discusses X') — it must be an assertive conclusion ('we assess X because Y')
- do not conflate the Issue (the precise question) with the Audience's broader area of responsibility
- do not skip the Storyline parameter — 'accurate analysis in the wrong order' is a common and costly failure mode

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
