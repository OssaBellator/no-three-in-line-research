#!/usr/bin/env python3
"""Finite checks for GC4z--GC4ac."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def verify_capacity_dichotomy() -> int:
    checked = 0
    for k in range(1, 5):
        for safe in range(7):
            for demands in product(range(5), repeat=k):
                total = safe + sum(demands)
                for capacities in product(range(5), repeat=k):
                    cap_sum = sum(capacities)
                    overloaded = any(
                        demand > capacity
                        for demand, capacity in zip(demands, capacities)
                    )
                    if not overloaded:
                        assert safe >= total - cap_sum
                    checked += 1
    return checked


def verify_relative_constants() -> int:
    checked = 0
    for safe in range(1, 10):
        for bad in range(10):
            total = safe + bad
            for cap_sum in range(0, total + 1):
                if bad <= cap_sum:
                    assert safe >= total - cap_sum
                    for eta_num in range(0, 10):
                        eta = Fraction(eta_num, 10)
                        if cap_sum <= eta * total and eta < 1:
                            assert safe >= (1 - eta) * total
                            for reuse in range(1, 4):
                                for kappa in range(1, 4):
                                    assert Fraction(safe, 2 * reuse * kappa) >= (
                                        (1 - eta) * total / (2 * reuse * kappa)
                                    )
                                    assert Fraction(safe, 2 * kappa) >= (
                                        (1 - eta) * total / (2 * kappa)
                                    )
                                    checked += 1
    return checked


def verify_labelled_composition() -> int:
    checked = 0
    for original_weight in range(1, 20):
        for conflict_degree in range(4):
            base = Fraction(original_weight, conflict_degree + 1)
            first_integer_at_least_base = (
                original_weight + conflict_degree
            ) // (conflict_degree + 1)
            for retained_integer in range(
                first_integer_at_least_base, original_weight + 1
            ):
                retained = Fraction(retained_integer, 1)
                if retained < base:
                    continue
                for eta_num in range(10):
                    eta = Fraction(eta_num, 10)
                    for cap_integer in range(0, retained_integer + 1):
                        cap_sum = Fraction(cap_integer, 1)
                        if cap_sum <= eta * base:
                            safe_lower = retained - cap_sum
                            target = (1 - eta) * base
                            assert safe_lower >= target
                            checked += 1
    return checked


def main() -> None:
    dichotomies = verify_capacity_dichotomy()
    relative = verify_relative_constants()
    compositions = verify_labelled_composition()
    print(
        f"verified {dichotomies} capacity partitions, {relative} relative bounds "
        f"and {compositions} labelled-fan compositions"
    )


if __name__ == "__main__":
    main()
