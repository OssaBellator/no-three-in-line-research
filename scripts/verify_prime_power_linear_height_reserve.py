#!/usr/bin/env python3
"""Arithmetic checks for CMR237--CMR239."""

from math import floor


def threshold_polynomial(t: int) -> int:
    return 178 * t**3 - 31125 * t**2 + 53450 * t - 30000


def local_load_upper_bound(t: int) -> float:
    height = 49 * t / 100
    top_load = 2 * (
        (t * t - 1) / 4 - height * (height - 1)
    ) / ((t - 1) * (t - 2))
    return 1 / t + 1 / 100 + top_load


def verify_threshold(max_t: int = 1_000_001) -> None:
    assert threshold_polynomial(173) < 0
    assert threshold_polynomial(175) > 0
    previous = threshold_polynomial(175)
    for t in range(175, max_t + 1, 2):
        current = threshold_polynomial(t)
        assert current > 0
        assert current >= previous
        previous = current
        assert local_load_upper_bound(t) < 1 / 24


def verify_reserve_arithmetic(max_t: int = 1_000_001) -> None:
    for t in range(175, max_t + 1, 2):
        reserve = floor(t / 100)
        assert (1 + reserve) / t <= 1 / t + 1 / 100
        assert reserve >= 1


def main() -> None:
    verify_threshold()
    verify_reserve_arithmetic()
    print(
        "verified linear lower-height reserve: cubic threshold for all odd "
        "t from 175 through 1000001 and floor(t/100) forbidden lines"
    )


if __name__ == "__main__":
    main()
