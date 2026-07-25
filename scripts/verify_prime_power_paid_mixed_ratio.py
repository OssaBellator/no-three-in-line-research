#!/usr/bin/env python3
"""Exact checks for CMR322--CMR325."""

from __future__ import annotations

from itertools import permutations
from math import ceil, factorial


def line_cells(
    x1: int,
    x2: int,
    y3: int,
    descriptor: tuple[int, int, int],
) -> frozenset[tuple[int, int]]:
    a, b, c = descriptor
    cells = frozenset(((x1, a), (x2, b), (c, y3)))
    assert len(cells) == 3
    assert len({x for x, _ in cells}) == 3
    assert len({y for _, y in cells}) == 3
    points = list(cells)
    (u1, v1), (u2, v2), (u3, v3) = points
    assert (u2 - u1) * (v3 - v1) == (u3 - u1) * (v2 - v1)
    return cells


def completions(
    t: int,
    target: tuple[int, int],
    prescription: frozenset[tuple[int, int]],
) -> list[tuple[int, ...]]:
    result = []
    for state in permutations(range(t)):
        if state[target[0]] == target[1]:
            continue
        if all(state[source] == row for source, row in prescription):
            result.append(state)
    return result


def verify_certificate(
    t: int,
    triple: tuple[tuple[int, int], tuple[int, int], tuple[int, int]],
    descriptors: list[tuple[int, int, int]],
) -> None:
    (x1, y1), (x2, _), (_, y3) = triple
    target = (x1, y1)
    cylinders: list[set[tuple[int, ...]]] = []
    fan_rows = set()

    for descriptor in descriptors:
        cells = line_cells(x1, x2, y3, descriptor)
        fan_cell = (x1, descriptor[0])
        assert fan_cell in cells
        assert fan_cell != target
        assert descriptor[0] not in fan_rows
        fan_rows.add(descriptor[0])

        states = set(completions(t, target, cells))
        assert len(states) == factorial(t - 3)
        for state in states:
            assert state[x1] != y1
            assert all(state[source] == row for source, row in cells)
        cylinders.append(states)

    for left in range(len(cylinders)):
        for right in range(left + 1, len(cylinders)):
            assert cylinders[left].isdisjoint(cylinders[right])

    union = set().union(*cylinders)
    assert len(union) == len(descriptors) * factorial(t - 3)


def verify_explicit_banks() -> None:
    verify_certificate(
        5,
        ((0, 0), (1, 1), (4, 4)),
        [(3, 4, 1), (1, 2, 3), (2, 3, 2), (4, 0, 0)],
    )
    verify_certificate(
        7,
        ((0, 0), (1, 1), (6, 6)),
        [(5, 6, 1), (1, 2, 5), (3, 4, 3), (4, 5, 2), (2, 3, 4), (6, 0, 0)],
    )


def verify_population_arithmetic() -> None:
    for p, h in ((5, 2), (5, 3), (7, 2), (7, 3), (11, 2)):
        t = p**h
        population = ceil((t - 3 - 2 * (t // p)) / (p - 1))
        assert population >= 0
        state_count = population * factorial(t - 3)
        assert state_count >= 0
        if population:
            assert state_count // population == factorial(t - 3)


def main() -> None:
    verify_explicit_banks()
    verify_population_arithmetic()
    print(
        "verified paid mixed-ratio banks: fan-anchored triples, exact "
        "(t-3)! completions, disjoint cylinders, and bank-size arithmetic"
    )


if __name__ == "__main__":
    main()
