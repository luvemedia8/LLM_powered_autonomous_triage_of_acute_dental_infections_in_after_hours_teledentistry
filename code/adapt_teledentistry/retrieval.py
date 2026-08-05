from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass

from .schema import RetrievalItem


@dataclass(frozen=True)
class GuidelineDocument:
    source: str
    title: str
    locator: str
    text: str


class LexicalIndex:
    def __init__(self, documents: tuple[GuidelineDocument, ...]) -> None:
        self.documents = documents
        self.tokens = tuple(self._tokenize(item.text) for item in documents)
        self.frequency = Counter(token for document in self.tokens for token in set(document))

    @staticmethod
    def _tokenize(text: str) -> tuple[str, ...]:
        return tuple(re.findall(r"[a-z0-9]+", text.casefold()))

    def _idf(self, token: str) -> float:
        return math.log((1 + len(self.documents)) / (1 + self.frequency[token])) + 1.0

    def _score(self, query: tuple[str, ...], document: tuple[str, ...]) -> float:
        if not query or not document:
            return 0.0
        counts = Counter(document)
        numerator = sum(counts[token] * self._idf(token) for token in set(query))
        denominator = math.sqrt(sum(value * value for value in counts.values()))
        return numerator / denominator if denominator else 0.0

    def search(self, query: str, limit: int = 5) -> tuple[RetrievalItem, ...]:
        query_tokens = self._tokenize(query)
        ranked = sorted(
            (
                (self._score(query_tokens, tokens), document)
                for tokens, document in zip(self.tokens, self.documents, strict=True)
            ),
            key=lambda item: item[0],
            reverse=True,
        )
        return tuple(
            RetrievalItem(
                source=document.source,
                title=document.title,
                passage=document.text,
                score=score,
                locator=document.locator,
            )
            for score, document in ranked[:limit]
            if score > 0
        )


def default_documents() -> tuple[GuidelineDocument, ...]:
    return (
        GuidelineDocument(
            "ADSI",
            "Emergent criteria",
            "Methods: ADSI",
            "Immediate emergency referral for airway compromise, bilateral floor-of-mouth "
            "elevation, stridor, tongue displacement, or uncontrolled haemorrhage.",
        ),
        GuidelineDocument(
            "ADSI",
            "Urgent criteria",
            "Methods: ADSI",
            "Same-day dental evaluation for spreading odontogenic cellulitis, significant "
            "trismus under 20 millimetres, or fever above 38.5 degrees Celsius.",
        ),
        GuidelineDocument(
            "ADSI",
            "Semi-urgent criteria",
            "Methods: ADSI",
            "Next-day evaluation for localised periapical abscess with moderate pain and "
            "controlled symptoms.",
        ),
        GuidelineDocument(
            "ADSI",
            "Non-urgent criteria",
            "Methods: ADSI",
            "Scheduled evaluation within 72 hours for minor symptoms without progression.",
        ),
        GuidelineDocument(
            "ADSI",
            "Routine criteria",
            "Methods: ADSI",
            "Standard follow-up for reversible pulpitis, minor trauma without displacement, "
            "and preventive care enquiries.",
        ),
    )
