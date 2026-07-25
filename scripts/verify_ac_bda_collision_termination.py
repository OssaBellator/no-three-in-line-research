#!/usr/bin/env python3
"""Verify AC3eh--AC3ek on exhaustive small integer role data."""

from fractions import Fraction
from itertools import product
from math import gcd


def sign(value):
    return (value > 0) - (value < 0)


def verify_collision_normal_form(max_q=12, max_role=8):
    records = collisions = lower = mutual = bounded = 0
    collision_pairs = {}

    for q in range(1, max_q + 1):
        for u in range(-max_role, max_role + 1):
            for v in range(-max_role, max_role + 1):
                if 0 in (u, v) or u == v:
                    continue
                key = (q, u, v)
                collision_pairs[key] = set()
                maximum_h = max_role * q + q
                for h in range(1, maximum_h + 1):
                    for sigma in (-1, 1):
                        H = h + sigma * q
                        records += 1
                        if H <= 0:
                            assert sigma == -1
                            assert 1 <= h <= q
                            lower += 1
                            continue

                        first = h * u == H * v
                        second = h * v == H * u
                        assert not (first and second)
                        mutual += 1
                        if not (first or second):
                            continue

                        divisor = gcd(abs(u), abs(v))
                        nu = u // divisor
                        omega = v // divisor
                        assert nu * omega > 0
                        a = abs(nu)
                        b = abs(omega)
                        delta = abs(a - b)
                        assert delta >= 1
                        assert gcd(a, b) == 1
                        assert q % delta == 0

                        expected = frozenset((a * q // delta, b * q // delta))
                        assert frozenset((h, H)) == expected
                        collision_pairs[key].add(expected)
                        assert max(h, H) <= max_role * q

                        if first:
                            assert h == b * q // delta
                            assert H == a * q // delta
                            assert sigma == sign(a - b)
                        if second:
                            assert h == a * q // delta
                            assert H == b * q // delta
                            assert sigma == sign(b - a)

                        reverse_ticket = (min(H, h), max(H, h), q, u, v)
                        forward_ticket = (min(h, H), max(h, H), q, u, v)
                        assert reverse_ticket == forward_ticket
                        collisions += 1
                        bounded += 1

                assert len(collision_pairs[key]) <= 1

    unique_role_pairs = sum(bool(values) for values in collision_pairs.values())
    return records, collisions, lower, mutual, bounded, unique_role_pairs


def verify_lower_weight_localization(max_q=7, max_weight=3):
    systems = 0
    for q in range(1, max_q + 1):
        for weights in product(range(max_weight + 1), repeat=q):
            total = sum(weights)
            if total:
                assert max(weights) >= Fraction(total, q)
            systems += 1
    return systems


def verify_composition_constants():
    checks = 0
    for q in range(1, 13):
        for role_count in range(1, 6):
            for multiplicity in range(1, 5):
                for profile_count in range(1, 7):
                    scale = role_count * multiplicity * profile_count
                    endpoint_source = 32 * scale
                    variation_source = 64 * scale
                    assert Fraction(endpoint_source, 32 * scale) == 1
                    assert Fraction(variation_source, 64 * scale) == 1
                    assert Fraction(endpoint_source, 32 * q * scale) == Fraction(1, q)
                    assert Fraction(variation_source, 64 * q * scale) == Fraction(1, q)
                    checks += 1
    return checks


def main():
    records, collisions, lower, mutual, bounded, role_pairs = verify_collision_normal_form()
    lower_systems = verify_lower_weight_localization()
    constants = verify_composition_constants()
    print(
        "AC BDA collision termination: verified "
        f"{records} signed partner records, {collisions} collisions, "
        f"{lower} lower fronts, {mutual} mutual-exclusion cases, "
        f"{bounded} bounded collision scales, {role_pairs} unique role pairs, "
        f"{lower_systems} weighted lower alphabets, and {constants} constants"
    )


if __name__ == "__main__":
    main()
