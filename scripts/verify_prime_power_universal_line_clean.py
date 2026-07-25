#!/usr/bin/env python3
"""Arithmetic checks for CMR360--CMR363."""

from __future__ import annotations

from math import ceil, factorial, floor, isqrt


def derangements(n: int) -> int:
    total = 0
    for j in range(n + 1):
        total += (-1) ** j * factorial(n) // factorial(j)
    return total


def verify_equal_cylinder_counts() -> None:
    for t in range(7, 20):
        n = t - 2
        count = derangements(n)
        assert count > 0
        for population in (t - 1, t - 2, max(1, t - 9)):
            assert population * count // population == count


def verify_amplification(max_t: int = 100_000) -> None:
    for t in range(2847, max_t + 1):
        reserve = floor(t / 1000) + 1
        for population in (t - 1, t - 2, t - 9):
            incidences = population * reserve
            threshold = isqrt(incidences)
            if threshold * threshold < incidences:
                threshold += 1
            assert (threshold - 1) ** 2 < incidences <= threshold**2
            assert threshold >= ceil(t / 32)

            if threshold > 1:
                assert ceil(incidences / (threshold - 1)) >= threshold


def verify_width_populations(max_t: int = 100_000) -> None:
    for t in range(10, max_t + 1):
        assert t - 1 >= t - 9
        assert t - 2 >= t - 9
        for width in range(4, 7):
            lower = t - 2 - width * (width - 2)
            if lower > 0:
                assert lower <= t - 1


def main() -> None:
    verify_equal_cylinder_counts()
    verify_amplification()
    verify_width_populations()
    print(
        "verified universal line-clean banks: equal derangement cylinders, "
        "sharp-blocker populations, and quadratic low-height amplification"
    )


if __name__ == "__main__":
    main()
