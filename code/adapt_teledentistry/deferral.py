from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]
IntArray = NDArray[np.int64]


@dataclass(frozen=True)
class DeferralPoint:
    threshold: float
    coverage: float
    error_rate: float
    undertriage_rate: float
    deferred: int


def selective_deferral(
    gold: IntArray, predicted: IntArray, disagreement: FloatArray, threshold: float
) -> DeferralPoint:
    selected = disagreement <= threshold
    deferred = int(np.sum(~selected))
    if not np.any(selected):
        return DeferralPoint(threshold, 0.0, 0.0, 0.0, deferred)
    error = float(np.mean(predicted[selected] != gold[selected]))
    high = selected & (gold >= 4)
    undertriage = float(np.mean(predicted[high] < gold[high])) if np.any(high) else 0.0
    return DeferralPoint(threshold, float(np.mean(selected)), error, undertriage, deferred)


def coverage_frontier(
    gold: IntArray, predicted: IntArray, disagreement: FloatArray, thresholds: FloatArray
) -> tuple[DeferralPoint, ...]:
    return tuple(
        selective_deferral(gold, predicted, disagreement, float(threshold))
        for threshold in thresholds
    )
