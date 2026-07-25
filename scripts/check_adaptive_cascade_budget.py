#!/usr/bin/env python3
"""Check adaptive sub-square-root cascade sizing."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    R = float(data["R"])
    depth = int(data["depth"])
    xi = float(data["xi"])
    ambient_size = float(data.get("ambient_size", R))
    upper_scale = int(data.get("upper_scale", max(3, math.floor(R ** 0.25))))

    if R <= 0 or depth <= 0 or xi <= 0 or ambient_size <= 2:
        raise ValueError("R, depth, xi and ambient_size must be positive")
    width = math.sqrt(R)
    raw_q = math.floor(math.sqrt(width / depth))
    q = min(upper_scale, raw_q)
    if q < 3:
        raise ValueError("finite parameters do not permit a marked subbank of size 3")

    cumulative_size = depth * q
    binary_domain_bound = cumulative_size * max(0, cumulative_size - 1)
    binary_ratio = binary_domain_bound / R
    star_lower_bound = xi * R / (2 * cumulative_size)
    target_ratio = star_lower_bound / width
    recapture_fraction = (q - 2) / (ambient_size - 2)
    joint_trace_scale = depth * q**3 / ambient_size

    outcome = (
        "sub_square_root_target_star_preserved"
        if cumulative_size < width
        and binary_ratio < xi
        and star_lower_bound > width
        and joint_trace_scale < 1
        else "finite_budget_or_host_failure"
    )

    return {
        "R": R,
        "target_width_sqrt_R": width,
        "planned_depth": depth,
        "raw_adaptive_subbank_size": raw_q,
        "chosen_subbank_size": q,
        "cumulative_inserted_size_bound": cumulative_size,
        "cumulative_to_target_ratio": cumulative_size / width,
        "binary_domain_bound": binary_domain_bound,
        "binary_to_R_ratio": binary_ratio,
        "xi": xi,
        "guaranteed_star_lower_bound": star_lower_bound,
        "star_to_target_ratio": target_ratio,
        "ambient_marked_size": ambient_size,
        "single_step_self_recapture_fraction": recapture_fraction,
        "joint_trace_scale": joint_trace_scale,
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
