# Workflow — Geolocation Verification

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract visual anchors (read)
Carefully examine the image for fixed geographic features: topography, road layout, building style, vehicle types, vegetation species, signage language, infrastructure (power lines, rail, waterways), and any partial text. Note shadow direction and angle if the sun is visible or implied. Record all candidate anchors before touching any map.

## Step 2 — Search reference data (web)
Query satellite imagery (Google Earth, Sentinel Hub, Maxar archive) and street-level sources (Google Street View, Mapillary, Yandex Maps) using the most distinctive anchors. Use a sun-angle calculator (SunCalc.org or equivalent) with the claimed date/time to derive expected shadow direction and length. Search for matching infrastructure or vegetation signatures.

## Step 3 — Triangulate and cross-check (reason)
Compare at least three independent features against reference data. Check whether terrain shape, built environment, and shadow direction are mutually consistent. If the claimed location matches on some features but not others, document the discrepancy. Assign a confidence tier: confirmed (three or more features match, none contradict), likely (two features match, no strong contradictions), inconclusive (features found but insufficient to fix a location), contradicted (at least one feature is physically incompatible with the claim).

## Step 4 — Produce assessment report (write)
Write a structured geolocation assessment stating the conclusion first, then listing each anchor feature, its reference source, and its match/mismatch result. Include the shadow-angle verdict, the confidence tier with rationale, and any alternative candidate locations that were considered and ruled out. Record methodology so a second analyst can reproduce it independently.

## Anti-criteria (must NOT happen)
- do not confirm a location from a single feature match — one landmark is spoofable; require at least three independent features
- do not start the search by looking at the claimed location first, as this anchors the analysis and biases feature selection toward confirmation
- do not treat metadata coordinates as ground truth — EXIF GPS is trivially spoofed and routinely stripped
- do not report a conclusion without documenting the specific reference sources used, making the result unreproducible

## AGEINT upstream
`docs/ageint/osint-integrity.md`
