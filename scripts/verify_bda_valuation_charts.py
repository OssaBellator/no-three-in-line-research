#!/usr/bin/env python3
"""Verify BDA3h prime-power valuation-pivot classification."""

from __future__ import annotations

from math import gcd


def truncated_valuation(value: int, prime: int, exponent: int) -> int:
    modulus = prime**exponent
    if value % modulus == 0:
        return exponent
    valuation = 0
    while value % prime == 0:
        value //= prime
        valuation += 1
    return valuation


def valuation(value: int, prime: int) -> int:
    assert value
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def prime_divisors(number: int) -> tuple[int, ...]:
    result: list[int] = []
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            result.append(divisor)
            while number % divisor == 0:
                number //= divisor
        divisor += 1
    if number > 1:
        result.append(number)
    return tuple(result)


def valuation_ceiling(bound: int, prime: int) -> int:
    exponent = 0
    power = 1
    while power * prime <= bound:
        power *= prime
        exponent += 1
    return exponent


def common_height(m: int, n: int, q: int) -> int:
    return sum(
        min(valuation(m, prime), valuation(n, prime))
        for prime in prime_divisors(q)
    )


def common_content(m: int, n: int, q: int) -> int:
    result = 1
    for prime in prime_divisors(q):
        result *= prime ** min(valuation(m, prime), valuation(n, prime))
    return result


def units(modulus: int) -> tuple[int, ...]:
    return tuple(
        value for value in range(modulus) if gcd(value, modulus) == 1
    )


def unimodular_vectors(modulus: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (first, second)
        for first in range(modulus)
        for second in range(modulus)
        if gcd(gcd(first, second), modulus) == 1
    )


def projective_class(
    vector: tuple[int, int],
    modulus: int,
) -> tuple[int, int]:
    return min(
        (
            unit * vector[0] % modulus,
            unit * vector[1] % modulus,
        )
        for unit in units(modulus)
    )


def projective_count(modulus: int) -> int:
    result = 1
    remaining = modulus
    for prime in prime_divisors(modulus):
        power = 1
        while remaining % prime == 0:
            remaining //= prime
            power *= prime
        result *= power + power // prime
    return result


def verify_global_projective_atlas(maximum_q: int = 12) -> None:
    for modulus in range(2, maximum_q + 1):
        vectors = unimodular_vectors(modulus)
        classes = {
            projective_class(vector, modulus) for vector in vectors
        }
        expected_classes = projective_count(modulus)
        assert len(classes) == expected_classes
        assert len(vectors) == len(units(modulus)) * expected_classes

        matrix_profiles: dict[
            tuple[int, int, int, int],
            set[tuple[tuple[int, int], tuple[int, int]]],
        ] = {}
        for direction in vectors:
            direction_class = projective_class(direction, modulus)
            for scales in vectors:
                scale_class = projective_class(scales, modulus)
                matrix = (
                    direction[0] * scales[0] % modulus,
                    direction[0] * scales[1] % modulus,
                    direction[1] * scales[0] % modulus,
                    direction[1] * scales[1] % modulus,
                )
                matrix_profiles.setdefault(matrix, set()).add(
                    (direction_class, scale_class)
                )
        assert all(
            len(profiles) == 1 for profiles in matrix_profiles.values()
        )
        assert len(matrix_profiles) == (
            len(units(modulus)) * expected_classes**2
        )


def verify_common_content(maximum_q: int = 30, maximum_bound: int = 20) -> None:
    for q in range(2, maximum_q + 1):
        primes = prime_divisors(q)
        for bound in range(1, maximum_bound + 1):
            ceiling = sum(valuation_ceiling(bound, prime) for prime in primes)
            nonzero = tuple(range(-bound, 0)) + tuple(range(1, bound + 1))
            for m in nonzero:
                for n in nonzero:
                    initial_height = common_height(m, n, q)
                    assert 0 <= initial_height <= ceiling
                    divisor = common_content(m, n, q)
                    reduced_m = m // divisor
                    reduced_n = n // divisor
                    assert divisor * reduced_m == m
                    assert divisor * reduced_n == n
                    assert all(
                        reduced_m % prime or reduced_n % prime
                        for prime in primes
                    )

                    current_m, current_n = m, n
                    steps = 0
                    while True:
                        common_prime = next(
                            (
                                prime
                                for prime in primes
                                if current_m % prime == 0
                                and current_n % prime == 0
                            ),
                            None,
                        )
                        if common_prime is None:
                            break
                        previous = common_height(current_m, current_n, q)
                        current_m //= common_prime
                        current_n //= common_prime
                        assert (
                            common_height(current_m, current_n, q)
                            == previous - 1
                        )
                        steps += 1
                    assert steps == initial_height
                    assert (current_m, current_n) == (reduced_m, reduced_n)

                    for a in range(1, 5):
                        for b in range(-4, 5):
                            if b == 0 or gcd(a, abs(b)) != 1:
                                continue
                            matrix = (
                                (a * reduced_m, a * reduced_n),
                                (b * reduced_m, b * reduced_n),
                            )
                            for prime in primes:
                                assert any(
                                    entry % prime
                                    for row in matrix
                                    for entry in row
                                )
    verify_global_projective_atlas()


def verify() -> None:
    for prime in (2, 3, 5):
        for exponent in range(1, 4):
            prime_power = prime**exponent
            for a in range(1, 8):
                for b in range(-7, 8):
                    if b == 0 or gcd(a, abs(b)) != 1:
                        continue
                    for m in range(-18, 19):
                        for n in range(-18, 19):
                            if m == 0 or n == 0 or m == n:
                                continue
                            matrix = (
                                (a * m, a * n),
                                (b * m, b * n),
                            )
                            kappa = min(
                                exponent,
                                truncated_valuation(m, prime, exponent),
                                truncated_valuation(n, prime, exponent),
                            )
                            entry_kappa = min(
                                truncated_valuation(
                                    entry,
                                    prime,
                                    exponent,
                                )
                                for row in matrix
                                for entry in row
                            )
                            assert entry_kappa == kappa

                            residues = tuple(
                                tuple(entry % prime_power for entry in row)
                                for row in matrix
                            )
                            if kappa == exponent:
                                assert all(
                                    entry == 0
                                    for row in residues
                                    for entry in row
                                )
                                assert m % prime_power == 0
                                assert n % prime_power == 0
                                continue

                            divisor = prime**kappa
                            modulus = prime ** (exponent - kappa)
                            normalized = tuple(
                                tuple((entry // divisor) % modulus for entry in row)
                                for row in matrix
                            )
                            unit_pivots = [
                                (row, column)
                                for row in range(2)
                                for column in range(2)
                                if normalized[row][column] % prime != 0
                            ]
                            assert unit_pivots

                            direction = (a, b)
                            scales = (m // divisor, n // divisor)
                            for row, column in unit_pivots:
                                pivot_inverse = pow(
                                    normalized[row][column],
                                    -1,
                                    modulus,
                                )
                                other_row = 1 - row
                                other_column = 1 - column
                                recovered_direction_ratio = (
                                    normalized[other_row][column]
                                    * pivot_inverse
                                ) % modulus
                                recovered_scale_ratio = (
                                    normalized[row][other_column]
                                    * pivot_inverse
                                ) % modulus
                                assert direction[row] % prime != 0
                                assert scales[column] % prime != 0
                                assert recovered_direction_ratio == (
                                    direction[other_row]
                                    * pow(direction[row], -1, modulus)
                                ) % modulus
                                assert recovered_scale_ratio == (
                                    scales[other_column]
                                    * pow(scales[column], -1, modulus)
                                ) % modulus
    verify_common_content()


def main() -> None:
    verify()
    print("BDA valuation-pivot charts: verified")


if __name__ == "__main__":
    main()
