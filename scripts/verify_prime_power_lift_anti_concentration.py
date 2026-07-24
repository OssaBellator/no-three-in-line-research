#!/usr/bin/env python3
"""Exhaustively verify CMR41--CMR43 for the first small prime lifts."""
from __future__ import annotations

import argparse
from itertools import combinations, product, permutations


def determinant(points: list[tuple[int, int]]) -> int:
    a, b, c = points
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def nonsquares(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [x for x in range(1, p) if x not in squares]


def conic_family(p: int) -> list[tuple[int, ...]]:
    h = (p - 1) // 2
    return [
        tuple(b if x == 0 else (b + c * pow(x, -1, p)) % p for x in range(p))
        for b in range(1, h + 1)
        for c in nonsquares(p)
    ]


def quotient_row(a: int, layer: int, column: int) -> int:
    return column if layer == 0 else (column + 1) % a


def fibre_data(
    p: int,
    a: int,
    columns: tuple[int, int, int],
    layers: tuple[int, int, int],
):
    keys: dict[tuple[int, int], list[int]] = {}
    lower_rows = []
    top_columns = []
    for i, (x, layer) in enumerate(zip(columns, layers)):
        lower = x % a
        top = x // a
        key = (layer, lower)
        keys.setdefault(key, []).append(i)
        lower_rows.append(quotient_row(a, layer, lower))
        top_columns.append(top)
    return keys, lower_rows, top_columns


def points_from_digits(
    a: int,
    columns: tuple[int, int, int],
    lower_rows: list[int],
    row_digits: list[int],
) -> list[tuple[int, int]]:
    return [
        (columns[i], lower_rows[i] + a * row_digits[i])
        for i in range(3)
    ]


def uniform_outputs(p: int, indices: list[int]):
    for values in permutations(range(p), len(indices)):
        yield dict(zip(indices, values))


def verify_triple(
    p: int,
    a: int,
    columns: tuple[int, int, int],
    layers: tuple[int, int, int],
    family: list[tuple[int, ...]],
) -> tuple[int, int]:
    keys, lower_rows, top_columns = fibre_data(p, a, columns, layers)

    # CMR41: changing one top row digit changes the determinant by a nonzero
    # multiple of the difference of the other two columns.
    base_digits = [0, 0, 0]
    base_det = determinant(points_from_digits(a, columns, lower_rows, base_digits))
    for j in range(3):
        changed = base_digits.copy()
        changed[j] = 1
        delta = determinant(points_from_digits(a, columns, lower_rows, changed)) - base_det
        expected = a * (
            columns[2] - columns[1]
            if j == 0
            else columns[0] - columns[2]
            if j == 1
            else columns[1] - columns[0]
        )
        assert delta == expected and delta != 0

    # CMR42: enumerate all injection outputs in the involved uniform fibres.
    key_items = list(keys.values())
    total = 0
    bad = 0
    choices = [list(uniform_outputs(p, indices)) for indices in key_items]
    for assignment_tuple in product(*choices):
        digits = [0, 0, 0]
        for assignment in assignment_tuple:
            for i, value in assignment.items():
                digits[i] = value
        total += 1
        if determinant(points_from_digits(a, columns, lower_rows, digits)) == 0:
            bad += 1

    all_same = len(keys) == 1
    if all_same:
        assert bad * (p - 2) <= total
    else:
        assert bad * p <= total

    # CMR43: enumerate one conic-family map for every involved fibre.
    conic_total = 0
    conic_bad = 0
    for maps in product(family, repeat=len(key_items)):
        digits = [0, 0, 0]
        for indices, mapping in zip(key_items, maps):
            for i in indices:
                digits[i] = mapping[top_columns[i]]
        conic_total += 1
        if determinant(points_from_digits(a, columns, lower_rows, digits)) == 0:
            conic_bad += 1

    h = (p - 1) // 2
    if all_same:
        assert conic_bad == 0
    else:
        assert conic_bad * h <= conic_total

    return total, conic_total


def verify_prime(p: int) -> tuple[int, int, int]:
    a = p
    n = p * p
    family = conic_family(p)
    triples = 0
    uniform_states = 0
    conic_states = 0
    for columns in combinations(range(n), 3):
        for layers in product((0, 1), repeat=3):
            uniform, conic = verify_triple(p, a, columns, layers, family)
            uniform_states += uniform
            conic_states += conic
            triples += 1
    return triples, uniform_states, conic_states


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=5)
    args = parser.parse_args()

    triples = 0
    uniform_states = 0
    conic_states = 0
    primes = 0
    for p in (3, 5):
        if p > args.max_prime:
            continue
        t, u, c = verify_prime(p)
        triples += t
        uniform_states += u
        conic_states += c
        primes += 1

    print(
        f"verified lift anti-concentration primes={primes}; triples={triples}; "
        f"uniform-assignments={uniform_states}; conic-assignments={conic_states}"
    )


if __name__ == "__main__":
    main()
