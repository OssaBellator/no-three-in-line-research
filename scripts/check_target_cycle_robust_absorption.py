#!/usr/bin/env python3
"""Check target-cycle direct absorption and source-star thresholds."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def analyse_case(
    R: float, xi: float, alpha: float, q: int, case: dict[str, Any]
) -> dict[str, Any]:
    unary_loss = float(case["unary_domain_loss"])
    W = math.sqrt(R)
    cycle_length = math.ceil(alpha * W) + q - 1
    binary_loss = cycle_length * (cycle_length - 1)
    reserved_margin = xi * R
    total_loss = unary_loss + binary_loss
    conservative_star = 3 * xi * R / (8 * cycle_length)

    if total_loss <= reserved_margin:
        outcome = "current_cycle_direct_absorption"
    elif binary_loss < reserved_margin / 4 and conservative_star > W:
        outcome = "super_target_final_source_star"
    else:
        outcome = "initial_base_certificate_or_scale_failure"

    return {
        "name": str(case.get("name", "case")),
        "unary_domain_loss": unary_loss,
        "total_domain_loss": total_loss,
        "outcome": outcome,
    }


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    R = float(data["R"])
    xi = float(data["xi"])
    alpha = float(data["alpha"])
    q = int(data["q"])
    if R <= 0 or xi <= 0 or alpha <= 0 or q < 1:
        raise ValueError("R, xi, alpha and q must be positive")

    W = math.sqrt(R)
    cycle_length = math.ceil(alpha * W) + q - 1
    binary_loss = cycle_length * (cycle_length - 1)
    conservative_star = 3 * xi * R / (8 * cycle_length)
    cases = [analyse_case(R, xi, alpha, q, case) for case in data["cases"]]

    return {
        "R": R,
        "W": W,
        "xi": xi,
        "alpha": alpha,
        "q": q,
        "target_cycle_length_upper": cycle_length,
        "binary_domain_loss": binary_loss,
        "binary_over_R": binary_loss / R,
        "reserved_margin": xi * R,
        "conservative_star_lower_bound": conservative_star,
        "star_over_target": conservative_star / W,
        "alpha_below_sqrt_xi_over_8": alpha < math.sqrt(xi / 8),
        "alpha_below_3xi_over_8": alpha < 3 * xi / 8,
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    with args.input.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    print(json.dumps(analyse(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
