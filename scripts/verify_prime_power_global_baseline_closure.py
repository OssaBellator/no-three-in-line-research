#!/usr/bin/env python3
"""Exact arithmetic checks for CMR123--CMR128."""

from __future__ import annotations

import argparse
from itertools import permutations, product
from math import comb


def threshold(s: int) -> int:
    return 12 * (s - 1) ** 2 * (3 * s - 2)


def frozen_bank_threshold(s: int) -> int:
    return 2 * threshold(s)


def sigma(t: int) -> int | None:
    """Largest s>=4 with 24(s-1)^2(3s-2)<=t."""
    if t < frozen_bank_threshold(4):
        return None
    value = max(4, int((t / 72) ** (1 / 3)))
    while frozen_bank_threshold(value + 1) <= t:
        value += 1
    while frozen_bank_threshold(value) > t:
        value -= 1
    return value


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
        edge_count = threshold(s)
        point_degree = edge_count / (3 * (s - 1))
        pair_codegree = point_degree / (4 * (s - 1))
        assert pair_codegree >= 3 * s - 2

    assert frozen_bank_threshold(4) == 2160
    for s in range(4, max_s + 1):
        t = frozen_bank_threshold(s)
        assert t // 2 == threshold(s)
        assert t > 12 * s**3
        assert sigma(t) == s


def has_allowed_perfect_matching(
    t: int, forbidden: set[tuple[int, int]]
) -> bool:
    allowed = [
        [column for column in range(t) if (row, column) not in forbidden]
        for row in range(t)
    ]
    row_order = sorted(range(t), key=lambda row: len(allowed[row]))

    def search(index: int, used: set[int]) -> bool:
        if index == t:
            return True
        row = row_order[index]
        for column in allowed[row]:
            if column in used:
                continue
            used.add(column)
            if search(index + 1, used):
                return True
            used.remove(column)
        return False

    return search(0, set())


def verify_small_forbidden_boards() -> None:
    # The universal threshold is sharp: identity plus a transposition with one
    # fixed point blocks every matching at t=3.
    forbidden_three = {(i, i) for i in range(3)}
    transposition = (1, 0, 2)
    forbidden_three.update((i, transposition[i]) for i in range(3))
    assert not has_allowed_perfect_matching(3, forbidden_three)

    # Any degree-two bipartite forbidden graph is the union of two partial
    # matchings, which may be extended to two full matchings. Normalize the first
    # full matching to the identity and exhaust the second one for t=4,5.
    for t in (4, 5):
        identity = {(i, i) for i in range(t)}
        for second in permutations(range(t)):
            forbidden = identity | {(i, second[i]) for i in range(t)}
            assert has_allowed_perfect_matching(t, forbidden)


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

    # In general one layer has at least 2s-1 endpoint incidences, and one pair
    # supplies at most two incidences of that layer.
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
    step = max(1, max_t // 1000)
    for initial in range(2160, max_t + 1, step):
        value = initial
        steps = 0
        while value >= 2160:
            next_value = sigma(value)
            assert next_value is not None
            assert next_value < (value / 12) ** (1 / 3)
            assert next_value < value
            value = next_value
            steps += 1
            assert steps < 20
        assert value < 2160


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=500)
    parser.add_argument("--max-value", type=int, default=20)
    parser.add_argument("--max-t", type=int, default=10**12)
    args = parser.parse_args()

    verify_baseline_transfer(args.max_value)
    verify_thresholds(args.max_s)
    verify_small_forbidden_boards()
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
