from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from .ontology import rule_level
from .schema import ADSILevel, AssessmentRecord


class BaselineFamily(StrEnum):
    ZERO_SHOT = "single_llm_zero_shot"
    CHAIN_OF_THOUGHT = "single_llm_chain_of_thought"
    FEW_SHOT = "single_llm_few_shot"
    RAG = "single_llm_rag"
    MULTI_AGENT = "multi_agent"
    RULE_BASED = "rule_based"
    HUMAN = "human"


@dataclass(frozen=True)
class BaselineSpec:
    key: str
    family: BaselineFamily
    model: str | None
    temperature: float
    max_output_tokens: int


BASELINES = (
    BaselineSpec("gpt_4o", BaselineFamily.ZERO_SHOT, "gpt-4o", 0.0, 4096),
    BaselineSpec("claude_sonnet_4", BaselineFamily.ZERO_SHOT, "claude-sonnet-4", 0.0, 4096),
    BaselineSpec("deepseek_r1", BaselineFamily.ZERO_SHOT, "deepseek-r1", 0.0, 4096),
    BaselineSpec("gemini_2_5_pro", BaselineFamily.ZERO_SHOT, "gemini-2.5-pro", 0.0, 4096),
    BaselineSpec("llama_3_1_70b", BaselineFamily.ZERO_SHOT, "llama-3.1-70b", 0.0, 4096),
    BaselineSpec("gpt_4o_cot", BaselineFamily.CHAIN_OF_THOUGHT, "gpt-4o", 0.0, 4096),
    BaselineSpec(
        "claude_sonnet_4_cot", BaselineFamily.CHAIN_OF_THOUGHT, "claude-sonnet-4", 0.0, 4096
    ),
    BaselineSpec("deepseek_r1_cot", BaselineFamily.CHAIN_OF_THOUGHT, "deepseek-r1", 0.0, 4096),
    BaselineSpec("gpt_4o_few_shot", BaselineFamily.FEW_SHOT, "gpt-4o", 0.0, 4096),
    BaselineSpec("gpt_4o_rag", BaselineFamily.RAG, "gpt-4o", 0.0, 4096),
    BaselineSpec("mdagents", BaselineFamily.MULTI_AGENT, None, 0.0, 4096),
    BaselineSpec("generic_six_agent", BaselineFamily.MULTI_AGENT, None, 0.0, 4096),
    BaselineSpec("adsi_rule", BaselineFamily.RULE_BASED, None, 0.0, 0),
    BaselineSpec("esi_adapted", BaselineFamily.RULE_BASED, None, 0.0, 0),
    BaselineSpec("mts_adapted", BaselineFamily.RULE_BASED, None, 0.0, 0),
)


def adsi_rule_baseline(record: AssessmentRecord) -> ADSILevel:
    return rule_level(record)
