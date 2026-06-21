# Wave 1 External Release And Reproducibility Digest

Worker: `019ee6d0-1dc1-7f01-937d-8dcbb87e72e5`

Key source-backed findings:
- `CITATION.cff` is appropriate repository-level citation metadata, but it is not a complete provenance system.
- CodeMeta supports discovery, citation, and interoperability, not proof of reproducibility or field validation.
- GitHub releases are tag-based; Zenodo archives GitHub releases and can mint a DOI only after the real release path exists.
- Zenodo may prefer `.zenodo.json` over `CITATION.cff` if both exist for its record metadata.
- FAIR4RS is aspirational and supports transparency/reuse wording, but should not be converted into a binary "FAIR compliant" claim.
- Reproducible-builds has a strict bit-for-bit artifact definition; CogSecSkills should use narrower wording unless bit-for-bit rebuilds are verified.

Planning implications:
- Add a release-claim matrix: safe to claim, needs evidence, and do not claim.
- Add metadata consistency checks across `CITATION.cff`, `codemeta.json`, package version, Git tag, manuscript release manifest, and generated outputs.
- Leave DOI/public-release fields unavailable until a real archive exists.
- Add optional rebuild verification only if the project wants stronger reproducibility claims than deterministic source generation.

Worker EXPAND:
- Verify whether CogSecSkills already has `CITATION.cff`, `codemeta.json`, and a Zenodo-linked GitHub release path, then tighten public claim language to the exact metadata present.
- Produce a release-claim matrix mapped to repo surfaces that must exist.

## EXPAND
- LEAD: Release-claim matrix — WHY: release wording must track exact repo metadata and archive state — ANGLE: plan generated/checkable `docs/release-claim-matrix.md`.
- LEAD: Metadata consistency checker — WHY: CFF/CodeMeta/version/tag/manuscript manifest can drift — ANGLE: plan a local `release-metadata --check` command.

