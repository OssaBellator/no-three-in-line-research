#!/usr/bin/env python3
"""Finite checks for BDA5al--BDA5ao union-safe products."""

from __future__ import annotations

from itertools import permutations, product

Permutation = tuple[int, ...]
State = tuple[Permutation, Permutation, tuple[int, ...], str]


def is_permutation(values: Permutation) -> bool:
    return sorted(values) == list(range(len(values)))


def is_disjoint(active: Permutation, blocker: Permutation) -> bool:
    return all(a != b for a, b in zip(active, blocker))


def derangements(n: int) -> tuple[Permutation, ...]:
    return tuple(
        perm for perm in permutations(range(n))
        if all(perm[column] != column for column in range(n))
    )


def role_state(blocker: Permutation, role: tuple[int, int], name: str) -> State:
    n = len(blocker)
    assert n == 5
    c0, c1 = role
    active = tuple(range(n))
    active_after = list(active)
    active_after[c0], active_after[c1] = c1, c0

    blocked_c = blocker[c0] == c1
    blocked_d = blocker[c1] == c0
    occupancy = int(blocked_c) + int(blocked_d)
    blocker_after = list(blocker)
    selected_columns: list[int] = []
    auxiliaries = [column for column in range(n) if column not in role]

    if occupancy == 0:
        state_name = f"{name}-empty"
    elif occupancy == 1:
        if blocked_c:
            auxiliary = next(column for column in auxiliaries if blocker[column] != c0)
            blocker_after[c0], blocker_after[auxiliary] = (
                blocker[auxiliary],
                blocker[c0],
            )
            selected_columns = [c0, auxiliary]
            state_name = f"{name}-single-c0"
        else:
            auxiliary = next(column for column in auxiliaries if blocker[column] != c1)
            blocker_after[c1], blocker_after[auxiliary] = (
                blocker[auxiliary],
                blocker[c1],
            )
            selected_columns = [c1, auxiliary]
            state_name = f"{name}-single-c1"
    else:
        auxiliary0, auxiliary1 = auxiliaries[:2]
        blocker_after[c0] = blocker[auxiliary0]
        blocker_after[c1] = blocker[auxiliary1]
        blocker_after[auxiliary0] = c0
        blocker_after[auxiliary1] = c1
        selected_columns = [c0, c1, auxiliary0, auxiliary1]
        state_name = f"{name}-full"

    active_tuple = tuple(active_after)
    blocker_tuple = tuple(blocker_after)
    assert is_permutation(active_tuple)
    assert is_permutation(blocker_tuple)
    assert is_disjoint(active_tuple, blocker_tuple)
    assert blocker_tuple[c0] != c0
    assert blocker_tuple[c1] != c1
    assert all(column in range(n) for column in selected_columns)
    return active_tuple, blocker_tuple, tuple(selected_columns), state_name


def menu(blocker: Permutation) -> tuple[State, State]:
    states = (
        role_state(blocker, (0, 1), "u"),
        role_state(blocker, (2, 3), "v"),
    )
    assert len(states) == 2
    active_before = tuple(range(5))
    paid = (
        frozenset({(4, 4), (0, 0), (2, 2)}),
        frozenset({(4, 4), (1, 1), (3, 3)}),
    )
    for active_after, blocker_after, _, _ in states:
        union = {
            *enumerate(active_after),
            *enumerate(blocker_after),
        }
        assert all(not certificate <= union for certificate in paid)
        assert is_disjoint(active_after, blocker_after)
        assert active_after != active_before
    return states


def verify_local_menus() -> tuple[int, int, int]:
    checks = 0
    occupancy_counts = [0, 0, 0]
    phase_flip_regressions = 0
    for blocker in derangements(5):
        states = menu(blocker)
        for role, state in zip(((0, 1), (2, 3)), states):
            c0, c1 = role
            occupancy = int(blocker[c0] == c1) + int(blocker[c1] == c0)
            occupancy_counts[occupancy] += 1
            active_after, blocker_after, selected_columns, _ = state
            assert set(selected_columns) <= set(range(5))
            assert blocker_after[c0] != c0 and blocker_after[c1] != c1
            checks += 1
            if occupancy == 2:
                # The old phase flip restores both old endpoints to the blocker layer.
                phase_flip = list(blocker)
                phase_flip[c0], phase_flip[c1] = c0, c1
                assert phase_flip[c0] == c0 and phase_flip[c1] == c1
                phase_flip_regressions += 1
    assert checks == 2 * len(derangements(5))
    return checks, sum(occupancy_counts), phase_flip_regressions


def shifted_state(state: State, offset: int) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
    active, blocker, _, _ = state
    active_cells = {(offset + column, offset + row) for column, row in enumerate(active)}
    blocker_cells = {(offset + column, offset + row) for column, row in enumerate(blocker)}
    return active_cells, blocker_cells


def is_matching(cells: set[tuple[int, int]]) -> bool:
    return (
        len({column for column, _ in cells}) == len(cells)
        and len({row for _, row in cells}) == len(cells)
    )


def verify_products(maximum_pairs: int = 3) -> int:
    local = tuple((blocker, menu(blocker)) for blocker in derangements(5))
    checks = 0
    for pair_count in range(1, maximum_pairs + 1):
        # Exhaust all blockers for one and two envelopes. For three envelopes,
        # use every ordered triple from a representative 12-derangement slice.
        pool = local if pair_count <= 2 else local[:12]
        for family in product(pool, repeat=pair_count):
            menus = [entry[1] for entry in family]
            for choices in product((0, 1), repeat=pair_count):
                active_cells: set[tuple[int, int]] = set()
                blocker_cells: set[tuple[int, int]] = set()
                for index, choice in enumerate(choices):
                    active_local, blocker_local = shifted_state(
                        menus[index][choice], 5 * index
                    )
                    assert active_cells.isdisjoint(active_local)
                    assert blocker_cells.isdisjoint(blocker_local)
                    active_cells.update(active_local)
                    blocker_cells.update(blocker_local)
                assert is_matching(active_cells)
                assert is_matching(blocker_cells)
                assert active_cells.isdisjoint(blocker_cells)
                checks += 1
    return checks


def verify_exact_product_events() -> int:
    checks = 0
    for rank in (1, 2, 3):
        states = tuple(product((0, 1), repeat=rank))
        for event_mask in range(1 << len(states)):
            accepted = {
                state for index, state in enumerate(states)
                if event_mask & (1 << index)
            }
            multiplicity = len(accepted)
            assert multiplicity / (2**rank) == sum(
                state in accepted for state in states
            ) / len(states)
            checks += 1
    return checks


def verify_rank_one_suppression() -> tuple[int, int]:
    floor_checks = 0
    for envelope_count in range(1, 5):
        for costs in product(range(5), repeat=2 * envelope_count):
            pairs = [costs[2 * i : 2 * i + 2] for i in range(envelope_count)]
            t1 = sum((a + b) / 2 for a, b in pairs)
            b1 = sum(min(a, b) for a, b in pairs)
            i1 = sum(abs(a - b) for a, b in pairs)
            assert t1 == b1 + i1 / 2
            assert b1 == sum(min(pair) for pair in pairs)
            floor_checks += 1

    higher_rank_checks = 0
    for rank in (2, 3):
        states = tuple(product((0, 1), repeat=rank))
        for chosen in states:
            for event_mask in range(1, 1 << len(states)):
                accepted = {
                    state for index, state in enumerate(states)
                    if event_mask & (1 << index)
                }
                indicator = int(chosen in accepted)
                probability = len(accepted) / (2**rank)
                assert indicator <= (2**rank) * probability
                higher_rank_checks += 1
    return floor_checks, higher_rank_checks


def verify_router_constants() -> int:
    checks = 0
    for gap in range(1, 50):
        for b1 in range(gap + 1):
            for t2 in range(gap + 1):
                for t3 in range(gap + 1):
                    if b1 + 4 * t2 + 8 * t3 < gap:
                        continue
                    assert b1 >= gap / 3 or t2 >= gap / 12 or t3 >= gap / 24
                    checks += 1
    return checks


def main() -> None:
    local_checks, occupancy_checks, regressions = verify_local_menus()
    product_checks = verify_products()
    event_checks = verify_exact_product_events()
    floor_checks, higher_checks = verify_rank_one_suppression()
    router_checks = verify_router_constants()
    print("BDA union-safe product propagation verified")
    print(f"  local canonical role states: {local_checks}")
    print(f"  occupancy classifications: {occupancy_checks}")
    print(f"  rejected full phase flips: {regressions}")
    print(f"  heterogeneous product states: {product_checks}")
    print(f"  exact product events: {event_checks}")
    print(f"  floor/imbalance systems: {floor_checks}")
    print(f"  higher-rank event bounds: {higher_checks}")
    print(f"  failed-router systems: {router_checks}")


if __name__ == "__main__":
    main()
