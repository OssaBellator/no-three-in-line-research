#!/usr/bin/env python3
"""Verify the partition and extrema of the complete exact m=10 Hall audit."""
from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def frac(text: str) -> Fraction:
    return Fraction(text)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    exp = root / "experiments"
    low = load(exp / "m10-weighted-hall-low-source-bands-audit.json")
    mid = load(exp / "m10-weighted-hall-mid-source-400-575-audit.json")
    hi1 = load(exp / "m10-weighted-hall-source-576-649-audit.json")
    hi2 = load(exp / "m10-weighted-hall-source-650-719-audit.json")
    full = load(exp / "m10-full-source-weighted-hall-tranche-audit.json")
    final = load(exp / "m10-weighted-hall-complete-audit.json")

    ranges = [
        (106, 199, low["bands"][0]["source_band_signed_flaws"],
         low["bands"][0]["source_band_proper_bottlenecks"],
         low["bands"][0]["source_band_worst_charge"]),
        (200, 399, low["bands"][1]["source_band_signed_flaws"],
         low["bands"][1]["source_band_proper_bottlenecks"],
         low["bands"][1]["source_band_worst_charge"]),
        (400, 575, mid["mid_source_signed_flaws_completed"],
         mid["mid_source_proper_bottlenecks"], mid["mid_source_worst_charge"]),
        (576, 649, hi1["summary"]["flaws"], hi1["summary"]["proper"],
         hi1["summary"]["worst_charge"]),
        (650, 719, hi2["summary"]["flaws"], hi2["summary"]["proper"],
         hi2["summary"]["worst_charge"]),
        (720, 720, full["full_source_tranche_signed_flaws"],
         full["full_source_tranche_proper_bottlenecks"],
         full["full_source_tranche_worst_charge"]),
    ]

    expected_ranges = final["completed_ranges"]
    assert len(ranges) == len(expected_ranges)
    for actual, recorded in zip(ranges, expected_ranges):
        lo, hi, flaws, proper, charge = actual
        assert recorded["source_cycle_range"] == [lo, hi]
        assert recorded["signed_flaws"] == flaws
        assert recorded["proper_bottlenecks"] == proper
        assert recorded["worst_charge"] == charge

    assert ranges[0][0] == 106 and ranges[-1][1] == 720
    for left, right in zip(ranges, ranges[1:]):
        assert left[1] + 1 == right[0]

    total = sum(row[2] for row in ranges)
    proper = sum(row[3] for row in ranges)
    assert total == proper == final["supported_signed_flaws"] == 47_512
    assert final["exact_mincuts_completed"] == total
    assert final["proper_bottlenecks"] == proper

    worst = max((frac(row[4]), row[4]) for row in ranges)
    assert worst[1] == final["global_worst_charge"] == "2397/349898"
    assert final["global_worst_source_count"] == 550
    assert final["global_worst_subset_size"] == 489
    assert final["global_worst_supply"] == 38_352
    assert final["global_worst_capacity"] == 5_598_368
    assert final["global_worst_flaw_source_owners"] == [5, 7, 8]
    assert final["global_worst_flaw_targets"] == [6, 8, 2]
    assert final["global_worst_flaw_orientations"] == [0, 0, 0]
    assert final["worst_complete_source_ratio"] == "2558/376281"
    assert final["maximum_merging_penalty"] == "1500597/656230"
    assert final["maximum_dinkelbach_cuts"] == 9
    assert final["all_supported_flaws_have_proper_bottlenecks"] is True
    assert final["all_47512_weighted_hall_mincuts_completed"] is True
    assert final["asymptotic_weighted_expansion_proved"] is False

    value = float(frac(final["global_worst_charge"]))
    assert math.isclose(final["global_worst_charge_decimal"], value,
                        rel_tol=0, abs_tol=1e-18)
    assert math.isclose(final["m_cubed_scaled_global_worst_charge"], 1000 * value,
                        rel_tol=0, abs_tol=1e-15)

    print("complete m=10 weighted-Hall audit verified")
    print(f"instances={total} proper={proper}")
    print(f"worst={final['global_worst_charge']} scaled={1000 * value:.12f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
