#!/usr/bin/env python3
"""Check disjoint fixed-centre petals in a rank-three outer-role family."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


Pair = tuple[int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def parse_indices(raw: Any, label: str, n: int, centre: int) -> set[int]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected list")
    result: set[int] = set()
    for pos, value in enumerate(raw):
        value = require_int(value, f"{label}[{pos}]")
        if value >= n or value == centre:
            raise ValueError(f"{label}[{pos}]: expected noncentre index in [0,n)")
        if value in result:
            raise ValueError(f"{label}: duplicate index {value}")
        result.add(value)
    return result


def parse_pairs(raw: Any, label: str, n: int, centre: int) -> set[Pair]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected list")
    result: set[Pair] = set()
    for pos, item in enumerate(raw):
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError(f"{label}[{pos}]: expected [predecessor,middle]")
        r = require_int(item[0], f"{label}[{pos}][0]")
        p = require_int(item[1], f"{label}[{pos}][1]")
        if r >= n or p >= n or centre in {r, p} or r == p:
            raise ValueError(f"{label}[{pos}]: expected distinct noncentre indices")
        pair = (r, p)
        if pair in result:
            raise ValueError(f"{label}: duplicate pair {pair}")
        result.add(pair)
    return result


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        n = require_int(payload.get("n"), "n", minimum=4)
        centre = require_int(payload.get("centre"), "centre")
        if centre >= n:
            raise ValueError("centre must lie in [0,n)")
        threshold = require_int(
            payload.get("heavy_threshold"), "heavy_threshold", minimum=1
        )
        default_weight = require_int(
            payload.get("default_weight"), "default_weight", minimum=1
        )
        target_bank = require_int(payload.get("target_bank"), "target_bank", minimum=1)
        source_invalid_limit = require_int(
            payload.get("source_invalid_limit", n * n),
            "source_invalid_limit",
        )
        exceptional = parse_indices(
            payload.get("exceptional_middle_indices", []),
            "exceptional_middle_indices",
            n,
            centre,
        )
        invalid = parse_pairs(
            payload.get("source_invalid_pairs", []),
            "source_invalid_pairs",
            n,
            centre,
        )
        raw_overrides = payload.get("weight_overrides", [])
        if not isinstance(raw_overrides, list):
            raise ValueError("weight_overrides: expected list")
        overrides: dict[Pair, int] = {}
        for pos, item in enumerate(raw_overrides):
            if not isinstance(item, list) or len(item) != 3:
                raise ValueError(
                    f"weight_overrides[{pos}]: expected [predecessor,middle,weight]"
                )
            r = require_int(item[0], f"weight_overrides[{pos}][0]")
            p = require_int(item[1], f"weight_overrides[{pos}][1]")
            weight = require_int(item[2], f"weight_overrides[{pos}][2]", minimum=1)
            if r >= n or p >= n or centre in {r, p} or r == p:
                raise ValueError(
                    f"weight_overrides[{pos}]: expected distinct noncentre indices"
                )
            pair = (r, p)
            if pair in overrides:
                raise ValueError(f"weight_overrides: duplicate pair {pair}")
            overrides[pair] = weight
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    noncentre = [x for x in range(n) if x != centre]
    all_pairs = {(r, p) for r in noncentre for p in noncentre if r != p}
    safe = all_pairs - invalid

    if len(invalid) > source_invalid_limit:
        print(json.dumps({
            "outcome": "outer_transition_source_core",
            "n": n,
            "source_invalid_pair_count": len(invalid),
            "source_invalid_limit": source_invalid_limit,
        }, indent=2, sort_keys=True))
        return

    def weight(pair: Pair) -> int:
        return overrides.get(pair, default_weight)

    low_counts: dict[int, int] = {}
    heavy: list[Pair] = []
    for p in noncentre:
        if p in exceptional:
            continue
        safe_at_p = [(r, p) for r in noncentre if r != p and (r, p) in safe]
        low = [pair for pair in safe_at_p if weight(pair) < threshold]
        low_counts[p] = len(low)
        if len(low) > 2:
            raise SystemExit(
                f"check failed: middle index {p} has {len(low)} low-cost choices (>2)"
            )
        heavy.extend(pair for pair in safe_at_p if weight(pair) >= threshold)

    if not heavy:
        raise SystemExit("check failed: heavy outer-role family is empty")

    max_weight = max(weight(pair) for pair in heavy)
    level_count = max_weight.bit_length()
    levels: dict[int, list[Pair]] = {}
    for pair in heavy:
        level = weight(pair).bit_length() - 1
        levels.setdefault(level, []).append(pair)
    chosen_level = max(levels, key=lambda level: (len(levels[level]), -level))
    level_edges = sorted(levels[chosen_level])

    if len(level_edges) * level_count < len(heavy):
        raise SystemExit("check failed: dyadic count pigeonhole violated")

    selected: list[Pair] = []
    used_indices: set[int] = set()
    for r, p in level_edges:
        if r in used_indices or p in used_indices:
            continue
        selected.append((r, p))
        used_indices.update((r, p))

    if len(selected) * 4 * n < len(level_edges):
        raise SystemExit("check failed: greedy resource-matching lower bound violated")

    typed_sets = [
        {f"L:{r}", f"L:{p}", f"R:{p}"}
        for r, p in selected
    ]
    for i, first in enumerate(typed_sets):
        for second in typed_sets[i + 1:]:
            if first & second:
                raise SystemExit("check failed: selected petals share a noncentral resource")

    outcome = (
        "target_path_petal_bank"
        if len(selected) >= target_bank
        else "disjoint_path_petal_bank"
    )
    result = {
        "outcome": outcome,
        "n": n,
        "centre": centre,
        "common_centre_resource": f"R:{centre}",
        "exceptional_middle_count": len(exceptional),
        "source_invalid_pair_count": len(invalid),
        "safe_pair_count": len(safe),
        "heavy_pair_count": len(heavy),
        "maximum_low_count_outside_core": max(low_counts.values(), default=0),
        "dyadic_level": chosen_level,
        "dyadic_lower_weight": 1 << chosen_level,
        "dyadic_upper_weight_exclusive": 1 << (chosen_level + 1),
        "dyadic_level_count": level_count,
        "dyadic_class_size": len(level_edges),
        "greedy_lower_bound_denominator": 4 * n,
        "selected_bank_size": len(selected),
        "target_bank": target_bank,
        "selected_petals": [
            {
                "predecessor": r,
                "middle": p,
                "path": [r, p, centre],
                "weight": weight((r, p)),
                "noncentral_resources": sorted(resource_set),
            }
            for (r, p), resource_set in zip(selected, typed_sets)
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
