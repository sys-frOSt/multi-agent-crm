"""Lead scoring tool placeholder."""

from __future__ import annotations


def score_lead(signals: dict[str, int]) -> int:
    return max(sum(signals.values()), 0)
