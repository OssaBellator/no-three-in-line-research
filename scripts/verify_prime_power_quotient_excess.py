#!/usr/bin/env python3
"""Exact finite checks for CMR85--CMR89."""
from __future__ import annotations

import argparse
import math
import random
from fractions import Fraction
from itertools import combinations

Point = tuple[int, int, int]


def determinant(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def nonsquares(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [x for x in range(1, p) if x not in squares]


def reciprocal_permutation(p: int, b: int, c: int) -> tuple[int, ...]:
    return tuple(
        b if x == 0 else (b + c * pow(x, -1, p)) % p
        for x in range(p)
    )


def balanced_recursive_state(p: int, k: int, seed: int) -> list[list[int]]:
    """Generate one corrected saturated balanced recursive state."""
    rng = random.Random(seed)
    ns = nonsquares(p)

    c = rng.choice(ns)
    b0, b1 = rng.sample(range(p), 2)
    values = [
        list(reciprocal_permutation(p, b0, c)),
        list(reciprocal_permutation(p, b1, c)),
    ]
    modulus = p

    for _depth in range(1, k):
        new_values: list[list[int]] = []
        for layer in range(2):
            local_maps = [
                reciprocal_permutation(p, rng.randrange(p), rng.choice(ns))
                for _ in range(modulus)
            ]
            lifted = [0] * (p * modulus)
            for prefix in range(modulus):
                for digit in range(p):
                    column = prefix + modulus * digit
                    lifted[column] = (
                        values[layer][prefix]
                        + modulus * local_maps[prefix][digit]
                    )
            new_values.append(lifted)
        values = new_values
        modulus *= p

    assert all(sorted(layer) == list(range(modulus)) for layer in values)
    assert all(values[0][x] != values[1][x] for x in range(modulus))
    return values


def primitive_line(p: Point, q: Point) -> tuple[int, int, int]:
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    common = math.gcd(abs(dx), abs(dy))
    assert common > 0
    a = -dy // common
    b = dx // common
    c = a * p[0] + b * p[1]
    return a, b, c


def selected_points(values: list[list[int]]) -> list[Point]:
    n = len(values[0])
    return [
        (x, values[layer][x], layer)
        for layer in range(2)
        for x in range(n)
    ]


def quotient_points(values: list[list[int]], modulus: int) -> list[Point]:
    points: list[Point] = []
    for layer in range(2):
        quotient: dict[int, int] = {}
        for x, y in enumerate(values[layer]):
            column = x % modulus
            row = y % modulus
            if column in quotient:
                assert quotient[column] == row
            else:
                quotient[column] = row
        assert len(quotient) == modulus
        points.extend((x, quotient[x], layer) for x in range(modulus))
    assert len({(x, y) for x, y, _ in points}) == 2 * modulus
    return points


def quotient_energies(
    values: list[list[int]], modulus: int
) -> tuple[int, int, int]:
    points = selected_points(values)
    quotient = quotient_points(values, modulus)
    modular_energy = 0
    collision_energy = 0
    collision_pairs = 0

    for p, q in combinations(points, 2):
        a, b, c = primitive_line(p, q)
        occupancy = sum(
            (a * x + b * y - c) % modulus == 0
            for x, y, _layer in quotient
        )
        projected_p = (p[0] % modulus, p[1] % modulus)
        projected_q = (q[0] % modulus, q[1] % modulus)
        if projected_p != projected_q:
            assert occupancy >= 2
            modular_energy += occupancy - 2
        else:
            assert p[2] == q[2]
            assert occupancy >= 1
            collision_energy += occupancy
            collision_pairs += 1

    return modular_energy, collision_energy, collision_pairs


def modular_triples(values: list[list[int]], modulus: int) -> tuple[int, int, int]:
    quotient = quotient_points(values, modulus)
    total = 0
    three_columns = 0
    vertical = 0
    for p, q, r in combinations(quotient, 3):
        if determinant(p[:2], q[:2], r[:2]) % modulus != 0:
            continue
        total += 1
        if len({p[0], q[0], r[0]}) == 3:
            three_columns += 1
        else:
            vertical += 1
    return total, three_columns, vertical


def rank_one_block_count(
    values: list[list[int]], modulus: int, residue: int, layer: int
) -> int:
    n = len(values[0])
    columns = [x for x in range(n) if x % modulus == residue]
    rows = {values[layer][x] for x in columns}
    moved = {(x, values[layer][x], layer) for x in columns}
    fixed = [point for point in selected_points(values) if point not in moved]

    allowed: list[tuple[int, int]] = []
    for x in columns:
        for y in rows:
            if y == values[layer][x]:
                continue
            if y == values[1 - layer][x]:
                continue
            allowed.append((x, y))

    count = 0
    for candidate in allowed:
        for p, q in combinations(fixed, 2):
            if determinant(candidate, p[:2], q[:2]) == 0:
                count += 1
    return count


def verify_deterministic_state(
    p: int, k: int, modulus: int, seed: int, check_rank_one: bool
) -> tuple[int, int, int, int]:
    values = balanced_recursive_state(p, k, seed)
    n = p**k
    t = n // modulus
    modular_energy, collision_energy, collision_pairs = quotient_energies(
        values, modulus
    )
    z_total, _z_three, _z_vertical = modular_triples(values, modulus)

    assert collision_pairs == n * (t - 1)
    assert modular_energy <= 3 * t * t * z_total
    collision_excess = collision_energy - collision_pairs
    assert 0 <= collision_excess < 2 * n * n

    rank_one = 0
    if check_rank_one:
        rank_one = sum(
            rank_one_block_count(values, modulus, residue, layer)
            for layer in range(2)
            for residue in range(modulus)
        )
        assert rank_one <= t * (modular_energy + collision_excess)

    return modular_energy, collision_energy, z_total, rank_one


def verify_root_modular_average(p: int) -> tuple[int, Fraction]:
    ns = nonsquares(p)
    totals = []
    for c in ns:
        for b0 in range(p):
            for b1 in range(p):
                if b0 == b1:
                    continue
                values = [
                    list(reciprocal_permutation(p, b0, c)),
                    list(reciprocal_permutation(p, b1, c)),
                ]
                total, _three, vertical = modular_triples(values, p)
                assert vertical == 0
                totals.append(total)

    average = Fraction(sum(totals), len(totals))
    bound = Fraction(p + 3, 3) * p * p
    assert average < bound
    return len(totals), average


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=4)
    args = parser.parse_args()

    root_states = 0
    root_average_numerator = 0
    root_average_denominator = 1
    for p in (5, 13):
        states, average = verify_root_modular_average(p)
        root_states += states
        # Keep an exact aggregate checksum rather than a floating-point summary.
        root_average_numerator += average.numerator
        root_average_denominator *= average.denominator

    deterministic_instances = 0
    energy_checks = 0
    rank_one_checks = 0
    for seed in range(args.seeds):
        for p, k, modulus, rank_one in (
            (5, 2, 5, True),
            (5, 3, 5, False),
            (5, 3, 25, False),
        ):
            modular_energy, collision_energy, z_total, rank_one_count = (
                verify_deterministic_state(p, k, modulus, seed, rank_one)
            )
            deterministic_instances += 1
            energy_checks += modular_energy + collision_energy + z_total
            rank_one_checks += rank_one_count

    print(
        "verified quotient excess charging "
        f"root-states={root_states}; root-average-checksum="
        f"{root_average_numerator}/{root_average_denominator}; "
        f"deterministic-instances={deterministic_instances}; "
        f"energy-checksum={energy_checks}; rank-one-certificates={rank_one_checks}"
    )


if __name__ == "__main__":
    main()
