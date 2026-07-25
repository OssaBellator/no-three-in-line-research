#!/usr/bin/env python3
"""Finite checks for AC3gk--AC3gm."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def verify_expectation_realization() -> int:
    checks = 0
    for state_count in range(1, 7):
        for values in product(range(5), repeat=state_count):
            expectation = Fraction(sum(values), state_count)
            assert max(values) >= expectation
            checks += 1
    return checks


def verify_weighted_distributions() -> int:
    checks = 0
    for state_count in range(1, 5):
        for values in product(range(4), repeat=state_count):
            for raw_weights in product(range(1, 4), repeat=state_count):
                total_weight = sum(raw_weights)
                expectation = sum(
                    Fraction(value * weight, total_weight)
                    for value, weight in zip(values, raw_weights)
                )
                assert max(values) >= expectation
                checks += 1
    return checks


def verify_bda_constants() -> int:
    checks = 0
    for gap in range(1, 100):
        for k in range(1, 31):
            floor_payment = Fraction(gap, 3 * k)
            floor_return = floor_payment / 3
            rank2_payment = Fraction(gap, 12 * k)
            rank2_return = rank2_payment / 3
            rank3_payment = Fraction(gap, 24 * k)
            rank3_return = rank3_payment / 3
            assert floor_return == Fraction(gap, 9 * k)
            assert rank2_return == Fraction(gap, 36 * k)
            assert rank3_return == Fraction(gap, 72 * k)
            checks += 1
    return checks


def verify_three_way_router() -> int:
    checks = 0
    for gap in range(1, 50):
        for b1 in range(gap + 1):
            for t2 in range(gap + 1):
                for t3 in range(gap + 1):
                    if b1 + 4 * t2 + 8 * t3 < gap:
                        continue
                    assert b1 >= Fraction(gap, 3) or t2 >= Fraction(gap, 12) or t3 >= Fraction(gap, 24)
                    checks += 1
    return checks


def verify_generic_composition() -> int:
    checks = 0
    for expected in range(1, 101):
        for k in range(1, 31):
            payment = Fraction(expected, k)
            returned = payment / 3
            assert returned == Fraction(expected, 3 * k)
            checks += 1
    return checks


def main() -> None:
    realization_checks = verify_expectation_realization()
    weighted_checks = verify_weighted_distributions()
    constant_checks = verify_bda_constants()
    router_checks = verify_three_way_router()
    composition_checks = verify_generic_composition()
    print("AC expected-rank pivot adapter verified")
    print(f"  uniform-bank realizations: {realization_checks}")
    print(f"  weighted-bank realizations: {weighted_checks}")
    print(f"  BDA pivot constants: {constant_checks}")
    print(f"  BDA three-way routers: {router_checks}")
    print(f"  generic composition identities: {composition_checks}")


if __name__ == "__main__":
    main()
