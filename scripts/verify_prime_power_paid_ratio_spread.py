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
    result = []
    for cells in combinations(points, 3):
        if compatible(cells) and collinear(cells):
            result.append(frozenset(cells))
    return result


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
    prescriptions = [
        frozenset(cells)
        for rank in (1, 2, 3)
        for cells in combinations(remaining_cells, rank)
        if compatible(cells)
    ]
    prescriptions.extend(
        frozenset((fixed, residual))
        for fixed in designated
        for residual in remaining_cells
        if compatible((fixed, residual))
    )

    for prescription in prescriptions:
        if not compatible(prescription | designated):
            continue
        overlap = len(prescription & designated)
        rank = len(prescription)
        count = sum(
            all(state[x] == y for x, y in prescription)
            for state in states
        )
        expected = factorial(n - (rank - overlap))
        assert count == expected


def verify_exact_collateral(
    t: int,
    target: Cell,
    designated: frozenset[Cell],
) -> None:
    states = completions(t, target, designated)
    triples = candidate_triples(t)
    n = t - 3
    u = [0, 0, 0]
    for triple in triples:
        if triple == designated:
            continue
        if not compatible(triple | designated):
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
        probability_numerator = sum(state[cell[0]] == cell[1] for state in states)
        assert probability_numerator * m * n <= len(states) * (m + n)

    for cells in combinations(all_cells, 2):
        if not compatible(cells):
            continue
        count = sum(all(state[x] == y for x, y in cells) for state in states)
        # Multiply the displayed CMR327 bound by m*(n)_2.
        right = (n * (n - 1) + 2 * (n - 1) + m) * factorial(n)
        assert count * m * n * (n - 1) <= right * m


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
            verify_exact_collateral(t, target, triple)
        verify_unconditional_atoms(t, target, designated)


def main() -> None:
    verify_examples()
    print(
        "verified paid ratio spread: conditional falling-factorial cylinders, "
        "exact collateral identities, rank-two bounds, and bank atom estimates"
    )


if __name__ == "__main__":
    main()
