#!/usr/bin/env python3
"""Checks for PX277--PX280."""

from __future__ import annotations

import random


def scalar(vector: tuple[int, ...], bound: int) -> int:
    base = bound + 1
    return sum(value * base ** (len(vector) - 1 - index) for index, value in enumerate(vector))


def check_designated(seed: int = 277) -> None:
    rng = random.Random(seed)
    for depth in range(1, 20):
        for _ in range(1000):
            bound = rng.randint(1, 30)
            vector = [0] * (depth + 1)
            level = rng.randrange(depth + 1)
            vector[level] = rng.randint(1, bound)
            for later in range(level + 1, depth + 1):
                vector[later] = rng.randint(0, bound)
            updated = vector.copy()
            updated[level] -= rng.randint(1, updated[level])
            for later in range(level + 1, depth + 1):
                updated[later] = rng.randint(0, bound)
            assert tuple(updated) < tuple(vector)
            assert scalar(tuple(updated), bound) < scalar(tuple(vector), bound)


def check_strict_sign_or_child(seed: int = 280) -> None:
    rng = random.Random(seed)
    for depth in range(1, 20):
        length = 2 * (depth + 1)
        for _ in range(1000):
            bound = rng.randint(1, 20)
            vector = [0] * length
            level = rng.randrange(depth + 1)
            unresolved_index = 2 * level
            vector[unresolved_index] = rng.randint(1, bound)
            for index in range(unresolved_index + 1, length):
                vector[index] = rng.randint(0, bound)
            updated = vector.copy()
            updated[unresolved_index] -= 1
            if level < depth and rng.random() < 0.5:
                updated[2 * (level + 1) + 1] = min(
                    bound, updated[2 * (level + 1) + 1] + 1
                )
            assert tuple(updated) < tuple(vector)
            assert scalar(tuple(updated), bound) < scalar(tuple(vector), bound)


def check_degree_and_spread() -> None:
    for delta0 in range(0, 10):
        for depth in range(0, 100):
            deltas = [delta0 + level for level in range(depth)]
            exponent = 2 * sum(deltas)
            assert exponent == depth * (2 * delta0 + depth - 1)


def main() -> None:
    check_designated()
    check_strict_sign_or_child()
    check_degree_and_spread()
    print("PX277--PX280 causal lexicographic checks passed")


if __name__ == "__main__":
    main()
