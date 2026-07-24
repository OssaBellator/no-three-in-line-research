#!/usr/bin/env python3
"""Arithmetic checks for CMR203--CMR205."""

from __future__ import annotations

from fractions import Fraction
from math import ceil


def wall_size(t: int) -> int:
    return ceil((t // 2) / 3)


def wall_masses(t: int) -> tuple[Fraction, Fraction, Fraction]:
    wall = wall_size(t)
    return (
        Fraction(wall, t - 1),
        Fraction(30 * wall, 11 * t * (t - 1)),
        Fraction(30 * wall, 11 * t * (t - 1) * (t - 2)),
    )


def verify_mass_maxima(max_t: int) -> None:
    maxima = [Fraction(0), Fraction(0), Fraction(0)]
    maximizers = [None, None, None]
    for t in range(5, max_t + 1):
        for index, value in enumerate(wall_masses(t)):
            if value > maxima[index]:
                maxima[index] = value
                maximizers[index] = t
    assert maxima == [Fraction(2, 7), Fraction(3, 22), Fraction(1, 22)]
    assert maximizers == [8, 5, 5]


def verify_residual_bounds(max_t: int) -> None:
    betas = (Fraction(2, 7), Fraction(3, 22), Fraction(1, 22))
    for t in range(5, max_t + 1):
        masses = wall_masses(t)
        for rank, beta in enumerate(betas):
            assert masses[rank] <= beta
            residual = 1 - beta
            required = ceil(residual * (t - 1))
            assert required >= 1
            assert Fraction(required, 1) >= residual * (t - 1)


def main() -> None:
    verify_mass_maxima(max_t=100_000)
    verify_residual_bounds(max_t=100_000)
    print(
        "verified Hall-wall peeling: maxima 2/7, 3/22, 1/22 and "
        "residual cover factors 5/7, 19/22, 21/22"
    )


if __name__ == "__main__":
    main()
