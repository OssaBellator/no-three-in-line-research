#!/usr/bin/env python3
"""Verify CMR75--CMR78 on finite prefix-block instances."""

from __future__ import annotations

import argparse
from itertools import combinations, permutations, product
from math import factorial
from typing import Iterable, Sequence

Point = tuple[int, int]


def vp_difference(a: int, b: int, p: int) -> int:
    """Return v_p(a-b) for distinct integers a and b."""
    d = abs(a - b)
    assert d > 0
    value = 0
    while d % p == 0:
        d //= p
        value += 1
    return value


def determinant(points: Sequence[Point]) -> int:
    (x1, y1), (x2, y2), (x3, y3) = points
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


def triple_count(points: Iterable[Point]) -> int:
    pts = tuple(points)
    return sum(determinant(triple) == 0 for triple in combinations(pts, 3))


def allowed_matchings(t: int, second: Sequence[int]) -> list[tuple[int, ...]]:
    """Permutations avoiding the identity and one second forbidden matching."""
    assert sorted(second) == list(range(t))
    return [
        pi
        for pi in permutations(range(t))
        if all(pi[i] != i and pi[i] != second[i] for i in range(t))
    ]


def verify_t5_bound() -> int:
    """Check the only block size below the AN1 threshold that can occur here."""
    t = 5
    minimum = factorial(t)
    checks = 0
    for second in permutations(range(t)):
        count = len(allowed_matchings(t, second))
        minimum = min(minimum, count)
        assert count * 128 >= factorial(t)
        checks += 1
    assert minimum == 12
    return checks


def build_state(n: int, shift: int) -> tuple[list[int], list[int]]:
    first = list(range(n))
    second = [(x + shift) % n for x in range(n)]
    assert sorted(first) == list(range(n))
    assert sorted(second) == list(range(n))
    assert all(first[x] != second[x] for x in range(n))
    return first, second


def block_data(
    first: Sequence[int],
    second: Sequence[int],
    p: int,
    s: int,
    residue: int,
) -> tuple[list[int], list[int], list[int], list[tuple[int, ...]]]:
    n = len(first)
    modulus = p**s
    columns = [x for x in range(n) if x % modulus == residue]
    rows = [first[x] for x in columns]
    row_index = {row: index for index, row in enumerate(rows)}

    forbidden_second: list[int] = []
    for index, column in enumerate(columns):
        other_row = second[column]
        if other_row in row_index:
            forbidden_second.append(row_index[other_row])
        else:
            # Complete the partial forbidden matching later.  For the concrete
            # instance used below every opposite row lies in the block.
            forbidden_second.append(index)

    assert sorted(forbidden_second) == list(range(len(columns)))
    allowed = allowed_matchings(len(columns), forbidden_second)
    return columns, rows, forbidden_second, allowed


def rematch_layer(
    first: Sequence[int], columns: Sequence[int], rows: Sequence[int], pi: Sequence[int]
) -> list[int]:
    changed = list(first)
    for index, column in enumerate(columns):
        changed[column] = rows[pi[index]]
    return changed


def verify_block_states() -> tuple[int, tuple[list[int], list[int], list[int], list[tuple[int, ...]]]]:
    """Use N=25 with an opposite matching inside every deepest prefix block."""
    p = 5
    n = 25
    first, second = build_state(n, shift=5)
    columns, rows, forbidden_second, allowed = block_data(
        first, second, p=p, s=1, residue=0
    )

    assert len(columns) == 5
    assert len(allowed) >= factorial(5) / 128

    checks = 0
    for pi in allowed:
        changed = rematch_layer(first, columns, rows, pi)
        assert sorted(changed) == list(range(n))
        assert all(changed[x] != second[x] for x in range(n))
        assert all(changed[x] != first[x] for x in columns)
        assert all(changed[x] == first[x] for x in set(range(n)) - set(columns))
        checks += n

    return checks, (first, second, columns, rows, allowed)


def closest_pair(columns: Sequence[int], p: int) -> tuple[int, int, int] | None:
    valuations = {
        (i, j): vp_difference(columns[i], columns[j], p)
        for i, j in combinations(range(3), 2)
    }
    maximum = max(valuations.values())
    pairs = [pair for pair, value in valuations.items() if value == maximum]
    if len(pairs) != 1:
        return None
    i, j = pairs[0]
    return i, j, maximum


def verify_binary_assignment(p: int, k: int) -> int:
    n = p**k
    loads: dict[tuple[int, int, int], int] = {}
    total = 0
    checks = 0

    for columns in combinations(range(n), 3):
        closest = closest_pair(columns, p)
        if closest is None:
            continue
        i, j, s = closest
        for layers in product(range(2), repeat=3):
            if layers[i] != layers[j]:
                continue
            layer = layers[i]
            modulus = p**s
            residue = columns[i] % modulus
            assert columns[j] % modulus == residue
            third = 3 - i - j
            assert columns[third] % modulus != residue
            key = (s, residue, layer)
            loads[key] = loads.get(key, 0) + 1
            total += 1
            checks += 1

    assert sum(loads.values()) == total
    for s in range(k):
        scale_total = sum(value for (depth, _, _), value in loads.items() if depth == s)
        if scale_total == 0:
            continue
        scale_loads = [
            loads.get((s, residue, layer), 0)
            for layer in range(2)
            for residue in range(p**s)
        ]
        assert max(scale_loads) * (2 * p**s) >= scale_total
    return checks


def compatible_block_cells(cells: Sequence[Point]) -> bool:
    columns = [point[0] for point in cells]
    rows = [point[1] for point in cells]
    return len(set(columns)) == len(columns) and len(set(rows)) == len(rows)


def verify_collateral_identity(
    first: Sequence[int],
    second: Sequence[int],
    columns: Sequence[int],
    rows: Sequence[int],
    allowed: Sequence[Sequence[int]],
) -> int:
    original = {(x, first[x]) for x in range(len(first))} | {
        (x, second[x]) for x in range(len(second))
    }
    anchor = {(x, first[x]) for x in columns}
    fixed = original - anchor

    original_index = {column: index for index, column in enumerate(columns)}
    opposite_cells = {(x, second[x]) for x in columns}
    candidate_cells = {
        (column, row)
        for column in columns
        for row in rows
        if row != first[column] and (column, row) not in opposite_cells
    }

    t_counts = {1: 0, 2: 0, 3: 0}
    universe = list(fixed | candidate_cells)
    for triple in combinations(universe, 3):
        block_cells = [point for point in triple if point in candidate_cells]
        rank = len(block_cells)
        if rank == 0:
            continue
        if len([point for point in triple if point in fixed]) != 3 - rank:
            continue
        if not compatible_block_cells(block_cells):
            continue
        if determinant(triple) == 0:
            t_counts[rank] += 1

    average_numerator = 0
    for pi in allowed:
        changed = rematch_layer(first, columns, rows, pi)
        state = {(x, changed[x]) for x in range(len(changed))} | {
            (x, second[x]) for x in range(len(second))
        }
        average_numerator += triple_count(state)

    expected = average_numerator / len(allowed)
    fixed_triples = triple_count(fixed)
    bound = fixed_triples + 128 * (
        t_counts[1] / len(columns)
        + t_counts[2] / (len(columns) * (len(columns) - 1))
        + t_counts[3]
        / (len(columns) * (len(columns) - 1) * (len(columns) - 2))
    )
    assert expected <= bound + 1e-12

    # Every original anchor cell is absent from every allowed state, so every
    # old triple touching the anchor is destroyed before collateral is added.
    for pi in allowed:
        assert all(pi[index] != index for index in range(len(columns)))

    return len(universe) + len(allowed)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()

    checks = verify_t5_bound()
    block_checks, block_instance = verify_block_states()
    checks += block_checks

    for p, k in ((5, 2), (5, 3), (13, 1)):
        if p**k <= args.max_modulus:
            checks += verify_binary_assignment(p, k)

    first, second, columns, rows, allowed = block_instance
    checks += verify_collateral_identity(first, second, columns, rows, allowed)

    print(
        "verified prefix-star bank: "
        f"allowed_t5_min=12, block_states={len(allowed)}, checks={checks}"
    )


if __name__ == "__main__":
    main()
