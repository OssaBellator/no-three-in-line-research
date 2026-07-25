#!/usr/bin/env python3
"""Check the finite-horizon defect-cycle and target-star inequalities."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    R = int(data["R"])
    xi = float(data["xi"])
    alpha = float(data["alpha"])
    q = int(data["q"])
    if R <= 0 or q < 3 or xi <= 0 or alpha <= 0:
        raise ValueError("R, xi, alpha, and q must be positive, with q>=3")
    W = math.sqrt(R)
    alpha_limit = min(math.sqrt(xi / 8.0), xi / 4.0)
    threshold = math.ceil(alpha * W)
    if q >= threshold:
        generations = 1
    else:
        generations = 1 + math.ceil((threshold - q) / (q - 1))
    defect = q + (generations - 1) * (q - 1)
    binary_loss = defect * (defect - 1)
    binary_ratio = binary_loss / R
    conservative_star = 3.0 * xi * R / (8.0 * defect)
    horizon_ratio = generations / W
    overshoot = defect - threshold
    conditions = {
        "alpha_below_limit": alpha < alpha_limit,
        "q_subtarget": q / W < 1.0,
        "binary_below_quarter_margin": binary_loss < xi * R / 4.0,
        "star_above_target": conservative_star > W,
    }
    outcome = (
        "target_scale_alternating_cycle_boundary"
        if all(conditions.values())
        else "finite_parameter_or_margin_failure"
    )
    return {
        "R": R,
        "W": W,
        "xi": xi,
        "alpha": alpha,
        "alpha_limit": alpha_limit,
        "q": q,
        "generations_to_threshold": generations,
        "generation_over_target_ratio": horizon_ratio,
        "threshold_defect": threshold,
        "actual_defect": defect,
        "overshoot": overshoot,
        "defect_over_target_ratio": defect / W,
        "binary_loss": binary_loss,
        "binary_over_R_ratio": binary_ratio,
        "conservative_star_lower_bound": conservative_star,
        "star_over_target_ratio": conservative_star / W,
        "conditions": conditions,
        "outcome": outcome,
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
