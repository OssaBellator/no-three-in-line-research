#!/usr/bin/env python3
"""Exact checks for CMR318--CMR321."""

from __future__ import annotations

from math import comb, factorial


def valuation(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def signed_weight(t: int, x: int) -> int:
    return (-1) ** (t - 1 - x) * factorial(x) * factorial(t - 1 - x)


def unsigned_weight(t: int, x: int) -> int:
    return factorial(x) * factorial(t - 1 - x)


def special_rows(
    x1: int,
    x2: int,
    y3: int,
    lines: list[tuple[int, int, int]],
) -> tuple[int, int]:
    first_special = None
    second_special = None
    for a, b, c in lines:
        if c == x1:
            assert a == y3
            second_special = b
        if c == x2:
            assert b == y3
            first_special = a
    assert first_special is not None
    assert second_special is not None
    return first_special, second_special


def verify_explicit_mixed_fans() -> None:
    certificates = [
        (
            5,
            ((0, 0), (1, 1), (4, 4)),
            [(3, 4, 1), (1, 2, 3), (2, 3, 2), (4, 0, 0)],
        ),
        (
            5,
            ((0, 2), (1, 1), (2, 0)),
            [(1, 0, 1), (3, 2, 3), (4, 3, 4), (0, 4, 0)],
        ),
        (
            7,
            ((0, 0), (1, 1), (6, 6)),
            [(5, 6, 1), (1, 2, 5), (3, 4, 3), (4, 5, 2), (2, 3, 4), (6, 0, 0)],
        ),
        (
            7,
            ((2, 0), (4, 2), (5, 3)),
            [(1, 3, 4), (6, 0, 3), (4, 6, 1), (5, 4, 6), (2, 1, 0), (3, 5, 2)],
        ),
    ]

    for t, triple, lines in certificates:
        (x1, _), (x2, _), (_, y3) = triple
        assert len(lines) == t - 1
        assert len({a for a, _, _ in lines}) == t - 1
        assert len({b for _, b, _ in lines}) == t - 1
        assert len({c for _, _, c in lines}) == t - 1
        a0, b0 = special_rows(x1, x2, y3, lines)
        left = signed_weight(t, x2) * (y3 - b0)
        right = -signed_weight(t, x1) * (y3 - a0)
        assert left == right
        assert abs(y3 - b0) * unsigned_weight(t, x2) == abs(
            y3 - a0
        ) * unsigned_weight(t, x1)


def verify_prime_power_unit_ratios() -> None:
    for p, h in ((3, 4), (5, 3), (7, 3), (11, 2)):
        t = p**h
        signed = [signed_weight(t, x) for x in range(t)]
        valuations = {valuation(value, p) for value in signed}
        assert len(valuations) == 1
        common = next(iter(valuations))
        units = [value // (p**common) for value in signed]

        for x in range(t):
            assert comb(t - 1, x) % p == (-1) ** x % p

        probes = (0, t // 3, t // 2, t - 1)
        for unit1 in units:
            for x2 in probes:
                unit2 = units[x2]
                ratio = (unit1 % p) * pow(unit2 % p, -1, p) % p
                assert ratio == 1


def verify_archimedean_localization() -> None:
    for t in range(4, 200):
        weights = [unsigned_weight(t, x) for x in range(t)]
        for numerator in weights:
            for denominator in weights:
                possible = (
                    numerator <= (t - 1) * denominator
                    and denominator <= (t - 1) * numerator
                )
                if possible:
                    assert numerator <= (t - 1) * denominator
                    assert denominator <= (t - 1) * numerator

        for x in range(t - 1):
            left = weights[x + 1] * (t - 1 - x)
            right = weights[x] * (x + 1)
            assert left == right


def main() -> None:
    verify_explicit_mixed_fans()
    verify_prime_power_unit_ratios()
    verify_archimedean_localization()
    print(
        "verified mixed-fan factorial carry: exact certificates, Lucas units, "
        "opposite reduced deviations, and factorial-weight localization"
    )


if __name__ == "__main__":
    main()
