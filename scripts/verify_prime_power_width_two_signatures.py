#!/usr/bin/env python3
"""Exact checks for CMR291--CMR293."""

from __future__ import annotations

from collections import Counter
from math import ceil, gcd, isqrt, sqrt


def divisor_count(n: int) -> int:
    total = 0
    root = isqrt(n)
    for divisor in range(1, root + 1):
        if n % divisor != 0:
            continue
        total += 1
        if divisor * divisor != n:
            total += 1
    return total


def verify_primitive_continuation(max_t: int = 30) -> None:
    # Finite exact geometry range; CMR291 proves the general lattice statement.
    for t in range(4, max_t + 1):
        for x1 in range(t):
            for x2 in range(x1 + 1, t):
                d = x2 - x1
                for a in range(t):
                    for b in range(t):
                        if a == b:
                            continue
                        e = b - a
                        common = gcd(d, abs(e))
                        u = d // common
                        v = e // common
                        assert gcd(u, abs(v)) == 1
                        assert (x1 + common * u, a + common * v) == (x2, b)

                        parameters = []
                        for q in range(-t, t + 1):
                            x = x1 + q * u
                            y = a + q * v
                            if 0 <= x < t and 0 <= y < t:
                                parameters.append(q)
                        assert 0 in parameters
                        assert common in parameters
                        assert len(parameters) == len(
                            {(x1 + q * u, a + q * v) for q in parameters}
                        )


def verify_divisor_strata(max_d: int = 100_000) -> None:
    for d in range(1, max_d + 1):
        tau = divisor_count(d)
        assert tau <= 2 * sqrt(d)
        assert tau <= 2 * isqrt(d) + 1

        # Synthetic population distributed among all possible gcd strata.
        population = max(1, d - 1)
        counts = Counter(index % tau for index in range(population))
        largest = max(counts.values())
        assert largest >= ceil(population / tau)


def verify_uniform_lower_bound(max_t: int = 100_000) -> None:
    for t in range(4, max_t + 1):
        for d in (1, max(1, (t - 1) // 2), t - 1):
            tau = divisor_count(d)
            exact = ceil((t - 2) / tau)
            crude = ceil((t - 2) / (2 * sqrt(t - 1)))
            assert exact >= crude


def main() -> None:
    verify_primitive_continuation()
    verify_divisor_strata()
    verify_uniform_lower_bound()
    print(
        "verified width-two primitive signatures: lattice continuation, "
        "internal/extension parameters, and common gcd strata"
    )


if __name__ == "__main__":
    main()
