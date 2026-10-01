"""Mechanical checks shared by reviewed scenario and offline answer fixtures.

Only answer sections supply response evidence. Source ids, provenance, request
text, rubric labels, and other metadata cannot satisfy an answer contract.
These checks establish answer shape and literal terms, not factual correctness.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol


class ResponseSection(Protocol):
    @property
    def title(self) -> str: ...

    @property
    def body(self) -> str: ...


def normalized_text(value: str) -> str:
    """Case-fold text and make line wrapping immaterial to literal checks."""
    return " ".join(value.split()).casefold()


def response_text(sections: Iterable[ResponseSection]) -> str:
    """Collect the actual answer headings and bodies, excluding metadata."""
    return normalized_text(
        " ".join(f"{section.title} {section.body}" for section in sections)
    )


def response_contract_findings(
    sections: Iterable[ResponseSection],
    *,
    required_sections: Iterable[str],
    must_include_terms: Iterable[str],
    must_exclude_terms: Iterable[str],
    label: str,
) -> list[str]:
    """Check required headings and literal include/exclude terms in an answer."""
    answer = tuple(sections)
    titles = {normalized_text(section.title) for section in answer}
    text = response_text(answer)
    findings = []
    for title in required_sections:
        if normalized_text(title) not in titles:
            findings.append(f"{label}: required response section {title!r} is missing")
    for term in must_include_terms:
        if normalized_text(term) not in text:
            findings.append(f"{label}: required response term {term!r} is missing")
    for term in must_exclude_terms:
        if normalized_text(term) in text:
            findings.append(f"{label}: excluded response term {term!r} is present")
    return findings
