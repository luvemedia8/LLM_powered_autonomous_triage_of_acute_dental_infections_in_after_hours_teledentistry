from __future__ import annotations

import csv
import json
from collections.abc import Iterable
from pathlib import Path

from .schema import TriageCase, TriageDecision


def load_cases(path: Path) -> tuple[TriageCase, ...]:
    if path.suffix == ".jsonl":
        with path.open(encoding="utf-8") as stream:
            return tuple(TriageCase.model_validate_json(line) for line in stream if line.strip())
    if path.suffix == ".json":
        with path.open(encoding="utf-8") as stream:
            body = json.load(stream)
        return tuple(TriageCase.model_validate(item) for item in body)
    if path.suffix == ".csv":
        with path.open(encoding="utf-8", newline="") as stream:
            return tuple(TriageCase.model_validate(row) for row in csv.DictReader(stream))
    raise ValueError("supported case formats are jsonl, json, and csv")


def save_decisions(path: Path, decisions: Iterable[TriageDecision]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        for decision in decisions:
            stream.write(decision.model_dump_json() + "\n")
