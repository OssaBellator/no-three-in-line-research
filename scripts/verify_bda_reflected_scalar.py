#!/usr/bin/env python3
"""Verify BDA5aa--BDA5ad by exhaustive integer and congruence checks."""

from math import gcd


def prime_factorization(value):
    factors = []
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def valuation(value, prime):
    if value == 0:
        return 10**9
    exponent = 0
    remaining = abs(value)
    while remaining % prime == 0:
        remaining //= prime
        exponent += 1
    return exponent


def verify_gcd_and_units(maximum_q=120, coefficient_bound=24, scale_bound=140):
    gcd_checks = 0
    valuation_checks = 0
    unit_checks = 0

    for q in range(2, maximum_q + 1):
        factors = prime_factorization(q)
        for coefficient in range(-coefficient_bound, coefficient_bound + 1):
            for scale in range(-scale_bound, scale_bound + 1):
                reflected = coefficient * (2 * scale + q)
                linear = 2 * coefficient * scale
                common = gcd(abs(reflected), q)
                assert common == gcd(abs(linear), q)
                gcd_checks += 1

                for prime, exponent in factors:
                    assert min(exponent, valuation(reflected, prime)) == min(
                        exponent, valuation(linear, prime)
                    )
                    valuation_checks += 1

                reduced_modulus = q // common
                if reduced_modulus > 1:
                    assert gcd(abs(reflected // common), reduced_modulus) == 1
                    assert (
                        reflected // common - linear // common
                    ) % reduced_modulus == 0
                    unit_checks += 1

    return gcd_checks, valuation_checks, unit_checks


def predicted_solutions(q, coefficient, residue):
    divisor = gcd(abs(2 * coefficient), q)
    if residue % divisor:
        return set()
    modulus = q // divisor
    if modulus == 1:
        return set(range(q))

    reduced_coefficient = (2 * coefficient // divisor) % modulus
    reduced_residue = (residue // divisor) % modulus
    inverse = pow(reduced_coefficient, -1, modulus)
    base = reduced_residue * inverse % modulus
    return {value for value in range(q) if value % modulus == base}


def verify_congruences(maximum_q=90, coefficient_bound=30):
    congruence_checks = 0
    spacing_checks = 0

    for q in range(2, maximum_q + 1):
        for coefficient in range(-coefficient_bound, coefficient_bound + 1):
            divisor = gcd(abs(2 * coefficient), q)
            modulus = q // divisor
            for residue in range(q):
                actual = {
                    scale
                    for scale in range(q)
                    if coefficient * (2 * scale + q) % q == residue
                }
                predicted = predicted_solutions(q, coefficient, residue)
                assert actual == predicted
                congruence_checks += 1

                ordered = sorted(actual)
                if len(ordered) >= 2:
                    differences = [
                        right - left
                        for left, right in zip(ordered, ordered[1:])
                    ]
                    assert all(difference == modulus for difference in differences)
                    horizon = ordered[-1] - ordered[0] + 1
                    assert horizon >= 1 + modulus * (len(ordered) - 1)
                    spacing_checks += 1

    return congruence_checks, spacing_checks


def verify_interval_bounds(maximum_horizon=160):
    checks = 0
    for modulus in range(1, 50):
        for horizon in range(1, maximum_horizon + 1):
            for start in range(modulus):
                occupied = [
                    value
                    for value in range(1, horizon + 1)
                    if value % modulus == start
                ]
                count = len(occupied)
                assert count <= 1 + (horizon - 1) // modulus
                if count:
                    assert horizon >= 1 + modulus * (count - 1)
                checks += 1
    return checks


def main():
    gcd_checks, valuations, units = verify_gcd_and_units()
    congruences, spacing = verify_congruences()
    intervals = verify_interval_bounds()
    print(
        "BDA reflected scalar: verified "
        f"{gcd_checks} gcd identities, {valuations} prime-power truncations, "
        f"{units} reduced units, {congruences} congruence systems, "
        f"{spacing} exact slot chains, and {intervals} interval bounds"
    )


if __name__ == "__main__":
    main()
