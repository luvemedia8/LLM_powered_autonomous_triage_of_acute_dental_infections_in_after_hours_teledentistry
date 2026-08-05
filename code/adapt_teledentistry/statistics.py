from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
from scipy.stats import chi2

FloatArray = NDArray[np.float64]
IntArray = NDArray[np.int64]


@dataclass(frozen=True)
class Interval:
    estimate: float
    lower: float
    upper: float
    standard_error: float


@dataclass(frozen=True)
class McNemarResult:
    statistic: float
    p_value: float
    discordant_a: int
    discordant_b: int


def stratified_bootstrap(
    values: FloatArray,
    strata: IntArray,
    iterations: int = 10000,
    seed: int = 42,
    alpha: float = 0.05,
) -> Interval:
    if values.shape != strata.shape:
        raise ValueError("values and strata must have identical shapes")
    generator = np.random.default_rng(seed)
    groups = tuple(np.flatnonzero(strata == group) for group in np.unique(strata))
    estimates = np.empty(iterations, dtype=np.float64)
    for index in range(iterations):
        sampled = np.concatenate(
            tuple(generator.choice(group, len(group), replace=True) for group in groups)
        )
        estimates[index] = np.mean(values[sampled])
    return Interval(
        float(np.mean(values)),
        float(np.quantile(estimates, alpha / 2)),
        float(np.quantile(estimates, 1 - alpha / 2)),
        float(np.std(estimates, ddof=1)),
    )


def mcnemar(
    gold: IntArray, first: IntArray, second: IntArray, continuity: bool = True
) -> McNemarResult:
    first_correct = first == gold
    second_correct = second == gold
    a = int(np.sum(first_correct & ~second_correct))
    b = int(np.sum(~first_correct & second_correct))
    denominator = a + b
    if denominator == 0:
        return McNemarResult(0.0, 1.0, a, b)
    adjustment = 1 if continuity else 0
    statistic = (abs(a - b) - adjustment) ** 2 / denominator
    return McNemarResult(float(statistic), float(chi2.sf(statistic, 1)), a, b)


def holm(p_values: FloatArray, alpha: float = 0.05) -> tuple[FloatArray, NDArray[np.bool_]]:
    order = np.argsort(p_values)
    adjusted = np.empty_like(p_values)
    running = 0.0
    count = len(p_values)
    for rank, original in enumerate(order):
        running = max(running, float(p_values[original]) * (count - rank))
        adjusted[original] = min(1.0, running)
    return adjusted, adjusted < alpha


def cohens_h(first: float, second: float) -> float:
    return float(2 * np.arcsin(np.sqrt(first)) - 2 * np.arcsin(np.sqrt(second)))
