#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path


def verify(root: Path) -> None:
    path = root / "experiments/terminal-normalizer-relative-cut-robustness-through-m10-audit.json"
    data = json.loads(path.read_text())
    lo = Fraction(data["common_stability_interval"]["lower_open"])
    hi = Fraction(data["common_stability_interval"]["upper_closed"])
    assert (lo, hi) == (Fraction(595, 186), Fraction(298, 93))
    assert lo < Fraction(16, 5) < hi

    expected = {
        8: (1096, 3488, 3524, 432, 1152, Fraction(58914, 81515)),
        9: (2976, 9520, 9536, 1024, 6144, Fraction(54752, 55335)),
        10: (9872, 31520, 31648, 896, 7168, Fraction(16664, 52445)),
    }
    limits = []
    for case in data["cases"]:
        m = int(case["m"])
        zmin, previous, selected, low, high, value = expected[m]
        assert (
            case["minimum_normalizer"],
            case["previous_observed_normalizer"],
            case["selected_observed_normalizer"],
            case["low_labels"],
            case["high_labels"],
        ) == (zmin, previous, selected, low, high)
        assert Fraction(case["selection_interval"][0]) == Fraction(previous, zmin)
        assert Fraction(case["selection_interval"][1]) == Fraction(selected, zmin)
        calculated = Fraction(low, zmin) + Fraction(high, zmin) / lo
        assert calculated == value == Fraction(case["lower_endpoint_limit_envelope"])
        limits.append(calculated)

    upper = max(limits)
    assert upper == Fraction(data["uniform_upper_limit"]) == Fraction(54752, 55335) < 1
    assert 1 - upper == Fraction(data["uniform_margin_below_one"]) == Fraction(583, 55335)
    assert data["same_selected_cut_throughout_common_interval"]
    assert data["reference_threshold_is_strictly_inside_interval"]
    assert not data["asymptotic_robust_interval_proved"]
    assert data["all_exact_regressions_verified"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    args = parser.parse_args()
    verify(args.root.resolve())
    print("terminal relative-cut robustness verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
