#!/usr/bin/env python3
"""Verify BDA5f--BDA5g heterogeneous radial decoder products."""

from __future__ import annotations

from itertools import product


Point = tuple[int, int]
State = tuple[frozenset[Point], frozenset[Point], str]


def is_matching(points: set[Point] | frozenset[Point]) -> bool:
    return (
        len({point[0] for point in points}) == len(points)
        and len({point[1] for point in points}) == len(points)
    )


def pair_data(index: int):
    base = 10 * index
    anchor = (base + 4, base + 4)
    active = {
        anchor,
        (base, base),
        (base + 1, base + 1),
        (base + 2, base + 2),
        (base + 3, base + 3),
    }
    roles = {
        "u": (
            (base, base),
            (base + 1, base + 1),
            (base, base + 1),
            (base + 1, base),
        ),
        "v": (
            (base + 2, base + 2),
            (base + 3, base + 3),
            (base + 2, base + 3),
            (base + 3, base + 2),
        ),
    }
    paid = (
        frozenset((anchor, roles["u"][0], roles["v"][0])),
        frozenset((anchor, roles["u"][1], roles["v"][1])),
    )
    return active, roles, paid


def blocker_cells(index: int, counts: tuple[int, int]) -> set[Point]:
    _, roles, _ = pair_data(index)
    cells: set[Point] = set()
    for role, count in zip(("u", "v"), counts):
        cross = roles[role][2:]
        if count == 1:
            cells.add(cross[0])
        elif count == 2:
            cells.update(cross)
    return cells


def local_menu(index: int, counts: tuple[int, int]) -> tuple[State, ...]:
    active_before, roles, paid = pair_data(index)
    blocker_before = blocker_cells(index, counts)
    states: list[State] = []

    for role, count in zip(("u", "v"), counts):
        first, second, cross_first, cross_second = roles[role]
        if count not in (0, 2):
            continue
        active_after = (
            active_before - {first, second}
        ) | {cross_first, cross_second}
        blocker_after = set(blocker_before)
        name = f"{role}-empty"
        if count == 2:
            blocker_after.difference_update({cross_first, cross_second})
            blocker_after.update({first, second})
            name = f"{role}-full"
        states.append((
            frozenset(active_after),
            frozenset(blocker_after),
            name,
        ))

    if counts == (1, 1):
        u = roles["u"]
        v = roles["v"]
        active_after = (
            active_before - {u[0], u[1], v[0], v[1]}
        ) | {u[2], u[3], v[2], v[3]}
        first_blocker = u[2]
        second_blocker = v[2]
        blocker_after = {
            (first_blocker[0], second_blocker[1]),
            (second_blocker[0], first_blocker[1]),
        }
        states.append((
            frozenset(active_after),
            frozenset(blocker_after),
            "double-single",
        ))

    assert states
    for active_after, blocker_after, _ in states:
        assert is_matching(active_after)
        assert is_matching(blocker_after)
        assert active_after.isdisjoint(blocker_after)
        assert {p[0] for p in active_after} == {
            p[0] for p in active_before
        }
        assert {p[1] for p in active_after} == {
            p[1] for p in active_before
        }
        assert {p[0] for p in blocker_after} == {
            p[0] for p in blocker_before
        }
        assert {p[1] for p in blocker_after} == {
            p[1] for p in blocker_before
        }
        assert all(not triple <= active_after for triple in paid)
    return tuple(states)


def verify_heterogeneous_products(maximum_pairs: int = 3) -> int:
    patterns = tuple(product(range(3), repeat=2))
    checked = 0
    for pair_count in range(1, maximum_pairs + 1):
        for family in product(patterns, repeat=pair_count):
            menus = tuple(
                local_menu(index, counts)
                for index, counts in enumerate(family)
            )
            for choices in product(*(
                range(len(menu)) for menu in menus
            )):
                active: set[Point] = set()
                blocker: set[Point] = set()
                for index, choice in enumerate(choices):
                    state = menus[index][choice]
                    assert active.isdisjoint(state[0])
                    assert blocker.isdisjoint(state[1])
                    active.update(state[0])
                    blocker.update(state[1])
                assert is_matching(active)
                assert is_matching(blocker)
                assert active.isdisjoint(blocker)
                checked += 1
    return checked


def verify_exact_product_accounting(maximum_pairs: int = 3) -> int:
    patterns = tuple(product(range(3), repeat=2))
    checked = 0
    for pair_count in range(1, maximum_pairs + 1):
        for family in product(patterns, repeat=pair_count):
            menu_sizes = tuple(
                len(local_menu(index, counts))
                for index, counts in enumerate(family)
            )
            global_states = tuple(product(*(
                range(size) for size in menu_sizes
            )))
            for mask in range(1, 1 << pair_count):
                affected = tuple(
                    index
                    for index in range(pair_count)
                    if mask & (1 << index)
                )
                local_states = tuple(product(*(
                    range(menu_sizes[index]) for index in affected
                )))
                denominator = 1
                for index in affected:
                    denominator *= menu_sizes[index]
                for event_mask in range(1 << len(local_states)):
                    accepted = {
                        local_states[offset]
                        for offset in range(len(local_states))
                        if event_mask & (1 << offset)
                    }
                    multiplicity = len(accepted)
                    direct = sum(
                        tuple(state[index] for index in affected)
                        in accepted
                        for state in global_states
                    )
                    assert direct * denominator == (
                        multiplicity * len(global_states)
                    )
                    checked += 1
    return checked


def main() -> None:
    products = verify_heterogeneous_products()
    accounting = verify_exact_product_accounting()
    print(
        "BDA heterogeneous radial decoder verified:",
        f"{products} joint decoder states,",
        f"{accounting} exact product events",
    )


if __name__ == "__main__":
    main()
