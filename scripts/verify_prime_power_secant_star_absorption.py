#!/usr/bin/env python3
"""Verify CMR611--CMR616 secant-star wall/absorption arithmetic."""

from itertools import combinations
from math import ceil, sqrt
from random import Random


Cell = tuple[int, int]
Arm = tuple[Cell, Cell]


def compatible_pair(a: Cell, b: Cell) -> bool:
    return a[0] != b[0] and a[1] != b[1]


def matching_vertices(arm: Arm) -> set[tuple[str, int]]:
    a, b = arm
    return {
        ("L", a[0]),
        ("R", a[1]),
        ("L", b[0]),
        ("R", b[1]),
    }


def is_cell_disjoint(family: list[Arm]) -> bool:
    cells = [cell for arm in family for cell in arm]
    return len(set(cells)) == len(cells)


def greedy_vertex_disjoint(family: list[Arm]) -> list[Arm]:
    remaining = list(family)
    selected: list[Arm] = []
    while remaining:
        arm = remaining[0]
        selected.append(arm)
        vertices = matching_vertices(arm)
        remaining = [
            other
            for other in remaining[1:]
            if matching_vertices(other).isdisjoint(vertices)
        ]
    return selected


def maximum_vertex_degree(family: list[Arm]) -> int:
    vertices = {
        vertex
        for arm in family
        for vertex in matching_vertices(arm)
    }
    return max(
        (
            sum(vertex in matching_vertices(arm) for arm in family)
            for vertex in vertices
        ),
        default=0,
    )


def check_family(n: int, family: list[Arm]) -> None:
    assert is_cell_disjoint(family)
    assert all(compatible_pair(*arm) for arm in family)
    size = len(family)
    if not size:
        return

    degree = maximum_vertex_degree(family)
    for threshold in range(2, size + 3):
        if degree >= threshold:
            continue
        selected = greedy_vertex_disjoint(family)
        assert len(selected) >= ceil(size / (4 * (threshold - 1)))

        for protected_size in range(n + 1):
            protected_vertices = {
                ("L", index) for index in range(protected_size)
            } | {
                ("R", index) for index in range(protected_size)
            }
            touching = [
                arm
                for arm in selected
                if not matching_vertices(arm).isdisjoint(protected_vertices)
            ]
            free = [arm for arm in selected if arm not in touching]
            assert len(touching) <= 2 * protected_size
            assert len(free) >= max(0, len(selected) - 2 * protected_size)

            free_cells = {cell for arm in free for cell in arm}
            assert len(free_cells) == 2 * len(free)
            assert (
                len({x for x, _ in free_cells}) == len(free_cells)
                and len({y for _, y in free_cells}) == len(free_cells)
            )


def random_families() -> int:
    rng = Random(20260726)
    checked = 0
    for n in range(3, 9):
        cells = [(x, y) for x in range(n) for y in range(n)]
        pairs = [
            (a, b)
            for a, b in combinations(cells, 2)
            if compatible_pair(a, b)
        ]
        for _ in range(800):
            rng.shuffle(pairs)
            family: list[Arm] = []
            used: set[Cell] = set()
            for arm in pairs:
                if used.isdisjoint(arm) and rng.random() < 0.25:
                    family.append(arm)
                    used.update(arm)
            check_family(n, family)
            checked += 1
    return checked


def structured_families() -> int:
    checked = 0
    for n in range(3, 20):
        # Pair two cyclic permutation matchings.  These create both low- and
        # high-vertex-degree arm systems depending on the shift.
        for shift in range(1, n):
            cells = [(i, i) for i in range(n)] + [
                (i, (i + shift) % n) for i in range(n)
            ]
            family: list[Arm] = []
            for index in range(0, len(cells) - 1, 2):
                a, b = cells[index], cells[index + 1]
                if compatible_pair(a, b):
                    family.append((a, b))
            if is_cell_disjoint(family):
                check_family(n, family)
                checked += 1
    return checked


def check_square_root_and_budget() -> None:
    for size in range(1, 5000):
        threshold = max(2, ceil(sqrt(size)))
        extracted = ceil(size / (4 * (threshold - 1)))
        assert extracted >= 1
        for protected_size in range(0, 100):
            growth = 2 * max(0, extracted - 2 * protected_size)
            if growth == 0:
                assert protected_size >= extracted / 2

    for n in range(1, 100):
        for initial in range(n + 1):
            for minimum_arms in range(1, 30):
                count = (n - initial) // (2 * minimum_arms)
                assert initial + 2 * count * minimum_arms <= n


def main() -> None:
    checked = random_families() + structured_families()
    check_square_root_and_budget()
    print(
        "verified secant-star protected absorption for "
        f"{checked} sampled and structured arm families"
    )


if __name__ == "__main__":
    main()
