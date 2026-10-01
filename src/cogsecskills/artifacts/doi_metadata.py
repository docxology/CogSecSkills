"""Syntactic DOI declaration checks without asserting archive availability."""

from __future__ import annotations

import re


def normalize_doi(value: object) -> str:
    """Return a plausible declared DOI in bare form, or an empty string.

    DOI prefixes are normalized solely for consistent metadata display. This
    does not resolve the identifier or verify its registration or source version.
    """
    if not isinstance(value, str):
        return ""
    text = value.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if text.lower().startswith(prefix):
            text = text[len(prefix) :].strip()
            break
    return text if re.fullmatch(r"10\.\d{4,9}/\S+", text) else ""
