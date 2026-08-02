#!/usr/bin/env python3
"""Verify universal 2 x 5 closure using blockwise affine digit maps."""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations

Point = tuple[int, int]
Permutation = tuple[int, ...]
FactorPair = tuple[Permutation, Permutation]

OUTER: FactorPair = ((0, 1), (1, 0))
TARGET: Permutation = (2, 4, 0, 3, 1)
REVERSAL: Permutation = (4, 3, 2, 1, 0)


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def is_no_three(points: tuple[Point, ...] | list[Point]) -> bool:
    return all(determinant(*triple) != 0 for triple in combinations(points, 3))


def compose(first: Permutation, second: Permutation) -> Permutation:
    """Return first after second."""
    return tuple(first[second[x]] for x in range(len(first)))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for x, value in enumerate(permutation):
        result[value] = x
    return tuple(result)


def affine_group() -> tuple[Permutation, ...]:
    return tuple(
        tuple((a * x + b) % 5 for x in range(5))
        for a in range(1, 5)
        for b in range(5)
    )


@lru_cache(maxsize=None)
def valid_factor_pairs(n: int) -> tuple[FactorPair, ...]:
    result: list[FactorPair] = []
    for first in permutations(range(n)):
        for second in permutations(range(n)):
            if any(first[x] == second[x] for x in range(n)):
                continue
            points = [(x, first[x]) for x in range(n)]
            points.extend((x, second[x]) for x in range(n))
            if is_no_three(points):
                result.append((first, second))
    return tuple(result)


def local_one_layer_state(
    tau: Permutation,
    alpha_0: Permutation,
    beta_0: Permutation,
) -> tuple[Point, ...]:
    alpha_1 = compose(REVERSAL, alpha_0)
    beta_1 = compose(REVERSAL, beta_0)
    row_maps = (alpha_0, alpha_1)
    column_maps = (beta_0, beta_1)
    points: set[Point] = set()
    for r in (0, 1):
        for i in range(2):
            j = OUTER[r][i]
            for u in range(5):
                v = tau[u]
                x = 2 * row_maps[i][u] + i
                y = 2 * column_maps[j][v] + j
                points.add((x, y))
    assert len(points) == 20
    return tuple(sorted(points))


def verify_saturation(points: tuple[Point, ...]) -> None:
    assert len(points) == 20
    assert all(sum(x == row for x, _ in points) == 2 for row in range(10))
    assert all(sum(y == column for _, y in points) == 2 for column in range(10))


def find_normalization(
    tau: Permutation,
    group: tuple[Permutation, ...],
) -> tuple[Permutation, Permutation]:
    solutions: list[tuple[Permutation, Permutation]] = []
    for alpha_0 in group:
        alpha_inverse = inverse(alpha_0)
        for beta_0 in group:
            normalized = compose(beta_0, compose(tau, alpha_inverse))
            if normalized == TARGET:
                solutions.append((alpha_0, beta_0))
    assert len(solutions) == 4
    return solutions[0]


def main() -> None:
    group = affine_group()
    assert len(group) == 20
    all_permutations = set(permutations(range(5)))
    affine = set(group)
    for permutation in group:
        graph = tuple((x, permutation[x]) for x in range(5))
        assert not is_no_three(graph)
    print("all 20 affine permutation graphs contain a collinear triple")

    double_coset_counts: dict[Permutation, int] = {}
    for alpha_0 in group:
        for beta_0 in group:
            tau = compose(inverse(beta_0), compose(TARGET, alpha_0))
            double_coset_counts[tau] = double_coset_counts.get(tau, 0) + 1

    assert len(double_coset_counts) == 100
    assert set(double_coset_counts.values()) == {4}
    assert set(double_coset_counts) == all_permutations - affine
    print("AGL(1,5) double cosets: affine=20, non-affine=100")

    factors = valid_factor_pairs(5)
    assert len(factors) == 64
    layer_permutations = {layer for pair in factors for layer in pair}
    assert len(layer_permutations) == 44
    assert layer_permutations.isdisjoint(affine)
    assert layer_permutations <= set(double_coset_counts)
    print("all 44 permutation layers used by saturated side-five factors are non-affine")

    verified = 0
    for pair in factors:
        for tau in pair:
            alpha_0, beta_0 = find_normalization(tau, group)
            assert compose(beta_0, compose(tau, inverse(alpha_0))) == TARGET
            points = local_one_layer_state(tau, alpha_0, beta_0)
            verify_saturation(points)
            assert is_no_three(points)
            verified += 1

    assert verified == 128
    print("universal affine 2x5 closure: verified both layers of all 64 ordered factors")


if __name__ == "__main__":
    main()
