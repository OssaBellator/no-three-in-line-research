#!/usr/bin/env python3
"""Verify D4 board symmetries, layer swap, and relative-cycle invariance."""
from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Any, Callable

Point = tuple[int, int]


def det(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def parse_perm(raw: Any, n: int, name: str) -> list[int]:
    if not isinstance(raw, list) or len(raw) != n:
        raise ValueError(f"{name} must have length {n}")
    if any(isinstance(v, bool) or not isinstance(v, int) for v in raw):
        raise ValueError(f"{name} entries must be integers")
    if sorted(raw) != list(range(1, n + 1)):
        raise ValueError(f"{name} is not a one-based permutation")
    return raw


def layer_points(perm: list[int]) -> list[Point]:
    return [(x + 1, y) for x, y in enumerate(perm)]


def points_to_perm(points: list[Point], n: int) -> list[int]:
    by_col: dict[int, int] = {}
    for x, y in points:
        if not (1 <= x <= n and 1 <= y <= n):
            raise ValueError("transformed point outside board")
        if x in by_col:
            raise ValueError("transformed layer is not a permutation graph")
        by_col[x] = y
    if set(by_col) != set(range(1, n + 1)) or set(by_col.values()) != set(range(1, n + 1)):
        raise ValueError("transformed layer is not a permutation")
    return [by_col[x] for x in range(1, n + 1)]


def verify_seed(sigma: list[int], tau: list[int]) -> None:
    n = len(sigma)
    if any(sigma[i] == tau[i] for i in range(n)):
        raise ValueError("layers are not edge-disjoint")
    pts = layer_points(sigma) + layer_points(tau)
    if len(set(pts)) != 2 * n:
        raise ValueError("duplicate selected point")
    for a, b, c in combinations(pts, 3):
        if det(a, b, c) == 0:
            raise ValueError(f"collinear triple {a}, {b}, {c}")


def relative_cycles(sigma: list[int], tau: list[int]) -> list[int]:
    n = len(sigma)
    inv = [0] * n
    for x, row in enumerate(sigma):
        inv[row - 1] = x
    pi = [inv[row - 1] for row in tau]
    if any(pi[i] == i for i in range(n)):
        raise ValueError("relative permutation has a fixed point")
    seen = [False] * n
    lengths: list[int] = []
    for i in range(n):
        if seen[i]:
            continue
        j = i
        length = 0
        while not seen[j]:
            seen[j] = True
            length += 1
            j = pi[j]
        lengths.append(length)
    return sorted(lengths, reverse=True)


def symmetries(n: int) -> list[tuple[str, Callable[[Point], Point]]]:
    j = lambda z: n + 1 - z
    return [
        ("identity", lambda p: (p[0], p[1])),
        ("rotate90", lambda p: (p[1], j(p[0]))),
        ("rotate180", lambda p: (j(p[0]), j(p[1]))),
        ("rotate270", lambda p: (j(p[1]), p[0])),
        ("reflect_vertical", lambda p: (j(p[0]), p[1])),
        ("reflect_horizontal", lambda p: (p[0], j(p[1]))),
        ("reflect_diagonal", lambda p: (p[1], p[0])),
        ("reflect_antidiagonal", lambda p: (j(p[1]), j(p[0]))),
    ]


def analyse(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError("input must be an object")
    p = raw.get("p")
    if isinstance(p, bool) or not isinstance(p, int) or p < 5:
        raise ValueError("p must be an integer at least 5")
    n = p - 1
    sigma = parse_perm(raw.get("sigma"), n, "sigma")
    tau = parse_perm(raw.get("tau"), n, "tau")
    verify_seed(sigma, tau)
    target_cycles = relative_cycles(sigma, tau)

    orbit: list[dict[str, Any]] = []
    seen_sets: set[tuple[Point, ...]] = set()
    for name, transform in symmetries(n):
        s2 = points_to_perm([transform(p) for p in layer_points(sigma)], n)
        t2 = points_to_perm([transform(p) for p in layer_points(tau)], n)
        for swapped in (False, True):
            a, b = (t2, s2) if swapped else (s2, t2)
            verify_seed(a, b)
            cycles = relative_cycles(a, b)
            if cycles != target_cycles:
                raise ValueError(f"cycle partition changed under {name}, swap={swapped}")
            selected = tuple(sorted(layer_points(a) + layer_points(b)))
            seen_sets.add(selected)
            orbit.append({"symmetry": name, "layer_swap": swapped, "cycles": cycles})

    collinear = [(1, 1), (2, 2), (3, 3)]
    row_swap = {1: 1, 2: 2, 3: 4, 4: 3}
    relabelled = [(x, row_swap[y]) for x, y in collinear]
    if det(*collinear) != 0 or det(*relabelled) == 0:
        raise ValueError("row-relabel counterexample failed")

    return {
        "p": p,
        "n": n,
        "relative_cycle_partition": target_cycles,
        "verified_group_operations": len(orbit),
        "distinct_selected_sets_in_orbit": len(seen_sets),
        "row_relabel_collinear_before": collinear,
        "row_relabel_noncollinear_after": relabelled,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        result = analyse(raw)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
