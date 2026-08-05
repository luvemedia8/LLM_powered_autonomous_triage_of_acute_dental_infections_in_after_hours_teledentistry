from __future__ import annotations

from dataclasses import dataclass

from .schema import ADSILevel, AssessmentRecord


@dataclass(frozen=True)
class Criterion:
    code: str
    level: ADSILevel
    phrases: tuple[str, ...]
    non_overridable: bool
    source: str
    explanation: str


CRITERIA = (
    Criterion(
        "airway_stridor",
        ADSILevel.EMERGENT,
        ("stridor", "noisy breathing"),
        True,
        "ADSI",
        "Airway compromise requires immediate emergency referral",
    ),
    Criterion(
        "airway_tongue",
        ADSILevel.EMERGENT,
        ("tongue displacement", "tongue pushed"),
        True,
        "ADSI",
        "Tongue displacement can indicate deep space infection",
    ),
    Criterion(
        "floor_bilateral",
        ADSILevel.EMERGENT,
        ("bilateral floor of mouth", "both sides under tongue"),
        True,
        "ADSI",
        "Bilateral floor-of-mouth elevation is an emergent trigger",
    ),
    Criterion(
        "airway_dyspnea",
        ADSILevel.EMERGENT,
        ("difficulty breathing", "cannot breathe", "shortness of breath"),
        True,
        "ADSI",
        "Breathing difficulty requires emergency services",
    ),
    Criterion(
        "hemorrhage_uncontrolled",
        ADSILevel.EMERGENT,
        ("uncontrolled bleeding", "bleeding will not stop", "soaking gauze"),
        True,
        "ADSI",
        "Uncontrolled haemorrhage requires emergency referral",
    ),
    Criterion(
        "dysphagia_severe",
        ADSILevel.EMERGENT,
        ("cannot swallow", "drooling", "unable to swallow saliva"),
        True,
        "ADSI",
        "Severe dysphagia can indicate airway risk",
    ),
    Criterion(
        "cellulitis_spreading",
        ADSILevel.URGENT,
        ("spreading swelling", "facial cellulitis", "swelling spreading"),
        False,
        "ADSI",
        "Spreading cellulitis requires same-day evaluation",
    ),
    Criterion(
        "trismus_significant",
        ADSILevel.URGENT,
        ("trismus", "mouth opening under 20 mm", "cannot open mouth"),
        False,
        "ADSI",
        "Significant trismus requires same-day evaluation",
    ),
    Criterion(
        "fever_high",
        ADSILevel.URGENT,
        ("fever over 38.5", "high fever", "temperature 39"),
        False,
        "ADSI",
        "High fever with dental symptoms requires same-day evaluation",
    ),
    Criterion(
        "immunocompromised_infection",
        ADSILevel.URGENT,
        ("chemotherapy", "neutropenia", "immunosuppressed", "hiv"),
        False,
        "ADSI",
        "Host vulnerability lowers the escalation threshold",
    ),
    Criterion(
        "abscess_local",
        ADSILevel.SEMI_URGENT,
        ("localised abscess", "localized abscess", "periapical abscess"),
        False,
        "ADSI",
        "Localised abscess needs next-day assessment",
    ),
    Criterion(
        "pain_moderate",
        ADSILevel.SEMI_URGENT,
        ("moderate pain", "persistent toothache"),
        False,
        "ADSI",
        "Persistent controlled symptoms need next-day assessment",
    ),
    Criterion(
        "minor_progression_absent",
        ADSILevel.NON_URGENT,
        ("minor symptoms", "not getting worse", "mild sensitivity"),
        False,
        "ADSI",
        "Minor non-progressive symptoms can be seen within 72 hours",
    ),
    Criterion(
        "pulpitis_reversible",
        ADSILevel.ROUTINE,
        ("reversible pulpitis", "brief cold sensitivity"),
        False,
        "ADSI",
        "Routine dental follow-up is appropriate",
    ),
    Criterion(
        "preventive",
        ADSILevel.ROUTINE,
        ("preventive care", "checkup", "cleaning enquiry"),
        False,
        "ADSI",
        "Preventive questions use routine follow-up",
    ),
)


def matching_criteria(record: AssessmentRecord) -> tuple[Criterion, ...]:
    text = " ".join(record.evidence).casefold()
    return tuple(item for item in CRITERIA if any(phrase in text for phrase in item.phrases))


def rule_level(record: AssessmentRecord) -> ADSILevel:
    matched = matching_criteria(record)
    if record.airway_indicators or record.bleeding_indicators:
        return ADSILevel.EMERGENT
    if record.duration_hours is not None and record.duration_hours < 0:
        raise ValueError("duration_hours must be non-negative")
    if matched:
        return max(item.level for item in matched)
    return ADSILevel.NON_URGENT


def has_non_overridable_trigger(record: AssessmentRecord) -> bool:
    return any(item.non_overridable for item in matching_criteria(record))
