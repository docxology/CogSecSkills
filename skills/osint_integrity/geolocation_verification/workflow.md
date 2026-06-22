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

## Evidence requirements
- For Geolocation Verification, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Geolocation Verification, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Geolocation Verification recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Geolocation Verification: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Geolocation Verification: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Geolocation Verification: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Geolocation Verification cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Geolocation Verification should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Geolocation Verification, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Geolocation Verification, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Geolocation Verification, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Geolocation Verification failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Geolocation Verification failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Geolocation Verification failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Geolocation Verification to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Geolocation Verification into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Geolocation Verification to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not confirm a location from a single feature match — one landmark is spoofable; require at least three independent features
- do not start the search by looking at the claimed location first, as this anchors the analysis and biases feature selection toward confirmation
- do not treat metadata coordinates as ground truth — EXIF GPS is trivially spoofed and routinely stripped
- do not report a conclusion without documenting the specific reference sources used, making the result unreproducible

## AGEINT upstream
`docs/ageint/osint-integrity.md`
