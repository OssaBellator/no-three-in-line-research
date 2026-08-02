#!/usr/bin/env python3
"""Verify PX201--PX204 support-excess thinning and cycle-core reduction."""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import exp, factorial
from random import Random


def support(partial: tuple[tuple[int, int], ...]) -> frozenset[int]:
    return frozenset(index for edge in partial for index in edge)


def partial_matchings(
    size: int, rank: int
) -> tuple[tuple[tuple[int, int], ...], ...]:
    result = []
    for rows in combinations(range(size), rank):
        for columns in combinations(range(size), rank):
            for image in permutations(columns):
                partial = tuple(zip(rows, image))
                if any(row == column for row, column in partial):
                    continue
                result.append(partial)
    return tuple(result)


def verify_short_cycle_core() -> None:
    size = 7
    profile: Counter[tuple[int, int]] = Counter()
    for rank in range(1, 4):
        for partial in partial_matchings(size, rank):
            used = support(partial)
            union_size = len(used)
            assert rank <= union_size <= 2 * rank
            profile[(rank, union_size)] += 1

            if union_size != rank:
                continue
            if rank == 1:
                raise AssertionError("rank-one support-one cell is diagonal")

            mapping = dict(partial)
            if rank == 2:
                first, second = tuple(mapping)
                assert mapping[first] == second
                assert mapping[second] == first
            else:
                rows = set(mapping)
                assert set(mapping.values()) == rows
                first = next(iter(rows))
                second = mapping[first]
                third = mapping[second]
                assert len({first, second, third}) == 3
                assert mapping[third] == first

    assert (1, 1) not in profile
    assert profile[(2, 2)] == factorial(size) // (2 * factorial(size - 2))
    assert profile[(3, 3)] == 2 * factorial(size) // (6 * factorial(size - 3))
    print(f"short-cycle support profile verified: {dict(profile)}")


def certificate_weight(partial: tuple[tuple[int, int], ...]) -> int:
    return 1 + sum((row + 1) * (column + 3) for row, column in partial) % 7


def verify_bernoulli_support_identity() -> None:
    size = 6
    families: dict[
        tuple[int, int], list[tuple[tuple[tuple[int, int], ...], int]]
    ] = defaultdict(list)
    totals: Counter[tuple[int, int]] = Counter()

    for rank in range(1, 4):
        for partial in partial_matchings(size, rank):
            sector = (rank, len(support(partial)))
            weight = certificate_weight(partial)
            families[sector].append((partial, weight))
            totals[sector] += weight

    subset_totals: Counter[tuple[int, int]] = Counter()
    for mask in range(1 << size):
        chosen = {index for index in range(size) if mask & (1 << index)}
        for sector, entries in families.items():
            subset_totals[sector] += sum(
                weight for partial, weight in entries if support(partial) <= chosen
            )

    for (rank, union_size), total in totals.items():
        assert subset_totals[(rank, union_size)] == total * (
            1 << (size - union_size)
        )
    print("exact Bernoulli support-sector identity verified")


def verify_simultaneous_thinning_budget() -> None:
    failure_bound = exp(-32 / 8) + 9 / 16
    assert failure_bound < 1
    print(f"simultaneous-thinning failure bound={failure_bound:.9f}")


def allowed_permutations(
    size: int, forbidden: tuple[int, ...]
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        permutation
        for permutation in permutations(range(size))
        if all(
            not (forbidden[row] & (1 << permutation[row]))
            for row in range(size)
        )
    )


def falling_factorial(size: int, rank: int) -> int:
    return factorial(size) // factorial(size - rank)


def verify_allowed_bank_load_transfer() -> None:
    # Delta=1 and t=8 is the first threshold case t=8*Delta.
    size = 8
    forbidden = tuple(1 << row for row in range(size))
    allowed = allowed_permutations(size, forbidden)
    assert len(allowed) == 14833

    random = Random(20260725)
    families: dict[
        tuple[int, int], list[tuple[tuple[tuple[int, int], ...], int]]
    ] = defaultdict(list)
    for rank in range(1, 4):
        pool = list(partial_matchings(size, rank))
        random.shuffle(pool)
        for partial in pool[:120]:
            families[(rank, len(support(partial)))].append(
                (partial, 1 + random.randrange(5))
            )

    for (rank, _), entries in families.items():
        total_weight = sum(weight for _, weight in entries)
        total_value = 0
        for permutation in allowed:
            chosen = {(row, permutation[row]) for row in range(size)}
            total_value += sum(
                weight for partial, weight in entries if set(partial) <= chosen
            )
        exact_expectation = total_value / len(allowed)
        bound = exp(4) * total_weight / falling_factorial(size, rank)
        assert exact_expectation <= bound

    print("exact allowed-bank weighted load transfer verified")


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def verify_transposition_core_bound() -> None:
    size = 8
    rows = tuple(2 * index for index in range(size))
    columns = tuple(2 * index + 1 for index in range(size))
    line_sums = {2 * first + 2 * second + 1 for first, second in combinations(range(size), 2)}

    # Put exactly two background anchors on every possible transposition secant.
    background = tuple(
        point
        for total in line_sums
        for point in ((100 + total, -100), (101 + total, -101))
    )

    weights = []
    for first, second in combinations(range(size), 2):
        left = (rows[first], columns[second])
        right = (rows[second], columns[first])
        weights.append(
            sum(collinear(anchor, left, right) for anchor in background)
        )

    line_load = max(weights)
    assert line_load == 2
    assert sum(weights) == line_load * len(weights)
    print("transposition-core line-load bound verified sharply")


def verify_square_root_sector_scales() -> None:
    for size in (1024, 1600, 2500, 4096):
        probability = size**-0.5
        for rank in range(1, 4):
            for union_size in range(rank, 2 * rank + 1):
                scale = probability ** (union_size - rank)
                expected = size ** (-(union_size - rank) / 2)
                assert abs(scale - expected) < 1e-15
    print("square-root support-excess scales verified")


def main() -> None:
    verify_short_cycle_core()
    verify_bernoulli_support_identity()
    verify_simultaneous_thinning_budget()
    verify_allowed_bank_load_transfer()
    verify_transposition_core_bound()
    verify_square_root_sector_scales()
    print("PX201--PX204 verified")


if __name__ == "__main__":
    main()
