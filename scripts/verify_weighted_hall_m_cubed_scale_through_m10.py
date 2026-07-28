#!/usr/bin/env python3
"""Verify exact m^3-scaled weighted-Hall maxima for m=4,...,10."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    exp = root / "experiments"
    small = load(exp / "weighted-hall-transport-m9-compressed-audit.json")
    m10 = load(exp / "m10-weighted-hall-complete-audit.json")

    charge: dict[int, Fraction] = {}
    for case in small["cases"]:
        m = int(case["m"])
        charge[m] = Fraction(
            int(case["optimal_charge_numerator"]),
            int(case["optimal_charge_denominator"]),
        )
    charge[10] = Fraction(m10["global_worst_charge"])

    expected = {
        4: Fraction(1, 24),
        5: Fraction(1, 37),
        6: Fraction(4, 215),
        7: Fraction(12, 931),
        8: Fraction(1, 93),
        9: Fraction(223, 29271),
        10: Fraction(2397, 349898),
    }
    assert charge == expected

    scaled = {m: m**3 * value for m, value in charge.items()}
    for m in range(4, 10):
        assert scaled[m] < scaled[m + 1]
    assert all(value < 7 for value in scaled.values())
    assert max(scaled, key=scaled.get) == 10
    assert Fraction(7) - scaled[10] == Fraction(26143, 174949)
    assert m10["all_47512_weighted_hall_mincuts_completed"] is True
    assert m10["asymptotic_weighted_expansion_proved"] is False

    print("weighted-Hall m^3 scale through m=10 verified")
    for m in range(4, 11):
        print(
            f"m={m} charge={charge[m]} scaled={scaled[m]} "
            f"decimal={float(scaled[m]):.12f}"
        )
    print(f"uniform_constant=7 endpoint_margin={Fraction(7)-scaled[10]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
