# Workflow — Cross-Impact Matrix

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish the driver set (read)
Read the input driver list and any background analysis. Confirm that the set is exhaustive for the focal question and not so large (>12) that the matrix becomes unworkable. Assign a short label to each driver.

## Step 2 — Fill the matrix cell by cell (reason)
For each ordered pair (driver i, driver j), assess: if driver i increases, what happens to driver j? Record the direction and magnitude using the agreed scale. Work row by row, treating each cell independently. Note conditional relationships explicitly (C) rather than forcing a sign.

## Step 3 — Identify feedback loops (reason)
Trace chains where the influence circles back to the originating driver. Flag reinforcing loops (all positive, or an even number of negatives) and balancing loops (odd number of negatives). Record each loop as an ordered list of drivers.

## Step 4 — Compute leverage rankings (reason, write)
Sum each driver's outgoing scores (active influence) and incoming scores (passive sensitivity). Rank drivers. Identify the top active drivers — interventions here cascade widely. Identify the top passive indicators — monitoring these reveals system state fastest.

## Step 5 — Synthesize findings (write)
Write the analytic narrative: which loops dominate under the focal scenario? Which leverage points should a decision-maker prioritize? What surprises does the matrix reveal relative to the initial intuition about the system?

## Anti-criteria (must NOT happen)
- do not conflate the influence of i on j with the influence of j on i — they are separate cells and need not be symmetric
- do not skip cells by assuming relationships are negligible without assessment — a zero score is a finding, not a default
- do not use the matrix to predict outcomes directly — it maps structure, not trajectories; scenario development is the next step

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
