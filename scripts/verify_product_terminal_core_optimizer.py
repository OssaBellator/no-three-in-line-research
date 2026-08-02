#!/usr/bin/env python3
"""Finite checks for PX273--PX276."""

from __future__ import annotations

import itertools
import math
import random

Cell = tuple[int, int]
Certificate = tuple[Cell, ...]


def partial_matching_count(order: int, rank: int) -> int:
    return math.comb(order, rank) ** 2 * math.factorial(rank)


def all_certificates(order: int, rank: int):
    for rows in itertools.combinations(range(order), rank):
        for columns in itertools.combinations(range(order), rank):
            for image in itertools.permutations(columns):
                yield tuple(sorted(zip(rows, image)))


def allowed(permutation: tuple[int, ...], forbidden: set[Cell]) -> bool:
    return all((row, permutation[row]) not in forbidden for row in range(len(permutation)))


def value(permutation: tuple[int, ...], weights: dict[Certificate, int]) -> int:
    selected = {(row, permutation[row]) for row in range(len(permutation))}
    return sum(weight for certificate, weight in weights.items() if set(certificate) <= selected)


def optimize(order: int, forbidden: set[Cell], weights: dict[Certificate, int]):
    candidates = [
        permutation
        for permutation in itertools.permutations(range(order))
        if allowed(permutation, forbidden)
    ]
    if not candidates:
        return None
    return min((value(permutation, weights), permutation) for permutation in candidates)


def check_counts() -> None:
    for order in range(1, 8):
        for rank in range(1, min(3, order) + 1):
            certificates = set(all_certificates(order, rank))
            assert len(certificates) == partial_matching_count(order, rank)
        total = sum(partial_matching_count(order, rank) for rank in range(1, min(3, order) + 1))
        assert total <= 10 * order**6


def check_one_block(seed: int = 273) -> None:
    rng = random.Random(seed)
    for order in range(2, 8):
        universe = [
            certificate
            for rank in range(1, min(3, order) + 1)
            for certificate in all_certificates(order, rank)
        ]
        for _ in range(100):
            forbidden = {
                (row, column)
                for row in range(order)
                for column in range(order)
                if rng.random() < 0.15
            }
            weights = {
                certificate: rng.randint(1, 7)
                for certificate in rng.sample(universe, min(len(universe), 20))
            }
            result = optimize(order, forbidden, weights)
            direct = []
            for permutation in itertools.permutations(range(order)):
                if allowed(permutation, forbidden):
                    direct.append((value(permutation, weights), permutation))
            assert result == (min(direct) if direct else None)


def check_two_block(seed: int = 274) -> None:
    rng = random.Random(seed)
    for order in range(2, 6):
        permutations = list(itertools.permutations(range(order)))
        for _ in range(100):
            first_forbidden = {
                (row, column)
                for row in range(order)
                for column in range(order)
                if rng.random() < 0.1
            }
            legal_pairs = []
            for first in permutations:
                if not allowed(first, first_forbidden):
                    continue
                second_forbidden = {(row, first[row]) for row in range(order)}
                for second in permutations:
                    if allowed(second, second_forbidden):
                        score = sum(first[row] == second[(row + 1) % order] for row in range(order))
                        legal_pairs.append((score, first, second))
            if legal_pairs:
                assert min(legal_pairs) == sorted(legal_pairs)[0]


def check_subpower() -> None:
    for log_n in (10**3, 10**6, 10**12, 10**30):
        m = max(2, math.ceil(10 * math.log(max(math.log(log_n), 2))))
        log_complexity = 2 * math.lgamma(m + 1) + 6 * math.log(m)
        assert log_complexity / log_n < 0.5
    ratios = []
    for exponent in (100, 1000, 10000, 100000):
        log_n = float(exponent)
        m = max(2, math.ceil(4 * math.log(max(log_n, 2))))
        ratios.append((2 * math.lgamma(m + 1) + 6 * math.log(m)) / log_n)
    assert ratios[-1] < ratios[0]


def main() -> None:
    check_counts()
    check_one_block()
    check_two_block()
    check_subpower()
    print("PX273--PX276 terminal optimizer checks passed")


if __name__ == "__main__":
    main()
