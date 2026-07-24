#!/usr/bin/env python3
"""Exact finite checks for CMR96--CMR99."""
from __future__ import annotations

import argparse
import random
from collections import Counter
from fractions import Fraction
from itertools import combinations


def determinant(
    a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]
) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def nonsquares(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [x for x in range(1, p) if x not in squares]


def reciprocal_permutation(p: int, b: int, c: int) -> tuple[int, ...]:
    return tuple(
        b if x == 0 else (b + c * pow(x, -1, p)) % p
        for x in range(p)
    )


def allowed_maps(
    p: int, current_b: int, current_c: int, first: int, second: int
) -> list[tuple[int, int, tuple[int, ...]]]:
    current = reciprocal_permutation(p, current_b, current_c)
    allowed = []
    for c in nonsquares(p):
        for b in range(p):
            values = reciprocal_permutation(p, b, c)
            if values[first] == current[first]:
                continue
            if values[second] == current[second]:
                continue
            allowed.append((b, c, values))
    return allowed


def verify_parameter_bank(p: int) -> tuple[int, int, int]:
    h = (p - 1) // 2
    current_b = 0
    current_c = nonsquares(p)[0]
    first, second = 0, 1
    allowed = allowed_maps(p, current_b, current_c, first, second)
    assert len(allowed) == h * (p - 2) + 1

    single_counts: Counter[tuple[int, int]] = Counter()
    pair_counts: Counter[tuple[int, int, int, int]] = Counter()
    for _b, _c, values in allowed:
        for x, y in enumerate(values):
            single_counts[(x, y)] += 1
        for x1, x2 in combinations(range(p), 2):
            pair_counts[(x1, values[x1], x2, values[x2])] += 1

    assert max(single_counts.values(), default=0) <= h
    assert max(pair_counts.values(), default=0) <= 1
    current = reciprocal_permutation(p, current_b, current_c)
    assert all(values[first] != current[first] for _, _, values in allowed)
    assert all(values[second] != current[second] for _, _, values in allowed)
    return len(allowed), len(single_counts), len(pair_counts)


def balanced_state_25(seed: int) -> tuple[list[list[int]], dict[tuple[int, int], tuple[int, int]]]:
    p = 5
    rng = random.Random(seed)
    ns = nonsquares(p)
    root_c = rng.choice(ns)
    root_b0, root_b1 = rng.sample(range(p), 2)
    root = [
        reciprocal_permutation(p, root_b0, root_c),
        reciprocal_permutation(p, root_b1, root_c),
    ]

    values = [[0] * 25 for _ in range(2)]
    parameters: dict[tuple[int, int], tuple[int, int]] = {}
    for layer in range(2):
        for prefix in range(p):
            b = rng.randrange(p)
            c = rng.choice(ns)
            parameters[(layer, prefix)] = (b, c)
            local = reciprocal_permutation(p, b, c)
            for digit in range(p):
                column = prefix + p * digit
                values[layer][column] = root[layer][prefix] + p * local[digit]

    assert all(sorted(layer) == list(range(25)) for layer in values)
    assert all(values[0][x] != values[1][x] for x in range(25))
    return values, parameters


def replace_node(
    values: list[list[int]], layer: int, prefix: int, new_map: tuple[int, ...]
) -> list[list[int]]:
    p = 5
    changed = [row[:] for row in values]
    columns = [prefix + p * digit for digit in range(p)]
    lower_row = values[layer][prefix] % p
    for digit, column in enumerate(columns):
        old = values[layer][column]
        high_suffix = old // (p * p)
        assert high_suffix == 0
        changed[layer][column] = lower_row + p * new_map[digit]
    assert all(sorted(row) == list(range(25)) for row in changed)
    assert all(changed[0][x] != changed[1][x] for x in range(25))
    return changed


def points(values: list[list[int]]) -> list[tuple[int, int, int]]:
    return [
        (x, values[layer][x], layer)
        for layer in range(2)
        for x in range(len(values[0]))
    ]


def potential(values: list[list[int]]) -> int:
    return sum(
        determinant(a[:2], b[:2], c[:2]) == 0
        for a, b, c in combinations(points(values), 3)
    )


def verify_node_collateral(seed: int) -> tuple[int, int, int]:
    p = 5
    h = 2
    values, parameters = balanced_state_25(seed)
    layer = 0
    prefix = 0
    current_b, current_c = parameters[(layer, prefix)]
    first, second = 0, 1
    allowed = allowed_maps(p, current_b, current_c, first, second)
    denominator = h * (p - 2) + 1
    assert len(allowed) == denominator

    columns = [prefix + p * digit for digit in range(p)]
    old_block = {(x, values[layer][x], layer) for x in columns}
    fixed = [point for point in points(values) if point not in old_block]

    certificate_sets = {1: set(), 2: set(), 3: set()}
    collateral_values = []
    for _b, _c, local in allowed:
        changed = replace_node(values, layer, prefix, local)
        new_block = [(x, changed[layer][x]) for x in columns]
        collateral = 0

        for rank in (1, 2, 3):
            for selected in combinations(new_block, rank):
                remaining = 3 - rank
                for outside in combinations(fixed, remaining):
                    triple = tuple(sorted(selected + tuple(point[:2] for point in outside)))
                    if determinant(*triple) != 0:
                        continue
                    collateral += 1
                    digits = {cell[0] // p for cell in selected}
                    node_rank = len(digits)
                    certificate_sets[node_rank].add(triple)
        collateral_values.append(collateral)

    average = Fraction(sum(collateral_values), denominator)
    bound = (
        Fraction(h, denominator) * len(certificate_sets[1])
        + Fraction(1, denominator)
        * (len(certificate_sets[2]) + len(certificate_sets[3]))
    )
    assert average <= bound

    old_potential = potential(values)
    fixed_potential = sum(
        determinant(a[:2], b[:2], c[:2]) == 0
        for a, b, c in combinations(fixed, 3)
    )
    assert old_potential - fixed_potential >= 0

    return len(certificate_sets[1]), len(certificate_sets[2]), len(certificate_sets[3])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=29)
    parser.add_argument("--seeds", type=int, default=4)
    args = parser.parse_args()

    parameter_instances = 0
    allowed_states = 0
    single_cells = 0
    pair_cells = 0
    for p in range(5, args.max_prime + 1, 2):
        if not is_prime(p) or p % 4 != 1:
            continue
        states, singles, pairs = verify_parameter_bank(p)
        parameter_instances += 1
        allowed_states += states
        single_cells += singles
        pair_cells += pairs

    rank_counts = [0, 0, 0]
    for seed in range(args.seeds):
        counts = verify_node_collateral(seed)
        for index, count in enumerate(counts):
            rank_counts[index] += count

    print(
        "verified recursive-compatible star bank "
        f"prime-instances={parameter_instances}; allowed-states={allowed_states}; "
        f"single-cells={single_cells}; pair-cells={pair_cells}; "
        f"node-rank-counts={tuple(rank_counts)}"
    )


if __name__ == "__main__":
    main()
