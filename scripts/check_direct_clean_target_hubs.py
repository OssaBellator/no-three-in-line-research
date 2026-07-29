#!/usr/bin/env python3
"""Exact action-graph audit for PP3bxj--PP3bxl."""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def powerset(items: list[str]):
    for size in range(1, len(items) + 1):
        yield from combinations(items, size)


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_direct_clean_target_hubs.py [graph.json]")
    path = (
        Path(sys.argv[1])
        if len(sys.argv) == 2
        else Path("experiments/direct-clean-target-hub-example.json")
    )
    data = json.loads(path.read_text())
    neighbourhoods = {source: set(targets) for source, targets in data["neighbourhoods"].items()}
    sources = sorted(neighbourhoods)
    rho = Fraction(data["rho_numerator"], data["rho_denominator"])

    subsets_checked = 0
    violations_checked = 0
    strongest_hub = (0, None, None)
    strongest_fan = (Fraction(0), None, None)

    for A_tuple in powerset(sources):
        A = set(A_tuple)
        union = set().union(*(neighbourhoods[x] for x in A))
        multiplicity = {
            y: sum(y in neighbourhoods[x] for x in A)
            for y in union
        }
        degrees = {x: len(neighbourhoods[x]) for x in A}
        bar_d = Fraction(sum(degrees.values()), len(A))
        loads = {}
        for x in A:
            codegrees = {
                xp: len(neighbourhoods[x] & neighbourhoods[xp])
                for xp in A
                if xp != x
            }
            load = sum(codegrees.values())
            loads[x] = load
            identity = sum(multiplicity[y] - 1 for y in neighbourhoods[x])
            assert load == identity
            max_mult = max(multiplicity[y] for y in neighbourhoods[x])
            assert max_mult >= 1 + math.ceil(Fraction(load, degrees[x]))
            if max_mult > strongest_hub[0]:
                target = max(neighbourhoods[x], key=lambda y: multiplicity[y])
                strongest_hub = (max_mult, x, target)

            if load > 0:
                J = 1 + int(math.log2(degrees[x]))
                bins = []
                for j in range(J):
                    count = sum(
                        1 for value in codegrees.values()
                        if 2**j <= value < 2 ** (j + 1)
                    )
                    bins.append((j, count))
                best = max((Fraction((2**j) * count), j, count) for j, count in bins)
                assert best[0] > Fraction(load, 2 * J)
                if best[0] > strongest_fan[0]:
                    strongest_fan = (best[0], x, (best[1], best[2]))

        if Fraction(len(A), len(union)) > rho:
            violations_checked += 1
            threshold = rho * bar_d * bar_d - bar_d
            roots = [x for x in A if loads[x] > threshold]
            assert roots
            x = roots[0]
            target = max(neighbourhoods[x], key=lambda y: multiplicity[y])
            assert Fraction(multiplicity[target], 1) > (
                1 + threshold / degrees[x]
            )

            d = min(degrees.values())
            D = max(degrees.values())
            window_rhs = 1 + (rho * d * d - d) / D
            assert Fraction(multiplicity[target], 1) > window_rhs

            J = 1 + int(math.log2(degrees[x]))
            codegrees = [
                len(neighbourhoods[x] & neighbourhoods[xp])
                for xp in A
                if xp != x and neighbourhoods[x] & neighbourhoods[xp]
            ]
            bins = [
                (j, sum(2**j <= c < 2 ** (j + 1) for c in codegrees))
                for j in range(J)
            ]
            assert max(Fraction((2**j) * count) for j, count in bins) > threshold / (2 * J)

        subsets_checked += 1

    print({
        "all_checks_passed": True,
        "subsets_checked": subsets_checked,
        "violating_subsets_checked": violations_checked,
        "rho": str(rho),
        "strongest_target_hub": {
            "multiplicity": strongest_hub[0],
            "root": strongest_hub[1],
            "target": strongest_hub[2],
        },
        "strongest_dyadic_fan_mass": str(strongest_fan[0]),
        "strongest_dyadic_fan_root": strongest_fan[1],
        "strongest_dyadic_fan_level_and_count": strongest_fan[2],
    })


if __name__ == "__main__":
    main()
