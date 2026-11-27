# Static Source-Record Verification {#sec:static_evidence_verification}

Structured evidence can become ambiguous before review begins. The repository's source YAML reader rejects duplicate mapping keys and reports the source file in its error. This preserves the ability to trace an ambiguous value back to its document. Keeping the source, transformation, and test together makes this narrow claim reproducible [@sandve2013reproducible].

A finite test uses two synthetic museum catalogue records. In the first, the loader retains a claim and its single named source on two reads. In the second, two `source` keys designate conflicting accession cards. The loader rejects the second record with a source-labelled error. These cases establish the reader's treatment of the specified inputs. A parsed claim still needs independent corroboration.

The test lives in `tests/core/test_static_evidence.py`. The files are produced under the test's temporary directory, and the results can be reproduced with `uv run --no-sync pytest -q tests/core/test_static_evidence.py` in the locked development environment. The replay exercises no skill workflow.
