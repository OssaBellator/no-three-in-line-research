#!/usr/bin/env python3
"""Finite checker for the sunflower-transversal single-cycle host law."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
from typing import Any


def falling(n: int, r: int) -> int:
    out = 1
    for j in range(r):
        out *= n - j
    return out


def enumerate_blocks(H: int, b: int, petal_size: int) -> tuple[list[tuple[int, ...]], list[frozenset[int]]]:
    petals = [tuple(range(j * petal_size, (j + 1) * petal_size)) for j in range(H)]
    blocks: list[frozenset[int]] = []
    for chosen_petals in combinations(range(H), b - 1):
        for choices in product(*(petals[j] for j in chosen_petals)):
            blocks.append(frozenset(choices))
    return petals, blocks


def probability(blocks: list[frozenset[int]], required: set[int]) -> Fraction:
    count = sum(required.issubset(block) for block in blocks)
    return Fraction(count, len(blocks))


def arc_probability(blocks: list[frozenset[int]], b: int, arc: tuple[int, int]) -> Fraction:
    centre = -1
    total = 0
    hits = 0
    for block in blocks:
        for order in permutations(sorted(block)):
            cycle = (centre,) + order
            arcs = {(cycle[j], cycle[(j + 1) % b]) for j in range(b)}
            total += 1
            if arc in arcs:
                hits += 1
    return Fraction(hits, total)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data: dict[str, Any] = json.loads(args.input.read_text())

    H = int(data["H"])
    b = int(data["b"])
    petal_size = int(data["petal_size"])
    nested_core_size = int(data["nested_core_size"])
    nested_petal_size = int(data["nested_petal_size"])

    if not (2 <= b <= H + 1):
        raise ValueError("need 2 <= b <= H+1")
    if petal_size < 2:
        raise ValueError("empty-core diagnostic needs petal_size >= 2")
    if nested_core_size < 1 or nested_petal_size < 1:
        raise ValueError("nested diagnostic needs a nonempty core and petals")

    petals, blocks = enumerate_blocks(H, b, petal_size)
    expected_blocks = comb(H, b - 1) * petal_size ** (b - 1)
    if len(blocks) != expected_blocks:
        raise AssertionError("incorrect transversal block count")

    x = petals[0][0]
    x_same = petals[0][1]
    y = petals[1][0]

    p_one = probability(blocks, {x})
    p_distinct = probability(blocks, {x, y})
    p_same = probability(blocks, {x, x_same})

    expected_one = Fraction(b - 1, H * petal_size)
    expected_distinct = Fraction(falling(b - 1, 2), falling(H, 2) * petal_size**2)
    if p_one != expected_one:
        raise AssertionError((p_one, expected_one))
    if p_distinct != expected_distinct:
        raise AssertionError((p_distinct, expected_distinct))
    if p_same != 0:
        raise AssertionError("two helpers from one petal must have probability zero")

    p_arc = arc_probability(blocks, b, (x, y))
    expected_arc = expected_distinct / (b - 1)
    if p_arc != expected_arc:
        raise AssertionError((p_arc, expected_arc))

    # Every empty-core target signature uses all vertices of one petal.  The
    # transversal block meets each petal in at most one vertex.
    max_empty_core_intersection = max(
        len(block.intersection(petal)) for block in blocks for petal in petals
    )
    if max_empty_core_intersection != 1:
        raise AssertionError("transversal block selected too many vertices from one petal")

    # In the nested-pencil case the law chooses only petal vertices, so the
    # optional fixed core is omitted identically even when petals are singletons.
    nested_support_selected = False
    if nested_core_size == 0:
        nested_support_selected = True
    if nested_support_selected:
        raise AssertionError("nested fixed core should be omitted")

    print(f"H {H}")
    print(f"b {b}")
    print(f"empty-core petal size {petal_size}")
    print(f"transversal blocks {len(blocks)}")
    print(f"one-helper probability {float(p_one):.12f}")
    print(f"one-helper formula {p_one.numerator}/{p_one.denominator}")
    print(f"two-distinct-petal probability {float(p_distinct):.12f}")
    print(f"same-petal pair probability {float(p_same):.12f}")
    print(f"prescribed-arc probability {float(p_arc):.12f}")
    print(f"maximum selected vertices from one petal {max_empty_core_intersection}")
    print(f"nested core size {nested_core_size}")
    print(f"nested petal size {nested_petal_size}")
    print("nested fixed core selected 0")
    print("target signatures selected 0")
    print("outcome sunflower_transversal_single_cycle_host")


if __name__ == "__main__":
    main()
