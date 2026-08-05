from __future__ import annotations

import time
import uuid
from dataclasses import dataclass

from .agents import CommunicationAgent, EscalationAgent, SafetyAgent, TriageAgent
from .audit import AuditLedger, digest
from .intake import structure_case
from .schema import ADSILevel, AgentOpinion, AuditEvent, TriageCase, TriageDecision


@dataclass(frozen=True)
class PipelineAgents:
    triage: TriageAgent
    safety: SafetyAgent
    escalation: EscalationAgent
    communication: CommunicationAgent


class AdaptPipeline:
    def __init__(self, agents: PipelineAgents, ledger: AuditLedger | None = None) -> None:
        self.agents = agents
        self.ledger = ledger or AuditLedger()

    def _event(
        self,
        case_id: str,
        agent: str,
        event_type: str,
        source: object,
        result: object,
        model: str,
        started: float,
        tokens: int = 0,
    ) -> AuditEvent:
        event = AuditEvent(
            event_id=str(uuid.uuid4()),
            case_id=case_id,
            agent=agent,
            event_type=event_type,
            input_digest=digest(source),
            output_digest=digest(result),
            model=model,
            duration_ms=int((time.monotonic() - started) * 1000),
            token_count=tokens,
        )
        self.ledger.append(event)
        return event

    def run(self, case: TriageCase) -> TriageDecision:
        events: list[AuditEvent] = []
        started = time.monotonic()
        record = structure_case(case)
        events.append(
            self._event(
                case.case_id,
                "intake",
                "structured",
                case.model_dump(),
                record.model_dump(),
                "deterministic",
                started,
            )
        )
        started = time.monotonic()
        triage = self.agents.triage.assess(record)
        events.append(
            self._event(
                case.case_id,
                "triage",
                "classified",
                record.model_dump(),
                triage.model_dump(),
                triage.model,
                started,
            )
        )
        started = time.monotonic()
        safety = self.agents.safety.challenge(record, triage)
        events.append(
            self._event(
                case.case_id,
                "safety",
                "challenged",
                triage.model_dump(),
                safety.model_dump(),
                safety.model,
                started,
            )
        )
        escalation: AgentOpinion | None = None
        if safety.level != triage.level or safety.safety_concern:
            started = time.monotonic()
            escalation = self.agents.escalation.resolve(record, triage, safety)
            events.append(
                self._event(
                    case.case_id,
                    "escalation",
                    "resolved",
                    {"triage": triage.model_dump(), "safety": safety.model_dump()},
                    escalation.model_dump(),
                    escalation.model,
                    started,
                )
            )
        level = escalation.level if escalation is not None else triage.level
        if safety.safety_concern:
            level = max(
                level, min(ADSILevel.EMERGENT, ADSILevel(int(triage.level) + 1)), safety.level
            )
        if safety.non_overridable:
            level = max(level, safety.level)
        confidence = (
            escalation.confidence
            if escalation is not None
            else min(triage.confidence, safety.confidence)
        )
        opinions = (triage.level, safety.level) + ((escalation.level,) if escalation else ())
        modal_count = max(opinions.count(item) for item in set(opinions))
        disagreement = 1.0 - modal_count / len(opinions)
        message = self.agents.communication.compose(level)
        events.append(
            self._event(
                case.case_id,
                "communication",
                "composed",
                int(level),
                message.model_dump(),
                "deterministic",
                time.monotonic(),
            )
        )
        return TriageDecision(
            case_id=case.case_id,
            level=level,
            confidence=confidence,
            triage_opinion=triage,
            safety_opinion=safety,
            escalation_opinion=escalation,
            message=message,
            disagreement=disagreement,
            safety_override=level > triage.level,
            audit_events=tuple(events),
            status="complete",
        )
