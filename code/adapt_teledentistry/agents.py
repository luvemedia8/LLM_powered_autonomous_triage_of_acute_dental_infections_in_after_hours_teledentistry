from __future__ import annotations

import json
from dataclasses import dataclass

from .ontology import has_non_overridable_trigger, rule_level
from .providers import ModelProvider, ModelRequest, parse_object
from .retrieval import LexicalIndex
from .schema import ADSILevel, AgentOpinion, AssessmentRecord, PatientMessage


@dataclass(frozen=True)
class AgentSettings:
    model: str
    temperature: float = 0.0
    max_output_tokens: int = 4096


def _level(value: object) -> ADSILevel:
    level = int(value)
    if level < 1 or level > 5:
        raise ValueError("ADSI level must be between 1 and 5")
    return ADSILevel(level)


def _confidence(value: object) -> float:
    return min(1.0, max(0.0, float(value)))


class TriageAgent:
    def __init__(
        self, provider: ModelProvider, index: LexicalIndex, settings: AgentSettings
    ) -> None:
        self.provider = provider
        self.index = index
        self.settings = settings

    def assess(self, record: AssessmentRecord) -> AgentOpinion:
        query = " ".join(record.evidence)
        context = self.index.search(query)
        system = (
            "Classify the structured dental emergency record into ADSI level 1 through 5. "
            "Return JSON with level, confidence, and rationale as an array. Use only the "
            "structured record and retrieved criteria."
        )
        user = json.dumps(
            {
                "record": record.model_dump(mode="json"),
                "guidelines": [item.model_dump(mode="json") for item in context],
            }
        )
        response = self.provider.complete(
            ModelRequest(
                self.settings.model,
                system,
                user,
                self.settings.temperature,
                self.settings.max_output_tokens,
            )
        )
        body = parse_object(response.text)
        rationale = tuple(str(item) for item in body.get("rationale", []))
        return AgentOpinion(
            agent="triage",
            model=response.model,
            level=_level(body["level"]),
            confidence=_confidence(body.get("confidence", 0.5)),
            rationale=rationale,
            citations=tuple(item.locator for item in context),
        )


class SafetyAgent:
    def __init__(
        self,
        provider: ModelProvider,
        index: LexicalIndex,
        settings: AgentSettings,
        escalation_threshold: float = 0.3,
    ) -> None:
        self.provider = provider
        self.index = index
        self.settings = settings
        self.escalation_threshold = escalation_threshold

    def challenge(self, record: AssessmentRecord, triage: AgentOpinion) -> AgentOpinion:
        query = "red flags airway haemorrhage infection " + " ".join(record.evidence)
        context = self.index.search(query)
        system = (
            "Independently inspect the structured dental record for undertriage. Return JSON "
            "with level, confidence, safety_concern, non_overridable, and rationale. Any credible "
            "concern at or above the escalation threshold is a safety concern."
        )
        user = json.dumps(
            {
                "record": record.model_dump(mode="json"),
                "proposed_level": int(triage.level),
                "threshold": self.escalation_threshold,
                "red_flag_guidance": [item.model_dump(mode="json") for item in context],
            }
        )
        response = self.provider.complete(
            ModelRequest(
                self.settings.model,
                system,
                user,
                self.settings.temperature,
                self.settings.max_output_tokens,
            )
        )
        body = parse_object(response.text)
        candidate = _level(body.get("level", int(triage.level)))
        confidence = _confidence(body.get("confidence", 0.5))
        rule_candidate = rule_level(record)
        non_overridable = has_non_overridable_trigger(record)
        candidate = max(candidate, rule_candidate) if non_overridable else candidate
        concern = (
            bool(body.get("safety_concern", False))
            or non_overridable
            or (candidate > triage.level and confidence >= self.escalation_threshold)
        )
        return AgentOpinion(
            agent="safety",
            model=response.model,
            level=candidate,
            confidence=confidence,
            rationale=tuple(str(item) for item in body.get("rationale", [])),
            citations=tuple(item.locator for item in context),
            safety_concern=concern,
            non_overridable=non_overridable,
        )


class EscalationAgent:
    def __init__(self, provider: ModelProvider, settings: AgentSettings) -> None:
        self.provider = provider
        self.settings = settings

    def resolve(
        self, record: AssessmentRecord, triage: AgentOpinion, safety: AgentOpinion
    ) -> AgentOpinion:
        system = (
            "Resolve a dental triage disagreement. Default to the safer higher ADSI level when "
            "evidence remains ambiguous. A non-overridable red flag cannot be reduced. Return "
            "JSON with level, confidence, and rationale."
        )
        user = json.dumps(
            {
                "record": record.model_dump(mode="json"),
                "triage": triage.model_dump(mode="json"),
                "safety": safety.model_dump(mode="json"),
            }
        )
        response = self.provider.complete(
            ModelRequest(
                self.settings.model,
                system,
                user,
                self.settings.temperature,
                self.settings.max_output_tokens,
            )
        )
        body = parse_object(response.text)
        candidate = _level(body.get("level", max(triage.level, safety.level)))
        if safety.non_overridable:
            candidate = max(candidate, safety.level)
        if candidate < triage.level and candidate != safety.level:
            candidate = max(triage.level, safety.level)
        return AgentOpinion(
            agent="escalation",
            model=response.model,
            level=candidate,
            confidence=_confidence(body.get("confidence", 0.5)),
            rationale=tuple(str(item) for item in body.get("rationale", [])),
            safety_concern=safety.safety_concern,
            non_overridable=safety.non_overridable,
        )


class CommunicationAgent:
    ACTIONS = {
        1: ("Routine follow-up", "Arrange standard dental follow-up."),
        2: ("Within 72 hours", "Arrange a dental evaluation within 72 hours."),
        3: ("Next day", "Arrange a dental appointment by the next day."),
        4: ("Same day", "Seek same-day emergency dental evaluation."),
        5: (
            "Immediate emergency care",
            "Contact emergency services or attend an emergency department now.",
        ),
    }

    def compose(self, level: ADSILevel) -> PatientMessage:
        urgency, action = self.ACTIONS[int(level)]
        precautions = (
            "Seek urgent help if breathing or swallowing becomes difficult.",
            "Seek urgent help for rapidly spreading swelling or bleeding that does not stop.",
        )
        return PatientMessage(
            urgency=urgency,
            action=action,
            precautions=precautions,
            disclaimer="This triage result does not replace an in-person clinical examination.",
        )
