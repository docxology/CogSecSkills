# Static evidence verification

This guide replays two synthetic museum-catalogue records through the repository's [source YAML reader](../src/cogsecskills/core/yaml_io.py). The test checks stable attribution and rejects ambiguous attribution before it reaches a consumer.

## Set up and run

Use Python 3.11 or newer and uv. From the repository root, install the locked development environment and run the isolated test module.

```sh
uv sync --locked --extra dev
uv run --no-sync pytest -q tests/core/test_static_evidence.py
```

The [test module](../tests/core/test_static_evidence.py) creates two UTF-8 YAML documents under pytest's temporary directory. The first returns the expected claim and source values on repeated reads. The second declares the source key twice and requires a `ValueError` identifying the file and the duplicated key. Pytest reports two passing tests.

The isolated test uses finite local files and the production YAML reader. Its result supports a narrow parser claim. Independent assessment of the material and field performance require separate evidence. See the [manuscript section](manuscript/08_static_evidence_verification.md) and the [claim boundaries](claim-boundaries.md).
