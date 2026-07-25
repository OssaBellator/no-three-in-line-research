#!/usr/bin/env python3
"""Arithmetic checks for CMR393--CMR395."""

from __future__ import annotations


def verify_per_reset_capacity() -> None:
    for p, h in ((3, 6), (5, 5), (7, 4), (11, 3)):
        t = p**h
        for depth in range(1, h):
            token_columns = t // (p**depth)
            for coarse in range(depth):
                block_size = t // (p**coarse)
                extensions = block_size // (p ** (depth - coarse))
                assert extensions == token_columns
                assert token_columns <= block_size


def verify_one_pass_bound() -> None:
    for p, h in ((3, 6), (5, 5), (7, 4), (11, 3)):
        t = p**h
        for depth in range(1, h):
            initial = t * t // (p ** (2 * depth))
            returns = 2 * depth * t // (p**depth)
            slots = 2 * depth
            per_slot = t // (p**depth)
            assert returns == slots * per_slot
            assert initial + returns >= initial


def verify_deep_thresholds() -> None:
    for p, h in ((3, 9), (5, 9), (7, 6), (11, 6)):
        t = p**h
        for depth in range(1, h):
            exact = t * t // (p ** (2 * depth)) + 2 * depth * t // (p**depth)

            if 3 * depth > h:
                upper = t ** 4 + (2 * h) ** 3 * t**2
                assert exact**3 < upper

            if 3 * depth >= 2 * h:
                initial = t * t // (p ** (2 * depth))
                returns = 2 * depth * t // (p**depth)
                assert initial**3 <= t**2
                assert returns**3 <= (2 * h) ** 3 * t


def main() -> None:
    verify_per_reset_capacity()
    verify_one_pass_bound()
    verify_deep_thresholds()
    print(
        "verified full-token reset profile: per-ancestor capacity, one-pass "
        "reintroduction sum, and cubic/deep threshold bounds"
    )


if __name__ == "__main__":
    main()
