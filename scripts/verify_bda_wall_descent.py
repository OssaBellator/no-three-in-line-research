#!/usr/bin/env python3
"""Exhaust BDA5t on small denominator data."""

from math import gcd


def primitive(x: int, y: int) -> tuple[int, int]:
    common = gcd(abs(x), abs(y))
    x //= common
    y //= common
    if x < 0:
        x = -x
        y = -y
    return x, y


def factorization(value: int) -> list[tuple[int, int]]:
    result = []
    prime = 2
    remaining = value
    while prime * prime <= remaining:
        if remaining % prime:
            prime += 1
            continue
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        result.append((prime, exponent))
        prime += 1
    if remaining > 1:
        result.append((remaining, 1))
    return result


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def verify(maximum_denominator: int = 30) -> tuple[int, int, int]:
    identity_count = 0
    prime_count = 0
    terminal_count = 0

    for denominator in range(2, maximum_denominator + 1):
        prime_powers = factorization(denominator)

        for scale in range(1, 3 * denominator + 1):
            common = gcd(scale, denominator)
            reduced_scale = scale // common
            reduced_denominator = denominator // common
            assert gcd(reduced_scale, reduced_denominator) == 1

            loss_product = 1
            for prime, exponent in prime_powers:
                loss_product *= prime ** min(
                    exponent, valuation(scale, prime)
                )
                prime_count += 1
            assert loss_product == common

            for a in range(1, 8):
                for b in range(-7, 8):
                    if b == 0 or gcd(a, abs(b)) != 1:
                        continue

                    mixed_c = primitive(
                        scale * a,
                        (scale + denominator) * b,
                    )
                    reduced_c = primitive(
                        reduced_scale * a,
                        (reduced_scale + reduced_denominator) * b,
                    )
                    assert mixed_c == reduced_c

                    mixed_d = primitive(
                        (scale + denominator) * a,
                        scale * b,
                    )
                    reduced_d = primitive(
                        (reduced_scale + reduced_denominator) * a,
                        reduced_scale * b,
                    )
                    assert mixed_d == reduced_d
                    identity_count += 2

                    if common == denominator:
                        assert reduced_denominator == 1
                        assert reduced_c == primitive(
                            reduced_scale * a,
                            (reduced_scale + 1) * b,
                        )
                        assert reduced_d == primitive(
                            (reduced_scale + 1) * a,
                            reduced_scale * b,
                        )
                        terminal_count += 1

    return identity_count, prime_count, terminal_count


def main() -> None:
    identities, prime_states, terminals = verify()
    print(
        "BDA mixed-wall descent verified: "
        f"{identities} primitive identities, "
        f"{prime_states} prime-power loss states, and "
        f"{terminals} denominator-one terminals"
    )


if __name__ == "__main__":
    main()
