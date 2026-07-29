#!/usr/bin/env python3
"""Verify the exact source-mass and capacity-deficit profile of the m=10 Hall transition count maxima."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

EXPECTED_S = [209, 215, 227, 234, 248, 272, 276, 278, 280, 281, 282, 284, 286]


def verify(root: Path) -> None:
    path = root / "experiments/m10-hall-transition-count-maximizer-source-mass-audit.json"
    data = json.loads(path.read_text())
    rows = data["violating_count_maxima"]
    assert [row["source_cycles"] for row in rows] == EXPECTED_S

    microscopic = []
    for row in rows:
        source_count = int(row["source_cycles"])
        subset_size = int(row["hall_subset_size"])
        supply = int(row["hall_subset_supply"])
        capacity = int(row["hall_subset_capacity"])
        mean_mass = Fraction(row["mean_source_mass"])
        deficit = int(row["capacity_deficit"])
        normalized = Fraction(row["normalized_capacity_deficit"])

        assert mean_mass == Fraction(supply, subset_size)
        assert deficit == source_count * supply - capacity > 0
        assert normalized == Fraction(deficit, capacity)
        if subset_size <= int(data["microscopic_subset_cutoff"]):
            microscopic.append(row)

    assert len(microscopic) == 9
    assert sum(Fraction(row["mean_source_mass"]) == 128 for row in microscopic) == 8
    assert sum(Fraction(row["mean_source_mass"]) == 64 for row in microscopic) == 1

    microscopic_max = max(
        (Fraction(row["normalized_capacity_deficit"]), row["source_cycles"])
        for row in microscopic
    )
    overall_max = max(
        (Fraction(row["normalized_capacity_deficit"]), row["source_cycles"])
        for row in rows
    )
    assert microscopic_max == (Fraction(421, 1563), 248)
    assert overall_max == (Fraction(12769, 38383), 278)
    assert all(Fraction(64) <= Fraction(row["mean_source_mass"]) <= Fraction(128) for row in rows)

    assert data["all_mean_source_masses_between_64_and_128"]
    assert data["all_exact_regressions_verified"]
    assert not data["asymptotic_source_mass_theorem_proved"]
    print("m10 Hall transition count-maximizer source-mass profile verified")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()
    verify(args.root.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
