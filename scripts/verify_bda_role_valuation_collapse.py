#!/usr/bin/env python3
"""Exhaust BDA5q--BDA5s on small prime-power data."""

from math import gcd


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def primitive(x: int, y: int) -> tuple[int, int]:
    common = gcd(abs(x), abs(y))
    x //= common
    y //= common
    if x < 0:
        x = -x
        y = -y
    return x, y


def verify() -> tuple[int, int, int, int]:
    identity_count = 0
    visible_count = 0
    wall_count = 0
    reflected_count = 0

    for prime in (2, 3, 5):
        for exponent in range(1, 4):
            modulus = prime**exponent

            for h in range(1, 2 * modulus + 1):
                capital_h = h + modulus

                for a in range(1, 6):
                    for b in range(-5, 6):
                        if b == 0 or gcd(a, abs(b)) != 1:
                            continue

                        channel_vectors = {
                            "A": (h * a, h * b),
                            "B": (capital_h * a, capital_h * b),
                            "C": (h * a, capital_h * b),
                            "D": (capital_h * a, h * b),
                        }

                        wall_loss = min(exponent, valuation(h, prime))
                        if wall_loss < exponent:
                            wall_modulus = prime ** (exponent - wall_loss)
                            for name in ("C", "D"):
                                x, y = primitive(*channel_vectors[name])
                                assert (x * b - y * a) % wall_modulus == 0
                                assert min(
                                    valuation(x, prime), valuation(y, prime)
                                ) == 0
                                wall_count += 1

                        for r in range(1, 5):
                            for s in range(-4, 5):
                                if s == 0 or gcd(r, abs(s)) != 1:
                                    continue

                                delta = a * s - b * r
                                if delta == 0:
                                    continue

                                exact = {
                                    "A": h * delta,
                                    "B": h * delta + modulus * delta,
                                    "C": h * delta - modulus * b * r,
                                    "D": h * delta + modulus * a * s,
                                }
                                base = h * delta
                                visible_valuation = min(
                                    exponent, valuation(base, prime)
                                )

                                for name, (x, y) in channel_vectors.items():
                                    determinant = x * s - y * r
                                    assert determinant == exact[name]
                                    assert (determinant - base) % modulus == 0
                                    identity_count += 1

                                    if visible_valuation < exponent:
                                        assert (
                                            valuation(determinant, prime)
                                            == visible_valuation
                                        )
                                        reduced_modulus = prime ** (
                                            exponent - visible_valuation
                                        )
                                        prime_power = prime**visible_valuation
                                        assert (
                                            determinant // prime_power
                                            - base // prime_power
                                        ) % reduced_modulus == 0
                                        visible_count += 1
                                    else:
                                        assert determinant % modulus == 0

                        for role in range(-3, 4):
                            if role == 0:
                                continue
                            scalar = 2 * h + modulus
                            offset = role * a * b * scalar
                            assert valuation(offset, prime) == (
                                valuation(role * a * b, prime)
                                + valuation(scalar, prime)
                            )
                            first_valuation = valuation(2 * h, prime)
                            if first_valuation != exponent:
                                assert valuation(scalar, prime) == min(
                                    first_valuation, exponent
                                )
                            else:
                                assert valuation(scalar, prime) >= exponent
                            reflected_count += 1

    return identity_count, visible_count, wall_count, reflected_count


def main() -> None:
    identities, visible, walls, reflected = verify()
    print(
        "BDA role valuation collapse verified: "
        f"{identities} determinant identities, "
        f"{visible} visible prime-power states, "
        f"{walls} wall-direction states, and "
        f"{reflected} reflected-offset valuations"
    )


if __name__ == "__main__":
    main()
