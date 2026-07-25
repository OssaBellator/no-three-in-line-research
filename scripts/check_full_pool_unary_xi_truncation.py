#!/usr/bin/env python3
"""Check full-pool unary-Xi truncation and forced heavy arc star."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


Arc = tuple[int, int]


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

        n = require_int(payload.get("n"), "n", minimum=4)
        b = require_int(payload.get("block_size"), "block_size", minimum=3)
        if b > n:
            raise ValueError("block_size must be at most n")
        centre = require_int(payload.get("centre"), "centre")
        if centre >= n:
            raise ValueError("centre must lie in [0,n)")

        threshold = require_int(
            payload.get("heavy_threshold"), "heavy_threshold", minimum=1
        )
        default_weight = require_int(
            payload.get("default_weight"), "default_weight", minimum=0
        )
        removal_credit = require_number(
            payload.get("removal_credit"), "removal_credit", minimum=1e-15
        )
        residual = require_number(
            payload.get("residual_objective"), "residual_objective"
        )
        tau = require_number(payload.get("tau"), "tau", minimum=1e-15)
        if tau >= 1:
            raise ValueError("tau must be less than one")
        target_bank = require_int(
            payload.get("target_bank"), "target_bank", minimum=1
        )

        overrides: dict[Arc, int] = {}
        raw_overrides = payload.get("weight_overrides", [])
        if not isinstance(raw_overrides, list):
            raise ValueError("weight_overrides: expected list")
        for pos, item in enumerate(raw_overrides):
            if not isinstance(item, list) or len(item) != 3:
                raise ValueError(
                    f"weight_overrides[{pos}]: expected [tail,head,weight]"
                )
            tail = require_int(item[0], f"weight_overrides[{pos}][0]")
            head = require_int(item[1], f"weight_overrides[{pos}][1]")
            weight = require_int(
                item[2], f"weight_overrides[{pos}][2]", minimum=0
            )
            if tail >= n or head >= n or tail == head:
                raise ValueError(
                    f"weight_overrides[{pos}]: expected distinct indices in [0,n)"
                )
            arc = (tail, head)
            if arc in overrides:
                raise ValueError(f"weight_overrides: duplicate arc {arc}")
            overrides[arc] = weight
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    allowed_threshold = tau * removal_credit / (4.0 * b)
    if threshold > allowed_threshold + 1e-12:
        raise SystemExit(
            "check failed: heavy_threshold exceeds tau*removal_credit/(4b)"
        )
    if residual > 1.0 - tau + 1e-12:
        raise SystemExit("check failed: residual_objective exceeds 1-tau")

    def weight(arc: Arc) -> int:
        return overrides.get(arc, default_weight)

    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    heavy = [arc for arc in arcs if weight(arc) >= threshold]
    incident = [arc for arc in heavy if centre in arc]
    nonincident = [arc for arc in heavy if centre not in arc]

    expected_heavy = (
        len(incident) / (n - 1)
        + len(nonincident) * (b - 2) / ((n - 1) * (n - 2))
    )

    indegree = [0] * n
    outdegree = [0] * n
    for tail, head in heavy:
        outdegree[tail] += 1
        indegree[head] += 1
    total_degree = [indegree[v] + outdegree[v] for v in range(n)]
    vertex = max(range(n), key=lambda v: (total_degree[v], -v))
    maximum_degree = total_degree[vertex]

    coefficient = (
        1.0 / (n - 1)
        + n * (b - 2) / (2.0 * (n - 1) * (n - 2))
    )
    if expected_heavy > coefficient * maximum_degree + 1e-12:
        raise SystemExit("check failed: heavy expectation degree bound violated")

    low_unary_fraction = b * threshold / removal_credit
    objective = expected_heavy + low_unary_fraction + residual
    gap = max(0.0, 1.0 - low_unary_fraction - residual)
    required_degree = gap / coefficient if coefficient > 0 else 0.0

    if objective < 1.0:
        outcome = "paid_heavy_arc_avoidance"
        orientation = None
        star_size = 0
        star_arcs: list[Arc] = []
    else:
        if maximum_degree + 1e-12 < required_degree:
            raise SystemExit("check failed: forced degree lower bound violated")
        if outdegree[vertex] >= indegree[vertex]:
            orientation = "outgoing"
            star_arcs = sorted(arc for arc in heavy if arc[0] == vertex)
        else:
            orientation = "incoming"
            star_arcs = sorted(arc for arc in heavy if arc[1] == vertex)
        star_size = len(star_arcs)
        if star_size * 2 < maximum_degree:
            raise SystemExit("check failed: oriented star split violated")
        outcome = (
            "target_heavy_arc_star"
            if star_size >= target_bank
            else "heavy_arc_star"
        )

    result = {
        "outcome": outcome,
        "n": n,
        "block_size": b,
        "centre": centre,
        "heavy_threshold": threshold,
        "allowed_threshold_upper_bound": allowed_threshold,
        "heavy_arc_count": len(heavy),
        "heavy_incident_to_centre_count": len(incident),
        "heavy_nonincident_count": len(nonincident),
        "expected_selected_heavy_arcs": expected_heavy,
        "low_unary_fraction_upper_bound": low_unary_fraction,
        "residual_objective": residual,
        "combined_objective": objective,
        "maximum_heavy_total_degree": maximum_degree,
        "maximum_degree_vertex": vertex,
        "degree_bound_coefficient": coefficient,
        "forced_degree_lower_bound": required_degree,
        "star_orientation": orientation,
        "oriented_star_size": star_size,
        "target_bank": target_bank,
        "selected_star_arcs": star_arcs[:target_bank],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
