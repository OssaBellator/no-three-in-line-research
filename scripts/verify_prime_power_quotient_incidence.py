#!/usr/bin/env python3
"""Verify CMR82--CMR84 on finite recursive quotient states."""

from __future__ import annotations

import argparse
from itertools import combinations
from math import gcd
from typing import Sequence

Point = tuple[int, int]
Line = tuple[int, int, int]


def primitive_line(first: Point, second: Point) -> Line:
    x1, y1 = first
    x2, y2 = second
    a0 = y1 - y2
    b0 = x2 - x1
    divisor = gcd(abs(a0), abs(b0))
    assert divisor > 0
    a = a0 // divisor
    b = b0 // divisor
    c = (a0 * x1 + b0 * y1) // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def build_state(n: int) -> tuple[list[int], list[int]]:
    first = list(range(n))
    second = [(x + 1) % n for x in range(n)]
    assert all(first[x] != second[x] for x in range(n))
    return first, second


def quotient_layers(
    first: Sequence[int], second: Sequence[int], modulus: int
) -> tuple[list[int], list[int]]:
    result: list[list[int]] = []
    for layer in (first, second):
        quotient: list[int] = []
        for residue in range(modulus):
            values = {
                layer[x] % modulus
                for x in range(residue, len(layer), modulus)
            }
            assert len(values) == 1
            quotient.append(values.pop())
        assert sorted(quotient) == list(range(modulus))
        result.append(quotient)
    assert all(result[0][x] != result[1][x] for x in range(modulus))
    return result[0], result[1]


def quotient_state(quotients: Sequence[Sequence[int]]) -> set[Point]:
    return {
        (x, quotient[x])
        for quotient in quotients
        for x in range(len(quotient))
    }


def quotient_occupancy(line: Line, selected: set[Point], modulus: int) -> int:
    a, b, c = line
    return sum((a * x + b * y - c) % modulus == 0 for x, y in selected)


def reduced_point(point: Point, modulus: int) -> Point:
    return point[0] % modulus, point[1] % modulus


def verify_instance(p: int, k: int, s: int) -> tuple[int, int, int, int]:
    n = p**k
    modulus = p**s
    t = n // modulus
    first, second = build_state(n)
    quotients = quotient_layers(first, second, modulus)
    selected_quotient = quotient_state(quotients)
    selected_full = {(x, first[x]) for x in range(n)} | {
        (x, second[x]) for x in range(n)
    }

    distinct_count = 0
    collision_count = 0
    modular_excess = 0
    collision_energy = 0
    total_energy = 0
    checks = 0

    for first_point, second_point in combinations(selected_full, 2):
        line = primitive_line(first_point, second_point)
        occupancy = quotient_occupancy(line, selected_quotient, modulus)
        total_energy += occupancy

        first_reduced = reduced_point(first_point, modulus)
        second_reduced = reduced_point(second_point, modulus)
        if first_reduced != second_reduced:
            distinct_count += 1
            assert occupancy >= 2
            modular_excess += occupancy - 2
        else:
            collision_count += 1
            collision_energy += occupancy

            dx = second_point[0] - first_point[0]
            dy = second_point[1] - first_point[1]
            assert dx % modulus == 0 and dy % modulus == 0
            u = dx // modulus
            v = dy // modulus
            divisor = gcd(abs(u), abs(v))
            assert divisor > 0
            u0 = u // divisor
            v0 = v // divisor
            x0, y0 = first_reduced
            carry_occupancy = sum(
                (-v0 * (x - x0) + u0 * (y - y0)) % modulus == 0
                for x, y in selected_quotient
            )
            assert carry_occupancy == occupancy
        checks += 1

    expected_collisions = 2 * modulus * (t * (t - 1) // 2)
    assert collision_count == expected_collisions == n * (t - 1)
    assert distinct_count + collision_count == len(selected_full) * (len(selected_full) - 1) // 2
    assert total_energy == 2 * distinct_count + modular_excess + collision_energy

    return checks, distinct_count, collision_count, total_energy


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()

    total_checks = 0
    summaries: list[str] = []
    for p, k in ((5, 2), (5, 3), (13, 2)):
        n = p**k
        if n > args.max_modulus:
            continue
        for s in range(1, k):
            checks, distinct, collisions, energy = verify_instance(p, k, s)
            total_checks += checks
            summaries.append(
                f"N={n},s={s},distinct={distinct},collision={collisions},J={energy}"
            )

    print(
        "verified quotient-incidence decomposition: "
        + "; ".join(summaries)
        + f"; checks={total_checks}"
    )


if __name__ == "__main__":
    main()
