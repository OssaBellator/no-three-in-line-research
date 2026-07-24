#!/usr/bin/env python3
"""Exact arithmetic checks for CMR123--CMR127."""

from __future__ import annotations

import argparse
from itertools import product
from math import comb, log


def threshold(s: int) -> int:
    return 12 * (s - 1) ** 2 * (3 * s - 2)


def verify_baseline_transfer(max_value: int) -> None:
    for phi0 in range(max_value + 1):
        for excess in range(max_value + 1):
            phi_star = phi0 + excess
            for destroyed in range(max_value + 1):
                phi_x = phi_star - destroyed
                if phi_x < 0:
                    continue
                for child_gap in range(max_value + 1):
                    phi_child = phi0 + child_gap
                    touching = phi_child - phi_x
                    assert touching == child_gap - excess + destroyed
                    assert touching >= destroyed - excess


def verify_thresholds(max_s: int) -> None:
    for s in range(2, max_s + 1):
        # The simple cubic hypothesis used in CMR125 dominates CMR124's exact one.
        assert 36 * s**3 > threshold(s)

        edge_count = threshold(s)
        point_degree = edge_count / (3 * (s - 1))
        pair_codegree = point_degree / (4 * (s - 1))
        assert pair_codegree >= 3 * s - 2

    for s in range(7, max_s + 1):
        t = 72 * s**3
        assert t // 2 >= 36 * s**3
        assert t // 2 > threshold(s)


def verify_layer_pigeonhole(max_s: int) -> None:
    # Exhaust the endpoint-layer assignments for the first few matching sizes.
    # Each matched pair has endpoint layers 00, 01, 10, or 11.
    for s in range(1, min(max_s, 4) + 1):
        pair_count = 2 * s - 1
        for assignment in product(range(4), repeat=pair_count):
            represented = [0, 0]
            for code in assignment:
                left = code // 2
                right = code % 2
                for layer in (0, 1):
                    if left == layer or right == layer:
                        represented[layer] += 1
            assert max(represented) >= s

    # The general numerical pigeonhole: one layer has at least 2s-1 incidences,
    # and one pair supplies at most two incidences of that layer.
    for s in range(1, max_s + 1):
        incidences = 2 * (2 * s - 1)
        majority_incidences = (incidences + 1) // 2
        represented_pairs = (majority_incidences + 1) // 2
        assert represented_pairs >= s


def verify_line_core(max_s: int) -> None:
    for s in range(1, max_s + 1):
        line_size = 3 * s
        for moved_count in range(line_size + 1):
            fixed_count = line_size - moved_count
            if moved_count >= s:
                # Choose s moved points; at least 2s other points remain.
                assert line_size - s >= 2 * s
            else:
                assert fixed_count > 2 * s


def verify_heavy_line_budget(max_s: int) -> None:
    for s in range(1, max_s + 1):
        minimum = comb(2 * s + 1, 3)
        occupancies = [2 * s + 1, 2 * s + 2, 3 * s + 1]
        phi = sum(comb(value, 3) for value in occupancies)
        assert len(occupancies) * minimum <= phi
        assert len(occupancies) <= phi // minimum


def verify_descent(max_t: int) -> None:
    for initial in range(24696, max_t + 1, max(1, max_t // 1000)):
        value = initial
        steps = 0
        while value >= 24696:
            next_value = int((value / 72) ** (1 / 3))
            # Correct any floating-point rounding at exact cubes.
            while 72 * (next_value + 1) ** 3 <= value:
                next_value += 1
            while 72 * next_value**3 > value:
                next_value -= 1
            assert next_value < value ** (1 / 3) + 1e-12
            assert next_value < value
            value = next_value
            steps += 1
            assert steps < 20

        if initial > 24696:
            explicit = max(0, int(log(log(initial) / log(24696), 3)) + 2)
            assert steps <= explicit + 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=500)
    parser.add_argument("--max-value", type=int, default=20)
    parser.add_argument("--max-t", type=int, default=10**12)
    args = parser.parse_args()

    verify_baseline_transfer(args.max_value)
    verify_thresholds(args.max_s)
    verify_layer_pigeonhole(args.max_s)
    verify_line_core(args.max_s)
    verify_heavy_line_budget(args.max_s)
    verify_descent(args.max_t)

    print(
        "verified global-baseline closure arithmetic: "
        f"max-s={args.max_s}, max-value={args.max_value}, max-t={args.max_t}"
    )


if __name__ == "__main__":
    main()
