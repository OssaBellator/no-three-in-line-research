#!/usr/bin/env python3
"""Enumerate blocker-cover, anchor-clean, and external width-two state domains."""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

from analyze_full_width_two_block_bank import no_three, patch_states
from analyze_matching_first_reservoirs import alternating_decomposition, load_cases

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def blocker_clean(retained: tuple[Point, ...], patch: tuple[Point, ...]) -> bool:
    source_pairs = tuple(itertools.combinations(retained, 2))
    return all(
        determinant(first, second, candidate) != 0
        for candidate in patch
        for first, second in source_pairs
    )


def anchor_clean(retained: tuple[Point, ...], patch: tuple[Point, ...]) -> bool:
    patch_pairs = tuple(itertools.combinations(patch, 2))
    return all(
        determinant(anchor, first, second) != 0
        for anchor in retained
        for first, second in patch_pairs
    )


def analyze_layer(
    n: int,
    core: tuple[Point, ...],
    layer_index: int,
    layer: tuple[Point, ...],
) -> dict[str, Any]:
    counts = {
        "patch_internal_clean": 0,
        "blocker_cover_clean": 0,
        "anchor_clean": 0,
        "internal_and_blocker_clean": 0,
        "internal_and_anchor_clean": 0,
        "blocker_and_anchor_clean": 0,
        "fully_external_clean": 0,
    }
    total_states = 0

    for selected_indices in itertools.combinations(range(n), 4):
        deleted = tuple(layer[index] for index in selected_indices)
        deleted_set = set(deleted)
        retained = tuple(point for point in core if point not in deleted_set)
        for patch in patch_states(deleted, n):
            total_states += 1
            internal = no_three(patch)
            blockers = blocker_clean(retained, patch)
            anchors = anchor_clean(retained, patch)
            counts["patch_internal_clean"] += int(internal)
            counts["blocker_cover_clean"] += int(blockers)
            counts["anchor_clean"] += int(anchors)
            counts["internal_and_blocker_clean"] += int(internal and blockers)
            counts["internal_and_anchor_clean"] += int(internal and anchors)
            counts["blocker_and_anchor_clean"] += int(blockers and anchors)
            counts["fully_external_clean"] += int(internal and blockers and anchors)

    return {
        "layer": layer_index,
        "edge_count": n,
        "total_state_count": total_states,
        "domain_counts": counts,
        "blocker_cover_domain_nonempty": counts["blocker_cover_clean"] > 0,
        "external_domain_nonempty": counts["fully_external_clean"] > 0,
    }


def analyze_case(n: int, core: tuple[Point, ...]) -> dict[str, Any]:
    if n < 4:
        return {"source_n": n, "layers": [], "status": "fewer-than-four-edges"}
    layer_zero, layer_one, cycle_lengths = alternating_decomposition(n, core)
    return {
        "source_n": n,
        "cycle_edge_lengths": list(cycle_lengths),
        "layers": [
            analyze_layer(n, core, layer_index, layer)
            for layer_index, layer in enumerate((layer_zero, layer_one))
        ],
        "status": "searched",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = load_cases(args.certificate, args.n)
        result = {"cases": [analyze_case(n, core) for n, core in cases]}
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
