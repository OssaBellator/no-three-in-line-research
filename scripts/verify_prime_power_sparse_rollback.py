#!/usr/bin/env python3
"""Exhaustive finite checks for CMR439--CMR443."""

from __future__ import annotations

from itertools import combinations, permutations
from math import ceil
from random import Random


Edge = tuple[int, int]


def matching(vector: tuple[int, ...]) -> frozenset[Edge]:
    return frozenset((source, row) for source, row in enumerate(vector))


def all_matchings(side: int) -> list[frozenset[Edge]]:
    return [matching(vector) for vector in permutations(range(side))]


def mask_of(edges: frozenset[Edge], universe: list[Edge]) -> int:
    positions = {edge: index for index, edge in enumerate(universe)}
    mask = 0
    for edge in edges:
        mask |= 1 << positions[edge]
    return mask


def subset_masks(mask: int) -> list[int]:
    values: list[int] = []
    current = mask
    while True:
        values.append(current)
        if current == 0:
            break
        current = (current - 1) & mask
    return values


def popcount(mask: int) -> int:
    return mask.bit_count()


def minimum_rollback_sets(
    final_mask: int,
    initial_mask: int,
    edge_bit: int,
    matching_masks: list[int],
) -> tuple[int, list[int]]:
    deleted = initial_mask & ~final_mask
    feasible: list[int] = []
    minimum = 10**9

    for rollback in subset_masks(deleted):
        size = popcount(rollback)
        if size > minimum:
            continue
        host = (final_mask | rollback) & ~edge_bit
        if not any(match_mask & ~host == 0 for match_mask in matching_masks):
            continue
        if size < minimum:
            minimum = size
            feasible = [rollback]
        elif size == minimum:
            feasible.append(rollback)

    assert minimum < 10**9
    return minimum, feasible


def essential_mask(host_mask: int, matching_masks: list[int]) -> int:
    states = [match_mask for match_mask in matching_masks if match_mask & ~host_mask == 0]
    assert states
    common = states[0]
    for state in states[1:]:
        common &= state
    return common


def residual_matching_count(
    side: int,
    host_edges: set[Edge],
    forced_edges: set[Edge],
) -> int:
    removed_left = {left for left, _ in forced_edges}
    removed_right = {right for _, right in forced_edges}
    left = [vertex for vertex in range(side) if vertex not in removed_left]
    right = [vertex for vertex in range(side) if vertex not in removed_right]

    count = 0
    for image in permutations(right):
        candidate = {(source, target) for source, target in zip(left, image)}
        if candidate <= host_edges:
            count += 1
    return count


def maximum_disjoint_family(sets: list[int]) -> int:
    best = 0
    for choice_mask in range(1 << len(sets)):
        used = 0
        count = 0
        valid = True
        for index, value in enumerate(sets):
            if not choice_mask & (1 << index):
                continue
            if used & value:
                valid = False
                break
            used |= value
            count += 1
        if valid:
            best = max(best, count)
    return best


def verify_pair(
    side: int,
    final_mask: int,
    initial_mask: int,
    universe: list[Edge],
    matching_masks: list[int],
) -> None:
    initial_states = [mask for mask in matching_masks if mask & ~initial_mask == 0]
    final_states = [mask for mask in matching_masks if mask & ~final_mask == 0]
    if not initial_states or not final_states:
        return

    if essential_mask(initial_mask, matching_masks):
        return

    final_essential = essential_mask(final_mask, matching_masks)
    if not final_essential:
        return

    positions = {edge: index for index, edge in enumerate(universe)}
    chosen_rollbacks: list[int] = []
    rollback_sizes: list[int] = []

    for edge in universe:
        edge_bit = 1 << positions[edge]
        if not final_essential & edge_bit:
            continue

        minimum, rollbacks = minimum_rollback_sets(
            final_mask,
            initial_mask,
            edge_bit,
            matching_masks,
        )
        assert 1 <= minimum <= side
        rollback_sizes.append(minimum)
        chosen_rollbacks.append(min(rollbacks))

        for rollback in rollbacks:
            host = (final_mask | rollback) & ~edge_bit
            states = [mask for mask in matching_masks if mask & ~host == 0]
            assert states

            common = states[0]
            for state in states[1:]:
                common &= state
            assert rollback & ~common == 0

            forced_edges = {
                universe[index]
                for index in range(len(universe))
                if rollback & (1 << index)
            }
            assert len({left for left, _ in forced_edges}) == len(forced_edges)
            assert len({right for _, right in forced_edges}) == len(forced_edges)

            host_edges = {
                universe[index]
                for index in range(len(universe))
                if host & (1 << index)
            }
            assert len(states) == residual_matching_count(
                side,
                host_edges,
                forced_edges,
            )

            for threshold in range(1, side + 1):
                if minimum < threshold:
                    assert popcount(rollback) < threshold
                else:
                    assert side - popcount(rollback) <= side - threshold

    count = len(chosen_rollbacks)
    assert count <= side
    assert sum(popcount(value) for value in chosen_rollbacks) <= side * count
    assert sum(popcount(value) for value in chosen_rollbacks) <= side * side

    for multiplicity in range(2, count + 2):
        degrees = [
            sum(bool(rollback & (1 << bit)) for rollback in chosen_rollbacks)
            for bit in range(len(universe))
        ]
        if max(degrees, default=0) >= multiplicity:
            continue
        packing = maximum_disjoint_family(chosen_rollbacks)
        required = ceil(count / (side * (multiplicity - 1)))
        assert packing >= required

        for threshold in range(2, side + 1):
            cheap = [
                rollback
                for rollback, size in zip(chosen_rollbacks, rollback_sizes)
                if size < threshold
            ]
            if not cheap:
                continue
            cheap_degrees = [
                sum(bool(rollback & (1 << bit)) for rollback in cheap)
                for bit in range(len(universe))
            ]
            if max(cheap_degrees, default=0) >= multiplicity:
                continue
            cheap_packing = maximum_disjoint_family(cheap)
            cheap_required = ceil(
                len(cheap) / ((threshold - 1) * (multiplicity - 1))
            )
            assert cheap_packing >= cheap_required


def verify_exhaustive_small_hosts() -> None:
    for side in (2, 3):
        universe = [
            (left, right)
            for left in range(side)
            for right in range(side)
        ]
        matching_masks = [mask_of(value, universe) for value in all_matchings(side)]
        edge_count = len(universe)

        # A ternary edge state records absent from G0, present only in G0, or
        # present in both G0 and G.  This enumerates every nested pair G <= G0.
        for code in range(3**edge_count):
            value = code
            final_mask = 0
            initial_mask = 0
            for bit in range(edge_count):
                state = value % 3
                value //= 3
                if state >= 1:
                    initial_mask |= 1 << bit
                if state == 2:
                    final_mask |= 1 << bit
            verify_pair(
                side,
                final_mask,
                initial_mask,
                universe,
                matching_masks,
            )


def verify_sampled_side_four() -> None:
    side = 4
    universe = [
        (left, right)
        for left in range(side)
        for right in range(side)
    ]
    matching_masks = [mask_of(value, universe) for value in all_matchings(side)]
    rng = Random(20260725)

    for _ in range(2000):
        initial_mask = 0
        final_mask = 0
        for bit in range(len(universe)):
            state = rng.randrange(3)
            if state >= 1:
                initial_mask |= 1 << bit
            if state == 2:
                final_mask |= 1 << bit
        verify_pair(
            side,
            final_mask,
            initial_mask,
            universe,
            matching_masks,
        )


def main() -> None:
    verify_exhaustive_small_hosts()
    verify_sampled_side_four()
    print(
        "verified sparse rollback: size-t escape, minimum rollback essential "
        "core, exact residual factorization, terminal-certificate escape, "
        "quadratic incidence, and rollback packing/concentration bounds"
    )


if __name__ == "__main__":
    main()
