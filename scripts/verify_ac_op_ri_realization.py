#!/usr/bin/env python3
"""Verify AC3ay--AC3bb on small real factors and weighted abstractions."""

from fractions import Fraction
from itertools import product


def determinant(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        - (second[1] - first[1]) * (third[0] - first[0])
    )


def prime_factors(value):
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(prime):
    phi = prime - 1
    factors = prime_factors(phi)
    for candidate in range(2, prime):
        if all(pow(candidate, phi // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def divisors(value):
    return [divisor for divisor in range(1, value + 1) if value % divisor == 0]


def subgroup(prime, order):
    generator = primitive_root(prime)
    step = (prime - 1) // order
    return {pow(generator, step * index, prime) for index in range(order)}


def coset(scalar, group, prime):
    return frozenset((scalar * element) % prime for element in group)


def verify_real_factors(primes=(5, 7, 11, 13)):
    factor_checks = 0
    quotient_checks = 0
    scale_checks = 0
    carry_checks = 0

    for prime in primes:
        groups = [subgroup(prime, order) for order in divisors(prime - 1)]
        for a in range(1, prime):
            for b in range(1, prime):
                if a == b:
                    continue
                r = (b * pow(a, -1, prime)) % prime
                for x in range(1, prime):
                    y_x = (a * pow(x, -1, prime)) % prime
                    for u in range(1, prime):
                        if u == x:
                            continue
                        y_u = (a * pow(u, -1, prime)) % prime
                        for z in range(1, prime):
                            w_z = (b * pow(z, -1, prime)) % prime
                            if determinant((x, y_x), (u, y_u), (z, w_z)) != 0:
                                continue

                            c = (z * pow(x, -1, prime)) % prime
                            g = (u * pow(x, -1, prime)) % prime
                            assert c not in (1, r)
                            computed_g = (
                                c
                                * (1 - c)
                                * pow((r - c) % prime, -1, prime)
                            ) % prime
                            assert computed_g == g

                            companion = (
                                r
                                * (c - 1)
                                * pow((c - r) % prime, -1, prime)
                            ) % prime
                            companion_image = (
                                companion
                                * (1 - companion)
                                * pow((r - companion) % prime, -1, prime)
                            ) % prime
                            assert companion_image == g
                            assert (c * companion - r * g) % prime == 0

                            reverse_c = (c * pow(g, -1, prime)) % prime
                            reverse_g = pow(g, -1, prime)
                            reverse_companion = (
                                r
                                * (reverse_c - 1)
                                * pow((reverse_c - r) % prime, -1, prime)
                            ) % prime
                            assert {
                                reverse_c,
                                reverse_companion,
                            } == {
                                (c * reverse_g) % prime,
                                (companion * reverse_g) % prime,
                            }
                            factor_checks += 1

                            numerator_x = (x - z) * (y_u - w_z) - (b - a)
                            numerator_u = (u - z) * (y_x - w_z) - (b - a)
                            assert numerator_x % prime == 0
                            assert numerator_u % prime == 0
                            assert numerator_x // prime == numerator_u // prime
                            carry_checks += 1

                            for group in groups:
                                root = coset(c, group, prime)
                                other = coset(companion, group, prime)
                                image = coset(g, group, prime)
                                ratio = coset(r, group, prime)
                                product_right = frozenset(
                                    (
                                        rr
                                        * gg
                                        * pow(aa, -1, prime)
                                    )
                                    % prime
                                    for rr in ratio
                                    for gg in image
                                    for aa in root
                                )
                                assert other == product_right
                                quotient_checks += 1

                                scale = coset(x, group, prime)
                                partner = coset(u, group, prime)
                                anchor = coset(z, group, prime)
                                expected_partner = frozenset(
                                    (cc * ss) % prime
                                    for cc in image
                                    for ss in scale
                                )
                                expected_anchor = frozenset(
                                    (aa * ss) % prime
                                    for aa in root
                                    for ss in scale
                                )
                                assert partner == expected_partner
                                assert anchor == expected_anchor
                                scale_checks += 1

    return factor_checks, quotient_checks, scale_checks, carry_checks


def verify_paid_fibre_router(max_records=5, max_pairs=3):
    router_checks = 0

    for record_count in range(1, max_records + 1):
        for pair_count in range(1, max_pairs + 1):
            states = list(product(range(pair_count), (False, True)))
            for records in product(states, repeat=record_count):
                for weights in product(range(3), repeat=record_count):
                    total = sum(weights)
                    if total == 0:
                        continue
                    pair_weights = [0] * pair_count
                    for (pair, _), weight in zip(records, weights, strict=True):
                        pair_weights[pair] += weight
                    heaviest_pair = max(range(pair_count), key=pair_weights.__getitem__)
                    selected_weight = pair_weights[heaviest_pair]
                    assert selected_weight * pair_count >= total

                    complete_weight = sum(
                        weight
                        for (pair, complete), weight in zip(
                            records, weights, strict=True
                        )
                        if pair == heaviest_pair and complete
                    )
                    incomplete_weight = selected_weight - complete_weight
                    assert (
                        2 * complete_weight >= selected_weight
                        or 2 * incomplete_weight >= selected_weight
                    )
                    if 2 * complete_weight >= selected_weight:
                        assert 2 * complete_weight * pair_count >= total
                    else:
                        assert 2 * incomplete_weight * pair_count > total
                    router_checks += 1

    return router_checks


def verify_composition(maximum_weight=48):
    composition_checks = 0

    for total in range(1, maximum_weight + 1):
        for roles in range(1, 5):
            for multiplicity in range(1, 5):
                for channel_pairs in range(1, 5):
                    for scales in range(1, 5):
                        for profiles in range(1, 5):
                            role_weight = Fraction(total, 2 * roles * multiplicity)
                            channel_weight = role_weight / channel_pairs
                            complete_weight = channel_weight / 2
                            coherent_weight = complete_weight / 2
                            scale_weight = coherent_weight / scales
                            decorated_weight = scale_weight / profiles
                            expected = Fraction(
                                total,
                                8
                                * roles
                                * multiplicity
                                * channel_pairs
                                * scales
                                * profiles,
                            )
                            assert decorated_weight == expected
                            composition_checks += 1

    return composition_checks


def main():
    factors, quotients, scales, carries = verify_real_factors()
    routers = verify_paid_fibre_router()
    compositions = verify_composition()
    print(
        "AC OP-RI realization: verified "
        f"{factors} real factors, {quotients} quotient identities, "
        f"{scales} physical scale identities, {carries} cross carries, "
        f"{routers} paid fibre routers, and {compositions} compositions"
    )


if __name__ == "__main__":
    main()
