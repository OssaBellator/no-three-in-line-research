#!/usr/bin/env python3
"""Check slab-scale blocker extraction and conversion routing."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def load(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(path: str) -> None:
    data = load(path)
    m = int(data["m"])
    delta = float(data["delta"])
    if m <= 1 or not (0 < delta <= 1):
        raise ValueError("require m>1 and 0<delta<=1")

    M = max(1, int(m**0.05))
    R = max(1, int(m**0.95))
    W = max(1, int(R**0.5))
    T = M * W
    bad_entries = int(2 * delta * M * T * R)
    source_star_entry_lower = max(1, M * R - 2 * T)
    resource_bank_lower = bad_entries // (4 * M * R)

    if resource_bank_lower < int(delta * T / 3):
        raise AssertionError("resource-bank lower bound lost the target exponent")

    print(f"M {M}")
    print(f"R {R}")
    print(f"W {W}")
    print(f"T {T}")
    print(f"bad entries {bad_entries}")
    print(f"star-entry lower bound {source_star_entry_lower}")
    print(f"resource-bank lower bound {resource_bank_lower}")

    for case in data["cases"]:
        kind = case["kind"]
        if kind == "free_star":
            outcome = "fresh_helper_free_star"
        elif kind == "captive_star":
            degree = int(case["degree"])
            free_partner_bank = int(case.get("free_partner_bank", 0))
            if bool(case.get("puncture_host", False)):
                outcome = "one_puncture_free_star"
            elif free_partner_bank >= degree / 4:
                outcome = "controller_preserving_free_partner_bank"
            else:
                outcome = "puncture_or_host_failure"
        elif kind == "resource_bank":
            outcome = "recapture_free_resource_bank"
        else:
            raise ValueError(f"unknown case kind: {kind}")
        print(f"case {case['name']}: {outcome}")

    print("outcome structured_initial_blocker_conversion")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_initial_blocker_conversion.py INSTANCE.json")
    main(sys.argv[1])
