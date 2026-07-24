#!/usr/bin/env python3
"""Arithmetic checks for CMR206--CMR209."""

from __future__ import annotations

from math import ceil


def peel_sequence(t: int) -> tuple[list[int], int]:
    threshold = ceil(t / 2)
    degree = t - 1
    peels = []
    while degree > threshold:
        excess = degree - threshold
        wall_majority = ceil((excess + 1) / 3)
        assert wall_majority >= 1
        peels.append(wall_majority)
        degree -= wall_majority
    return peels, degree


def verify_sequences(max_t: int) -> None:
    for t in range(5, max_t + 1):
        peels, degree = peel_sequence(t)
        threshold = ceil(t / 2)
        assert degree == threshold
        assert sum(peels) == (t // 2) - 1
        assert all(value >= 1 for value in peels)
        assert len(peels) <= 1 + t.bit_length()

        current_degree = t - 1
        for value in peels:
            excess = current_degree - threshold
            wall_size = current_degree - ((t - 1) // 2)
            assert wall_size == excess + 1
            assert value == ceil(wall_size / 3)
            next_degree = current_degree - value
            assert next_degree >= threshold
            if excess >= 1:
                next_excess = next_degree - threshold
                assert 3 * next_excess < 2 * excess + 1
            current_degree = next_degree


def main() -> None:
    verify_sequences(max_t=1_000_000)
    print(
        "verified iterated Hall peeling: logarithmic peel count, exact "
        "floor(t/2)-1 telescoping loss, and final half-degree host"
    )


if __name__ == "__main__":
    main()
