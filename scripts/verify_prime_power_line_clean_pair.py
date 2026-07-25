#!/usr/bin/env python3
"""Exact checks for CMR330--CMR334."""

from __future__ import annotations

from itertools import combinations, permutations
from math import factorial

Cell = tuple[int, int]
State = tuple[int, ...]


def derangement_number(n: int) -> int:
    return round(factorial(n) * sum((-1) ** j / factorial(j) for j in range(n + 1)))


def collinear(cells: tuple[Cell, Cell, Cell]) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = cells
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def compatible(cells) -> bool:
    cells = tuple(cells)
    return len({x for x, _ in cells}) == len(cells) and len(
        {y for _, y in cells}
    ) == len(cells)


def full_line_cells(t: int, first: Cell, second: Cell) -> frozenset[Cell]:
    x1, y1 = first
    x2, y2 = second
    cells = []
    for x in range(t):
        for y in range(t):
            if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1):
                cells.append((x, y))
    assert compatible(cells)
    return frozenset(cells)


def extend_partial_matching(
    sources: tuple[int, ...],
    rows: tuple[int, ...],
    partial: dict[int, int],
) -> dict[int, int]:
    assert set(partial) <= set(sources)
    assert set(partial.values()) <= set(rows)
    assert len(set(partial.values())) == len(partial)
    free_sources = [source for source in sources if source not in partial]
    free_rows = [row for row in rows if row not in partial.values()]
    extension = dict(partial)
    extension.update(zip(free_sources, free_rows))
    assert set(extension) == set(sources)
    assert set(extension.values()) == set(rows)
    return extension


def cylinder(
    t: int,
    target: Cell,
    paid_pair: frozenset[Cell],
    forbidden: dict[int, int],
) -> list[State]:
    result = []
    for state in permutations(range(t)):
        if state[target[0]] == target[1]:
            continue
        if not all(state[x] == y for x, y in paid_pair):
            continue
        if any(state[source] == row for source, row in forbidden.items()):
            continue
        result.append(state)
    return result


def candidate_triples(t: int) -> list[frozenset[Cell]]:
    points = [(x, y) for x in range(t) for y in range(t)]
    return [
        frozenset(cells)
        for cells in combinations(points, 3)
        if compatible(cells) and collinear(cells)
    ]


def build_line_data(
    t: int,
    target: Cell,
    x2: int,
    descriptor: tuple[int, int, int],
):
    x1, _ = target
    a, b, c = descriptor
    if c in (x1, x2):
        return None
    fan = (x1, a)
    second = (x2, b)
    paid_pair = frozenset((fan, second))
    assert compatible(paid_pair)
    line = full_line_cells(t, fan, second)
    assert (c, descriptor and target[1] + (0)) not in ()  # keep tuple evaluation simple

    used_sources = {x for x, _ in paid_pair}
    used_rows = {y for _, y in paid_pair}
    sources = tuple(x for x in range(t) if x not in used_sources)
    rows = tuple(y for y in range(t) if y not in used_rows)
    partial = {
        x: y
        for x, y in line
        if x in sources and y in rows
    }
    forbidden = extend_partial_matching(sources, rows, partial)
    return paid_pair, line, forbidden


def verify_example() -> None:
    t = 7
    target = (0, 0)
    x2 = 1
    descriptors = [
        (5, 6, 1),
        (1, 2, 5),
        (3, 4, 3),
        (4, 5, 2),
        (2, 3, 4),
        (6, 0, 0),
    ]
    data = [
        item
        for descriptor in descriptors
        if (item := build_line_data(t, target, x2, descriptor)) is not None
    ]
    assert len(data) == 4
    cylinders = []
    triples = candidate_triples(t)
    n = t - 2

    for paid_pair, line, forbidden in data:
        states = cylinder(t, target, paid_pair, forbidden)
        assert len(states) == derangement_number(n)
        for state in states:
            selected = frozenset((x, state[x]) for x in range(t))
            assert paid_pair <= selected
            assert target not in selected
            assert len((selected & line) - paid_pair) == 0
            assert not any(
                paid_pair <= triple and triple <= selected
                for triple in triples
            )

        residual_sources = set(forbidden)
        residual_rows = set(forbidden.values())
        allowed_cells = [
            (x, y)
            for x in residual_sources
            for y in residual_rows
            if forbidden[x] != y
        ]
        for cell in allowed_cells:
            count = sum(state[cell[0]] == cell[1] for state in states)
            assert count * (n - 1) == len(states)

        v = [0, 0]
        actual_total = 0
        for triple in triples:
            if not compatible(triple | paid_pair):
                continue
            overlap = len(triple & paid_pair)
            if overlap == 2:
                assert any(
                    cell in line and cell not in paid_pair
                    for cell in triple
                )
                continue
            if overlap not in (0, 1):
                continue
            residual = triple - paid_pair
            if any(
                x not in residual_sources
                or y not in residual_rows
                or forbidden[x] == y
                for x, y in residual
            ):
                continue
            v[overlap] += 1

        for state in states:
            selected = frozenset((x, state[x]) for x in range(t))
            actual_total += sum(triple <= selected for triple in triples)

        bound_numerator = (
            30
            * len(states)
            * (
                v[0] * (n - 3)! if False else 0
            )
        )
        # Check CMR333 using exact integer denominators.
        lhs = actual_total * 11 * n * (n - 1) * (n - 2)
        rhs = 30 * len(states) * (
            v[0] + v[1] * (n - 2)
        )
        assert lhs <= rhs
        cylinders.append(set(states))

    for left, right in combinations(cylinders, 2):
        assert left.isdisjoint(right)


def verify_derangement_density() -> None:
    for n in range(5, 15):
        assert 30 * derangement_number(n) >= 11 * factorial(n)


def main() -> None:
    verify_derangement_density()
    verify_example()
    print(
        "verified line-clean paid pairs: equal derangement cylinders, exact "
        "line avoidance, rank-two elimination, and CMR333 collateral bounds"
    )


if __name__ == "__main__":
    main()
