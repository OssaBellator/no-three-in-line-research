#!/usr/bin/env python3
"""Verify pool-compatible paired secant switches on a finite model."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

Cell = tuple[int, int]


def cell_set(raw: Iterable[Iterable[int]]) -> set[Cell]:
    return {tuple(map(int, cell)) for cell in raw}


def margins(cells: set[Cell]) -> tuple[list[int], list[int]]:
    return sorted(x for x, _ in cells), sorted(y for _, y in cells)


def is_matching(cells: set[Cell]) -> bool:
    xs, ys = zip(*cells)
    return len(xs) == len(set(xs)) and len(ys) == len(set(ys))


def main(path: str) -> None:
    data = json.loads(Path(path).read_text())

    a0 = cell_set(data["tentative_diagonal"])
    a1 = cell_set(data["tentative_cross"])
    z0 = cell_set(data["witness_diagonal"])
    z1 = cell_set(data["witness_cross"])
    pivots = a0 | z0

    assert len(a0) == len(a1) == len(z0) == len(z1) == 2
    assert is_matching(a0) and is_matching(a1)
    assert is_matching(z0) and is_matching(z1)
    assert margins(a0) == margins(a1)
    assert margins(z0) == margins(z1)

    states: list[set[Cell]] = []
    for a_state in (a0, a1):
        for z_state in (z0, z1):
            state = a_state | z_state
            assert is_matching(state)
            assert margins(a_state) == margins(a0)
            assert margins(z_state) == margins(z0)
            states.append(state)

    all_cross = a1 | z1
    assert all_cross.isdisjoint(pivots)

    print("tentative block margins", list(map(list, margins(a0))))
    print("witness block margins", list(map(list, margins(z0))))
    print("four product states", len(states))
    print("all-cross state", [list(cell) for cell in sorted(all_cross)])
    print("designated pivots omitted", len(pivots))
    print("permanent blocks preserved", True)
    print("outcome paired_secant_block_preservation")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} EXAMPLE.json")
    main(sys.argv[1])
