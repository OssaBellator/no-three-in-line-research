#!/usr/bin/env python3
"""Finite diagnostic for PP3aln--PP3alt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main(path: str) -> None:
    data = json.loads(Path(path).read_text())

    W = int(data["W"])
    R = int(data["R"])
    T = int(data["T"])
    delta = float(data["delta"])
    macro_refill_defect_mass = int(data["macro_refill_defect_mass"])
    anchor_row_mass = int(data["anchor_row_mass"])

    required_combined_mass = delta * R * T
    if macro_refill_defect_mass + anchor_row_mass <= required_combined_mass:
        raise AssertionError("dead-row mass identity is not satisfied")

    resource_threshold = W * T
    greedy_bank_lower_bound = macro_refill_defect_mass / (4 * resource_threshold)
    star_partner_lower_bound = (resource_threshold - T) / T

    if anchor_row_mass >= required_combined_mass / 2:
        outcome = "fixed_label_anchor_conversion"
    elif macro_refill_defect_mass >= required_combined_mass / 2:
        outcome = "fixed_macro_refill_resource_conversion"
    else:
        outcome = "mass_dichotomy_failure"

    print(f"W {W}")
    print(f"R {R}")
    print(f"T {T}")
    print(f"required combined mass {required_combined_mass}")
    print(f"macro refill defect mass {macro_refill_defect_mass}")
    print(f"anchor row mass {anchor_row_mass}")
    print(f"resource threshold W*T {resource_threshold}")
    print(f"greedy bank lower bound {greedy_bank_lower_bound}")
    print(f"star partner lower bound {star_partner_lower_bound}")
    print(f"outcome {outcome}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} INSTANCE.json")
    main(sys.argv[1])
