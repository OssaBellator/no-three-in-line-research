#!/usr/bin/env python3
"""Analyze canonical four-edge states inside perfect-matching source blocks."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_matching_first_reservoirs import alternating_decomposition, load_cases
from analyze_matching_first_width_two import canonical_state, certificate_counts

Point = tuple[int, int]


def analyze_layer(
    n: int,
    core: tuple[Point, ...],
    layer_index: int,
    layer: tuple[Point, ...],
    max_examples: int,
) -> dict[str, Any]:
    local_hist: Counter[tuple[int, int]] = Counter()
    global_hist: Counter[tuple[int, int]] = Counter()
    clean_local = 0
    clean_global = 0
    examples: list[dict[str, Any]] = []
    core_set = set(core)
    layer_set = set(layer)
    other_points = tuple(sorted(core_set.difference(layer_set)))

    for deleted in combinations(layer, 4):
        inserted = canonical_state(deleted, n)
        deleted_set = set(deleted)
        retained_layer = tuple(point for point in layer if point not in deleted_set)
        local_blocked, local_anchored, local_internal = certificate_counts(
            retained_layer, inserted
        )
        if local_internal != 0:
            raise AssertionError("canonical patch has an internal triple")
        local_hist[(local_blocked, local_anchored)] += 1
        locally_clean = local_blocked + local_anchored == 0
        clean_local += locally_clean

        retained_global = tuple(point for point in core if point not in deleted_set)
        global_blocked, global_anchored, global_internal = certificate_counts(
            retained_global, inserted
        )
        if global_internal != 0:
            raise AssertionError("canonical patch has an internal triple")
        global_hist[(global_blocked, global_anchored)] += 1
        clean_global += global_blocked + global_anchored == 0

        if locally_clean and len(examples) < max_examples:
            examples.append(
                {
                    "deleted": [list(point) for point in deleted],
                    "inserted": [list(point) for point in inserted],
                    "global_blockers": global_blocked,
                    "global_anchors": global_anchored,
                    "other_layer_point_count": len(other_points),
                }
            )

    total = sum(local_hist.values())
    return {
        "layer": layer_index,
        "edge_count": len(layer),
        "state_count": total,
        "locally_clean_state_count": clean_local,
        "locally_clean_fraction": f"{clean_local}/{total}",
        "globally_clean_state_count": clean_global,
        "minimum_local_defects": min(sum(key) for key in local_hist),
        "minimum_global_defects": min(sum(key) for key in global_hist),
        "local_defect_histogram": {
            f"{blocked},{anchored}": count
            for (blocked, anchored), count in sorted(local_hist.items())
        },
        "global_defect_histogram": {
            f"{blocked},{anchored}": count
            for (blocked, anchored), count in sorted(global_hist.items())
        },
        "locally_clean_examples": examples,
    }


def analyze_case(
    n: int, core: tuple[Point, ...], max_examples: int
) -> dict[str, Any]:
    if n < 4:
        return {"source_n": n, "layers": [], "status": "fewer-than-four-edges"}
    layer_zero, layer_one, cycle_lengths = alternating_decomposition(n, core)
    return {
        "source_n": n,
        "cycle_edge_lengths": list(cycle_lengths),
        "layers": [
            analyze_layer(n, core, index, layer, max_examples)
            for index, layer in enumerate((layer_zero, layer_one))
        ],
        "status": "searched",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--max-examples", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_examples < 0:
        raise SystemExit("--max-examples must be nonnegative")

    try:
        cases = load_cases(args.certificate, args.n)
        result = {
            "cases": [
                analyze_case(n, core, args.max_examples) for n, core in cases
            ]
        }
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
