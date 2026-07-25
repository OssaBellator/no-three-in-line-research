#!/usr/bin/env python3
"""Exact checks for CMR335--CMR339."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, gcd

Cell = tuple[int, int]


def primitive_height(cells: tuple[Cell, Cell, Cell]) -> int:
    first, second, _ = cells
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    common = gcd(abs(dx), abs(dy))
    return max(abs(dx) // common, abs(dy) // common)


def collinear(cells: tuple[Cell, Cell, Cell]) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = cells
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def compatible(cells) -> bool:
    cells = tuple(cells)
    return len({x for x, _ in cells}) == len(cells) and len(
        {y for _, y in cells}
    ) == len(cells)


def candidate_triples(t: int, height: int) -> list[frozenset[Cell]]:
    points = [(x, y) for x in range(t) for y in range(t)]
    result = []
    for cells in combinations(points, 3):
        if not compatible(cells) or not collinear(cells):
            continue
        ordered = tuple(sorted(cells))
        if primitive_height(ordered) >= height:
            result.append(frozenset(cells))
    return result


def sum_first(left: int, right: int) -> int:
    if left > right:
        return 0
    return (left + right) * (right - left + 1) // 2


def sum_second(left: int, right: int) -> int:
    if left > right:
        return 0

    def prefix(value: int) -> int:
        return value * (value + 1) * (2 * value + 1) // 6

    return prefix(right) - prefix(left - 1)


def discrete_mod_six_bound(t: int) -> Fraction:
    height = ceil(Fraction(21 * t, 50))
    top = (t - 1) // 2
    count = max(0, top - height + 1)
    first = sum_first(height, top)
    second = sum_second(height, top)
    s_value = t * first - second
    r_value = count * t - 2 * first
    return (
        Fraction(4, 3) * s_value
        + Fraction(20, 9) * t * t
        + 2 * (t - 1) * r_value
    )


def verify_load_arithmetic() -> None:
    for t in range(1677, 20_002, 2):
        n = t - 2
        high = discrete_mod_six_bound(t)
        load = (
            Fraction(1, n)
            + Fraction(2, n * (n - 1))
            + high / (n * (n - 1) * (n - 2))
        )
        assert load < Fraction(1, 24)

        if t >= 2847:
            protected = t // 1000
            reserve_load = (
                Fraction(protected + 1, n)
                + Fraction(2, n * (n - 1))
                + high / (n * (n - 1) * (n - 2))
            )
            assert reserve_load < Fraction(1, 24)


def threshold_polynomial(t: int) -> int:
    return 2731 * t**3 - 4579975 * t**2 + 5516250 * t - 3875000


def reserve_polynomial(t: int) -> int:
    return 803 * t**3 - 2286050 * t**2 + 2751375 * t - 1937500


def verify_polynomial_margins() -> None:
    assert threshold_polynomial(1675) < 0
    assert threshold_polynomial(1677) > 0
    assert 8193 * 1677**2 - 9159950 * 1677 + 5516250 > 0
    assert 16386 * 1677 - 9159950 > 0

    assert reserve_polynomial(2845) < 0
    assert reserve_polynomial(2847) > 0
    assert 2409 * 2847**2 - 4572100 * 2847 + 2751375 > 0
    assert 4818 * 2847 - 4572100 > 0


def full_line_cells(t: int, first: Cell, second: Cell) -> frozenset[Cell]:
    x1, y1 = first
    x2, y2 = second
    return frozenset(
        (x, y)
        for x in range(t)
        for y in range(t)
        if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1)
    )


def verify_small_exact_completion() -> None:
    t = 7
    target = (0, 0)
    height = ceil(Fraction(21 * t, 50))
    high_triples = candidate_triples(t, height)
    descriptors = [(1, 2, 5), (3, 4, 3), (4, 5, 2), (2, 3, 4)]

    for a, b, c in descriptors:
        paid_pair = frozenset(((0, a), (1, b)))
        line = full_line_cells(t, (0, a), (1, b))
        assert (c, 6) in line
        residual_sources = [x for x in range(t) if x not in (0, 1)]
        residual_rows = [y for y in range(t) if y not in (a, b)]
        partial = {
            x: y
            for x, y in line
            if x in residual_sources and y in residual_rows
        }
        free_sources = [x for x in residual_sources if x not in partial]
        free_rows = [y for y in residual_rows if y not in partial.values()]
        forbidden = dict(partial)
        forbidden.update(zip(free_sources, free_rows))

        found = False
        for state in permutations(range(t)):
            selected = frozenset((x, state[x]) for x in range(t))
            if target in selected or not paid_pair <= selected:
                continue
            if any(state[x] == y for x, y in forbidden.items()):
                continue
            if any(triple <= selected for triple in high_triples):
                continue
            assert len((selected & line) - paid_pair) == 0
            found = True
            break
        assert found


def main() -> None:
    verify_polynomial_margins()
    verify_load_arithmetic()
    verify_small_exact_completion()
    print(
        "verified line-clean high-slice completion: residual loads, exact "
        "thresholds, protected-line reserve, and t=7 completion certificates"
    )


if __name__ == "__main__":
    main()
