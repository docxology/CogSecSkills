# Wave 1 Manuscript, Figures, And Render Contract Digest

Sources:
- Parallel manuscript/render researcher result.
- Direct string audit of figure inventory references in `src/cogsecskills/manuscript_assets.py`, manuscript tests, generated supplements, and docs.
- Prior local gate baseline recorded in `verify-local-gates.md`.

Key findings:
- The manuscript and render surfaces are currently green, including eight generated figures, generated supplements, markdown validation, and PDF render.
- Figure inventory is repeated in code, generated supplement text, and tests. This is workable now but fragile: the next implementation should centralize figure metadata so names, captions, semantic expectations, and tests share one source.
- Figure tests currently emphasize existence and dimensions. The next useful contract is semantic: each generated figure should contain the intended title/key annotations at the source metadata layer, and manuscript captions should name what the figure supports and what it does not prove.
- The cover figure is treated specially: `output/figures/` is the authoritative generated figure directory and `figures/` mirrors the cover image for the manuscript title-page slot. Documentation should keep that split explicit.
- The manuscript has a release manifest and claim-boundary language, but a more machine-scannable claim provenance and figure map would make local evidence status easier to audit.

Expansion markers:
- LEAD: Central figure metadata registry for filename, label, title, caption, semantic checks, and output path.
- LEAD: Generated claim-provenance map linking local gates, generated surfaces, bibliography, and deferred claims.
- LEAD: Keep PDF/render checks in the sibling template checkout, but keep source ownership in the CogSecSkills repo.

## EXPAND
- LEAD: Figure inventory centralization - WHY: duplicated lists drift silently - ANGLE: one metadata list consumed by generator, docs, and tests.
- LEAD: Claim provenance map - WHY: manuscript defensibility depends on evidence boundaries - ANGLE: generated table with local, bibliographic, future, and unsupported status.
