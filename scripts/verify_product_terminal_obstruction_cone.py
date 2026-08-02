#!/usr/bin/env python3
"""Finite checks for PX336--PX340."""

from itertools import combinations, permutations
from math import comb, factorial
import random


def feature_count(s: int) -> int:
    return sum(comb(s, r) ** 2 * factorial(r) for r in range(1, min(3, s) + 1))


def partial_matchings(s: int):
    out = []
    for r in range(1, min(3, s) + 1):
        for rows in combinations(range(s), r):
            for cols in combinations(range(s), r):
                for p in permutations(cols):
                    out.append(tuple(zip(rows, p)))
    return out


def principal_states(s: int):
    for p in permutations(range(s)):
        yield frozenset(enumerate(p))


def direct_value(state, weights):
    total = 0
    for feature, weight in weights.items():
        if set(feature).issubset(state):
            total += weight
    return total


def main() -> None:
    rng = random.Random(142)
    for s in range(1, 6):
        features = partial_matchings(s)
        assert len(features) == feature_count(s)
        move_bound = (2 ** (s * (s - 1))) * sum(comb(s, k) * factorial(k) for k in range(s + 1))
        assert move_bound >= factorial(s)

        if s <= 4:
            weights = {feature: rng.randrange(0, 8) for feature in features}
            current = frozenset((i, i) for i in range(s))
            current_value = direct_value(current, weights)
            for state in principal_states(s):
                direct_delta = direct_value(state, weights) - current_value
                coefficients = {}
                for feature in features:
                    coefficients[feature] = int(set(feature).issubset(state)) - int(set(feature).issubset(current))
                linear_delta = sum(coefficients[f] * weights[f] for f in features)
                assert direct_delta == linear_delta

    print("PX336--PX340 terminal obstruction-cone verifier: PASS")


if __name__ == "__main__":
    main()
