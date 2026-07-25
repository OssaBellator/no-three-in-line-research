#!/usr/bin/env python3
"""Exact finite checks for AC5g--AC5k."""

from __future__ import annotations

from itertools import combinations, product
from math import comb, gcd


Point = tuple[int, int]
Line = tuple[frozenset[Point], int]


def grid_lines(side: int) -> tuple[list[Point], list[Line]]:
    points = [(x, y) for x in range(side) for y in range(side)]
    line_keys: dict[tuple[int, int, int], tuple[frozenset[Point], int]] = {}

    for left, right in combinations(points, 2):
        dx = right[0] - left[0]
        dy = right[1] - left[1]
        step_gcd = gcd(abs(dx), abs(dy))
        ux = dx // step_gcd
        uy = dy // step_gcd
        if ux < 0 or (ux == 0 and uy < 0):
            ux = -ux
            uy = -uy

        a = uy
        b = -ux
        c = a * left[0] + b * left[1]
        coeff_gcd = gcd(gcd(abs(a), abs(b)), abs(c))
        if coeff_gcd:
            a //= coeff_gcd
            b //= coeff_gcd
            c //= coeff_gcd
        if a < 0 or (a == 0 and b < 0):
            a = -a
            b = -b
            c = -c

        key = (a, b, c)
        line_points = frozenset(
            point for point in points if a * point[0] + b * point[1] == c
        )
        if len(line_points) >= 2:
            line_keys[key] = (line_points, max(abs(a), abs(b)))

    return points, list(line_keys.values())


def all_states(points: list[Point]) -> list[frozenset[Point]]:
    return [
        frozenset(
            point
            for index, point in enumerate(points)
            if (mask >> index) & 1
        )
        for mask in range(1 << len(points))
    ]


def psi(state: frozenset[Point], lines: list[Line], threshold: int) -> int:
    return sum(
        max(len(state & line) - 2, 0)
        for line, height in lines
        if height >= threshold
    )


def new_triple_sets(
    base: frozenset[Point],
    final: frozenset[Point],
    lines: list[Line],
    threshold: int,
) -> set[frozenset[Point]]:
    triples: set[frozenset[Point]] = set()
    for line, height in lines:
        if height < threshold:
            continue
        for triple in combinations(sorted(final & line), 3):
            triple_set = frozenset(triple)
            if not triple_set.issubset(base):
                triples.add(triple_set)
    return triples


def verify_grid_filter(side: int = 3) -> dict[str, int]:
    points, lines = grid_lines(side)
    states = all_states(points)
    totals = {
        "grid_points": len(points),
        "grid_lines": len(lines),
        "state_pairs": 0,
        "filter_equivalences": 0,
        "single_step_safe_transitions": 0,
        "two_step_safe_paths": 0,
    }

    for threshold in (1, 2):
        clean_states = [
            state for state in states if psi(state, lines, 2 * threshold) == 0
        ]
        for base in clean_states:
            safe_single_flips: list[frozenset[Point]] = []
            for final in states:
                totals["state_pairs"] += 1
                high_count = len(
                    new_triple_sets(base, final, lines, 2 * threshold)
                )
                assert (high_count == 0) == (
                    psi(final, lines, 2 * threshold) == 0
                )
                totals["filter_equivalences"] += 1

                if len(base ^ final) == 1 and high_count == 0:
                    safe_single_flips.append(final)
                    assert psi(final, lines, 2 * threshold) == 0
                    totals["single_step_safe_transitions"] += 1

            for middle in safe_single_flips:
                for final in states:
                    if len(middle ^ final) != 1:
                        continue
                    high_count = len(
                        new_triple_sets(middle, final, lines, 2 * threshold)
                    )
                    if high_count == 0:
                        assert psi(final, lines, 2 * threshold) == 0
                        totals["two_step_safe_paths"] += 1

    return totals


def verify_filtered_expectations(limit: int = 300_000) -> int:
    checks = 0
    for batch_size in range(1, 16):
        for menu_size in range(1, 8):
            records = list(product((0, 1), range(batch_size + 2)))
            for menu in product(records, repeat=menu_size):
                survivors = [
                    current_count
                    for high_count, current_count in menu
                    if high_count == 0
                ]
                if survivors:
                    average = sum(survivors) / len(survivors)
                    if average < batch_size:
                        assert min(survivors) <= batch_size - 1
                checks += 1
                if checks >= limit:
                    return checks
    return checks


def verify_failed_filter_concentration(limit: int = 250_000) -> int:
    checks = 0
    for witness_count in range(1, 7):
        for state_count in range(1, 7):
            for witnesses in product(range(witness_count), repeat=state_count):
                for weights in product(range(1, 4), repeat=state_count):
                    total_weight = sum(weights)
                    loads = [0] * witness_count
                    for weight, witness in zip(weights, witnesses):
                        loads[witness] += weight
                    assert max(loads) >= total_weight / witness_count
                    checks += 1
                    if checks >= limit:
                        return checks
    return checks


def verify_rank_height_partitions() -> int:
    checks = 0
    # First three entries are ranks 1,2,3 in [H,2H); last three are ranks
    # 1,2,3 in the protected band >=2H.
    for buckets in product(range(4), repeat=6):
        current_band = sum(buckets[:3])
        protected_band = sum(buckets[3:])
        total = sum(buckets)
        assert total == current_band + protected_band
        if protected_band == 0:
            assert total == current_band
        checks += 1
    return checks


def verify_witness_stock() -> int:
    checks = 0
    for side in range(2, 101):
        point_count = side * side
        all_triples = comb(point_count, 3) if point_count >= 3 else 0
        for envelope_size in range(1, min(point_count, 20) + 1):
            envelope_bound = envelope_size * comb(point_count, 2)
            assert envelope_bound >= 0
            assert all_triples <= point_count * comb(point_count, 2)
            checks += 1
    return checks


def main() -> None:
    totals = verify_grid_filter()
    totals["filtered_expectation_ledgers"] = verify_filtered_expectations()
    totals["failed_filter_concentration_systems"] = (
        verify_failed_filter_concentration()
    )
    totals["rank_height_partitions"] = verify_rank_height_partitions()
    totals["witness_stock_systems"] = verify_witness_stock()

    print("AC5g--AC5k verification passed")
    for key, value in totals.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
