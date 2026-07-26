#!/usr/bin/env python3
"""Finite checks for SAS5u--SAS5y."""

from __future__ import annotations

from collections import Counter
from math import ceil, floor, gcd


def disjoint_adjacent_pairs(occupied: set[int]) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    used: set[int] = set()
    for value in sorted(occupied):
        if value in used or value + 1 not in occupied or value + 1 in used:
            continue
        pairs.append((value, value + 1))
        used.add(value)
        used.add(value + 1)
    return pairs


def weight_profiles(length: int, occupied: set[int]) -> tuple[tuple[int, ...], ...]:
    profiles: list[tuple[int, ...]] = []
    for mode in range(4):
        weights = []
        for value in range(length):
            if value not in occupied:
                weights.append(0)
            elif mode == 0:
                weights.append(1)
            elif mode == 1:
                weights.append(1 + value % 2)
            elif mode == 2:
                weights.append(3 if value == min(occupied) else 1)
            else:
                weights.append(1 + (value % 3))
        profiles.append(tuple(weights))
    return tuple(profiles)


def verify_interval_combinatorics(counts: Counter[str]) -> None:
    for length in range(1, 13):
        interval = set(range(length))
        for mask in range(1 << length):
            occupied = {value for value in interval if mask >> value & 1}
            k = len(occupied)
            adjacent = sum(value + 1 in occupied for value in occupied)
            lower = max(0, 2 * k - length - 1)
            assert adjacent >= lower
            selected = disjoint_adjacent_pairs(occupied)
            assert len(selected) >= ceil(lower / 2)
            assert len({endpoint for pair in selected for endpoint in pair}) == 2 * len(selected)
            counts["occupied subsets"] += 1

            if not occupied:
                continue
            for weights in weight_profiles(length, occupied):
                total = sum(weights)
                for threshold in (1, 2, 3):
                    positive = [weights[value] for value in occupied if weights[value] > 0]
                    if any(weight > threshold for weight in positive):
                        counts["heavy parameters"] += 1
                    else:
                        assert len(positive) >= ceil(total / threshold)
                        counts["diffuse parameters"] += 1


def valid_double_parameters(
    size: int,
    base_row: int,
    base_col: int,
    row_step: int,
    col_step: int,
) -> list[int]:
    values = []
    for parameter in range(-size, size + 1):
        row = base_row + parameter * row_step
        col = base_col + parameter * col_step
        if 0 <= row < size and 0 <= col < size:
            values.append(parameter)
    return values


def valid_single_parameters(
    size: int,
    fixed_col: int,
    first_step: int,
    second_step: int,
) -> list[int]:
    values = []
    for parameter in range(-size, size + 1):
        first = fixed_col + parameter * first_step
        second = fixed_col + parameter * second_step
        if 0 <= first < size and 0 <= second < size:
            values.append(parameter)
    return values


def verify_board_bounds(counts: Counter[str]) -> None:
    for size in range(2, 16):
        for u in range(-(size - 1), size):
            for v in range(-(size - 1), size):
                if u == 0 or v == 0 or gcd(abs(u), abs(v)) != 1:
                    continue
                height = max(abs(u), abs(v))
                bound = 1 + floor((size - 1) / height)
                for base_row in range(size):
                    for base_col in range(size):
                        values = valid_double_parameters(size, base_row, base_col, u, v)
                        if values:
                            assert values == list(range(values[0], values[-1] + 1))
                        assert len(values) <= bound
                        if len(values) >= 2:
                            assert size >= height * (len(values) - 1) + 1
                        for parameter in values[:-1]:
                            first = (base_row + parameter * u, base_col + parameter * v)
                            second = (base_row + (parameter + 1) * u, base_col + (parameter + 1) * v)
                            assert (second[0] - first[0], second[1] - first[1]) == (u, v)
                        counts["double families"] += 1

                if u == v:
                    continue
                for fixed_col in range(size):
                    values = valid_single_parameters(size, fixed_col, u, v)
                    if values:
                        assert values == list(range(values[0], values[-1] + 1))
                    assert len(values) <= bound
                    if len(values) >= 2:
                        assert size >= height * (len(values) - 1) + 1
                    for parameter in values[:-1]:
                        first = (fixed_col + parameter * u, fixed_col + parameter * v)
                        second = (fixed_col + (parameter + 1) * u, fixed_col + (parameter + 1) * v)
                        assert (second[0] - first[0], second[1] - first[1]) == (u, v)
                    counts["singleton families"] += 1


def verify_shape_stocks(counts: Counter[str]) -> None:
    for bound in range(1, 20):
        double = [
            (u, v)
            for u in range(1, bound + 1)
            for v in range(-bound, bound + 1)
            if v != 0 and gcd(u, abs(v)) == 1
        ]
        singleton = [
            (u, v)
            for u in range(-bound, bound + 1)
            for v in range(-bound, bound + 1)
            if u != 0 and v != 0 and u != v and gcd(abs(u), abs(v)) == 1
        ]
        assert len(double) <= 2 * bound * bound
        assert len(singleton) <= 4 * bound * bound
        counts["shape bounds"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_interval_combinatorics(counts)
    verify_board_bounds(counts)
    verify_shape_stocks(counts)
    print("SAS5u--SAS5y parameter-chain audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
