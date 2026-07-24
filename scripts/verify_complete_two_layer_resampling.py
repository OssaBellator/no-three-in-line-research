#!/usr/bin/env python3
"""Verify stationary resampling on two disjoint complete matchings."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from math import comb, factorial, prod

State = tuple[tuple[int, ...], tuple[int, ...]]


def states(n: int) -> list[State]:
    result: list[State] = []
    for first in permutations(range(n)):
        for second in permutations(range(n)):
            if all(first[row] != second[row] for row in range(n)):
                result.append((first, second))
    return result


def swap_images(permutation: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    output = list(permutation)
    output[left], output[right] = output[right], output[left]
    return tuple(output)


def forward_targets(state: State) -> list[State]:
    first, second = state
    assert first[0] == 0
    bad_one = first.index(second[0])
    bad_two = second.index(0)
    allowed = [
        row
        for row in range(1, len(first))
        if row not in {bad_one, bad_two}
    ]
    if bad_one == bad_two:
        allowed.remove(min(allowed))
    return [(swap_images(first, 0, row), second) for row in allowed]


def falling(value: int, rank: int) -> int:
    return prod(value - offset for offset in range(rank))


def contains(
    permutation: tuple[int, ...], partial: tuple[tuple[int, int], ...]
) -> bool:
    return all(permutation[row] == column for row, column in partial)


def partial_derangements(size: int, forbidden: int) -> int:
    return sum(
        (-1) ** rank
        * comb(forbidden, rank)
        * factorial(size - rank)
        for rank in range(forbidden + 1)
    )


def verify_remote(omega: list[State], n: int) -> None:
    scale = n - 3
    for rank_flaw in range(1, min(3, n - 1) + 1):
        flaw = tuple((row, row) for row in range(rank_flaw))
        sources = [
            state for state in omega if contains(state[0], flaw)
        ]
        assert sources
        for rank_remote in range(1, n - rank_flaw + 1):
            remote = tuple(
                (row, row)
                for row in range(
                    rank_flaw, rank_flaw + rank_remote
                )
            )
            source_with_remote = sum(
                contains(state[0], remote) for state in sources
            )
            transition_with_remote = 0
            for source in sources:
                before = contains(source[0], remote)
                for target in forward_targets(source):
                    after = contains(target[0], remote)
                    assert not after or before
                    transition_with_remote += after

            observed = Fraction(
                transition_with_remote, len(sources) * scale
            )
            conditioned = Fraction(
                source_with_remote, len(sources)
            )
            exact_conditioned = Fraction(
                1, falling(n - rank_flaw, rank_remote)
            )
            stationary = Fraction(1, falling(n, rank_remote))
            inflation = Fraction(
                falling(n, rank_remote),
                falling(n - rank_flaw, rank_remote),
            )
            assert conditioned == exact_conditioned
            assert observed <= conditioned
            assert observed / stationary <= inflation


def verify_untouched_remote(omega: list[State], n: int) -> None:
    derangements = partial_derangements(n, n)
    for rank_flaw in range(1, min(3, n - 1) + 1):
        flaw = tuple((row, row) for row in range(rank_flaw))
        sources = [
            state for state in omega if contains(state[0], flaw)
        ]
        assert sources
        maximum_remote_rank = min(n // 2, n - rank_flaw)
        for rank_remote in range(1, maximum_remote_rank + 1):
            remote = tuple(
                (row, row)
                for row in range(
                    rank_flaw, rank_flaw + rank_remote
                )
            )
            observed = Fraction(
                sum(contains(state[1], remote) for state in sources),
                len(sources),
            )
            size = n - rank_remote
            upper = Fraction(
                partial_derangements(size, n - 2 * rank_remote),
                derangements,
            )
            stationary = Fraction(1, falling(n, rank_remote))
            inflation = Fraction(
                partial_derangements(size, n - 2 * rank_remote),
                factorial(size),
            ) / Fraction(derangements, factorial(n))
            assert observed <= upper
            assert observed / stationary <= inflation


def verify_mixed_remote(omega: list[State], n: int) -> None:
    derangements = partial_derangements(n, n)
    for rank_flaw in range(1, min(2, n - 2) + 1):
        flaw = tuple((row, row) for row in range(rank_flaw))
        sources = [
            state for state in omega if contains(state[0], flaw)
        ]
        for rank_first in range(1, n - rank_flaw):
            maximum_second = min(
                n // 2, n - rank_flaw - rank_first
            )
            for rank_second in range(1, maximum_second + 1):
                first_remote = tuple(
                    (row, row)
                    for row in range(
                        rank_flaw, rank_flaw + rank_first
                    )
                )
                second_remote = tuple(
                    (row, row)
                    for row in range(
                        rank_flaw + rank_first,
                        rank_flaw + rank_first + rank_second,
                    )
                )

                def event(state: State) -> bool:
                    return contains(
                        state[0], first_remote
                    ) and contains(state[1], second_remote)

                transition_count = 0
                for source in sources:
                    before = event(source)
                    for target in forward_targets(source):
                        after = event(target)
                        assert not after or before
                        transition_count += after

                observed = Fraction(
                    transition_count, len(sources) * (n - 3)
                )
                conditional_upper = Fraction(
                    1, falling(n - rank_flaw, rank_first)
                ) * Fraction(
                    partial_derangements(
                        n - rank_second, n - 2 * rank_second
                    ),
                    derangements,
                )
                stationary = Fraction(
                    sum(event(state) for state in omega), len(omega)
                )
                stationary_lower = Fraction(
                    partial_derangements(
                        n - rank_first, rank_second
                    )
                    * partial_derangements(
                        n - rank_second, n - rank_second
                    ),
                    factorial(n) * derangements,
                )
                ratio_bound = conditional_upper / stationary_lower
                assert observed <= conditional_upper
                assert stationary >= stationary_lower
                assert observed / stationary <= ratio_bound


def cylinder(
    state: State,
    first: tuple[tuple[int, int], ...],
    second: tuple[tuple[int, int], ...],
) -> bool:
    return contains(state[0], first) and contains(state[1], second)


def cylinder_upper(
    n: int, first_rank: int, second_rank: int
) -> Fraction:
    derangements = partial_derangements(n, n)
    return Fraction(
        factorial(n - first_rank)
        * partial_derangements(
            n - second_rank, n - 2 * second_rank
        ),
        factorial(n) * derangements,
    )


def cylinder_lower(
    n: int, first_rank: int, second_rank: int
) -> Fraction:
    derangements = partial_derangements(n, n)
    return Fraction(
        partial_derangements(n - first_rank, second_rank)
        * partial_derangements(
            n - second_rank, n - second_rank
        ),
        factorial(n) * derangements,
    )


def verify_general_locality(omega: list[State], n: int) -> None:
    for flaw_second_rank in range(2):
        flaw_first_rank = 1
        for remote_first_rank in range(3):
            for remote_second_rank in range(3):
                if remote_first_rank + remote_second_rank == 0:
                    continue
                total_rank = (
                    flaw_first_rank
                    + flaw_second_rank
                    + remote_first_rank
                    + remote_second_rank
                )
                if total_rank > n:
                    continue
                if 2 * (
                    flaw_second_rank + remote_second_rank
                ) > n:
                    continue

                cursor = 0
                flaw_first = ((cursor, cursor),)
                cursor += flaw_first_rank
                flaw_second = tuple(
                    (row, row)
                    for row in range(cursor, cursor + flaw_second_rank)
                )
                cursor += flaw_second_rank
                remote_first = tuple(
                    (row, row)
                    for row in range(cursor, cursor + remote_first_rank)
                )
                cursor += remote_first_rank
                remote_second = tuple(
                    (row, row)
                    for row in range(cursor, cursor + remote_second_rank)
                )

                sources = [
                    state
                    for state in omega
                    if cylinder(state, flaw_first, flaw_second)
                ]
                assert sources
                transition_count = 0
                for source in sources:
                    before = cylinder(
                        source, remote_first, remote_second
                    )
                    for target in forward_targets(source):
                        after = cylinder(
                            target, remote_first, remote_second
                        )
                        assert not after or before
                        transition_count += after

                observed = Fraction(
                    transition_count, len(sources) * (n - 3)
                )
                stationary = Fraction(
                    sum(
                        cylinder(
                            state, remote_first, remote_second
                        )
                        for state in omega
                    ),
                    len(omega),
                )
                upper_union = cylinder_upper(
                    n,
                    flaw_first_rank + remote_first_rank,
                    flaw_second_rank + remote_second_rank,
                )
                lower_flaw = cylinder_lower(
                    n, flaw_first_rank, flaw_second_rank
                )
                lower_remote = cylinder_lower(
                    n, remote_first_rank, remote_second_rank
                )
                ratio_bound = upper_union / (
                    lower_flaw * lower_remote
                )
                union_probability = Fraction(
                    sum(
                        cylinder(
                            state,
                            flaw_first + remote_first,
                            flaw_second + remote_second,
                        )
                        for state in omega
                    ),
                    len(omega),
                )
                assert union_probability <= upper_union
                assert Fraction(len(sources), len(omega)) >= lower_flaw
                assert stationary >= lower_remote
                assert observed / stationary <= ratio_bound


def verify(n: int) -> None:
    omega = states(n)
    state_set = set(omega)
    flawed = {state for state in omega if state[0][0] == 0}
    scale = n - 3
    reverse: dict[State, list[State]] = {
        state: [] for state in omega if state not in flawed
    }

    for source in flawed:
        targets = forward_targets(source)
        assert len(targets) == scale
        assert len(set(targets)) == scale
        for target in targets:
            assert target in state_set
            assert target not in flawed
            first_old, second = source
            first_new, second_new = target
            assert second_new == second
            old_edges = {(row, first_old[row]) for row in range(n)}
            new_edges = {(row, first_new[row]) for row in range(n)}
            assert len(old_edges ^ new_edges) == 4
            assert all(first_new[row] != second[row] for row in range(n))
            reverse[target].append(source)

    assert all(len(predecessors) <= 1 for predecessors in reverse.values())

    incoming = {state: Fraction(0) for state in omega}
    for source in flawed:
        for target in forward_targets(source):
            incoming[target] += Fraction(1, scale)
    for source, predecessors in reverse.items():
        for target in predecessors:
            incoming[target] += Fraction(1, scale)
        incoming[source] += Fraction(scale - len(predecessors), scale)
    assert all(total == 1 for total in incoming.values())
    verify_remote(omega, n)
    verify_untouched_remote(omega, n)
    verify_mixed_remote(omega, n)
    verify_general_locality(omega, n)


def main() -> None:
    for n in (4, 5):
        verify(n)
    print("complete two-layer resampling: verified for N=4,5")


if __name__ == "__main__":
    main()
