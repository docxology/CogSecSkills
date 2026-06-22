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
- For Geolocation Verification, bind the location fix and every anchor in the assessment to concrete evidence — the specific reference imagery showing the matched terrain, building, or sign, and the sun-angle computation for the claimed date and time — and document each source so a second analyst can reproduce the result, because an undocumented match is an unreproducible assertion, not verified geolocation.
- For Geolocation Verification, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the geolocation assessment.
- Before recommending any Geolocation Verification action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Geolocation Verification: at least three independent visual anchors such as terrain, infrastructure, and signage match authoritative reference imagery with none contradicting, the computed shadow angle is consistent with the claimed date and time, the search began landmark-agnostic rather than anchored to the claim, and no unresolved discrepancy would move the confidence tier.
- Medium for Geolocation Verification: the geolocation assessment is plausible, but one important image or video source, comparison case, or alternative explanation remains incomplete.
- Low for Geolocation Verification: the geolocation assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Geolocation Verification cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Geolocation Verification, use only authorized image or video, claimed location, and claimed date time, public or source-approved records, and caller-provided context needed for the defensive task.
- For Geolocation Verification, minimize person-level detail in the geolocation assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Geolocation Verification, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Geolocation Verification: confirming a location from a single spoofable landmark, anchoring the search to the claimed coordinates and selecting only confirming features, or treating EXIF GPS as ground truth, so the assessment reflects confirmation bias rather than convergent feature matching against reference data.
- Geolocation Verification: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Geolocation Verification: reporting the geolocation assessment without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Geolocation Verification outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the geolocation assessment from Geolocation Verification into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Geolocation Verification to verify supplied claims, media, sources, or datasets with documented public-source methods with image or video, claimed location, and claimed date time' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not confirm a location from a single feature match — one landmark is spoofable; require at least three independent features
- do not start the search by looking at the claimed location first, as this anchors the analysis and biases feature selection toward confirmation
- do not treat metadata coordinates as ground truth — EXIF GPS is trivially spoofed and routinely stripped
- do not report a conclusion without documenting the specific reference sources used, making the result unreproducible

## AGEINT upstream
`docs/ageint/osint-integrity.md`
