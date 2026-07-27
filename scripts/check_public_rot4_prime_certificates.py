#!/usr/bin/env python3
"""Verify public quarter-turn archive certificates for p=41,43,53."""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;,."
Point = tuple[int, int]


def decode_standard_code(code: str, n: int) -> set[Point]:
    if not isinstance(code, str) or not code.startswith("o"):
        raise ValueError("standard code must begin with nonassertive tag o")
    payload = code[1:]
    if len(payload) != 2 * n:
        raise ValueError(f"standard code payload must have length {2*n}")
    index = {ch: i for i, ch in enumerate(ALPHABET)}
    points: set[Point] = set()
    for row in range(n):
        pair = payload[2 * row:2 * row + 2]
        if any(ch not in index for ch in pair):
            raise ValueError("standard code contains an unknown symbol")
        columns = [index[ch] for ch in pair]
        if columns != sorted(columns) or columns[0] == columns[1]:
            raise ValueError("row-pair columns must be distinct and sorted")
        if columns[-1] >= n:
            raise ValueError("standard code column lies outside board")
        points.update((column, row) for column in columns)
    if len(points) != 2 * n:
        raise ValueError("standard code does not decode to 2n distinct points")
    return points


def regenerate_standard_code(points: set[Point], n: int) -> str:
    rows: dict[int, list[int]] = defaultdict(list)
    for x, y in points:
        rows[y].append(x)
    return "o" + "".join(ALPHABET[x] for y in range(n) for x in sorted(rows[y]))


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
                        raise ValueError("no swapped-equivariant edge colouring")
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


def verify_archive(raw: dict[str, Any], archive_dir: Path) -> None:
    source = archive_dir / str(raw["source_file"])
    data = source.read_bytes()
    if len(data) != raw["source_bytes"]:
        raise ValueError(f"archive byte count mismatch for {source.name}")
    if hashlib.sha256(data).hexdigest() != raw["source_sha256"]:
        raise ValueError(f"archive SHA-256 mismatch for {source.name}")
    lines = data.decode("ascii").splitlines()
    if len(lines) != raw["source_records"]:
        raise ValueError(f"archive record count mismatch for {source.name}")
    if not lines or lines[0] != raw["standard_code"]:
        raise ValueError(f"stored code is not first archive record for {source.name}")


def verify_certificate(raw: dict[str, Any], archive_dir: Path | None) -> dict[str, Any]:
    p = raw.get("p")
    n = raw.get("n")
    if p not in (41, 43, 53) or n != p - 1:
        raise ValueError("expected p in {41,43,53} with n=p-1")
    if archive_dir is not None:
        verify_archive(raw, archive_dir)
    points = decode_standard_code(raw.get("standard_code"), n)
    rows = Counter(y for _, y in points)
    columns = Counter(x for x, _ in points)
    if any(rows[i] != 2 or columns[i] != 2 for i in range(n)):
        raise ValueError(f"p={p}: configuration is not saturated")
    if {rotate(point, n) for point in points} != points:
        raise ValueError(f"p={p}: configuration is not quarter-turn invariant")
    checks = 0
    minimum: int | None = None
    for a, b, c in combinations(sorted(points), 3):
        checks += 1
        value = determinant(a, b, c)
        if value == 0:
            raise ValueError(f"p={p}: collinear triple {a}, {b}, {c}")
        magnitude = abs(value)
        minimum = magnitude if minimum is None else min(minimum, magnitude)
    if checks != comb(2 * n, 3):
        raise ValueError(f"p={p}: determinant count mismatch")
    sigma, tau = colour_swapped(points, n)
    if sigma != [x - 1 for x in int_list(raw, "sigma", n)]:
        raise ValueError(f"p={p}: stored sigma mismatch")
    if tau != [x - 1 for x in int_list(raw, "tau", n)]:
        raise ValueError(f"p={p}: stored tau mismatch")
    if any(sigma[x] == tau[x] for x in range(n)):
        raise ValueError(f"p={p}: permutation layers intersect")
    reversal = [n - 1 - x for x in range(n)]
    inverse = [0] * n
    for x, y in enumerate(sigma):
        inverse[y] = x
    if tau != [inverse[reversal[x]] for x in range(n)]:
        raise ValueError(f"p={p}: forced swapped second-layer identity failed")
    if any(sigma[reversal[x]] != reversal[sigma[x]] for x in range(n)):
        raise ValueError(f"p={p}: sigma does not commute with reversal")
    m = n // 2
    rho: list[int] = []
    orientations: list[int] = []
    for source in range(m):
        target = sigma[source]
        rho.append(target if target < m else n - 1 - target)
        orientations.append(0 if target < m else 1)
    if [x + 1 for x in rho] != int_list(raw, "pair_permutation", m):
        raise ValueError(f"p={p}: pair permutation mismatch")
    if orientations != int_list(raw, "pair_orientations", m):
        raise ValueError(f"p={p}: pair orientations mismatch")
    pair_cycles, pair_parities = cycle_data(rho, orientations)
    if pair_cycles != int_list(raw, "pair_cycle_partition"):
        raise ValueError(f"p={p}: pair cycle mismatch")
    if pair_parities != int_list(raw, "pair_cycle_orientation_parities"):
        raise ValueError(f"p={p}: pair parity mismatch")
    relative = [inverse[tau[x]] for x in range(n)]
    relative_cycles, _ = cycle_data(relative)
    if relative_cycles != int_list(raw, "relative_cycle_partition"):
        raise ValueError(f"p={p}: relative cycle mismatch")
    if regenerate_standard_code(points, n) != raw.get("standard_code"):
        raise ValueError(f"p={p}: code regeneration mismatch")
    if checks != raw.get("determinant_checks") or minimum != raw.get("minimum_absolute_determinant"):
        raise ValueError(f"p={p}: stored determinant statistics mismatch")
    if raw.get("valid_seed") is not True:
        raise ValueError(f"p={p}: valid_seed must be true")
    return {
        "p": p,
        "n": n,
        "selected_points": len(points),
        "determinant_checks": checks,
        "minimum_absolute_determinant": minimum,
        "pair_cycle_partition": pair_cycles,
        "relative_cycle_partition": relative_cycles,
        "source_file": raw.get("source_file"),
        "archive_bytes_verified": archive_dir is not None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--archive-dir", type=Path)
    args = parser.parse_args()
    try:
        root = json.loads(args.input.read_text())
        certificates = root.get("certificates") if isinstance(root, dict) else None
        if not isinstance(certificates, list) or len(certificates) != 3:
            raise ValueError("expected exactly three certificates")
        results = [verify_certificate(raw, args.archive_dir) for raw in certificates]
        if [item["p"] for item in results] != [41, 43, 53]:
            raise ValueError("certificates must be ordered p=41,43,53")
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc
    print(json.dumps({
        "outcome": "public_rot4_prime_certificates_verified",
        "certificates": results,
        "every_odd_prime_through_73_now_covered": True,
        "asymptotic_seed_theorem_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
