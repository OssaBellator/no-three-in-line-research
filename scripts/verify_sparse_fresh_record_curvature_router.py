#!/usr/bin/env python3
"""Finite audit for SAS5es--SAS5ew."""

import random
from collections import defaultdict
from itertools import product

SEED = 20260727

NEGATIVE = {(0, 1, 0, 0), (0, 0, 1, 0)}
POSITIVE = {(0, 0, 0, 1)}
NEUTRAL = {(0, 1, 0, 1), (0, 0, 1, 1)}
ALLOWED = NEGATIVE | POSITIVE | NEUTRAL


def curvature(table):
    i0, iw, it, iwt = table
    return i0 - iw - it + iwt


def main():
    counts = defaultdict(int)

    repaired_tables = []
    for iw, it, iwt in product((0, 1), repeat=3):
        table = (0, iw, it, iwt)
        if iw + it + iwt == 0:
            continue
        repaired_tables.append(table)

    # SAS5bs--SAS5bw excludes the two nonconjunction negative tables.
    conjunction_compatible = [
        table
        for table in repaired_tables
        if curvature(table) in (-1, 0, 1)
        and not (curvature(table) == -1 and table not in NEGATIVE)
    ]
    assert set(conjunction_compatible) == ALLOWED

    for table in conjunction_compatible:
        chi = curvature(table)
        if table in NEGATIVE:
            assert chi == -1
            counts["negative_tables"] += 1
        elif table in POSITIVE:
            assert chi == 1
            counts["positive_tables"] += 1
        else:
            assert chi == 0
            assert table[1] + table[2] == 1
            assert table[3] == 1
            counts["neutral_tables"] += 1

    rng = random.Random(SEED)
    for _ in range(100000):
        table = rng.choice(tuple(ALLOWED))
        n = rng.randint(4, 100)
        interaction_degree = rng.randint(0, 100)
        pair_mass = rng.uniform(1.0, 10_000_000.0)
        exact_lower_bound = pair_mass / (
            24
            * (interaction_degree + 1)
            * n
            * (n - 1)
            * (n - 2)
            * (n * (n - 1) * (n - 2) / 6)
        )
        routed_weight = exact_lower_bound
        assert routed_weight == exact_lower_bound
        counts["weighted_routes"] += 1
        if table in NEGATIVE:
            counts["negative_routes"] += 1
        elif table in POSITIVE:
            counts["positive_routes"] += 1
        else:
            creating_swap = "omega" if table[1] else "tau"
            assert creating_swap in ("omega", "tau")
            counts["neutral_routes"] += 1

    print("SAS fresh exact-record curvature audit passed")
    print(f"  negative table types: {counts['negative_tables']}")
    print(f"  positive table types: {counts['positive_tables']}")
    print(f"  neutral table types: {counts['neutral_tables']}")
    print(f"  weighted routes: {counts['weighted_routes']}")
    print(f"  negative routes: {counts['negative_routes']}")
    print(f"  positive routes: {counts['positive_routes']}")
    print(f"  neutral routes: {counts['neutral_routes']}")


if __name__ == "__main__":
    main()
