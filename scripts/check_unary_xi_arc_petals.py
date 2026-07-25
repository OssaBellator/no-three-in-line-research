#!/usr/bin/env python3
"""Check fixed-centre unary-Xi arc-petal extraction and paid threshold."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def require_number(value: Any, label: str, minimum: float = 0.0) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label}: expected number")
    result = float(value)
    if result < minimum:
        raise ValueError(f"{label}: expected number >= {minimum}")
    return result


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")

        n = require_int(payload.get("n"), "n", minimum=3)
        centre = require_int(payload.get("centre"), "centre")
        if centre >= n:
            raise ValueError("centre must lie in [0,n)")

        orientation = payload.get("orientation")
        if orientation not in {"incoming", "outgoing"}:
            raise ValueError("orientation must be 'incoming' or 'outgoing'")

        heavy_threshold = require_int(
            payload.get("heavy_threshold"), "heavy_threshold", minimum=1
        )
        default_weight = require_int(
            payload.get("default_weight"), "default_weight", minimum=1
        )
        target_bank = require_int(
            payload.get("target_bank"), "target_bank", minimum=1
        )
        removal_credit = require_number(
            payload.get("removal_credit"), "removal_credit", minimum=1e-15
        )
        residual_objective = require_number(
            payload.get("residual_objective", 0.0),
            "residual_objective",
            minimum=0.0,
        )

        raw_admissible = payload.get(
            "admissible_indices", [x for x in range(n) if x != centre]
        )
        if not isinstance(raw_admissible, list):
            raise ValueError("admissible_indices: expected list")
        admissible: list[int] = []
        seen: set[int] = set()
        for pos, value in enumerate(raw_admissible):
            value = require_int(value, f"admissible_indices[{pos}]")
            if value >= n or value == centre:
                raise ValueError(
                    f"admissible_indices[{pos}]: expected noncentre index"
                )
            if value in seen:
                raise ValueError(f"admissible_indices: duplicate index {value}")
            seen.add(value)
            admissible.append(value)

        overrides: dict[int, int] = {}
        raw_overrides = payload.get("weight_overrides", [])
        if not isinstance(raw_overrides, list):
            raise ValueError("weight_overrides: expected list")
        for pos, item in enumerate(raw_overrides):
            if not isinstance(item, list) or len(item) != 2:
                raise ValueError(
                    f"weight_overrides[{pos}]: expected [index,weight]"
                )
            index = require_int(item[0], f"weight_overrides[{pos}][0]")
            weight = require_int(
                item[1], f"weight_overrides[{pos}][1]", minimum=1
            )
            if index >= n or index == centre:
                raise ValueError(
                    f"weight_overrides[{pos}]: expected noncentre index"
                )
            if index in overrides:
                raise ValueError(f"weight_overrides: duplicate index {index}")
            overrides[index] = weight
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    def weight(index: int) -> int:
        return overrides.get(index, default_weight)

    heavy = [index for index in admissible if weight(index) >= heavy_threshold]
    if not heavy:
        raise SystemExit("check failed: heavy star is empty")

    max_weight = max(weight(index) for index in heavy)
    level_count = max_weight.bit_length()
    levels: dict[int, list[int]] = {}
    for index in heavy:
        level = weight(index).bit_length() - 1
        levels.setdefault(level, []).append(index)

    chosen_level = max(levels, key=lambda level: (len(levels[level]), -level))
    level_indices = sorted(levels[chosen_level])
    if len(level_indices) * level_count < len(heavy):
        raise SystemExit("check failed: dyadic pigeonhole bound violated")

    lower_weight = 1 << chosen_level
    upper_weight = 1 << (chosen_level + 1)

    common_resource = (
        f"R:{centre}" if orientation == "incoming" else f"L:{centre}"
    )
    variable_resources = [
        f"L:{index}" if orientation == "incoming" else f"R:{index}"
        for index in level_indices
    ]
    if len(set(variable_resources)) != len(variable_resources):
        raise SystemExit("check failed: variable resources are not disjoint")

    bank_indices = level_indices[:target_bank]
    bank_available = len(bank_indices) == target_bank
    upper_objective = upper_weight / removal_credit + residual_objective

    if not bank_available:
        outcome = "finite_bank_too_small"
    elif residual_objective >= 1.0:
        outcome = "residual_concentration"
    elif upper_objective < 1.0:
        outcome = "paid_arc_petal_average"
    else:
        outcome = "global_rank_two_unary_threshold"

    bank_weight = sum(weight(index) for index in bank_indices)
    tau = max(0.0, 1.0 - residual_objective)
    required_threshold_weight = (
        tau * removal_credit * len(bank_indices) / 2.0
    )
    if outcome == "global_rank_two_unary_threshold":
        if lower_weight + 1e-12 < tau * removal_credit / 2.0:
            raise SystemExit("check failed: dyadic threshold implication violated")
        if bank_weight + 1e-12 < required_threshold_weight:
            raise SystemExit("check failed: global weight lower bound violated")

    result = {
        "outcome": outcome,
        "n": n,
        "centre": centre,
        "orientation": orientation,
        "common_centre_resource": common_resource,
        "admissible_count": len(admissible),
        "heavy_arc_count": len(heavy),
        "dyadic_level_count": level_count,
        "chosen_dyadic_level": chosen_level,
        "dyadic_lower_weight": lower_weight,
        "dyadic_upper_weight_exclusive": upper_weight,
        "dyadic_class_size": len(level_indices),
        "target_bank": target_bank,
        "selected_bank_size": len(bank_indices),
        "selected_indices": bank_indices,
        "selected_variable_resources": variable_resources[:target_bank],
        "selected_bank_weight": bank_weight,
        "removal_credit": removal_credit,
        "residual_objective": residual_objective,
        "paid_upper_objective": upper_objective,
        "threshold_tau": tau,
        "required_threshold_weight": required_threshold_weight,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
