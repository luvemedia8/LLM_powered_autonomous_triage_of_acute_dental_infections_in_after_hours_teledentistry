from __future__ import annotations

import re

from .schema import AssessmentRecord, TriageCase

AIRWAY_TERMS = (
    "stridor",
    "difficulty breathing",
    "cannot breathe",
    "tongue displacement",
    "bilateral floor",
    "drooling",
    "cannot swallow",
)
SPREAD_TERMS = (
    "spreading",
    "cellulitis",
    "submandibular",
    "neck swelling",
    "facial swelling",
    "trismus",
    "fever",
)
BLEED_TERMS = (
    "uncontrolled bleeding",
    "bleeding will not stop",
    "soaking gauze",
    "haemorrhage",
    "hemorrhage",
)
TRAUMA_TERMS = ("avulsion", "luxation", "fracture", "displaced tooth", "dental trauma")
VULNERABILITY_TERMS = (
    "chemotherapy",
    "neutropenia",
    "immunosuppressed",
    "hiv",
    "diabetes",
    "child",
    "pregnant",
)


def _present(text: str, terms: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(term for term in terms if term in text)


def _pain(text: str) -> int | None:
    matches = re.findall(r"(?:pain|severity)\s*(?:is|of|:)?\s*(\d{1,2})(?:\s*/\s*10)?", text)
    if not matches:
        return None
    value = int(matches[0])
    return min(10, max(0, value))


def structure_case(case: TriageCase) -> AssessmentRecord:
    text = " ".join(
        (case.narrative, *case.symptoms, *case.anatomical_locations, *case.comorbidities)
    ).casefold()
    temperature_evidence = ()
    if case.vitals.temperature_c is not None and case.vitals.temperature_c > 38.5:
        temperature_evidence = (f"fever over 38.5 temperature {case.vitals.temperature_c}",)
    evidence = tuple(
        part
        for part in (
            case.narrative,
            *case.symptoms,
            *case.anatomical_locations,
            *case.comorbidities,
            *temperature_evidence,
        )
        if part
    )
    return AssessmentRecord(
        case_id=case.case_id,
        pain_severity=_pain(text),
        duration_hours=case.duration_hours,
        locations=case.anatomical_locations,
        spread_indicators=_present(text, SPREAD_TERMS) + temperature_evidence,
        airway_indicators=_present(text, AIRWAY_TERMS),
        bleeding_indicators=_present(text, BLEED_TERMS),
        trauma_indicators=_present(text, TRAUMA_TERMS),
        vulnerability_indicators=_present(text, VULNERABILITY_TERMS),
        evidence=evidence,
    )
