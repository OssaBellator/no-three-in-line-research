#!/usr/bin/env python3
"""Exact rational audit for PP3bxg--PP3bxi."""

from __future__ import annotations

from fractions import Fraction


Matrix = list[list[Fraction]]
Vector = list[Fraction]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return [
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), Fraction(0))
        for i in range(len(matrix))
    ]


def ratios(next_vector: Vector, vector: Vector) -> Vector:
    return [a / b for a, b in zip(next_vector, vector)]


def backward_distribution(
    matrix: Matrix,
    potentials: list[Vector],
    depth: int,
    root: int,
) -> dict[int, Fraction]:
    distribution = {root: Fraction(1)}
    for level in range(depth, 0, -1):
        next_distribution: dict[int, Fraction] = {}
        for x, mass in distribution.items():
            denominator = potentials[level][x]
            for xp in range(len(matrix)):
                probability = matrix[x][xp] * potentials[level - 1][xp] / denominator
                if probability:
                    next_distribution[xp] = (
                        next_distribution.get(xp, Fraction(0)) + mass * probability
                    )
        assert sum(next_distribution.values(), Fraction(0)) == 1
        distribution = next_distribution
    return distribution


def extract_bad_path(
    matrix: Matrix,
    ratio_levels: list[Vector],
    depth: int,
    root: int,
    threshold: Fraction,
) -> list[int]:
    path = [root]
    current = root
    for level in range(depth, 0, -1):
        candidates = [
            xp
            for xp in range(len(matrix))
            if matrix[current][xp] > 0 and ratio_levels[level - 1][xp] > threshold
        ]
        assert candidates
        current = candidates[0]
        path.append(current)
    return path


def main() -> None:
    K: Matrix = [
        [Fraction(1), Fraction(1, 2), Fraction(0)],
        [Fraction(1, 3), Fraction(1), Fraction(1, 4)],
        [Fraction(0), Fraction(2, 5), Fraction(1)],
    ]
    depth_max = 6
    potentials: list[Vector] = [[Fraction(1) for _ in K]]
    for _ in range(depth_max + 1):
        potentials.append(matvec(K, potentials[-1]))

    ratio_levels = [
        ratios(potentials[t + 1], potentials[t]) for t in range(depth_max + 1)
    ]

    for t in range(1, depth_max + 1):
        for x in range(len(K)):
            denominator = potentials[t][x]
            probabilities = [
                K[x][xp] * potentials[t - 1][xp] / denominator
                for xp in range(len(K))
            ]
            assert sum(probabilities, Fraction(0)) == 1
            average = sum(
                (
                    probabilities[xp] * ratio_levels[t - 1][xp]
                    for xp in range(len(K))
                ),
                Fraction(0),
            )
            assert average == ratio_levels[t][x]
            neighbours = [
                ratio_levels[t - 1][xp]
                for xp in range(len(K))
                if K[x][xp] > 0
            ]
            assert min(neighbours) <= average <= max(neighbours)

    maxima = [max(level) for level in ratio_levels]
    assert all(maxima[t + 1] <= maxima[t] for t in range(depth_max))

    depth = depth_max
    root = max(range(len(K)), key=lambda x: ratio_levels[depth][x])
    threshold = min(ratio_levels[depth][root], maxima[-1]) - Fraction(1, 100)
    path = extract_bad_path(K, ratio_levels, depth, root, threshold)
    assert len(path) == depth + 1
    for offset, vertex in enumerate(path):
        level = depth - offset
        assert ratio_levels[level][vertex] > threshold

    distribution = backward_distribution(K, potentials, depth, root)
    expectation = sum(
        (mass * ratio_levels[0][endpoint] for endpoint, mass in distribution.items()),
        Fraction(0),
    )
    assert expectation == ratio_levels[depth][root]

    M = max(ratio_levels[0])
    theta = min(ratio_levels[0])
    C = ratio_levels[depth][root]
    bad_mass = sum(
        (mass for endpoint, mass in distribution.items() if ratio_levels[0][endpoint] > theta),
        Fraction(0),
    )
    lower_bound = (C - theta) / (M - theta)
    assert bad_mass >= lower_bound

    plateau: Matrix = [
        [Fraction(1), Fraction(1, 2)],
        [Fraction(1, 2), Fraction(1)],
    ]
    plateau_a = [[Fraction(1), Fraction(1)]]
    for _ in range(4):
        plateau_a.append(matvec(plateau, plateau_a[-1]))
    plateau_r = [ratios(plateau_a[t + 1], plateau_a[t]) for t in range(4)]
    assert all(value == Fraction(3, 2) for level in plateau_r for value in level)

    print({
        "all_checks_passed": True,
        "depth": depth,
        "root": root,
        "nested_bad_path": path,
        "endpoint_distribution": {k: str(v) for k, v in distribution.items()},
        "endpoint_expectation": str(expectation),
        "threshold_mass_lower_bound": str(lower_bound),
    })


if __name__ == "__main__":
    main()
