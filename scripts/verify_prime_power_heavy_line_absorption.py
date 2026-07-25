#!/usr/bin/env python3
"""Verify CMR605--CMR610 protected heavy-line absorption."""

from itertools import combinations
from math import comb, gcd


Cell = tuple[int, int]
Line = tuple[int, int, int]


def line_key(a: Cell, b: Cell) -> Line:
    x1, y1 = a
    x2, y2 = b
    aa = y2 - y1
    bb = x1 - x2
    cc = -(aa * x1 + bb * y1)
    divisor = gcd(gcd(abs(aa), abs(bb)), abs(cc))
    if divisor:
        aa //= divisor
        bb //= divisor
        cc //= divisor
    if aa < 0 or (aa == 0 and bb < 0):
        aa, bb, cc = -aa, -bb, -cc
    return aa, bb, cc


def on_line(line: Line, cell: Cell) -> bool:
    aa, bb, cc = line
    x, y = cell
    return aa * x + bb * y + cc == 0


def is_nonaxis(line: Line) -> bool:
    aa, bb, _ = line
    return aa != 0 and bb != 0


def is_matching(cells: set[Cell]) -> bool:
    return (
        len({x for x, _ in cells}) == len(cells)
        and len({y for _, y in cells}) == len(cells)
    )


def rho(rank: int, atoms: int) -> int:
    size = rank
    while comb(size, rank) < atoms:
        size += 1
    return size


def check_board(n: int) -> int:
    cells = [(x, y) for x in range(n) for y in range(n)]
    lines: dict[Line, set[Cell]] = {}
    for a, b in combinations(cells, 2):
        line = line_key(a, b)
        if not is_nonaxis(line):
            continue
        lines.setdefault(line, {cell for cell in cells if on_line(line, cell)})

    checked = 0
    for line_cells in lines.values():
        assert is_matching(line_cells)
        for protected_size in range(n + 1):
            protected = {(i, i) for i in range(protected_size)}
            protected_left = {x for x, _ in protected}
            protected_right = {y for _, y in protected}

            touching = {
                cell
                for cell in line_cells
                if cell[0] in protected_left or cell[1] in protected_right
            }
            free = line_cells - touching

            assert len(touching) <= 2 * protected_size
            assert len(free) >= max(0, len(line_cells) - 2 * protected_size)
            assert is_matching(free)
            assert all(
                x not in protected_left and y not in protected_right
                for x, y in free
            )
            assert is_matching(protected | free)

            rank0_cap = comb(len(touching), 3) if len(touching) >= 3 else 0
            rank1_cap = comb(len(touching), 2) if len(touching) >= 2 else 0
            assert rank0_cap <= (
                comb(2 * protected_size, 3)
                if 2 * protected_size >= 3
                else 0
            )
            assert rank1_cap <= (
                comb(2 * protected_size, 2)
                if 2 * protected_size >= 2
                else 0
            )
            checked += 1
    return checked


def check_thresholds() -> None:
    for atoms in range(1, 500):
        r2 = rho(2, atoms)
        r3 = rho(3, atoms)
        assert comb(r2, 2) >= atoms
        assert r2 == 2 or comb(r2 - 1, 2) < atoms
        assert comb(r3, 3) >= atoms
        assert r3 == 3 or comb(r3 - 1, 3) < atoms

        for protected_size in range(0, 30):
            growth2 = max(0, r2 - 2 * protected_size)
            growth3 = max(0, r3 - 2 * protected_size)
            if growth2 == 0:
                assert protected_size >= r2 / 2
            if growth3 == 0:
                assert protected_size >= r3 / 2


def check_growth_budget() -> None:
    for n in range(1, 100):
        for initial in range(n + 1):
            budget = n - initial
            for minimum_growth in range(1, n + 1):
                count = budget // minimum_growth
                assert count * minimum_growth <= budget
                assert (count + 1) * minimum_growth > budget


def main() -> None:
    checked = sum(check_board(n) for n in range(3, 8))
    check_thresholds()
    check_growth_budget()
    print(
        "verified heavy-line protected absorption for "
        f"{checked} line/core configurations through side seven"
    )


if __name__ == "__main__":
    main()
