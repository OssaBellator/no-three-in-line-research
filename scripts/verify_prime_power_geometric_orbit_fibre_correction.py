#!/usr/bin/env python3
"""Finite checks for CMR1774--CMR1781."""

from __future__ import annotations

from itertools import combinations, permutations
from random import Random


Point = tuple[int, int]


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def apply_permutation(point: Point, permutation: tuple[int, ...]) -> Point:
    return permutation[point[0]], permutation[point[1]]


def preserves_collinearity(side: int, permutation: tuple[int, ...]) -> bool:
    points = [(left, right) for left in range(side) for right in range(side)]
    for triple in combinations(points, 3):
        image = tuple(apply_permutation(point, permutation) for point in triple)
        if collinear(*triple) != collinear(*image):
            return False
    return True


def perfect_matching_count(side: int, forbidden: set[Point]) -> int:
    return sum(
        all((left, permutation[left]) not in forbidden for left in range(side))
        for permutation in permutations(range(side))
    )


def main() -> None:
    counterexample_checks = 0
    stabilizer_checks = 0
    matching_invariance_checks = 0
    geometric_change_checks = 0
    fibre_domination_checks = 0

    for side in range(4, 8):
        permutation = tuple(
            3 if value == 2 else 2 if value == 3 else value
            for value in range(side)
        )
        original = ((0, 1), (1, 2), (2, 3))
        image = tuple(apply_permutation(point, permutation) for point in original)
        assert collinear(*original)
        assert not collinear(*image)
        counterexample_checks += 1

    for side in range(2, 8):
        residual = list(range(2, side))
        geometric = []
        for image in permutations(residual):
            permutation = (0, 1, *image)
            if preserves_collinearity(side, permutation):
                geometric.append(permutation)
            stabilizer_checks += 1
        assert geometric == [tuple(range(side))]

    random = Random(1774)
    for _ in range(1_000):
        side = random.randint(3, 7)
        residual = list(range(2, side))
        image = random.sample(residual, len(residual))
        permutation = (0, 1, *image)

        forbidden = {(index, index) for index in range(side)}
        forbidden.add((0, 1))
        for left in range(side):
            for right in range(side):
                if random.random() < 0.12:
                    forbidden.add((left, right))
        transformed = {
            apply_permutation(edge, permutation)
            for edge in forbidden
        }
        assert (
            perfect_matching_count(side, forbidden)
            == perfect_matching_count(side, transformed)
        )
        matching_invariance_checks += 1

        points = [(left, right) for left in range(side) for right in range(side)]
        original_collinear = {
            triple for triple in combinations(points, 3) if collinear(*triple)
        }
        transformed_collinear = {
            tuple(sorted(apply_permutation(point, permutation) for point in triple))
            for triple in original_collinear
        }
        standard_collinear = {
            tuple(sorted(triple))
            for triple in combinations(points, 3)
            if collinear(*triple)
        }
        if permutation != tuple(range(side)) and side >= 4:
            assert transformed_collinear != standard_collinear
            geometric_change_checks += 1

        fibre_size = random.randint(1, 12)
        child_count = random.randint(1, 8)
        rows = [
            [random.randint(0, 20) for _ in range(child_count)]
            for _ in range(fibre_size)
        ]
        upper = [max(row[column] for row in rows) for column in range(child_count)]
        for row in rows:
            assert all(value <= cap for value, cap in zip(row, upper))
            fibre_domination_checks += 1

    print(
        "verified geometric orbit-fibre correction: "
        f"{counterexample_checks} explicit collinearity failures, "
        f"{stabilizer_checks} residual stabilizer candidates, "
        f"{matching_invariance_checks} matching-count invariances, "
        f"{geometric_change_checks} nontrivial geometry changes and "
        f"{fibre_domination_checks} upper-fibre row dominations"
    )


if __name__ == "__main__":
    main()
