from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Protocol

import httpx


@dataclass(frozen=True)
class ModelRequest:
    model: str
    system: str
    user: str
    temperature: float
    max_output_tokens: int


@dataclass(frozen=True)
class ModelResponse:
    text: str
    input_tokens: int
    output_tokens: int
    model: str


class ModelProvider(Protocol):
    def complete(self, request: ModelRequest) -> ModelResponse: ...


class OpenAIProvider:
    def __init__(
        self, api_key: str | None = None, base_url: str = "https://api.openai.com/v1"
    ) -> None:
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY", "")
        self.base_url = base_url.rstrip("/")

    def complete(self, request: ModelRequest) -> ModelResponse:
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is required")
        payload = {
            "model": request.model,
            "temperature": request.temperature,
            "max_tokens": request.max_output_tokens,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": request.system},
                {"role": "user", "content": request.user},
            ],
        }
        response = httpx.post(
            f"{self.base_url}/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=payload,
            timeout=120.0,
        )
        response.raise_for_status()
        body = response.json()
        return ModelResponse(
            text=body["choices"][0]["message"]["content"],
            input_tokens=int(body.get("usage", {}).get("prompt_tokens", 0)),
            output_tokens=int(body.get("usage", {}).get("completion_tokens", 0)),
            model=str(body.get("model", request.model)),
        )


class AnthropicProvider:
    def __init__(
        self, api_key: str | None = None, base_url: str = "https://api.anthropic.com/v1"
    ) -> None:
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        self.base_url = base_url.rstrip("/")

    def complete(self, request: ModelRequest) -> ModelResponse:
        if not self.api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is required")
        payload = {
            "model": request.model,
            "temperature": request.temperature,
            "max_tokens": request.max_output_tokens,
            "system": request.system,
            "messages": [{"role": "user", "content": request.user}],
        }
        response = httpx.post(
            f"{self.base_url}/messages",
            headers={"x-api-key": self.api_key, "anthropic-version": "2023-06-01"},
            json=payload,
            timeout=120.0,
        )
        response.raise_for_status()
        body = response.json()
        text = "".join(
            block.get("text", "")
            for block in body.get("content", [])
            if block.get("type") == "text"
        )
        usage = body.get("usage", {})
        return ModelResponse(
            text=text,
            input_tokens=int(usage.get("input_tokens", 0)),
            output_tokens=int(usage.get("output_tokens", 0)),
            model=str(body.get("model", request.model)),
        )


class DeepSeekProvider(OpenAIProvider):
    def __init__(self, api_key: str | None = None) -> None:
        super().__init__(
            api_key or os.environ.get("DEEPSEEK_API_KEY", ""), "https://api.deepseek.com"
        )


def parse_object(text: str) -> dict[str, object]:
    value = json.loads(text)
    if not isinstance(value, dict):
        raise ValueError("model response must be a JSON object")
    return value
