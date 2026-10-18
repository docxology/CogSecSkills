# What The Gates Prove

CogSecSkills uses local, deterministic gates. They are strong evidence for
source coherence and structural readiness, but they are not field validation.

## Proved Locally

| Gate | Proves |
|---|---|
| `definitions --check` | Canonical definitions and rendered skill files match. |
| `validate` | Registry, skill folders, workflows, closed verbs, and configured harness adapters conform. |
| `doctor` | Required quality fields, defensive boundaries, evidence discipline, uncertainty handling, and negative controls are present and specific enough for the current oracle. |
| `scenarios --check` | Curated safe-use and unsafe-redirect fixtures route to expected skills and include expected response-shape and expected-answer contracts. |
| `examples --check` | Source-owned worked examples cover all 100 skills and generated example docs/data are current. |
| `dashboard --check` | Generated quality dashboard matches the live registry, skills, scenarios, worked examples, quality capsules, and verified-state lines. |
| `manuscript-assets --check` | Generated supplements/data match the live library metadata; PNGs pass structural checks, are distinct, and the cover mirror matches its canonical bytes. The gate does not re-render or prove figure pixel/source equivalence. |
| `release-metadata --check` | Source metadata and generated release mirrors agree; stricter modes require clean git state and, for public-archive, a valid DOI declaration. It does not contact the archive or verify DOI/version/revision identity. |
| pytest and coverage | Runner behavior is covered by the checked regression suite. |

## Authored fixtures and routing limits

Scenario queries and expected routes are authored together. Passing those probes
is query-echo self-consistency: it checks regressions on that closed fixture set; it does not measure routing
accuracy on unseen or independently labeled requests. The default gate has no
held-out paraphrase benchmark. Separately authored name-free paraphrase and
distractor controls live in `tests/fixtures/routing_paraphrases.yaml`. They test
software retrieval behavior without skill names or full triggers, but remain
authored software controls, not independently labeled performance evidence. Answer keys are authored and unscored. Heading
and vocabulary-presence checks do not grade truth, uncertainty calibration, or
defensive judgment. Independent scoring requires a separately produced output,
review record, and provenance as described in `future-validation-protocols.md`.

## Not Proved

- A live model will select the same skill.
- A live harness will execute every tool correctly.
- A worked example is a live model transcript.
- An OSINT connector will return complete or lawful data.
- The skills improve analyst judgment in operational use.
- The manuscript is externally peer reviewed, archived, or publication-ready.

## Wording Rule

Use "locally validated", "structurally conforming", and "scenario-ready" for
passing gates. Do not use "field validated", "empirically effective", or
"runtime certified" unless a separate source-owned evaluation proves it.
