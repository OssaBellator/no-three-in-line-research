#!/usr/bin/env python3
"""Independently verify the Wikimedia 58x58 coordinate record as a p=59 seed."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;,."
Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def rotate(point: Point, n: int) -> Point:
    x, y = point
    return n - 1 - y, x


def equivariant_colour(points: set[Point], n: int, rotation_parity: int) -> tuple[list[int], list[int]] | None:
    rows: dict[int, list[Point]] = defaultdict(list)
    columns: dict[int, list[Point]] = defaultdict(list)
    for edge in points:
        columns[edge[0]].append(edge)
        rows[edge[1]].append(edge)
    adjacency: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    for edge in points:
        for other in rows[edge[1]] + columns[edge[0]]:
            if other != edge:
                adjacency[edge].append((other, 1))
        adjacency[edge].append((rotate(edge, n), rotation_parity))
    colours: dict[Point, int] = {}
    for start in sorted(points):
        if start in colours:
            continue
        colours[start] = 0
        queue = deque([start])
        while queue:
            edge = queue.popleft()
            for other, parity in adjacency[edge]:
                wanted = colours[edge] ^ parity
                if other in colours:
                    if colours[other] != wanted:
                        return None
                else:
                    colours[other] = wanted
                    queue.append(other)
    layers = [[-1] * n, [-1] * n]
    for (x, y), colour in colours.items():
        if layers[colour][x] != -1:
            return None
        layers[colour][x] = y
    if any(sorted(layer) != list(range(n)) for layer in layers):
        return None
    return layers[0], layers[1]


def cycle_records(permutation: list[int], bits: list[int] | None = None) -> list[tuple[int, int]]:
    seen = [False] * len(permutation)
    records: list[tuple[int, int]] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        cycle: list[int] = []
        current = start
        while not seen[current]:
            seen[current] = True
            cycle.append(current)
            current = permutation[current]
        parity = 0 if bits is None else sum(bits[i] for i in cycle) % 2
        records.append((len(cycle), parity))
    records.sort(reverse=True)
    return records


def int_list(raw: dict[str, Any], key: str, length: int | None = None) -> list[int]:
    value = raw.get(key)
    if not isinstance(value, list) or any(isinstance(x, bool) or not isinstance(x, int) for x in value):
        raise ValueError(f"{key} must be an integer list")
    if length is not None and len(value) != length:
        raise ValueError(f"{key} must have length {length}")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.input.read_text())
        if not isinstance(raw, dict) or raw.get("p") != 59:
            raise ValueError("expected one p=59 object")
        n = 58
        point_raw = raw.get("points")
        if not isinstance(point_raw, list):
            raise ValueError("points must be a list")
        point_list: list[Point] = []
        for entry in point_raw:
            if not isinstance(entry, list) or len(entry) != 2 or any(isinstance(x, bool) or not isinstance(x, int) for x in entry):
                raise ValueError("each point must be an integer pair")
            point_list.append((entry[0], entry[1]))
        points = set(point_list)
        if len(point_list) != 2 * n or len(points) != 2 * n:
            raise ValueError("coordinate record does not contain 116 distinct points")
        if any(not (0 <= x < n and 0 <= y < n) for x, y in points):
            raise ValueError("point outside [58]^2")
        rows = Counter(y for _, y in points)
        columns = Counter(x for x, _ in points)
        if any(rows[i] != 2 or columns[i] != 2 for i in range(n)):
            raise ValueError("configuration is not saturated")
        if {rotate(point, n) for point in points} != points:
            raise ValueError("configuration is not quarter-turn invariant")

        checks = 0
        minimum: int | None = None
        for a, b, c in combinations(sorted(points), 3):
            checks += 1
            value = determinant(a, b, c)
            if value == 0:
                raise ValueError(f"collinear triple {a}, {b}, {c}")
            magnitude = abs(value)
            minimum = magnitude if minimum is None else min(minimum, magnitude)
        if checks != comb(2 * n, 3):
            raise ValueError("determinant count mismatch")

        fixed = equivariant_colour(points, n, 0)
        swapped = equivariant_colour(points, n, 1)
        if fixed is not None or swapped is None:
            raise ValueError("expected swapped-only quarter-turn action")
        sigma, tau = swapped
        if sigma != [x - 1 for x in int_list(raw, "sigma", n)]:
            raise ValueError("stored sigma mismatch")
        if tau != [x - 1 for x in int_list(raw, "tau", n)]:
            raise ValueError("stored tau mismatch")
        reversal = [n - 1 - x for x in range(n)]
        inverse = [0] * n
        for x, y in enumerate(sigma):
            inverse[y] = x
        if tau != [inverse[reversal[x]] for x in range(n)]:
            raise ValueError("forced swapped layer identity failed")
        if any(sigma[reversal[x]] != reversal[sigma[x]] for x in range(n)):
            raise ValueError("sigma does not commute with reversal")

        m = n // 2
        rho: list[int] = []
        orientations: list[int] = []
        for source in range(m):
            target = sigma[source]
            rho.append(target if target < m else n - 1 - target)
            orientations.append(0 if target < m else 1)
        if [x + 1 for x in rho] != int_list(raw, "pair_permutation", m):
            raise ValueError("pair permutation mismatch")
        if orientations != int_list(raw, "pair_orientations", m):
            raise ValueError("pair orientations mismatch")
        pair_records = cycle_records(rho, orientations)
        pair_cycles = [length for length, _ in pair_records]
        pair_parities = [parity for _, parity in pair_records]
        if pair_cycles != int_list(raw, "pair_cycle_partition"):
            raise ValueError("pair cycle partition mismatch")
        if pair_parities != int_list(raw, "pair_cycle_orientation_parities"):
            raise ValueError("pair cycle parity mismatch")

        relative = [inverse[tau[x]] for x in range(n)]
        relative_cycles = [length for length, _ in cycle_records(relative)]
        if relative_cycles != int_list(raw, "relative_cycle_partition"):
            raise ValueError("relative cycle partition mismatch")

        rows_to_columns: dict[int, list[int]] = defaultdict(list)
        for x, y in points:
            rows_to_columns[y].append(x)
        code = "o" + "".join(ALPHABET[x] for y in range(n) for x in sorted(rows_to_columns[y]))
        if code != raw.get("standard_code"):
            raise ValueError("standard code mismatch")
        if checks != raw.get("determinant_checks") or minimum != raw.get("minimum_absolute_determinant"):
            raise ValueError("stored determinant statistics mismatch")
        if raw.get("maximal_grid_lines_checked") != 476358:
            raise ValueError("stored maximal-line count mismatch")
        if raw.get("valid_seed") is not True:
            raise ValueError("valid_seed must be true")
        if raw.get("source_author") != "Prellberg" or raw.get("source_license") != "CC BY-SA 4.0":
            raise ValueError("source attribution metadata mismatch")
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps({
        "outcome": "p59_wikimedia_coordinate_certificate_verified",
        "p": 59,
        "n": 58,
        "selected_points": len(points),
        "determinant_checks": checks,
        "minimum_absolute_determinant": minimum,
        "maximal_grid_lines_checked": raw.get("maximal_grid_lines_checked"),
        "quarter_turn_mode": "swapped",
        "pair_cycle_partition": pair_cycles,
        "relative_cycle_partition": relative_cycles,
        "source_page": raw.get("source_page"),
        "source_author": raw.get("source_author"),
        "source_license": raw.get("source_license"),
        "asymptotic_seed_theorem_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
