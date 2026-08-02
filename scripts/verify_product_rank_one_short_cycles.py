#!/usr/bin/env python3
"""Verify PX228--PX231 rank-one and short-cycle bounds."""
from __future__ import annotations

from itertools import combinations, permutations
from math import comb, exp, floor


def integer_partitions(total: int, maximum: int, minimum: int = 1):
    if total == 0:
        yield ()
        return
    for first in range(min(maximum, total), minimum - 1, -1):
        for rest in integer_partitions(total - first, first, minimum):
            yield (first,) + rest


def verify_line_clique_star_extraction() -> None:
    for line_cap in range(2, 10):
        for total in range(1, 20):
            for parts in integer_partitions(total, line_cap):
                certificate_pairs = sum(comb(size, 2) for size in parts)
                star_rays = sum(floor(size / 2) for size in parts)
                assert star_rays * line_cap >= certificate_pairs
    print("line-clique secant-star extraction verified")


def verify_rank_one_weight_bound() -> None:
    for order in range(2, 20):
        for line_cap in range(2, 8):
            for threshold in range(1, 6):
                max_cell_weight = line_cap * threshold - 1
                total_weight = order * (order - 1) * max_cell_weight
                assert total_weight < line_cap * threshold * order * (order - 1)
    print("rank-one no-star weight bound verified")


def directed_rank_two_patterns(order: int):
    patterns = []
    for rows in combinations(range(order), 2):
        for columns in combinations(range(order), 2):
            for image in permutations(columns):
                partial = tuple(zip(rows, image))
                if any(row == column for row, column in partial):
                    continue
                support = {index for edge in partial for index in edge}
                patterns.append((partial, len(support)))
    return patterns


def directed_rank_three_cycles(order: int):
    cycles = []
    for labels in combinations(range(order), 3):
        first, second, third = labels
        cycles.append(((first, second), (second, third), (third, first)))
        cycles.append(((first, third), (third, second), (second, first)))
    return cycles


def verify_exact_pattern_populations() -> None:
    for order in range(3, 11):
        profile = {2: 0, 3: 0, 4: 0}
        for _, support_size in directed_rank_two_patterns(order):
            profile[support_size] += 1
        assert profile[2] == comb(order, 2)
        assert profile[3] == order * (order - 1) * (order - 2)
        assert profile[4] == 12 * comb(order, 4)
        assert len(directed_rank_three_cycles(order)) == 2 * comb(order, 3)
    print("exact short-cycle and path populations verified")


def verify_expected_load_identities() -> None:
    for order in range(4, 30):
        rank_two_denominator = order * (order - 1)
        rank_three_denominator = rank_two_denominator * (order - 2)

        transposition_ratio = comb(order, 2) / rank_two_denominator
        path_ratio = (
            order * (order - 1) * (order - 2) / rank_two_denominator
        )
        cycle_ratio = 2 * comb(order, 3) / rank_three_denominator

        assert abs(transposition_ratio - 0.5) < 1e-12
        assert abs(path_ratio - (order - 2)) < 1e-12
        assert abs(cycle_ratio - 1 / 3) < 1e-12
    print("expected-load coefficient identities verified")


def verify_conditioned_form() -> None:
    # The formulas depend only on the residual order, so repeat them after
    # arbitrary bounded exposure sizes.
    for original in range(10, 25):
        for exposed in range(0, 5):
            residual = original - exposed
            if residual < 4:
                continue
            assert comb(residual, 2) * 2 == residual * (residual - 1)
            assert 2 * comb(residual, 3) * 3 == (
                residual * (residual - 1) * (residual - 2)
            )
    print("conditioned residual-order identities verified")


def main() -> None:
    verify_line_clique_star_extraction()
    verify_rank_one_weight_bound()
    verify_exact_pattern_populations()
    verify_expected_load_identities()
    verify_conditioned_form()
    print("PX228--PX231 verified")


if __name__ == "__main__":
    main()
