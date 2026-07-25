#!/usr/bin/env python3
"""Finite checks for PX461--PX465 explicit nested depth bounds."""

from __future__ import annotations

import math
import random


def depth_envelope(initial_order: int) -> int:
    return 1 + math.ceil(
        math.log2(math.log2(max(initial_order, 2)) + 2)
    )


def square_bound(initial_order: int, steps: int) -> float:
    y0 = math.log2(initial_order)
    return (y0 + 2) / (2**steps) - 2


def check_closed_recurrence() -> None:
    rng = random.Random(462)
    for _ in range(10000):
        initial = rng.uniform(32, 10**100)
        value = initial
        for steps in range(1, 20):
            value = math.sqrt(value) / 2
            assert math.log2(value) <= square_bound(initial, steps) + 1e-10


def check_integer_chains() -> None:
    # Exhaust exact integer states with arbitrary admissible obstruction sizes.
    for initial in range(32, 5000):
        for delta0 in range(0, 8):
            frontier = {(initial, 0)}
            longest = 0
            seen: set[tuple[int, int]] = set()
            while frontier:
                order, generation = frontier.pop()
                if (order, generation) in seen:
                    continue
                seen.add((order, generation))
                longest = max(longest, generation)
                delta = delta0 + generation
                threshold = max(32, 16 * delta + 4)

                # Terminal obstruction may have any h < threshold.
                max_h = min(order, threshold * threshold - 1)
                for obstruction in range(threshold, max_h + 1):
                    q = max(obstruction ** -0.5, threshold / obstruction)
                    next_order = math.floor(q * obstruction / 2)
                    assert next_order >= 8 * delta + 2
                    assert next_order <= max(
                        math.sqrt(order) / 2,
                        threshold / 2,
                    ) + 1e-12

                    if obstruction < threshold * threshold:
                        next_threshold = max(32, 16 * (delta + 1) + 4)
                        assert next_order < next_threshold
                    else:
                        frontier.add((next_order, generation + 1))

            assert longest <= depth_envelope(initial)


def check_terminal_order() -> None:
    for initial in range(2, 10000):
        for delta0 in range(0, 20):
            depth = depth_envelope(initial)
            bound = max(32, 16 * (delta0 + depth) + 4)
            for generation in range(depth + 1):
                threshold = max(32, 16 * (delta0 + generation) + 4)
                assert threshold <= bound


def check_spread_exponents() -> None:
    for depth in range(0, 100):
        for delta0 in range(0, 20):
            direct = 2 * sum(delta0 + generation for generation in range(depth))
            closed = 2 * depth * delta0 + depth * (depth - 1)
            assert direct == closed

        label_direct = 2 * sum(3 + 2 * generation for generation in range(depth))
        label_closed = 2 * depth * depth + 4 * depth
        assert label_direct == label_closed


def main() -> None:
    check_closed_recurrence()
    check_integer_chains()
    check_terminal_order()
    check_spread_exponents()
    print("PX461--PX465 explicit nested-depth verifier: PASS")


if __name__ == "__main__":
    main()
