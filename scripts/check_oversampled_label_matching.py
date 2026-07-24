#!/usr/bin/env python3
"""Evaluate PP3ft--PP3fv from refined-domain analyzer JSON output.

Generate the input with ``analyze_same_edge_anchor_domains.py --output FILE``.
The checker reconstructs the average movement/refill boundary shadows, applies
the divisor-energy edge loss, and reports the rigorous refined-graph edge and
matching lower bounds.  An optional target width tests the PP3fu matching
condition.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(raw: Any, context: str) -> Fraction:
    if isinstance(raw, bool):
        raise ValueError(f"{context}: invalid boolean fraction")
    try:
        return Fraction(raw)
    except (ValueError, ZeroDivisionError, TypeError) as exc:
        raise ValueError(f"{context}: invalid fraction") from exc


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def fraction_json(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
        "decimal": float(value),
    }


def analyze_layer(layer: dict[str, Any], target_width: int | None) -> dict[str, Any]:
    pool_size = layer.get("pool_size")
    labels = layer.get("candidate_labels")
    movement_sizes = layer.get("movement_safe_sizes")
    refill_sizes = layer.get("refill_safe_sizes")
    energy = layer.get("pool_anchor_divisor_energy")
    actual_edges = layer.get("refined_graph_edge_count")
    actual_matching = layer.get("refined_graph_maximum_matching")
    if (
        isinstance(pool_size, bool)
        or not isinstance(pool_size, int)
        or pool_size <= 0
        or not isinstance(labels, list)
        or not labels
        or not isinstance(movement_sizes, dict)
        or not isinstance(refill_sizes, dict)
        or isinstance(energy, bool)
        or not isinstance(energy, int)
        or energy < 0
        or isinstance(actual_edges, bool)
        or not isinstance(actual_edges, int)
        or isinstance(actual_matching, bool)
        or not isinstance(actual_matching, int)
    ):
        raise ValueError("malformed analyzer layer")

    gamma = parse_fraction(layer.get("gamma"), "gamma")
    epsilon = parse_fraction(layer.get("epsilon"), "epsilon")
    if not 0 < epsilon < gamma < 1:
        raise ValueError("require 0 < epsilon < gamma < 1")

    label_count = len(labels)
    movement_total = 0
    refill_total = 0
    for label in labels:
        key = str(label)
        movement_value = movement_sizes.get(key)
        refill_value = refill_sizes.get(key)
        if (
            isinstance(movement_value, bool)
            or not isinstance(movement_value, int)
            or isinstance(refill_value, bool)
            or not isinstance(refill_value, int)
        ):
            raise ValueError(f"missing safe-size data for label {label}")
        movement_total += movement_value
        refill_total += refill_value

    movement_shadow = label_count * pool_size - movement_total
    refill_shadow = label_count * pool_size - refill_total
    total_shadow = movement_shadow + refill_shadow

    fixed_pair_loss = Fraction(
        label_count * total_shadow,
        (1 - gamma) * pool_size,
    )
    divisor_loss = Fraction(energy, epsilon * pool_size)
    real_edge_lower = Fraction(label_count * label_count) - fixed_pair_loss - divisor_loss
    integer_edge_lower = max(0, ceil_fraction(real_edge_lower))
    matching_lower = ceil_fraction(Fraction(integer_edge_lower, label_count))

    sigma = Fraction(total_shadow, pool_size * label_count)
    eta = Fraction(energy, pool_size * label_count * label_count)
    normalized_matching_fraction = 1 - sigma / (1 - gamma) - eta / epsilon

    result: dict[str, Any] = {
        "source_n": layer.get("source_n"),
        "layer": layer.get("layer"),
        "pool_size": pool_size,
        "label_count": label_count,
        "movement_shadow": movement_shadow,
        "refill_shadow": refill_shadow,
        "normalized_total_shadow_sigma": fraction_json(sigma),
        "normalized_divisor_energy_eta": fraction_json(eta),
        "PP3ft_real_edge_lower_bound": fraction_json(real_edge_lower),
        "PP3ft_integer_edge_lower_bound": integer_edge_lower,
        "actual_refined_graph_edges": actual_edges,
        "PP3ft_matching_lower_bound": matching_lower,
        "actual_maximum_matching": actual_matching,
        "PP3fv_normalized_matching_fraction": fraction_json(
            normalized_matching_fraction
        ),
        "edge_bound_consistent": actual_edges >= integer_edge_lower,
        "matching_bound_consistent": actual_matching >= matching_lower,
    }
    if target_width is not None:
        result["target_width"] = target_width
        result["PP3fu_matching_condition"] = matching_lower >= target_width
        result["actual_matching_reaches_target"] = actual_matching >= target_width
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("analysis", type=Path)
    parser.add_argument("--width", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.width is not None and args.width < 1:
        raise SystemExit("--width must be positive")

    try:
        payload = json.loads(args.analysis.read_text(encoding="utf-8"))
        raw_cases = payload.get("cases")
        if not isinstance(raw_cases, list):
            raise ValueError("analysis JSON must contain a cases list")
        results = []
        for case in raw_cases:
            if not isinstance(case, dict) or not isinstance(case.get("layers"), list):
                raise ValueError("malformed case")
            for layer in case["layers"]:
                if not isinstance(layer, dict):
                    raise ValueError("malformed layer")
                results.append(analyze_layer(layer, args.width))
        output = {"layers": results}
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(output, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
