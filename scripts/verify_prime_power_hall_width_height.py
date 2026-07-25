#!/usr/bin/env python3
"""Arithmetic checks for CMR271--CMR273."""

from __future__ import annotations

from math import ceil


def verify_incidence_average(max_t: int = 100_000) -> None:
    for t in range(4, max_t + 1):
        for n in range(2, (t + 1) // 2 + 1):
            covered = n * (t + 1 - n) - 1
            assert 2 * covered >= n * (t - 1)
            assert ceil(covered / (t - 1)) >= ceil(n / 2)


def verify_height_conversion(max_t: int = 100_000) -> None:
    for t in range(7, max_t + 1):
        for n in range(3, (t + 1) // 2 + 1):
            guaranteed_cells = ceil(n / 2)
            denominator = guaranteed_cells - 1
            if denominator == 0:
                continue
            height_bound = (t - 1) / denominator
            assert height_bound <= 2 * (t - 1) / (n - 2)

            if n >= 7:
                assert 2 * (t - 1) / (n - 2) < 43 * t / 100


def verify_width_six_boundary(max_t: int = 100_000) -> None:
    for t in range(7, max_t + 1):
        width_six_bound = 2 * (t - 1) / 4
        width_seven_bound = 2 * (t - 1) / 5
        assert width_seven_bound < 43 * t / 100
        assert width_six_bound >= width_seven_bound


def main() -> None:
    verify_incidence_average()
    verify_height_conversion()
    verify_width_six_boundary()
    print(
        "verified Hall-width reduction: long-line averaging and the width-seven "
        "entry into the sub-0.43t primitive-height regime"
    )


if __name__ == "__main__":
    main()
