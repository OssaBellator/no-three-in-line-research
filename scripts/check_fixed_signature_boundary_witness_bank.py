#!/usr/bin/env python3
"""Verify PP3bwi--PP3bwk on a finite fixed-signature path packing."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def parse_fraction(value: Any, where: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        raise ValueError(f"{where} must be an integer or rational string")
    result = Fraction(value)
    if result <= 0:
        raise ValueError(f"{where} must be positive")
    return result


def main() -> None:
    args = parse_args()
    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError("top-level JSON must be an object")
        r = raw.get("boundary_role_count")
        if isinstance(r, bool) or not isinstance(r, int) or not 2 <= r <= 4:
            raise ValueError("boundary_role_count must be an integer from 2 to 4")
        threshold = parse_fraction(raw.get("threshold"), "threshold")
        paths_raw = raw.get("paths")
        if not isinstance(paths_raw, list) or not paths_raw:
            raise ValueError("paths must be a nonempty list")

        paths: list[tuple[str, tuple[str, ...], Fraction]] = []
        for index, item in enumerate(paths_raw):
            if not isinstance(item, dict):
                raise ValueError(f"paths[{index}] must be an object")
            path_id = item.get("id")
            vertices = item.get("boundary_vertices")
            if not isinstance(path_id, str) or not path_id:
                raise ValueError(f"paths[{index}].id must be a nonempty string")
            if not isinstance(vertices, list) or len(vertices) != r:
                raise ValueError(f"paths[{index}] must contain exactly {r} boundary vertices")
            if any(not isinstance(vertex, str) or not vertex for vertex in vertices):
                raise ValueError(f"paths[{index}] contains an invalid vertex")
            if len(set(vertices)) != r:
                raise ValueError(f"paths[{index}] must be simple in boundary vertices")
            weight = parse_fraction(item.get("weight"), f"paths[{index}].weight")
            paths.append((path_id, tuple(vertices), weight))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    role_load: list[dict[str, Fraction]] = [defaultdict(Fraction) for _ in range(r)]
    total_load: dict[str, Fraction] = defaultdict(Fraction)
    total_weight = sum((weight for _, _, weight in paths), Fraction())
    for _, vertices, weight in paths:
        for role, vertex in enumerate(vertices):
            role_load[role][vertex] += weight
            total_load[vertex] += weight

    assert sum(total_load.values(), Fraction()) == r * total_weight
    for loads in role_load:
        assert sum(loads.values(), Fraction()) == total_weight
    for vertex, load in total_load.items():
        assert load == sum((loads[vertex] for loads in role_load), Fraction())

    hubs = sorted(vertex for vertex, load in total_load.items() if load > threshold)
    role_hubs = [
        {vertex: str(load) for vertex, load in sorted(loads.items()) if load > threshold / r}
        for loads in role_load
    ]

    remaining = list(paths)
    selected: list[str] = []
    while remaining:
        path_id, vertices, _ = remaining[0]
        selected.append(path_id)
        occupied = set(vertices)
        remaining = [entry for entry in remaining if occupied.isdisjoint(entry[1])]

    ratio = total_weight / (r * threshold)
    lower_bound = (ratio.numerator + ratio.denominator - 1) // ratio.denominator
    if not hubs:
        assert len(selected) >= lower_bound
    else:
        assert any(role_hubs)

    print(
        json.dumps(
            {
                "boundary_role_count": r,
                "total_packing_weight": str(total_weight),
                "total_boundary_load": str(sum(total_load.values(), Fraction())),
                "threshold": str(threshold),
                "boundary_hubs": hubs,
                "role_hubs": role_hubs,
                "greedy_boundary_disjoint_bank": selected,
                "required_bank_size_when_hub_free": int(lower_bound),
                "all_checks_passed": True,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
