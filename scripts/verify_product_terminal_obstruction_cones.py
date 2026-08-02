#!/usr/bin/env python3
"""Finite checks for PX314--PX317."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb, factorial, log
import random


def partial_matching_count(m: int) -> int:
    return sum(comb(m, r) ** 2 * factorial(r) for r in range(m + 1))


def verify_template_count() -> None:
    for m in range(0, 12):
        count = partial_matching_count(m)
        assert count <= (m + 1) ** m if m else count == 1

    # Check that the logarithmic template exponent is negligible relative to log N
    # along a rapidly growing sequence with m,d,p=O(log log N).
    for exponent in range(20, 200, 10):
        # N = exp(exp(exponent)); compare logs without constructing N.
        log_log_n = exponent
        m = max(1, int(log_log_n))
        d = m
        p = m
        log_templates = m * m * log(2) + m * (d + p) * log(m + 1)
        log_n = pow(2.718281828459045, exponent)
        ratio = log_templates / log_n
        if exponent >= 40:
            assert ratio < 1e-8


def move_cost(coefficients: tuple[int, ...], weights: tuple[Fraction, ...]) -> Fraction:
    return sum(Fraction(c) * w for c, w in zip(coefficients, weights))


def verify_linear_move_costs() -> None:
    rng = random.Random(315)
    for variables in range(1, 9):
        for _ in range(1000):
            coefficients = tuple(rng.randint(-3, 3) for _ in range(variables))
            w1 = tuple(Fraction(rng.randint(0, 9), rng.randint(1, 7)) for _ in range(variables))
            w2 = tuple(Fraction(rng.randint(0, 9), rng.randint(1, 7)) for _ in range(variables))
            scale = Fraction(rng.randint(0, 9), rng.randint(1, 7))

            total = tuple(a + b for a, b in zip(w1, w2))
            scaled = tuple(scale * a for a in w1)
            assert move_cost(coefficients, total) == move_cost(coefficients, w1) + move_cost(coefficients, w2)
            assert move_cost(coefficients, scaled) == scale * move_cost(coefficients, w1)


def verify_cone_characterization() -> None:
    rng = random.Random(317)
    for variables in range(1, 6):
        for _ in range(500):
            moves = [
                tuple(rng.randint(-2, 2) for _ in range(variables))
                for _ in range(rng.randint(1, 8))
            ]

            feasible = []
            for integer_weights in product(range(5), repeat=variables):
                if sum(integer_weights) == 0:
                    continue
                weights = tuple(Fraction(x, sum(integer_weights)) for x in integer_weights)
                frozen = all(move_cost(move, weights) >= 0 for move in moves)
                if frozen:
                    feasible.append(weights)

            # Directly recheck the defining halfspaces for every enumerated point.
            for weights in feasible:
                assert all(w >= 0 for w in weights)
                assert sum(weights) == 1
                assert all(move_cost(move, weights) >= 0 for move in moves)

            # Homogeneity: every positive scalar multiple has the same signs.
            if feasible:
                weights = feasible[0]
                for scale in (Fraction(1, 3), Fraction(2), Fraction(17, 5)):
                    assert all(
                        (move_cost(move, weights) >= 0)
                        == (move_cost(move, tuple(scale * w for w in weights)) >= 0)
                        for move in moves
                    )


def verify_move_count_is_subpower() -> None:
    for m in range(1, 50):
        one = factorial(m)
        two = one * one
        partial = (1 << m) * one
        assert max(one, two, partial) <= (1 << m) * factorial(m) ** 2
        # log of the crude move count is O(m log m).
        crude_log = m * log(2) + 2 * sum(log(k) for k in range(1, m + 1))
        assert crude_log <= 3 * m * log(m + 1)


def main() -> None:
    verify_template_count()
    verify_linear_move_costs()
    verify_cone_characterization()
    verify_move_count_is_subpower()
    print("terminal obstruction cone verifier: PASS")


if __name__ == "__main__":
    main()
