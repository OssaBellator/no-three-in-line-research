#!/usr/bin/env python3
"""Exact rational audits for PP3bxz--PP3byb."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction

Matrix = list[list[Fraction]]
Vector = list[Fraction]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return [
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), Fraction(0))
        for i in range(len(matrix))
    ]


def enumerate_paths(
    matrix: Matrix,
    potentials: list[Vector],
    depth: int,
    root: int,
) -> list[tuple[tuple[int, ...], Fraction]]:
    paths = [((root,), Fraction(1))]
    for level in range(depth, 0, -1):
        extended: list[tuple[tuple[int, ...], Fraction]] = []
        for path, mass in paths:
            current = path[-1]
            denominator = potentials[level][current]
            for predecessor in range(len(matrix)):
                probability = (
                    matrix[current][predecessor]
                    * potentials[level - 1][predecessor]
                    / denominator
                )
                if probability:
                    extended.append((path + (predecessor,), mass * probability))
        paths = extended
    assert sum((mass for _, mass in paths), Fraction(0)) == 1
    return paths


def main() -> None:
    K: Matrix = [
        [Fraction(1), Fraction(1, 2), Fraction(0)],
        [Fraction(1, 3), Fraction(1), Fraction(1, 4)],
        [Fraction(0), Fraction(2, 5), Fraction(1)],
    ]
    depth = 6
    potentials: list[Vector] = [[Fraction(1) for _ in K]]
    for _ in range(depth + 1):
        potentials.append(matvec(K, potentials[-1]))
    ratios = [
        [potentials[t + 1][i] / potentials[t][i] for i in range(len(K))]
        for t in range(depth + 1)
    ]
    root = max(range(len(K)), key=lambda i: ratios[depth][i])
    C = ratios[depth][root]
    M = max(ratios[0])

    paths = enumerate_paths(K, potentials, depth, root)
    endpoint_mass: dict[int, Fraction] = defaultdict(Fraction)
    endpoint_path_count: dict[int, int] = defaultdict(int)
    for path, mass in paths:
        endpoint_mass[path[-1]] += mass
        endpoint_path_count[path[-1]] += 1
    assert sum(endpoint_mass.values(), Fraction(0)) == 1
    expectation = sum(
        (mass * ratios[0][endpoint] for endpoint, mass in endpoint_mass.items()),
        Fraction(0),
    )
    assert expectation == C

    chi = sum((mass * mass for mass in endpoint_mass.values()), Fraction(0))
    beta = max(endpoint_mass.values())
    assert chi <= beta
    q_path = max(mass for _, mass in paths)
    N_path = max(endpoint_path_count.values())
    assert beta <= N_path * q_path

    raw_values = sorted(set(ratios[0]))
    thresholds = set(raw_values[:-1])
    for left, right in zip(raw_values, raw_values[1:]):
        thresholds.add((left + right) / 2)

    checks = 0
    for theta in sorted(thresholds):
        if not theta < C <= M:
            continue
        high = {z for z in endpoint_mass if ratios[0][z] > theta}
        p = sum((endpoint_mass[z] for z in high), Fraction(0))
        p_lower = (C - theta) / (M - theta)
        assert p >= p_lower
        assert Fraction(len(high), 1) * chi >= p * p >= p_lower * p_lower
        assert Fraction(len(high), 1) * beta >= p >= p_lower
        assert Fraction(len(high), 1) * N_path * q_path >= p_lower
        checks += 1

    b_levels: list[Fraction] = []
    for level in range(depth, 0, -1):
        b = Fraction(0)
        for current in range(len(K)):
            denominator = potentials[level][current]
            for predecessor in range(len(K)):
                atom = (
                    K[current][predecessor]
                    * potentials[level - 1][predecessor]
                    / denominator
                )
                b = max(b, atom)
        b_levels.append(b)
    product_bound = Fraction(1)
    for b in b_levels:
        product_bound *= b
    assert q_path <= product_bound

    print({
        "all_checks_passed": True,
        "depth": depth,
        "root": root,
        "positive_paths": len(paths),
        "endpoint_distribution": {k: str(v) for k, v in endpoint_mass.items()},
        "collision_energy": str(chi),
        "maximum_endpoint_atom": str(beta),
        "maximum_path_probability": str(q_path),
        "maximum_paths_per_endpoint": N_path,
        "thresholds_checked": checks,
        "endpoint_expectation": str(expectation),
    })


if __name__ == "__main__":
    main()
