#!/usr/bin/env python3
"""Verify RI2g polynomial gcd certificates for involution boundary."""

from __future__ import annotations

from itertools import combinations

Polynomial = list[int]


def trim(polynomial: Polynomial) -> Polynomial:
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def multiply(left: Polynomial, right: Polynomial, p: int) -> Polynomial:
    result = [0] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            result[left_degree + right_degree] = (
                result[left_degree + right_degree]
                + left_coefficient * right_coefficient
            ) % p
    return trim(result)


def divide_with_remainder(
    dividend: Polynomial,
    divisor: Polynomial,
    p: int,
) -> tuple[Polynomial, Polynomial]:
    remainder = trim(dividend.copy())
    divisor = trim(divisor.copy())
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, p)
    while len(remainder) >= len(divisor) and remainder != [0]:
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % p
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + degree] = (
                remainder[index + degree] - coefficient * value
            ) % p
        trim(remainder)
    return trim(quotient), trim(remainder)


def monic(polynomial: Polynomial, p: int) -> Polynomial:
    polynomial = trim(polynomial.copy())
    inverse = pow(polynomial[-1], -1, p)
    return [(coefficient * inverse) % p for coefficient in polynomial]


def polynomial_gcd(
    left: Polynomial,
    right: Polynomial,
    p: int,
) -> Polynomial:
    left = trim(left.copy())
    right = trim(right.copy())
    while right != [0]:
        _, remainder = divide_with_remainder(left, right, p)
        left, right = right, remainder
    return monic(left, p)


def root_polynomial(values: set[int], p: int) -> Polynomial:
    result = [1]
    for value in sorted(values):
        result = multiply(result, [(-value) % p, 1], p)
    return result


def transformed_polynomial(
    values: set[int],
    r: int,
    p: int,
) -> Polynomial:
    result = [1]
    for value in sorted(values):
        result = multiply(
            result,
            [r * (value - 1) % p, (r - value) % p],
            p,
        )
    return result


def primes_through(limit: int) -> list[int]:
    return [
        value
        for value in range(3, limit + 1, 2)
        if all(
            value % divisor
            for divisor in range(2, int(value**0.5) + 1)
        )
    ]


def prime_factors(number: int) -> set[int]:
    factors: set[int] = set()
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.add(number)
    return factors


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    return next(
        candidate
        for candidate in range(2, p)
        if all(
            pow(candidate, (p - 1) // factor, p) != 1
            for factor in factors
        )
    )


def divisors(number: int) -> list[int]:
    return [value for value in range(1, number + 1) if number % value == 0]


def partner(x: int, r: int, p: int) -> int:
    return r * (x - 1) * pow(x - r, -1, p) % p


def rational_image(x: int, r: int, p: int) -> int:
    return x * (1 - x) * pow(r - x, -1, p) % p


def orbit_trace(x: int, r: int, p: int) -> int:
    shifted = (x - r) % p
    delta = r * (r - 1) % p
    return (shifted + delta * pow(shifted, -1, p)) % p


def orbit_factor_polynomial(
    core: set[int],
    r: int,
    p: int,
) -> Polynomial:
    result = [1]
    seen: set[int] = set()
    delta = r * (r - 1) % p
    for value in sorted(core):
        if value in seen:
            continue
        mate = partner(value, r, p)
        if mate == value:
            factor = [(-value) % p, 1]
            seen.add(value)
        else:
            trace = orbit_trace(value, r, p)
            factor = [
                (r * r + trace * r + delta) % p,
                (-2 * r - trace) % p,
                1,
            ]
            seen.update((value, mate))
        result = multiply(result, factor, p)
    return result


def verify_orbit_trace(limit: int = 43) -> None:
    for p in primes_through(limit):
        for r in range(2, p):
            domain = tuple(
                x for x in range(1, p) if x not in (1, r)
            )
            for x in domain:
                trace = orbit_trace(x, r, p)
                mate = partner(x, r, p)
                image = rational_image(x, r, p)
                assert rational_image(x, r, p) == (
                    2 * r - 1 + trace
                ) % p
                assert orbit_trace(mate, r, p) == trace
                assert (x + mate) % p == (image + 1) % p
                assert x * mate % p == r * image % p
                assert (
                    x * x - (image + 1) * x + r * image
                ) % p == 0
                assert (
                    mate * mate - (image + 1) * mate + r * image
                ) % p == 0
                for z in domain:
                    assert (orbit_trace(z, r, p) == trace) == (
                        z == x or z == mate
                    )


def quotient_subsets(index: int) -> set[frozenset[int]]:
    labels = set(range(index))
    if index <= 7:
        return {
            frozenset(
                label for label in range(index) if mask & (1 << label)
            )
            for mask in range(1 << index)
        }
    selected: set[frozenset[int]] = set()
    for size in range(3):
        for subset in combinations(range(index), size):
            frozen = frozenset(subset)
            selected.add(frozen)
            selected.add(frozenset(labels - set(frozen)))
    return selected


def sparse_coset_polynomial(
    representatives: list[int],
    order: int,
    p: int,
) -> Polynomial:
    result = [1]
    for representative in representatives:
        factor = [0] * (order + 1)
        factor[0] = -pow(representative, order, p) % p
        factor[order] = 1
        result = multiply(result, factor, p)
    return result


def verify(limit: int = 23) -> None:
    for p in primes_through(limit):
        generator = primitive_root(p)
        logarithm = {
            pow(generator, exponent, p): exponent
            for exponent in range(p - 1)
        }
        for order in divisors(p - 1):
            index = (p - 1) // order
            subgroup = {
                pow(generator, index * exponent, p)
                for exponent in range(order)
            }
            cosets = [
                {
                    pow(generator, label, p) * value % p
                    for value in subgroup
                }
                for label in range(index)
            ]
            subsets = quotient_subsets(index)
            for labels in subsets:
                full = set().union(*(cosets[label] for label in labels))
                representatives = [pow(generator, label, p) for label in labels]
                assert root_polynomial(full, p) == sparse_coset_polynomial(
                    representatives,
                    order,
                    p,
                )

                for r in range(2, p):
                    domain = full - {1, r}
                    boundary = sum(
                        partner(x, r, p) not in domain for x in domain
                    )
                    polynomial = root_polynomial(domain, p)
                    transformed = transformed_polynomial(domain, r, p)
                    common = polynomial_gcd(polynomial, transformed, p)
                    assert len(common) - 1 == len(domain) - boundary
                    if boundary == 0:
                        assert monic(transformed, p) == polynomial

                    core = {
                        x for x in domain if partner(x, r, p) in domain
                    }
                    outliers = domain - core
                    assert len(outliers) == boundary
                    assert {
                        partner(x, r, p) for x in core
                    } == core
                    assert common == root_polynomial(core, p)

                    core_polynomial = root_polynomial(core, p)
                    core_transformed = transformed_polynomial(core, r, p)
                    leading = 1
                    for value in core:
                        leading = leading * (r - value) % p
                    assert core_transformed == [
                        leading * coefficient % p
                        for coefficient in core_polynomial
                    ]

                    core_image = {
                        rational_image(x, r, p) for x in core
                    }
                    outlier_image = {
                        rational_image(x, r, p) for x in outliers
                    }
                    assert len(outlier_image) == len(outliers)
                    assert core_image.isdisjoint(outlier_image)
                    assert core_image | outlier_image == {
                        rational_image(x, r, p) for x in domain
                    }
                    fixed = sum(
                        partner(x, r, p) == x for x in core
                    )
                    assert 2 * len(core_image) == len(core) + fixed
                    assert orbit_factor_polynomial(core, r, p) == (
                        core_polynomial
                    )
                    assert core_image == {
                        (2 * r - 1 + orbit_trace(x, r, p)) % p
                        for x in core
                    }

                    target_labels = {
                        logarithm[value] % index for value in core_image
                    }
                    neighbours_by_colour: dict[
                        int,
                        dict[int, int],
                    ] = {}
                    seen_orbits: set[int] = set()
                    r_label = logarithm[r] % index
                    for x in core:
                        if x in seen_orbits:
                            continue
                        mate = partner(x, r, p)
                        image = rational_image(x, r, p)
                        left = logarithm[x] % index
                        right = logarithm[mate] % index
                        colour = logarithm[image] % index
                        assert colour == (left + right - r_label) % index
                        for source, neighbour in (
                            (left, right),
                            (right, left),
                        ):
                            colour_map = neighbours_by_colour.setdefault(
                                source,
                                {},
                            )
                            if colour in colour_map:
                                assert colour_map[colour] == neighbour
                            else:
                                colour_map[colour] = neighbour
                        seen_orbits.update((x, mate))
                    assert all(
                        len(set(colour_map.values())) <= len(target_labels)
                        for colour_map in neighbours_by_colour.values()
                    )

                    if len(domain) <= 8:
                        ordered = tuple(sorted(domain))
                        for mask in range(1 << len(ordered)):
                            candidate = {
                                value
                                for index, value in enumerate(ordered)
                                if mask & (1 << index)
                            }
                            if {
                                partner(x, r, p) for x in candidate
                            } == candidate:
                                assert candidate <= core


def main() -> None:
    verify_orbit_trace()
    verify()
    print("rational boundary gcd/orbit traces: verified")


if __name__ == "__main__":
    main()
