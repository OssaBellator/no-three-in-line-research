#!/usr/bin/env python3
"""Finite checks for completed reciprocal and digital prime-power channels.

The script verifies the claims in docs/28-prime-power-completed-reciprocals.md:
- valuation-completed reciprocals are full involutive permutations;
- every real secant obeys the exact stratum quadratic and the stated
  Hensel-tangent line bound;
- the affine companion map is fixed-point-free, one full cycle, and has
  bounded corresponding-column vertical displacement multiplicity;
- the listed binary digit-linear channels at N=8,16,32 contain no real
  collinear triple.

All checks use exact integer arithmetic.  They are sanity checks, not proofs
for arbitrary prime powers.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd

Point = tuple[int, int]

DIGITAL_MASKS: dict[int, tuple[int, ...]] = {
    3: (4, 2, 5),
    4: (8, 4, 2, 13),
    5: (28, 8, 2, 25, 29),
}


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


def line_occupancies(points: list[Point]) -> dict[tuple[int, int, int], set[Point]]:
    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    for a, b in combinations(points, 2):
        key = line_key(a, b)
        lines[key].add(a)
        lines[key].add(b)
    return lines


def valuation(value: int, p: int) -> int:
    if value == 0:
        raise ValueError("valuation(0) is infinite and must be handled separately")
    value = abs(value)
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def residue_valuation(value: int, p: int, k: int) -> int:
    if value == 0:
        return k
    return min(valuation(value, p), k)


def completed_reciprocal(p: int, k: int, parameters: tuple[int, ...]) -> list[Point]:
    if len(parameters) != k:
        raise ValueError("one parameter is required for each nonzero valuation stratum")
    n = p**k
    points: list[Point] = []
    for x in range(n):
        if x == 0:
            y = 0
        else:
            r = valuation(x, p)
            modulus = p ** (k - r)
            c = parameters[r] % modulus
            if gcd(c, p) != 1:
                raise ValueError("every stratum parameter must be a unit")
            unit = x // (p**r)
            y = p**r * ((c * pow(unit, -1, modulus)) % modulus)
        points.append((x, y))
    return points


def square_root_count_formula(p: int, m: int, delta: int) -> int:
    modulus = p**m
    delta %= modulus
    if delta == 0:
        return p ** (m // 2)
    nu = valuation(delta, p)
    if nu % 2:
        return 0
    t = nu // 2
    unit = delta // (p ** (2 * t))
    if pow(unit % p, (p - 1) // 2, p) != 1:
        return 0
    return 2 * p**t


def line_bound(
    line: tuple[int, int, int],
    p: int,
    k: int,
    parameters: tuple[int, ...],
) -> int:
    A, B, C = line
    assert gcd(abs(A), abs(B)) == 1
    if C == 0:
        return 2 * k + 1
    h = valuation(C, p)
    if h >= k:
        return 2 * k
    if A % p == 0 or B % p == 0:
        return 1
    m = k - h
    top_constant = C // (p**h)
    delta = top_constant * top_constant - 4 * A * B * parameters[h]
    return 2 * h + square_root_count_formula(p, m, delta)


def verify_square_root_formula(max_prime: int, max_exponent: int) -> int:
    checks = 0
    for p in (3, 5, 7, 11):
        if p > max_prime:
            continue
        for m in range(1, max_exponent + 1):
            modulus = p**m
            for delta in range(modulus):
                brute = sum(1 for z in range(modulus) if (z * z - delta) % modulus == 0)
                assert brute == square_root_count_formula(p, m, delta), (p, m, delta, brute)
                checks += 1
    return checks


def verify_completed_reciprocals(max_modulus: int) -> int:
    checks = 0
    for p in (3, 5, 7):
        k = 1
        while p**k <= max_modulus:
            n = p**k
            parameters = tuple((1 + p * (r + 1)) % (p ** (k - r)) or 1 for r in range(k))
            parameters = tuple(c if gcd(c, p) == 1 else 1 for c in parameters)
            points = completed_reciprocal(p, k, parameters)
            values = [y for _, y in points]
            assert sorted(values) == list(range(n))
            for x, y in points:
                assert points[y][1] == x
                assert residue_valuation(x, p, k) == residue_valuation(y, p, k)

            lines = line_occupancies(points)
            for line, occupants in lines.items():
                A, B, C = line
                assert all(A * x + B * y == C for x, y in occupants)
                bound = line_bound(line, p, k, parameters)
                assert len(occupants) <= bound, (p, k, line, len(occupants), bound)

                if C != 0:
                    h = valuation(C, p)
                    if h < k and A % p and B % p:
                        lower = [
                            (x, y)
                            for x, y in occupants
                            if x and valuation(x, p) < h
                        ]
                        assert len(lower) <= 2 * h
                        top = [
                            (x, y)
                            for x, y in occupants
                            if x and valuation(x, p) == h
                        ]
                        top_constant = C // (p**h)
                        delta = top_constant**2 - 4 * A * B * parameters[h]
                        if delta % p == 0:
                            target = (top_constant * pow(2 * A, -1, p)) % p
                            assert all(((x // (p**h)) - target) % p == 0 for x, _ in top)
            checks += len(lines) + n
            k += 1
    return checks


def companion_map(y: int, p: int, k: int) -> int:
    n = p**k
    q = p if p % 2 else 4
    return ((1 + q) * y + 1) % n


def cycle_length_of_zero(permutation: list[int]) -> int:
    seen: set[int] = set()
    value = 0
    while value not in seen:
        seen.add(value)
        value = permutation[value]
    assert value == 0
    return len(seen)


def verify_companion_layers(max_modulus: int) -> int:
    checks = 0
    for p in (2, 3, 5, 7):
        k = 1
        while p**k <= max_modulus:
            n = p**k
            sigma = [companion_map(y, p, k) for y in range(n)]
            assert sorted(sigma) == list(range(n))
            assert all(sigma[y] != y for y in range(n))
            assert cycle_length_of_zero(sigma) == n

            displacement = Counter(sigma[y] - y for y in range(n))
            cap = p if p % 2 else min(4, n)
            assert max(displacement.values()) <= cap

            parameters = tuple(1 for _ in range(k))
            first = completed_reciprocal(p, k, parameters)
            first_values = [y for _, y in first]
            second_values = [sigma[y] for y in first_values]
            assert sorted(second_values) == list(range(n))
            assert all(first_values[x] != second_values[x] for x in range(n))

            inverse_first = {y: x for x, y in first}
            inverse_sigma = {sigma[y]: y for y in range(n)}
            transition = [
                inverse_first[inverse_sigma[first_values[x]]]
                for x in range(n)
            ]
            assert cycle_length_of_zero(transition) == n
            checks += n
            k += 1
    return checks


def binary_rank(row_masks: tuple[int, ...]) -> int:
    rows = list(row_masks)
    rank = 0
    width = len(rows)
    for column in range(width):
        pivot = next((i for i in range(rank, width) if rows[i] & (1 << column)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(width):
            if i != rank and rows[i] & (1 << column):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def digital_channel(k: int, row_masks: tuple[int, ...]) -> list[Point]:
    n = 1 << k
    return [
        (
            x,
            sum((((x & mask).bit_count() & 1) << i) for i, mask in enumerate(row_masks)),
        )
        for x in range(n)
    ]


def verify_digital_channels() -> int:
    checks = 0
    for k, masks in DIGITAL_MASKS.items():
        n = 1 << k
        assert binary_rank(masks) == k
        points = digital_channel(k, masks)
        assert sorted(y for _, y in points) == list(range(n))
        assert all(determinant(a, b, c) != 0 for a, b, c in combinations(points, 3))
        checks += n * (n - 1) * (n - 2) // 6
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()
    if args.max_modulus < 32:
        parser.error("--max-modulus must be at least 32")

    root_checks = verify_square_root_formula(max_prime=11, max_exponent=3)
    reciprocal_checks = verify_completed_reciprocals(args.max_modulus)
    companion_checks = verify_companion_layers(args.max_modulus)
    digital_checks = verify_digital_channels()
    print(
        f"verified through N={args.max_modulus}: "
        f"square-roots={root_checks}, "
        f"completed-reciprocals={reciprocal_checks}, "
        f"companion={companion_checks}, "
        f"digital-triples={digital_checks}"
    )


if __name__ == "__main__":
    main()
