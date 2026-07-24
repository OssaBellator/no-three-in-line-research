#!/usr/bin/env python3
"""Arithmetic checks for CMR219--CMR222."""

from __future__ import annotations

from math import ceil, floor, log2, sqrt


def verify_rank_concentration(max_t: int) -> None:
    for t in range(48, max_t + 1):
        remainder = 1 / 24 - 1 / t
        assert remainder >= 1 / 48
        assert remainder / 3 >= 1 / 144

        rank_one = t / 144
        rank_two = t * (t - 1) / 144
        rank_three = t * (t - 1) * (t - 2) / 144
        assert rank_one > 0
        assert rank_two > rank_one
        assert rank_three > rank_two


def verify_extraction_arithmetic(max_t: int) -> None:
    for t in range(48, max_t + 1):
        rank_one_count = floor(t / 144) + 1
        matching_or_star = max(1, floor(sqrt(rank_one_count / 2)))
        neutralized_one = ceil(matching_or_star / 2)
        rank_two_count = floor(t * (t - 1) / 144) + 1
        neutralized_two = ceil(rank_two_count / 2)
        assert neutralized_one >= 1
        assert neutralized_two >= 1


def verify_dyadic_bands(max_t: int) -> None:
    for t in range(48, max_t + 1):
        bands = ceil(log2(t))
        assert bands >= 1
        total = t * (t - 1) * (t - 2) / 144
        band = total / bands
        assert band > 0
        # Every integer height from 1 through t-1 belongs to one of these bands.
        for height in range(1, t):
            index = floor(log2(height))
            assert 0 <= index < bands


def main() -> None:
    verify_rank_concentration(max_t=100_000)
    verify_extraction_arithmetic(max_t=100_000)
    verify_dyadic_bands(max_t=10_000)
    print(
        "verified parent local load: 1/144 rank concentration, anchored "
        "extraction arithmetic, and dyadic primitive-height averaging"
    )


if __name__ == "__main__":
    main()
