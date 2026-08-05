from __future__ import annotations

import random
import re

from .schema import TriageCase

COLLOQUIAL = {
    "bilateral floor-of-mouth swelling": "my mouth is really swollen on both sides",
    "dysphagia": "hard to swallow",
    "trismus": "cannot open my mouth much",
    "odontogenic": "coming from a tooth",
}


def typographical_errors(case: TriageCase, rate: float = 0.05, seed: int = 42) -> TriageCase:
    generator = random.Random(seed)
    letters = "abcdefghijklmnopqrstuvwxyz"
    narrative = "".join(
        generator.choice(letters)
        if character.isalpha() and generator.random() < rate
        else character
        for character in case.narrative
    )
    return case.model_copy(update={"narrative": narrative})


def vague_language(case: TriageCase) -> TriageCase:
    narrative = case.narrative
    for clinical, colloquial in COLLOQUIAL.items():
        narrative = re.sub(re.escape(clinical), colloquial, narrative, flags=re.IGNORECASE)
    return case.model_copy(update={"narrative": narrative})


def incomplete_history(case: TriageCase, removal_rate: float = 0.3, seed: int = 42) -> TriageCase:
    generator = random.Random(seed)
    comorbidities = tuple(item for item in case.comorbidities if generator.random() >= removal_rate)
    medications = tuple(item for item in case.medications if generator.random() >= removal_rate)
    return case.model_copy(update={"comorbidities": comorbidities, "medications": medications})


def non_english_fragments(case: TriageCase, language: str = "es") -> TriageCase:
    fragment = (
        "También tengo hinchazón y dolor."
        if language == "es"
        else "wo de lian zhong le, ye hen tong."
    )
    return case.model_copy(update={"narrative": f"{case.narrative} {fragment}"})
