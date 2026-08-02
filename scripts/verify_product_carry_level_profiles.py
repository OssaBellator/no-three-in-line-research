#!/usr/bin/env python3
"""Verify exact fixed-area peak and support profiles for small factor pairs."""
from __future__ import annotations

from collections import Counter

from verify_product_carry_multiplicity import valid_factor_pairs, signed_area_histogram

EXPECTED = {
    2: {
        "pairs": 2,
        "peaks": Counter({12: 2}),
        "positive_support": Counter({1: 2}),
        "maximizing_signed_levels": Counter({2: 2}),
    },
    3: {
        "pairs": 4,
        "peaks": Counter({36: 4}),
        "positive_support": Counter({3: 4}),
        "maximizing_signed_levels": Counter({2: 4}),
    },
    4: {
        "pairs": 40,
        "peaks": Counter({42: 20, 36: 16, 48: 4}),
        "positive_support": Counter({7: 20, 8: 16, 6: 4}),
        "maximizing_signed_levels": Counter({2: 24, 6: 16}),
    },
    5: {
        "pairs": 64,
        "peaks": Counter({66: 24, 63: 16, 54: 16, 72: 8}),
        "positive_support": Counter({11: 24, 14: 16, 12: 16, 13: 8}),
        "maximizing_signed_levels": Counter({2: 64}),
    },
}


def check_side(side: int) -> None:
    pairs = valid_factor_pairs(side)
    peaks: Counter[int] = Counter()
    positive_support: Counter[int] = Counter()
    maximizing_signed_levels: Counter[int] = Counter()

    for pair in pairs:
        histogram = signed_area_histogram(pair)
        nonzero = {level: count for level, count in histogram.items() if level}
        assert nonzero
        assert all(nonzero[level] == nonzero[-level] for level in nonzero)
        maximum = max(nonzero.values())
        peaks[maximum] += 1
        positive_support[sum(level > 0 for level in nonzero)] += 1
        maximizing_signed_levels[
            sum(count == maximum for count in nonzero.values())
        ] += 1

    expected = EXPECTED[side]
    assert len(pairs) == expected["pairs"]
    assert peaks == expected["peaks"]
    assert positive_support == expected["positive_support"]
    assert maximizing_signed_levels == expected["maximizing_signed_levels"]
    print(
        f"side={side} pairs={len(pairs)} peaks={dict(sorted(peaks.items()))} "
        f"positive_support={dict(sorted(positive_support.items()))} "
        f"maximizing_signed_levels={dict(sorted(maximizing_signed_levels.items()))} PASS"
    )


def main() -> None:
    for side in range(2, 6):
        check_side(side)
    print("PX1146--PX1148 exact small-side carry level profiles: PASS")


if __name__ == "__main__":
    main()
