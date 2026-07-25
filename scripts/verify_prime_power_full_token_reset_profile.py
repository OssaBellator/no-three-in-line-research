#!/usr/bin/env python3
"""Arithmetic checks for CMR398--CMR402."""

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
            initial = t * t // (p ** (2 * depth))
            returns = 2 * depth * t // (p**depth)

            if 3 * depth > h:
                assert initial**3 < t**4
                assert returns**3 < (2 * h) ** 3 * t**2

            if 3 * depth >= 2 * h:
                assert initial**3 <= t**2
                assert returns**3 <= (2 * h) ** 3 * t


def verify_reset_occurrence_factorization() -> None:
    for p, h in ((3, 7), (5, 5), (7, 4)):
        t = p**h
        for depth in range(1, h):
            slots = 2 * depth
            per_reset = t // (p**depth)
            initial = t * t // (p ** (2 * depth))
            for cap in range(7):
                counts = [cap] * slots
                total_returns = sum(counts) * per_reset
                assert total_returns == 2 * depth * cap * per_reset
                assert initial + total_returns == (
                    initial + 2 * depth * cap * t // (p**depth)
                )

                counts[0] += 1
                assert max(counts) > cap
                assert sum(counts) * per_reset > 2 * depth * cap * per_reset


def verify_aggregate_labelled_sum() -> None:
    for p, h in ((3, 7), (5, 6), (7, 5), (11, 4)):
        t = p**h
        directions = p + 1
        exact = 0
        for depth in range(1, h):
            token_count = directions * p ** (2 * depth)
            per_token = 2 * depth * t // (p**depth)
            exact += token_count * per_token

        displayed = 2 * directions * t * sum(
            depth * p**depth for depth in range(1, h)
        )
        assert exact == displayed
        assert exact < 2 * directions * h * t * t // (p - 1)


def main() -> None:
    verify_per_reset_capacity()
    verify_one_pass_bound()
    verify_deep_thresholds()
    verify_reset_occurrence_factorization()
    verify_aggregate_labelled_sum()
    print(
        "verified full-token reset profile: per-ancestor capacity, one-pass "
        "visit bounds, deep thresholds, reset multiplicity, and aggregate mass"
    )


if __name__ == "__main__":
    main()
