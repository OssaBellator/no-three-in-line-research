#!/usr/bin/env python3
"""Exact checks for CMR326--CMR329."""

from __future__ import annotations

from itertools import combinations, permutations
from math import factorial

Cell = tuple[int, int]
State = tuple[int, ...]


def collinear(triple: tuple[Cell, Cell, Cell]) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = triple
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def compatible(cells: tuple[Cell, ...] | frozenset[Cell]) -> bool:
    return len({x for x, _ in cells}) == len(cells) and len(
        {y for _, y in cells}
    ) == len(cells)


def completions(t: int, target: Cell, prescribed: frozenset[Cell]) -> list[State]:
    return [
        state
        for state in permutations(range(t))
        if state[target[0]] != target[1]
        and all(state[x] == y for x, y in prescribed)
    ]


def candidate_triples(t: int) -> list[frozenset[Cell]]:
    points = [(x, y) for x in range(t) for y in range(t)]
    return [
        frozenset(cells)
        for cells in combinations(points, 3)
        if compatible(cells) and collinear(cells)
    ]


def explicit_designated_triples(
    t: int,
    x1: int,
    x2: int,
    y3: int,
    descriptors: list[tuple[int, int, int]],
) -> list[frozenset[Cell]]:
    triples = []
    for a, b, c in descriptors:
        if c in (x1, x2):
            continue
        cells = frozenset(((x1, a), (x2, b), (c, y3)))
        assert compatible(cells)
        assert collinear(tuple(cells))
        triples.append(cells)
    return triples


def verify_conditional_law(
    t: int,
    target: Cell,
    designated: frozenset[Cell],
) -> None:
    states = completions(t, target, designated)
    n = t - 3
    assert len(states) == factorial(n)

    remaining_cells = [
        (x, y)
        for x in range(t)
        for y in range(t)
        if x not in {u for u, _ in designated}
        and y not in {v for _, v in designated}
    ]
    prescriptions: set[frozenset[Cell]] = set()
    for fixed_count in range(4):
        for fixed in combinations(tuple(designated), fixed_count):
            for residual_count in range(4 - fixed_count):
                if residual_count > n:
                    continue
                for residual in combinations(remaining_cells, residual_count):
                    prescription = frozenset(fixed + residual)
                    if not prescription or not compatible(prescription | designated):
                        continue
                    prescriptions.add(prescription)

    for prescription in prescriptions:
        overlap = len(prescription & designated)
        rank = len(prescription)
        residual_rank = rank - overlap
        assert residual_rank <= n
        count = sum(
            all(state[x] == y for x, y in prescription)
            for state in states
        )
        assert count == factorial(n - residual_rank)


def verify_exact_collateral(
    t: int,
    target: Cell,
    designated: frozenset[Cell],
) -> None:
    assert t >= 6
    states = completions(t, target, designated)
    triples = candidate_triples(t)
    n = t - 3
    u = [0, 0, 0]
    for triple in triples:
        if triple == designated or not compatible(triple | designated):
            continue
        overlap = len(triple & designated)
        assert overlap in (0, 1, 2)
        u[overlap] += 1

    total_occurrences = 0
    for state in states:
        selected = frozenset((x, state[x]) for x in range(t))
        total_occurrences += sum(triple <= selected for triple in triples)

    scaled_expected = (
        factorial(n)
        + u[0] * factorial(n - 3)
        + u[1] * factorial(n - 2)
        + u[2] * factorial(n - 1)
    )
    assert total_occurrences == scaled_expected
    assert u[2] <= 3 * (t - 3)


def verify_unconditional_atoms(
    t: int,
    target: Cell,
    designated: list[frozenset[Cell]],
) -> None:
    cylinders = [set(completions(t, target, triple)) for triple in designated]
    assert all(len(cylinder) == factorial(t - 3) for cylinder in cylinders)
    assert all(
        cylinders[i].isdisjoint(cylinders[j])
        for i in range(len(cylinders))
        for j in range(i + 1, len(cylinders))
    )
    states = list(set().union(*cylinders))
    m = len(designated)
    n = t - 3
    assert len(states) == m * factorial(n)

    all_cells = [(x, y) for x in range(t) for y in range(t)]
    for cell in all_cells:
        count = sum(state[cell[0]] == cell[1] for state in states)
        assert count * m * n <= len(states) * (m + n)

    if n < 2:
        return
    for cells in combinations(all_cells, 2):
        if not compatible(cells):
            continue
        count = sum(all(state[x] == y for x, y in cells) for state in states)
        right_factor = n * (n - 1) + 2 * (n - 1) + m
        assert count * m * n * (n - 1) <= len(states) * right_factor


def verify_examples() -> None:
    examples = [
        (
            5,
            (0, 0),
            explicit_designated_triples(
                5,
                0,
                1,
                4,
                [(3, 4, 1), (1, 2, 3), (2, 3, 2), (4, 0, 0)],
            ),
        ),
        (
            7,
            (0, 0),
            explicit_designated_triples(
                7,
                0,
                1,
                6,
                [(5, 6, 1), (1, 2, 5), (3, 4, 3), (4, 5, 2), (2, 3, 4), (6, 0, 0)],
            ),
        ),
    ]
    for t, target, designated in examples:
        assert designated
        for triple in designated:
            verify_conditional_law(t, target, triple)
            if t >= 6:
                verify_exact_collateral(t, target, triple)
        verify_unconditional_atoms(t, target, designated)


def main() -> None:
    verify_examples()
    print(
        "verified paid ratio spread: conditional falling-factorial cylinders, "
        "t>=6 collateral identities, rank-two bounds, and bank atom estimates"
    )


if __name__ == "__main__":
    main()
