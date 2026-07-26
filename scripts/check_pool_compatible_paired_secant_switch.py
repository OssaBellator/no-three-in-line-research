#!/usr/bin/env python3
"""Check pool-compatible paired secant switches and record pairing."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def adjacent(i: int, j: int, successor: dict[int, int]) -> bool:
    return bool({i, successor[i]} & {j, successor[j]})


def state_resources(cells: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    return sorted(x for x, _ in cells), sorted(y for _, y in cells)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())

    h = int(data["records"])
    step_a = int(data["tentative_cycle_step"])
    step_z = int(data["witness_cycle_step"])
    successor_a = {i: (i + step_a) % h for i in range(h)}
    successor_z = {i: (i + step_z) % h for i in range(h)}

    conflict = {i: set() for i in range(h)}
    for i, j in itertools.combinations(range(h), 2):
        if adjacent(i, j, successor_a) or adjacent(i, j, successor_z):
            conflict[i].add(j)
            conflict[j].add(i)

    unused = set(range(h))
    pairs: list[tuple[int, int]] = []
    while True:
        chosen = None
        for i in sorted(unused):
            for j in sorted(unused):
                if i < j and j not in conflict[i]:
                    chosen = (i, j)
                    break
            if chosen is not None:
                break
        if chosen is None:
            break
        pairs.append(chosen)
        unused.difference_update(chosen)

    assert len(unused) <= max(len(neighbours) for neighbours in conflict.values()) + 1

    i, j = pairs[0]
    a0 = [(i, successor_a[i]), (j, successor_a[j])]
    a1 = [(i, successor_a[j]), (j, successor_a[i])]
    z0 = [(i, successor_z[i]), (j, successor_z[j])]
    z1 = [(i, successor_z[j]), (j, successor_z[i])]

    assert state_resources(a0) == state_resources(a1)
    assert state_resources(z0) == state_resources(z1)
    assert all(x != y for x, y in a1)
    assert all(x != y for x, y in z1)
    assert not set(a0) & set(a1)
    assert not set(z0) & set(z1)

    print("secant records", h)
    print("tentative cycle step", step_a)
    print("witness cycle step", step_z)
    print("conflict maximum degree", max(len(v) for v in conflict.values()))
    print("paired switches", len(pairs))
    print("unpaired records", sorted(unused))
    print("record pairs", [list(pair) for pair in pairs])
    print("sample tentative diagonal", [list(cell) for cell in a0])
    print("sample tentative cross", [list(cell) for cell in a1])
    print("sample witness diagonal", [list(cell) for cell in z0])
    print("sample witness cross", [list(cell) for cell in z1])
    print("tentative resources preserved", state_resources(a0) == state_resources(a1))
    print("witness resources preserved", state_resources(z0) == state_resources(z1))
    print("all four pivots omitted", not set(a0) & set(a1) and not set(z0) & set(z1))
    print("outcome pool_compatible_paired_secant_switch")


if __name__ == "__main__":
    main()
