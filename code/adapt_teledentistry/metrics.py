from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
from sklearn.metrics import cohen_kappa_score, roc_auc_score

FloatArray = NDArray[np.float64]
IntArray = NDArray[np.int64]


@dataclass(frozen=True)
class TriageMetrics:
    accuracy: float
    weighted_kappa: float
    macro_auc: float | None
    undertriage: float
    critical_miss: float
    overtriage: float


def accuracy(gold: IntArray, predicted: IntArray) -> float:
    if len(gold) == 0:
        raise ValueError("at least one observation is required")
    return float(np.mean(gold == predicted))


def weighted_kappa(gold: IntArray, predicted: IntArray) -> float:
    return float(cohen_kappa_score(gold, predicted, weights="linear"))


def undertriage_rate(gold: IntArray, predicted: IntArray) -> float:
    high = gold >= 4
    return float(np.mean(predicted[high] < gold[high])) if np.any(high) else 0.0


def critical_miss_rate(gold: IntArray, predicted: IntArray) -> float:
    critical = gold == 5
    return float(np.mean(predicted[critical] < 5)) if np.any(critical) else 0.0


def overtriage_rate(gold: IntArray, predicted: IntArray) -> float:
    return float(np.mean(predicted > gold))


def macro_auc(gold: IntArray, probabilities: FloatArray | None) -> float | None:
    if probabilities is None:
        return None
    return float(
        roc_auc_score(
            gold, probabilities, multi_class="ovr", average="macro", labels=np.arange(1, 6)
        )
    )


def evaluate(
    gold: IntArray, predicted: IntArray, probabilities: FloatArray | None = None
) -> TriageMetrics:
    if gold.shape != predicted.shape:
        raise ValueError("gold and predicted arrays must have identical shapes")
    return TriageMetrics(
        accuracy(gold, predicted),
        weighted_kappa(gold, predicted),
        macro_auc(gold, probabilities),
        undertriage_rate(gold, predicted),
        critical_miss_rate(gold, predicted),
        overtriage_rate(gold, predicted),
    )


def disagreement(levels: IntArray) -> float:
    if len(levels) == 0:
        raise ValueError("at least one agent level is required")
    counts = np.bincount(levels, minlength=6)[1:]
    return float(1.0 - counts.max() / len(levels))


def expected_calibration_error(confidence: FloatArray, correct: IntArray, bins: int = 10) -> float:
    boundaries = np.linspace(0.0, 1.0, bins + 1)
    total = 0.0
    for lower, upper in zip(boundaries[:-1], boundaries[1:], strict=True):
        selected = (confidence > lower) & (confidence <= upper)
        if np.any(selected):
            total += float(np.mean(selected)) * abs(
                float(np.mean(correct[selected])) - float(np.mean(confidence[selected]))
            )
    return total
