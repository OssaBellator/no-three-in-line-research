#!/usr/bin/env python3
"""Exact finite checks for CMR100--CMR101."""
from __future__ import annotations

import argparse
import random
from itertools import combinations


def determinant(
    a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]
) -> int:
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


def balanced_recursive_state(p: int, k: int, seed: int) -> tuple[list[list[int]], dict]:
    rng = random.Random(seed)
    ns = nonsquares(p)
    root_c = rng.choice(ns)
    root_b0, root_b1 = rng.sample(range(p), 2)
    values = [
        list(reciprocal_permutation(p, root_b0, root_c)),
        list(reciprocal_permutation(p, root_b1, root_c)),
    ]
    parameters = {}
    modulus = p

    for depth in range(1, k):
        lifted_layers = []
        for layer in range(2):
            local_maps = []
            for prefix in range(modulus):
                b = rng.randrange(p)
                c = rng.choice(ns)
                parameters[(depth, layer, prefix)] = (b, c)
                local_maps.append(reciprocal_permutation(p, b, c))
            lifted = [0] * (p * modulus)
            for prefix in range(modulus):
                for digit in range(p):
                    column = prefix + modulus * digit
                    lifted[column] = values[layer][prefix] + modulus * local_maps[prefix][digit]
            lifted_layers.append(lifted)
        values = lifted_layers
        modulus *= p

    assert all(sorted(layer) == list(range(modulus)) for layer in values)
    assert all(values[0][x] != values[1][x] for x in range(modulus))
    return values, parameters


def allowed_maps(
    p: int, current_b: int, current_c: int, first: int, second: int
) -> list[tuple[int, ...]]:
    current = reciprocal_permutation(p, current_b, current_c)
    maps = []
    for c in nonsquares(p):
        for b in range(p):
            values = reciprocal_permutation(p, b, c)
            if values[first] == current[first] or values[second] == current[second]:
                continue
            maps.append(values)
    return maps


def replace_depth_one_node(
    values: list[list[int]], prefix: int, layer: int, local: tuple[int, ...]
) -> list[list[int]]:
    p = 5
    changed = [row[:] for row in values]
    lower_row = values[layer][prefix] % p
    for column in range(len(values[0])):
        if column % p != prefix:
            continue
        child = (column // p) % p
        high = values[layer][column] // (p * p)
        changed[layer][column] = lower_row + p * local[child] + p * p * high

    assert all(sorted(row) == list(range(len(values[0]))) for row in changed)
    assert all(changed[0][x] != changed[1][x] for x in range(len(values[0])))
    return changed


def child_internal_counts(
    values: list[list[int]], prefix: int, layer: int
) -> tuple[int, ...]:
    p = 5
    counts = []
    for child in range(p):
        columns = [
            x
            for x in range(len(values[0]))
            if x % p == prefix and (x // p) % p == child
        ]
        points = [(x, values[layer][x]) for x in columns]
        count = sum(determinant(*triple) == 0 for triple in combinations(points, 3))
        counts.append(count)
    return tuple(counts)


def verify_instance(seed: int) -> tuple[int, int]:
    p = 5
    values, parameters = balanced_recursive_state(p, 3, seed)
    prefix = 0
    layer = 0
    current_b, current_c = parameters[(1, layer, prefix)]
    maps = allowed_maps(p, current_b, current_c, 0, 1)

    baseline = child_internal_counts(values, prefix, layer)
    determinant_checks = 0
    for local in maps:
        changed = replace_depth_one_node(values, prefix, layer, local)
        assert child_internal_counts(changed, prefix, layer) == baseline

        for child in range(p):
            columns = [
                x
                for x in range(len(values[0]))
                if x % p == prefix and (x // p) % p == child
            ]
            for triple_columns in combinations(columns, 3):
                old_points = [(x, values[layer][x]) for x in triple_columns]
                new_points = [(x, changed[layer][x]) for x in triple_columns]
                assert determinant(*old_points) == determinant(*new_points)
                determinant_checks += 1

    return len(maps), determinant_checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=4)
    args = parser.parse_args()

    states = 0
    determinant_checks = 0
    for seed in range(args.seeds):
        local_states, local_checks = verify_instance(seed)
        states += local_states
        determinant_checks += local_checks

    print(
        "verified child-core cancellation "
        f"instances={args.seeds}; node-states={states}; "
        f"determinant-checks={determinant_checks}"
    )


if __name__ == "__main__":
    main()
