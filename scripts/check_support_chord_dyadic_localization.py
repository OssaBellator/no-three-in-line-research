#!/usr/bin/env python3
"""Exhaustively verify PP3bws--PP3bwu for small Hamilton cycles."""

from __future__ import annotations

import json
import math
from itertools import combinations


def distance(m: int, x: int, y: int) -> int:
    gap = abs(x - y)
    return min(gap, m - gap)


def alternates(m: int, a1: int, a2: int, b1: int, b2: int) -> bool:
    labels = {a1: "A", a2: "A", b1: "B", b2: "B"}
    word = [labels[position] for position in sorted(labels)]
    return all(word[i] != word[(i + 1) % 4] for i in range(4))


def dyadic_type(m: int, leaves: tuple[int, int, int, int]) -> tuple[bool, tuple[int, int]]:
    a1, a2, b1, b2 = leaves
    pair = sorted(
        (
            int(math.log2(distance(m, a1, a2))),
            int(math.log2(distance(m, b1, b2))),
        )
    )
    return alternates(m, a1, a2, b1, b2), (pair[0], pair[1])


def transform(m: int, value: int, shift: int, reverse: bool) -> int:
    transformed = (-value if reverse else value) + shift
    return transformed % m


def main() -> None:
    rows = []
    for m in range(5, 13):
        observed = set()
        checked = 0
        # Fix the common centre at 0; choose and partition four distinct leaves.
        for leaf_set in combinations(range(1, m), 4):
            leaf_set_values = tuple(leaf_set)
            for a_pair in combinations(leaf_set_values, 2):
                b_pair = tuple(value for value in leaf_set_values if value not in a_pair)
                a1, a2 = a_pair
                b1, b2 = b_pair
                base = dyadic_type(m, (a1, a2, b1, b2))
                observed.add(base)
                swapped = dyadic_type(m, (b1, b2, a1, a2))
                assert swapped == base
                for shift in range(m):
                    for reverse in (False, True):
                        transformed = tuple(
                            transform(m, value, shift, reverse)
                            for value in (a1, a2, b1, b2)
                        )
                        assert dyadic_type(m, transformed) == base
                checked += 1
        M = m // 2
        L = 1 + int(math.log2(M))
        assert len(observed) <= L * (L + 1)
        rows.append(
            {
                "m": m,
                "leaf_partitions_checked": checked,
                "observed_dyadic_types": len(observed),
                "theorem_upper_bound": L * (L + 1),
            }
        )
    print(json.dumps({"rows": rows, "all_checks_passed": True}, indent=2))


if __name__ == "__main__":
    main()
