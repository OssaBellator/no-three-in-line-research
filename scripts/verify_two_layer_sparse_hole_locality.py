#!/usr/bin/env python3
"""Verify SRR3g two-layer locality for arbitrary sparse holes."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial

Edge = tuple[int, int]
Cylinder = tuple[tuple[Edge, ...], tuple[Edge, ...]]
State = tuple[tuple[int, ...], tuple[int, ...]]


def derangement(number: int) -> int:
    return sum(
        (-1) ** count * comb(number, count) * factorial(number - count)
        for count in range(number + 1)
    )


def avoidance_count(number: int, forbidden: int) -> int:
    return sum(
        (-1) ** count
        * comb(forbidden, count)
        * factorial(number - count)
        for count in range(forbidden + 1)
    )


def lower(n: int, first_rank: int, second_rank: int) -> Fraction:
    return Fraction(
        avoidance_count(n - first_rank, second_rank)
        * derangement(n - second_rank),
        factorial(n) * derangement(n),
    )


def upper(n: int, first_rank: int, second_rank: int) -> Fraction:
    assert n >= 2 * second_rank
    return Fraction(
        factorial(n - first_rank)
        * avoidance_count(n - second_rank, n - 2 * second_rank),
        factorial(n) * derangement(n),
    )


def crude_upper(n: int, first_rank: int, second_rank: int) -> Fraction:
    return Fraction(
        factorial(n - first_rank) * factorial(n - second_rank),
        factorial(n) * derangement(n),
    )


def epsilon(
    n: int,
    missing_size: int,
    first_rank: int,
    second_rank: int,
) -> Fraction:
    return missing_size * (
        crude_upper(n, first_rank + 1, second_rank)
        + crude_upper(n, first_rank, second_rank + 1)
    ) / lower(n, first_rank, second_rank)


def verify_linear_hole_ceiling(maximum_n: int = 36) -> None:
    for n in range(2, maximum_n + 1):
        for first_rank in range(n + 1):
            for second_rank in range(n + 1):
                if n < max(
                    2,
                    2 * second_rank,
                    second_rank + 2,
                    first_rank + second_rank + 1,
                ):
                    continue
                denominator = n - first_rank - second_rank
                base = lower(n, first_rank, second_rank)
                first_ratio = (
                    crude_upper(n, first_rank + 1, second_rank) / base
                )
                second_ratio = (
                    crude_upper(n, first_rank, second_rank + 1) / base
                )
                assert first_ratio <= Fraction(3, denominator)
                assert second_ratio <= Fraction(6, denominator)
                for missing_size in range(n + 1):
                    assert epsilon(
                        n,
                        missing_size,
                        first_rank,
                        second_rank,
                    ) <= Fraction(
                        9 * missing_size,
                        denominator,
                    )


def globally_compatible(cylinder: Cylinder) -> bool:
    edges = cylinder[0] + cylinder[1]
    return (
        len({row for row, _ in edges}) == len(edges)
        and len({column for _, column in edges}) == len(edges)
    )


def contains(state: State, cylinder: Cylinder) -> bool:
    return all(
        state[layer][row] == column
        for layer in range(2)
        for row, column in cylinder[layer]
    )


def avoids(state: State, missing: set[Edge]) -> bool:
    return all(
        (row, state[layer][row]) not in missing
        for layer in range(2)
        for row in range(len(state[layer]))
    )


def union(left: Cylinder, right: Cylinder) -> Cylinder:
    return (
        tuple(sorted(left[0] + right[0])),
        tuple(sorted(left[1] + right[1])),
    )


def host_valid(cylinder: Cylinder, missing: set[Edge]) -> bool:
    return all(edge not in missing for layer in cylinder for edge in layer)


def verify(n: int = 4) -> None:
    all_edges = tuple((row, column) for row in range(n) for column in range(n))
    all_permutations = tuple(permutations(range(n)))
    complete_states = tuple(
        (first, second)
        for first in all_permutations
        for second in all_permutations
        if all(first[row] != second[row] for row in range(n))
    )
    assert len(complete_states) == factorial(n) * derangement(n)

    empty: Cylinder = ((), ())
    single_events: list[Cylinder] = []
    for edge in all_edges:
        single_events.append(((edge,), ()))
        single_events.append(((), (edge,)))
    cylinders = [empty] + single_events
    cylinders.extend(
        union(left, right)
        for left, right in combinations(single_events, 2)
        if globally_compatible(union(left, right))
    )

    counts = {
        cylinder: sum(contains(state, cylinder) for state in complete_states)
        for cylinder in cylinders
    }
    for cylinder, count in counts.items():
        first_rank = len(cylinder[0])
        second_rank = len(cylinder[1])
        probability = Fraction(count, len(complete_states))
        assert lower(n, first_rank, second_rank) <= probability
        assert probability <= crude_upper(n, first_rank, second_rank)
        if n >= 2 * second_rank:
            assert probability <= upper(n, first_rank, second_rank)

    for missing_size in range(3):
        for missing_tuple in combinations(all_edges, missing_size):
            missing = set(missing_tuple)
            host_states = tuple(
                state for state in complete_states if avoids(state, missing)
            )
            assert host_states
            for cylinder in cylinders:
                if not host_valid(cylinder, missing):
                    continue
                complete_count = counts[cylinder]
                host_count = sum(
                    contains(state, cylinder) for state in host_states
                )
                conditional_avoidance = Fraction(
                    host_count,
                    complete_count,
                )
                first_rank = len(cylinder[0])
                second_rank = len(cylinder[1])
                assert conditional_avoidance >= (
                    1
                    - epsilon(
                        n,
                        missing_size,
                        first_rank,
                        second_rank,
                    )
                )

            if missing_size > 1:
                continue
            for flaw in single_events:
                if not host_valid(flaw, missing):
                    continue
                for remote in single_events:
                    combined = union(flaw, remote)
                    if not globally_compatible(combined):
                        continue
                    if not host_valid(remote, missing):
                        continue
                    flaw_count = sum(
                        contains(state, flaw) for state in host_states
                    )
                    remote_count = sum(
                        contains(state, remote) for state in host_states
                    )
                    combined_count = sum(
                        contains(state, combined) for state in host_states
                    )
                    if not flaw_count or not remote_count:
                        continue
                    ratio = Fraction(
                        combined_count * len(host_states),
                        flaw_count * remote_count,
                    )
                    flaw_ranks = (len(flaw[0]), len(flaw[1]))
                    remote_ranks = (len(remote[0]), len(remote[1]))
                    flaw_epsilon = epsilon(
                        n,
                        missing_size,
                        *flaw_ranks,
                    )
                    remote_epsilon = epsilon(
                        n,
                        missing_size,
                        *remote_ranks,
                    )
                    if flaw_epsilon >= 1 or remote_epsilon >= 1:
                        continue
                    bound = (
                        upper(
                            n,
                            flaw_ranks[0] + remote_ranks[0],
                            flaw_ranks[1] + remote_ranks[1],
                        )
                        / lower(n, *flaw_ranks)
                        / lower(n, *remote_ranks)
                        / (1 - flaw_epsilon)
                        / (1 - remote_epsilon)
                    )
                    assert ratio <= bound


def main() -> None:
    verify()
    verify_linear_hole_ceiling()
    print("two-layer sparse/linear-hole locality: regressions passed")


if __name__ == "__main__":
    main()
