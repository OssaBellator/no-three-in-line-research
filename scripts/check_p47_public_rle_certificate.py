#!/usr/bin/env python3
"""Independently verify the first public c4-46 RLE record as a p=47 seed."""
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


def decode_rle(rle: str) -> list[Point]:
    x = y = 0
    number = ""
    points: list[Point] = []
    terminated = False
    for ch in rle:
        if ch.isdigit():
            number += ch
            continue
        if ch not in "bo$!":
            raise ValueError(f"invalid RLE symbol {ch!r}")
        run = int(number) if number else 1
        number = ""
        if run < 1:
            raise ValueError("RLE run lengths must be positive")
        if ch == "b":
            x += run
        elif ch == "o":
            points.extend((x + offset, y) for offset in range(run))
            x += run
        elif ch == "$":
            y += run
            x = 0
        else:
            if run != 1:
                raise ValueError("terminator cannot have a run length")
            terminated = True
            break
    if not terminated:
        raise ValueError("RLE has no terminator")
    return points


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def rotate(point: Point, n: int) -> Point:
    x, y = point
    return n - 1 - y, x


def colour_swapped(points: set[Point], n: int) -> tuple[list[int], list[int]]:
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
        adjacency[edge].append((rotate(edge, n), 1))
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
                        raise ValueError("no swapped equivariant edge-colouring")
                else:
                    colours[other] = wanted
                    queue.append(other)
    layers = [[-1] * n, [-1] * n]
    for (x, y), colour in colours.items():
        if layers[colour][x] != -1:
            raise ValueError("colour class repeats a column")
        layers[colour][x] = y
    if any(sorted(layer) != list(range(n)) for layer in layers):
        raise ValueError("colour classes are not permutations")
    return layers[0], layers[1]


def cycle_data(permutation: list[int], bits: list[int] | None = None) -> tuple[list[int], list[int]]:
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
    return [length for length, _ in records], [parity for _, parity in records]


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
        if not isinstance(raw, dict) or raw.get("p") != 47:
            raise ValueError("expected one p=47 object")
        n = 46
        rle = raw.get("rle")
        if not isinstance(rle, str):
            raise ValueError("rle must be a string")
        point_list = decode_rle(rle)
        points = set(point_list)
        if len(point_list) != 2 * n or len(points) != 2 * n:
            raise ValueError("RLE does not encode 92 distinct points")
        if any(not (0 <= x < n and 0 <= y < n) for x, y in points):
            raise ValueError("RLE point outside [46]^2")
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

        sigma, tau = colour_swapped(points, n)
        if sigma != [x - 1 for x in int_list(raw, "sigma", n)]:
            raise ValueError("stored sigma does not match RLE colouring")
        if tau != [x - 1 for x in int_list(raw, "tau", n)]:
            raise ValueError("stored tau does not match RLE colouring")
        reversal = [n - 1 - x for x in range(n)]
        inverse = [0] * n
        for x, y in enumerate(sigma):
            inverse[y] = x
        if tau != [inverse[reversal[x]] for x in range(n)]:
            raise ValueError("forced swapped second-layer identity failed")
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
        pair_cycles, pair_parities = cycle_data(rho, orientations)
        if pair_cycles != int_list(raw, "pair_cycle_partition"):
            raise ValueError("pair cycle partition mismatch")
        if pair_parities != int_list(raw, "pair_cycle_orientation_parities"):
            raise ValueError("pair cycle parity mismatch")

        relative = [inverse[tau[x]] for x in range(n)]
        relative_cycles, _ = cycle_data(relative)
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
        if raw.get("valid_seed") is not True:
            raise ValueError("valid_seed must be true")
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps({
        "outcome": "p47_public_rle_certificate_verified",
        "p": 47,
        "n": 46,
        "selected_points": len(points),
        "determinant_checks": checks,
        "minimum_absolute_determinant": minimum,
        "quarter_turn_mode": "swapped",
        "pair_cycle_partition": pair_cycles,
        "relative_cycle_partition": relative_cycles,
        "source_repository": raw.get("source_repository"),
        "source_path": raw.get("source_path"),
        "source_blob_sha": raw.get("source_blob_sha"),
        "asymptotic_seed_theorem_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
