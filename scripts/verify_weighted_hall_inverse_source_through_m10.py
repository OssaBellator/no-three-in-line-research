#!/usr/bin/env python3
"""Verify the exact inverse-source Hall ledger through m=10."""
from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    exp = root / "experiments"
    ledger = load(exp / "weighted-hall-inverse-source-through-m10-audit.json")
    small = load(exp / "weighted-hall-transport-m9-compressed-audit.json")
    m10 = load(exp / "m10-hall-inverse-source-support-audit.json")

    cases = {int(case["m"]): case for case in ledger["cases"]}
    assert set(cases) == set(range(4, 11))

    expected_products = {
        4: Fraction(1, 24),
        5: Fraction(1, 37),
        6: Fraction(8, 215),
        7: Fraction(72, 931),
        8: Fraction(192, 745),
        9: Fraction(83040, 96029),
        10: Fraction(3152400, 791819),
    }
    expected_supports = {4: 1, 5: 1, 6: 2, 7: 6, 8: 24, 9: 120, 10: 600}
    expected_ranges = {
        4: [1, 1], 5: [1, 1], 6: [1, 2], 7: [1, 6],
        8: [2, 24], 9: [17, 120], 10: [106, 720],
    }

    small_by_m = {int(case["m"]): case for case in small["cases"]}
    for m in range(4, 10):
        case = cases[m]
        product = Fraction(case["maximum_support_normalized_charge"])
        raw = Fraction(case["maximizing_raw_charge"])
        support = int(case["maximizing_source_count"])
        assert product == expected_products[m]
        assert support == expected_supports[m]
        assert raw * support == product
        assert case["compatible_source_cycle_range"] == expected_ranges[m]
        published = small_by_m[m]
        assert case["supported_signed_flaws"] == published["atomic_signed_assignment_flaws"]
        assert Fraction(case["global_worst_charge"]) == Fraction(
            published["optimal_charge_numerator"], published["optimal_charge_denominator"]
        )
        assert support == math.factorial(m - 4)
        assert product < 1

    case10 = cases[10]
    assert Fraction(case10["maximum_support_normalized_charge"]) == expected_products[10]
    assert int(case10["maximizing_source_count"]) == 600
    assert Fraction(case10["maximizing_raw_charge"]) == Fraction(5254, 791819)
    assert case10["compatible_source_cycle_range"] == expected_ranges[10]
    assert case10["supported_signed_flaws"] == m10["supported_signed_flaws"]
    assert Fraction(case10["maximum_support_normalized_charge"]) > 1
    assert Fraction(case10["maximum_support_normalized_charge"]) < 4

    assert Fraction(1) - expected_products[9] == Fraction(12989, 96029)
    assert Fraction(4) - expected_products[10] == Fraction(14876, 791819)
    assert ledger["all_complete_exact_weighted_hall_audits_through_m10"] is True
    assert ledger["asymptotic_inverse_source_bound_proved"] is False

    print("weighted-Hall inverse-source ledger through m=10 verified")
    for m in range(4, 11):
        print(
            f"m={m} max_s_gamma={expected_products[m]} "
            f"source_count={expected_supports[m]}"
        )
    print("constant_one_holds_through_m9_and_first_fails_at_m10")
    print("constant_four_holds_through_m10")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
