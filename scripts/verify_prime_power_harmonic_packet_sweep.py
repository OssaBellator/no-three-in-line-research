#!/usr/bin/env python3
"""Arithmetic checks for CMR406--CMR409."""

from __future__ import annotations

from math import ceil, log2


def verify_packet_counts() -> None:
    for side in range(5, 100_001):
        lower_endpoints = []
        value = 1
        while value <= side - 1:
            if value >= 5:
                lower_endpoints.append(value)
            value *= 2
        bands = len(lower_endpoints)
        packets = ceil(bands / 2)
        assert packets <= ceil((1 + log2(side)) / 2)


def verify_per_token_budget() -> None:
    for p, h in ((3, 8), (5, 6), (7, 5), (11, 4)):
        side = p**h
        packets = ceil((1 + log2(side)) / 2)
        for depth in range(1, h):
            width = side // (p**depth)
            packet_return = packets * width
            prefix_return = 2 * depth * width
            initial = width**2
            combined = initial + prefix_return + packet_return
            assert combined == initial + (2 * depth + packets) * width

            if 3 * depth >= 2 * h:
                assert initial**3 <= side**2
                assert width**3 <= side


def verify_aggregate_sum() -> None:
    for p, h in ((3, 8), (5, 6), (7, 5), (11, 4)):
        side = p**h
        packets = ceil((1 + log2(side)) / 2)
        directions = p + 1
        exact = sum(
            directions
            * p ** (2 * depth)
            * packets
            * side
            // (p**depth)
            for depth in range(1, h)
        )
        displayed = directions * packets * side * sum(
            p**depth for depth in range(1, h)
        )
        assert exact == displayed
        assert exact < directions * packets * side * side // (p - 1)


def main() -> None:
    verify_packet_counts()
    verify_per_token_budget()
    verify_aggregate_sum()
    print(
        "verified harmonic packet sweep: packet counts, per-token return, "
        "deep thresholds, and aggregate quadratic-logarithmic cost"
    )


if __name__ == "__main__":
    main()
