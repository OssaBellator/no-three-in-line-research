#!/usr/bin/env python3
"""Check the fixed-attempt Ore-failure-to-direct-repair arithmetic."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} EXAMPLE.json")

    data = json.loads(Path(sys.argv[1]).read_text())
    R = int(data["R"])
    T = int(data["T"])
    delta = float(data["delta"])
    h = int(data["h"])
    movement_unsafe = int(data["movement_unsafe"])
    refill_unsafe = int(data["refill_unsafe"])
    rho = int(data["rho"])
    chi = int(data["chi"])
    masses = [int(x) for x in data["numerator_masses"]]
    credit = int(data["direct_repair_credit"])
    insertion = int(data["direct_repair_insertion"])

    margin_threshold = delta * R
    if movement_unsafe >= margin_threshold or refill_unsafe >= margin_threshold:
        raise AssertionError("stored example should enter the uniform-margin score branch")

    ore_threshold = T - h
    score_sum = rho + chi
    if score_sum <= ore_threshold:
        raise AssertionError("stored pair does not violate the local Ore inequality")

    numerator_lower = delta * R * max(rho, chi)
    if sum(masses) < numerator_lower:
        raise AssertionError("stored numerator masses do not meet the score lower bound")

    one_mass_threshold = delta * R * (T - h) / 4.0
    largest_mass = max(masses)
    if largest_mass < one_mass_threshold:
        raise AssertionError("no numerator summand crosses the conversion threshold")

    repair_change = insertion - credit
    if repair_change >= 0:
        raise AssertionError("direct repair is not strictly paid")

    print("R", R)
    print("T", T)
    print("delta", delta)
    print("h", h)
    print("individual margin threshold", margin_threshold)
    print("movement unsafe", movement_unsafe)
    print("refill unsafe", refill_unsafe)
    print("rho", rho)
    print("chi", chi)
    print("score sum", score_sum)
    print("Ore threshold", ore_threshold)
    print("score numerator lower bound", numerator_lower)
    print("numerator masses", masses)
    print("one-mass conversion threshold", one_mass_threshold)
    print("largest numerator mass", largest_mass)
    print("direct repair insertion", insertion)
    print("direct repair credit", credit)
    print("direct repair change", repair_change)
    print("outcome fixed_attempt_allocation_or_direct_repair")


if __name__ == "__main__":
    main()
