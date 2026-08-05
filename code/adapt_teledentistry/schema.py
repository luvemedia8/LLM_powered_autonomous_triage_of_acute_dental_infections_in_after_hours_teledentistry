from __future__ import annotations

from datetime import UTC, datetime
from enum import IntEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ADSILevel(IntEnum):
    ROUTINE = 1
    NON_URGENT = 2
    SEMI_URGENT = 3
    URGENT = 4
    EMERGENT = 5


class VitalSigns(BaseModel):
    model_config = ConfigDict(frozen=True)
    temperature_c: float | None = None
    heart_rate: int | None = None
    respiratory_rate: int | None = None
    oxygen_saturation: float | None = None


class TriageCase(BaseModel):
    model_config = ConfigDict(frozen=True)
    case_id: str
    narrative: str
    age_years: float | None = None
    symptoms: tuple[str, ...] = ()
    duration_hours: float | None = None
    anatomical_locations: tuple[str, ...] = ()
    medications: tuple[str, ...] = ()
    comorbidities: tuple[str, ...] = ()
    vitals: VitalSigns = Field(default_factory=VitalSigns)


class AssessmentRecord(BaseModel):
    model_config = ConfigDict(frozen=True)
    case_id: str
    pain_severity: int | None
    duration_hours: float | None
    locations: tuple[str, ...]
    spread_indicators: tuple[str, ...]
    airway_indicators: tuple[str, ...]
    bleeding_indicators: tuple[str, ...]
    trauma_indicators: tuple[str, ...]
    vulnerability_indicators: tuple[str, ...]
    evidence: tuple[str, ...]


class RetrievalItem(BaseModel):
    model_config = ConfigDict(frozen=True)
    source: str
    title: str
    passage: str
    score: float
    locator: str


class AgentOpinion(BaseModel):
    model_config = ConfigDict(frozen=True)
    agent: str
    model: str
    level: ADSILevel
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: tuple[str, ...]
    citations: tuple[str, ...] = ()
    safety_concern: bool = False
    non_overridable: bool = False


class PatientMessage(BaseModel):
    model_config = ConfigDict(frozen=True)
    urgency: str
    action: str
    precautions: tuple[str, ...]
    disclaimer: str


class AuditEvent(BaseModel):
    model_config = ConfigDict(frozen=True)
    event_id: str
    case_id: str
    agent: str
    event_type: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    input_digest: str
    output_digest: str
    model: str
    duration_ms: int
    token_count: int


class TriageDecision(BaseModel):
    model_config = ConfigDict(frozen=True)
    case_id: str
    level: ADSILevel
    confidence: float
    triage_opinion: AgentOpinion
    safety_opinion: AgentOpinion
    escalation_opinion: AgentOpinion | None
    message: PatientMessage
    disagreement: float
    safety_override: bool
    audit_events: tuple[AuditEvent, ...]
    status: Literal["complete", "deferred"]
