#!/usr/bin/env python3
"""Check the random two-sided score-to-mass conversion inequalities."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(message)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: check_random_two_sided_score_mass.py INSTANCE.json")

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    W = int(data["W"])
    R = int(data["R"])
    T = int(data["T"])
    delta = float(data["delta"])
    h = float(data["h"])
    rho = float(data["rho"])
    chi = float(data["chi"])
    B_i = float(data["macro_refill_defect_mass"])
    U_i_A = float(data["movement_anchor_row_mass"])

    if min(W, R, T) <= 0 or not 0 < delta < 1:
        fail("invalid scale parameters")
    if h < 0 or h >= T:
        fail("h must lie in [0,T)")
    if rho < 0 or chi < 0 or rho > T or chi > T:
        fail("scores must lie in [0,T]")

    score_failure = rho + chi > T - h
    high_score = max(rho, chi)
    score_lower_bound = (T - h) / 2
    numerator_lower_bound = delta * R * high_score
    theorem_mass_threshold = delta * R * (T - h) / 4
    stored_numerator = B_i + U_i_A

    if not score_failure:
        outcome = "random_two_sided_direct_allocation"
    else:
        if high_score <= score_lower_bound:
            fail("complementary score failure did not force a high score")
        if rho == high_score and stored_numerator + 1e-9 < numerator_lower_bound:
            fail("stored movement-score numerator is below delta*R*rho")
        if max(B_i, U_i_A) + 1e-9 < theorem_mass_threshold:
            fail("neither movement numerator summand reaches the theorem threshold")
        outcome = (
            "fixed_macro_refill_defect_conversion"
            if B_i >= U_i_A
            else "fixed_label_anchor_row_conversion"
        )

    print(f"W {W}")
    print(f"R {R}")
    print(f"T {T}")
    print(f"random Ore slack h {h}")
    print(f"rho {rho}")
    print(f"chi {chi}")
    print(f"score sum {rho + chi}")
    print(f"failure threshold {T - h}")
    print(f"forced high-score threshold {score_lower_bound}")
    print(f"stored movement numerator {stored_numerator}")
    print(f"delta R high-score bound {numerator_lower_bound}")
    print(f"one-summand mass threshold {theorem_mass_threshold}")
    print(f"outcome {outcome}")


if __name__ == "__main__":
    main()
