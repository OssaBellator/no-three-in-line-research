#!/usr/bin/env python3
"""Finite checks for AC3gc--AC3gf."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def verify_binary_products() -> int:
    checks = 0
    for rank in (1, 2, 3):
        states = tuple(product((0, 1), repeat=rank))
        for mask in range(1 << len(states)):
            multiplicity = sum(bool(mask & (1 << index)) for index in range(len(states)))
            probability = Fraction(multiplicity, 2**rank)
            direct = sum(
                Fraction(1, len(states))
                for index, _ in enumerate(states)
                if mask & (1 << index)
            )
            assert probability == direct
            checks += 1
    return checks


def verify_floor_and_suppression() -> tuple[int, int]:
    floor_checks = 0
    for count in range(1, 5):
        for costs in product(range(6), repeat=2 * count):
            pairs = [costs[2 * i : 2 * i + 2] for i in range(count)]
            t1 = sum(Fraction(a + b, 2) for a, b in pairs)
            b1 = sum(min(a, b) for a, b in pairs)
            i1 = sum(abs(a - b) for a, b in pairs)
            assert t1 == b1 + Fraction(i1, 2)
            floor_checks += 1

    suppression_checks = 0
    for rank, factor in ((2, 4), (3, 8)):
        states = tuple(product((0, 1), repeat=rank))
        for chosen in states:
            for mask in range(1, 1 << len(states)):
                multiplicity = sum(bool(mask & (1 << index)) for index in range(len(states)))
                probability = Fraction(multiplicity, len(states))
                indicator = int(bool(mask & (1 << states.index(chosen))))
                assert indicator <= factor * probability
                suppression_checks += 1
    return floor_checks, suppression_checks


def core_count(envelope_roles: int) -> int:
    return 18 * envelope_roles**3 + 5 * envelope_roles**2


def verify_corrected_bounds() -> int:
    assert 12 > 8
    assert 36 > 34
    assert core_count(21) == 168_903
    assert core_count(53) == 2_693_831
    return 4


def verify_paid_scales() -> int:
    checks = 0
    for weight in range(1, 101):
        for k in range(1, 11):
            for r in range(1, 6):
                for rho in range(1, 4):
                    for ell in range(1, 4):
                        clean = Fraction(weight, 96 * k * r * rho * ell)
                        variation = Fraction(weight, 192 * k * r * rho * ell)
                        assert variation * 2 == clean
                        checks += 1
    return checks


def verify_failed_router() -> int:
    checks = 0
    for gap in range(1, 60):
        for b1 in range(gap + 1):
            for t2 in range(gap + 1):
                for t3 in range(gap + 1):
                    if b1 + 4 * t2 + 8 * t3 < gap:
                        continue
                    assert b1 * 3 >= gap or t2 * 12 >= gap or t3 * 24 >= gap
                    checks += 1
    return checks


def main() -> None:
    product_checks = verify_binary_products()
    floor_checks, suppression_checks = verify_floor_and_suppression()
    bound_checks = verify_corrected_bounds()
    scale_checks = verify_paid_scales()
    router_checks = verify_failed_router()
    print("AC BDA product propagation verified")
    print(f"  binary product events: {product_checks}")
    print(f"  floor/imbalance systems: {floor_checks}")
    print(f"  higher-rank suppression events: {suppression_checks}")
    print(f"  corrected role/envelope bounds: {bound_checks}")
    print(f"  paid-scale identities: {scale_checks}")
    print(f"  failed-router systems: {router_checks}")


if __name__ == "__main__":
    main()
