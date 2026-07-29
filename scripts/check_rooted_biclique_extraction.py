#!/usr/bin/env python3
"""Exact audits for PP3byc--PP3bye."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from math import comb, ceil, floor, log2
from pathlib import Path


def nonempty_subsets(items: list[str]):
    for size in range(1, len(items) + 1):
        yield from combinations(items, size)


def main() -> None:
    path = Path("experiments/direct-clean-target-hub-example.json")
    data = json.loads(path.read_text())
    neighbourhoods = {
        source: set(targets) for source, targets in data["neighbourhoods"].items()
    }
    sources = sorted(neighbourhoods)
    weights = {source: Fraction(index + 1, 3) for index, source in enumerate(sources)}

    fan_families_checked = 0
    target_orders_checked = 0
    strongest = None

    for root in sources:
        candidates = [
            source for source in sources
            if source != root and neighbourhoods[root] & neighbourhoods[source]
        ]
        for fan_tuple in nonempty_subsets(candidates):
            fan = list(fan_tuple)
            d = len(neighbourhoods[root])
            codegrees = {
                source: len(neighbourhoods[root] & neighbourhoods[source])
                for source in fan
            }
            a = min(codegrees.values())
            W = sum((weights[source] for source in fan), Fraction(0))
            for q in range(1, a + 1):
                target_subsets = list(combinations(sorted(neighbourhoods[root]), q))
                multiplicities = {
                    Q: sum(set(Q) <= neighbourhoods[source] for source in fan)
                    for Q in target_subsets
                }
                weighted = {
                    Q: sum(
                        (weights[source] for source in fan if set(Q) <= neighbourhoods[source]),
                        Fraction(0),
                    )
                    for Q in target_subsets
                }
                exact = max(multiplicities.values())
                exact_weight = max(weighted.values())
                unweighted_average = Fraction(len(fan) * comb(a, q), comb(d, q))
                weighted_average = W * Fraction(comb(a, q), comb(d, q))
                assert exact >= ceil(unweighted_average)
                assert exact_weight >= weighted_average
                target_orders_checked += 1
                candidate = (exact, root, tuple(fan), q)
                if strongest is None or candidate[0] > strongest[0]:
                    strongest = candidate
            fan_families_checked += 1

        if candidates:
            d = len(neighbourhoods[root])
            J = 1 + floor(log2(d))
            loads = {
                source: len(neighbourhoods[root] & neighbourhoods[source])
                for source in candidates
            }
            L = sum(loads.values())
            bins = []
            for j in range(J):
                F = [source for source, value in loads.items() if 2**j <= value < 2 ** (j + 1)]
                bins.append((j, F))
            j, fan = max(bins, key=lambda item: (2 ** item[0]) * len(item[1]))
            assert (2**j) * len(fan) > Fraction(L, 2 * J)
            a = 2**j
            for q in range(1, a + 1):
                exact = max(
                    sum(set(Q) <= neighbourhoods[source] for source in fan)
                    for Q in combinations(sorted(neighbourhoods[root]), q)
                )
                assert exact >= ceil(Fraction(len(fan) * comb(a, q), comb(d, q)))
            if j >= 1 and d >= 2:
                lower = Fraction(L * (2**j - 1), 2 * J * d * (d - 1))
                exact_two = max(
                    sum(set(Q) <= neighbourhoods[source] for source in fan)
                    for Q in combinations(sorted(neighbourhoods[root]), 2)
                )
                assert Fraction(exact_two, 1) > lower

    print({
        "all_checks_passed": True,
        "fan_families_checked": fan_families_checked,
        "target_orders_checked": target_orders_checked,
        "strongest_common_target_multiplicity": strongest[0],
        "strongest_root": strongest[1],
        "strongest_fan": strongest[2],
        "strongest_target_order": strongest[3],
    })


if __name__ == "__main__":
    main()
