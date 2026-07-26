#!/usr/bin/env python3
"""Check exact arc/path-conditioned Hamilton-cycle spaces."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Any


def cycles(vertices: list[int]) -> list[tuple[int, ...]]:
    root = vertices[0]
    return [(root, *perm) for perm in itertools.permutations(vertices[1:])]


def arc_set(cycle: tuple[int, ...]) -> set[tuple[int, int]]:
    return {(cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(len(cycle))}


def parse_arcs(value: Any, label: str) -> set[tuple[int, int]]:
    if not isinstance(value, list):
        raise ValueError(f"{label}: expected list")
    result: set[tuple[int, int]] = set()
    for pos, raw in enumerate(value):
        if not isinstance(raw, list) or len(raw) != 2:
            raise ValueError(f"{label}[{pos}]: expected [tail,head]")
        a, b = raw
        if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, int) or not isinstance(b, int):
            raise ValueError(f"{label}[{pos}]: endpoints must be integers")
        if a == b:
            raise ValueError(f"{label}[{pos}]: loops are not allowed")
        result.add((a, b))
    return result


def falling(n: int, u: int) -> int:
    value = 1
    for j in range(u):
        value *= n - j
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        b = int(payload["block_size"])
        if b < 4 or b > 9:
            raise ValueError("block_size must lie between 4 and 9 for finite enumeration")
        vertices = list(range(b))
        all_cycles = cycles(vertices)
        all_arc_sets = [arc_set(c) for c in all_cycles]

        arc = tuple(payload["arc"])
        path = [tuple(v) for v in payload["path"]]
        if len(arc) != 2 or len(path) != 2 or path[0][1] != path[1][0]:
            raise ValueError("invalid arc or two-arc path")
        arc_required = {arc}
        path_required = set(path)
        arc_cycles = [s for s in all_arc_sets if arc_required <= s]
        path_cycles = [s for s in all_arc_sets if path_required <= s]
        if len(arc_cycles) != math.factorial(b - 2):
            raise ValueError("arc-conditioned cycle count mismatch")
        if len(path_cycles) != math.factorial(b - 3):
            raise ValueError("path-conditioned cycle count mismatch")

        arc_extra = parse_arcs(payload.get("arc_extra_forest", []), "arc_extra_forest")
        path_extra = parse_arcs(payload.get("path_extra_forest", []), "path_extra_forest")
        arc_hits = sum(1 for s in arc_cycles if arc_extra <= s)
        path_hits = sum(1 for s in path_cycles if path_extra <= s)
        ua = len(arc_extra)
        up = len(path_extra)
        expected_arc_hits = len(arc_cycles) // falling(b - 2, ua) if ua else len(arc_cycles)
        expected_path_hits = len(path_cycles) // falling(b - 3, up) if up else len(path_cycles)
        if arc_hits != expected_arc_hits:
            raise ValueError("arc-conditioned forest cylinder count mismatch")
        if path_hits != expected_path_hits:
            raise ValueError("path-conditioned forest cylinder count mismatch")

        allowed_outcomes = payload.get("allowed_outcomes")
        required = {"paid_completion", "typed_weighted_concentration"}
        if not isinstance(allowed_outcomes, list) or set(allowed_outcomes) != required:
            raise ValueError("allowed_outcomes must be exactly the two typed petal outcomes")
        if "host_failure" in allowed_outcomes:
            raise ValueError("host_failure is not an allowed petal endpoint")
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    print(json.dumps({
        "outcome": "petal_host_leaf_eliminated",
        "block_size": b,
        "total_directed_hamilton_cycles": len(all_cycles),
        "arc_conditioned_count": len(arc_cycles),
        "expected_arc_conditioned_count": math.factorial(b - 2),
        "path_conditioned_count": len(path_cycles),
        "expected_path_conditioned_count": math.factorial(b - 3),
        "arc_extra_forest_hits": arc_hits,
        "path_extra_forest_hits": path_hits,
        "allowed_outcomes": sorted(required),
        "host_failure_allowed": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
