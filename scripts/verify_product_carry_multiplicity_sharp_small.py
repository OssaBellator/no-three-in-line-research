#!/usr/bin/env python3
"""Exact small-side sharp profiles for fixed signed-area multiplicity."""
from __future__ import annotations

from collections import Counter

from verify_product_carry_multiplicity import (
    signed_area_histogram,
    valid_factor_pairs,
)

EXPECTED = {
    2: (2, 12, Counter({12: 2})),
    3: (4, 36, Counter({36: 4})),
    4: (40, 48, Counter({42: 20, 36: 16, 48: 4})),
    5: (64, 72, Counter({66: 24, 63: 16, 54: 16, 72: 8})),
}


def main() -> None:
    for side, (expected_pairs, expected_maximum, expected_profile) in EXPECTED.items():
        profile: Counter[int] = Counter()
        maximizing_levels: Counter[int] = Counter()
        maximum = 0
        for pair in valid_factor_pairs(side):
            histogram = signed_area_histogram(pair)
            pair_maximum = max(histogram.values())
            profile[pair_maximum] += 1
            for level, count in histogram.items():
                if count > maximum:
                    maximum = count
                    maximizing_levels = Counter({level: 1})
                elif count == maximum:
                    maximizing_levels[level] += 1
        assert len(valid_factor_pairs(side)) == expected_pairs
        assert maximum == expected_maximum
        assert profile == expected_profile
        general_bound = 4 * side * (2 * side - 1)
        assert 5 * maximum <= 3 * general_bound
        print(
            f"side={side} pairs={expected_pairs} maximum={maximum} "
            f"general_bound={general_bound} profile={dict(sorted(profile.items()))} "
            f"maximizing_levels={dict(sorted(maximizing_levels.items()))} PASS"
        )
    print("PX1105--PX1108 sharp small-side carry multiplicity: PASS")


if __name__ == "__main__":
    main()
