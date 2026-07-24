#!/usr/bin/env python3
"""Exact checks for tangent-cell spacing and binary digit lifts.

The script verifies Theorems CMR11--CMR13:
- coefficient-sensitive exact-real bounds inside completed-reciprocal tangent cells;
- the listed 64-point binary digit-linear no-three channel;
- absence of a direct one-bit block extension of that matrix at 128 points.

Only exact integer arithmetic is used.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations
from math import gcd

Point = tuple[int, int]

DIGITAL_MASKS: dict[int, tuple[int, ...]] = {
    3: (4, 2, 5),
    4: (8, 4, 2, 13),
    5: (25, 8, 2, 11, 20),
    6: (25, 8, 2, 11, 52, 28),
}


def valuation(value: int, p: int) -> int:
    if value == 0:
        raise ValueError("valuation(0) is infinite")
    value = abs(value)
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def determinant(a: Point, b: Point, c: Point) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def line_key(a: Point, b: Point) -> tuple[int, int, int]:
    x1, y1 = a
    x2, y2 = b
    A = y2 - y1
    B = x1 - x2
    C = A * x1 + B * y1
    common = gcd(gcd(abs(A), abs(B)), abs(C))
    if common:
        A //= common
        B //= common
        C //= common
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def completed_reciprocal(p: int, k: int) -> list[Point]:
    n = p**k
    points: list[Point] = []
    for x in range(n):
        if x == 0:
            y = 0
        else:
            r = valuation(x, p)
            modulus = p ** (k - r)
            unit = x // (p**r)
            y = p**r * pow(unit, -1, modulus)
        points.append((x, y))
    return points


def line_occupancies(points: list[Point]) -> dict[tuple[int, int, int], set[Point]]:
    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    for a, b in combinations(points, 2):
        key = line_key(a, b)
        lines[key].add(a)
        lines[key].add(b)
    return lines


def tangent_spacing_bound(A: int, B: int, C: int, p: int, k: int) -> int:
    """CMR11 top-stratum bound for the uniform parameters c_h=1."""
    h = valuation(C, p)
    m = k - h
    modulus = p**m
    reduced_c = C // (p**h)
    delta = (reduced_c * reduced_c - 4 * A * B) % modulus
    small = min(abs(A), abs(B))
    large = max(abs(A), abs(B))

    if delta == 0:
        spacing = p ** ((m + 1) // 2)
        return 1 + ((modulus - 1) * small) // (large * spacing)

    nu = valuation(delta, p)
    if nu % 2:
        return 0
    t = nu // 2
    unit = delta // (p ** (2 * t))
    if pow(unit % p, (p - 1) // 2, p) != 1:
        return 0
    spacing = p ** (m - t)
    return 2 * (1 + ((modulus - 1) * small) // (large * spacing))


def verify_tangent_spacing(max_modulus: int) -> int:
    checks = 0
    for p in (3, 5, 7):
        k = 2
        while p**k <= max_modulus:
            points = completed_reciprocal(p, k)
            for (A, B, C), occupants in line_occupancies(points).items():
                if C == 0:
                    continue
                h = valuation(C, p)
                if h >= k or A % p == 0 or B % p == 0:
                    continue
                top = [
                    (x, y)
                    for x, y in occupants
                    if x != 0 and valuation(x, p) == h
                ]
                bound = tangent_spacing_bound(A, B, C, p, k)
                assert len(top) <= bound, (p, k, (A, B, C), len(top), bound)
                checks += 1
            k += 1
    return checks


def binary_rank(row_masks: tuple[int, ...]) -> int:
    rows = list(row_masks)
    rank = 0
    width = len(rows)
    for column in range(width):
        pivot = next(
            (i for i in range(rank, width) if rows[i] & (1 << column)),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(width):
            if i != rank and rows[i] & (1 << column):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def digital_values(row_masks: tuple[int, ...]) -> list[int]:
    return [
        sum((((x & mask).bit_count() & 1) << i) for i, mask in enumerate(row_masks))
        for x in range(1 << len(row_masks))
    ]


def contains_collinear_triple(values: list[int]) -> bool:
    n = len(values)
    # Equal-column-spacing triples catch almost every failed extension quickly.
    for step in range(1, (n + 1) // 2):
        for x in range(n - 2 * step):
            if values[x + step] - values[x] == values[x + 2 * step] - values[x + step]:
                return True
    for i in range(n):
        for j in range(i + 1, n):
            left = j - i
            row_left = values[j] - values[i]
            for ell in range(j + 1, n):
                if left * (values[ell] - values[i]) == (ell - i) * row_left:
                    return True
    return False


def verify_digital_masks() -> int:
    checks = 0
    for k, masks in DIGITAL_MASKS.items():
        assert binary_rank(masks) == k
        values = digital_values(masks)
        assert sorted(values) == list(range(1 << k))
        assert not contains_collinear_triple(values)
        checks += 1
    return checks


def one_bit_extensions(base: tuple[int, ...]):
    k = len(base)
    for new_column in range(1 << k):
        top = tuple(
            base[i] | (((new_column >> i) & 1) << k)
            for i in range(k)
        )
        for bottom_old in range(1 << k):
            yield top + (bottom_old,)
            yield top + (bottom_old | (1 << k),)


def verify_no_direct_128_extension() -> tuple[int, int]:
    base = DIGITAL_MASKS[6]
    total = 0
    invertible = 0
    for masks in one_bit_extensions(base):
        total += 1
        if binary_rank(masks) != 7:
            continue
        invertible += 1
        assert contains_collinear_triple(digital_values(masks)), masks
    assert total == 8192
    assert invertible == 4096
    return total, invertible


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()
    if args.max_modulus < 25:
        parser.error("--max-modulus must be at least 25")

    tangent = verify_tangent_spacing(args.max_modulus)
    digital = verify_digital_masks()
    total, invertible = verify_no_direct_128_extension()
    print(
        f"verified tangent cells={tangent}; digital channels={digital}; "
        f"direct 128 extensions={total}, invertible={invertible}, survivors=0"
    )


if __name__ == "__main__":
    main()
