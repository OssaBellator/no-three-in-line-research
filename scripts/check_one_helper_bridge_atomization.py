#!/usr/bin/env python3
"""Finite checker for path atom counts and one-helper bridge localization."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial, ceil
from pathlib import Path
from typing import Any


def path_atoms(r: int) -> tuple[int, int, int, int]:
    unary = r
    rank3 = r - 1
    rank4 = comb(r, 2) - (r - 1)
    return unary, rank3, rank4, unary + rank3 + rank4


def conditioned_cycles(vertices: list[int], fixed_arcs: set[tuple[int, int]]) -> int:
    root = min(vertices)
    count = 0
    for order in permutations(v for v in vertices if v != root):
        cyc = (root,) + order
        arcs = {(cyc[j], cyc[(j + 1) % len(cyc)]) for j in range(len(cyc))}
        if fixed_arcs.issubset(arcs):
            count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data: dict[str, Any] = json.loads(args.input.read_text())

    expected_totals = [1, 3, 6, 10]
    totals = []
    for r in range(1, 5):
        unary, rank3, rank4, total = path_atoms(r)
        totals.append(total)
        if total != expected_totals[r - 1]:
            raise AssertionError("path atom count mismatch")
        print(f"path length {r} A2 atoms {unary} B3 atoms {rank3} B4 atoms {rank4} total {total}")

    q = int(data["cycle_size"])
    extra = int(data["extra_filler"])
    x = int(data["bridge_helper"])
    vertices = [0, 1, x, 2, 3, extra]
    fixed = {(0, 1), (1, x), (x, 2), (2, 3)}
    cycle_count = conditioned_cycles(vertices, fixed)
    formula_count = factorial(q - 5)
    if cycle_count != formula_count:
        raise AssertionError((cycle_count, formula_count))

    credit = int(data["removal_credit"])
    helpers = list(map(int, data["heavy_helpers"]))
    records = [
        (helper, data["heavy_orientation"], data["heavy_atom_role"], int(data["heavy_atom_weight"]))
        for helper in helpers
    ]
    if any(weight < credit / 10 for _, _, _, weight in records):
        raise AssertionError("stored atom is below credit/10")
    classes = Counter((orientation, role) for _, orientation, role, _ in records)
    exact_class = max(classes.values())
    theorem_class = ceil(len(records) / 20)
    if exact_class < theorem_class:
        raise AssertionError("pigeonhole class below theorem bound")

    print(f"bridge cycle size {q}")
    print(f"bridge fixed path arcs {len(fixed)}")
    print(f"bridge conditional cycles {cycle_count}")
    print(f"bridge formula count {formula_count}")
    print(f"bridge local atoms {totals[-1]}")
    print(f"removal credit {credit}")
    print(f"credit per ten atoms {credit/10:.6f}")
    print(f"heavy bridge helpers {len(records)}")
    print(f"exact fixed-role subfamily {exact_class}")
    print(f"theorem fixed-role lower bound {theorem_class}")
    print(f"heavy role {data['heavy_atom_role']}")
    print(f"heavy atom weight {data['heavy_atom_weight']}")
    print("outcome one_helper_bridge_credit_scale_pencil")


if __name__ == "__main__":
    main()
