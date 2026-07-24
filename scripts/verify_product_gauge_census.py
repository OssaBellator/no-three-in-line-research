#!/usr/bin/env python3
"""Verify PX28 gauge invariance and the complete normalized census through n=5."""
from __future__ import annotations

from itertools import permutations
from math import gcd

Point = tuple[int, int]
Permutation = tuple[int, ...]
ORIENTATIONS = ("cc", "cf", "fc", "ff")
EXPECTED = {
    2: (16, 9),
    3: (0, 0),
    4: (4, 4),
    5: (8, 5),
}


def compose(first: Permutation, second: Permutation) -> Permutation:
    return tuple(first[second[x]] for x in range(len(first)))


def inverse(permutation: Permutation) -> Permutation:
    result = [-1] * len(permutation)
    for x, value in enumerate(permutation):
        result[value] = x
    return tuple(result)


def state(
    n: int,
    tau: Permutation,
    row_maps: tuple[Permutation, Permutation],
    column_maps: tuple[Permutation, Permutation],
    orientation: str,
) -> tuple[Point, ...]:
    outer = ((0, 1), (1, 0))
    points = []
    for layer in (0, 1):
        for i in (0, 1):
            j = outer[layer][i]
            for u in range(n):
                v = tau[u]
                row_digit = row_maps[i][u]
                column_digit = column_maps[j][v]
                x = n * i + row_digit if orientation[0] == "c" else 2 * row_digit + i
                y = n * j + column_digit if orientation[1] == "c" else 2 * column_digit + j
                points.append((x, y))
    return tuple(points)


def is_no_three(points: tuple[Point, ...]) -> bool:
    for anchor, first in enumerate(points):
        directions: set[Point] = set()
        for second in points[anchor + 1 :]:
            dx = second[0] - first[0]
            dy = second[1] - first[1]
            divisor = gcd(abs(dx), abs(dy))
            dx //= divisor
            dy //= divisor
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
            direction = (dx, dy)
            if direction in directions:
                return False
            directions.add(direction)
    return True


def verify_gauge_identity() -> None:
    for n in range(2, 6):
        identity = tuple(range(n))
        sample = tuple(reversed(range(n)))
        tau = tuple((2 * x + 1) % n for x in range(n)) if n % 2 else sample
        if len(set(tau)) != n:
            tau = sample
        alpha = (identity, sample)
        beta = (sample, identity)
        gamma = sample
        delta = tuple((x + 1) % n for x in range(n))
        gamma_inverse = inverse(gamma)
        delta_inverse = inverse(delta)
        transformed_tau = compose(delta, compose(tau, gamma_inverse))
        transformed_alpha = tuple(compose(value, gamma_inverse) for value in alpha)
        transformed_beta = tuple(compose(value, delta_inverse) for value in beta)
        for orientation in ORIENTATIONS:
            assert set(state(n, tau, alpha, beta, orientation)) == set(
                state(
                    n,
                    transformed_tau,
                    transformed_alpha,
                    transformed_beta,
                    orientation,
                )
            )


def normalized_census(n: int) -> tuple[int, int]:
    maps = tuple(permutations(range(n)))
    identity = tuple(range(n))
    successes = 0
    configurations: set[tuple[Point, ...]] = set()
    for tau in maps:
        for row_map in maps:
            for column_map in maps:
                for orientation in ORIENTATIONS:
                    points = state(
                        n,
                        tau,
                        (identity, row_map),
                        (identity, column_map),
                        orientation,
                    )
                    if is_no_three(points):
                        successes += 1
                        configurations.add(tuple(sorted(points)))
    return successes, len(configurations)


def main() -> None:
    verify_gauge_identity()
    for n in range(2, 6):
        result = normalized_census(n)
        assert result == EXPECTED[n], (n, result, EXPECTED[n])
        print(
            f"n={n}: normalized successes={result[0]}, "
            f"distinct configurations={result[1]}"
        )

    side_eight = state(
        4,
        (1, 3, 0, 2),
        ((0, 1, 2, 3), (0, 1, 2, 3)),
        ((0, 1, 2, 3), (0, 1, 2, 3)),
        "ff",
    )
    assert is_no_three(side_eight)
    print("PX28 gauge census through n=5 verified")


if __name__ == "__main__":
    main()
