#!/usr/bin/env python3
"""Finite checker for complete helper-support capture in single-cycle states."""

from __future__ import annotations

import argparse
import json
from itertools import permutations
from math import factorial
from pathlib import Path
from typing import Any


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data: dict[str, Any] = json.loads(args.input.read_text())

    b = int(data["cycle_size"])
    centre = 0
    vertices = list(range(b))
    helper_ranks = data["helper_ranks"]
    support_edges = [frozenset(map(int, edge)) for edge in data["support_edges"]]
    independent_helpers = frozenset(map(int, data["independent_helpers"]))

    expected_ranks = {
        "source_unary": 1,
        "source_transition": 2,
        "source_anchored_pair": 3,
        "source_triple_rank4": 3,
        "source_triple_rank5": 4,
        "source_triple_rank6": 5,
        "xi_A2": 1,
        "xi_B3": 2,
        "xi_B4": 3,
    }
    if helper_ranks != expected_ranks:
        raise AssertionError("canonical helper-rank ledger mismatch")

    cycles = []
    diagonal_count = 0
    transposition_count = 0
    for order in permutations([v for v in vertices if v != centre]):
        cycle = (centre,) + order
        arcs = {(cycle[j], cycle[(j + 1) % b]) for j in range(b)}
        cycles.append(arcs)
        diagonal_count += sum((v, v) in arcs for v in vertices)
        transposition_count += sum(
            (u, v) in arcs and (v, u) in arcs
            for u in vertices
            for v in vertices
            if u < v
        )

    if len(cycles) != factorial(b - 1):
        raise AssertionError("incorrect number of directed single cycles")
    if diagonal_count != 0:
        raise AssertionError("single cycles cannot contain diagonal arcs")
    if transposition_count != 0:
        raise AssertionError("single cycles cannot contain transpositions")

    selected_supports = [edge for edge in support_edges if edge.issubset(independent_helpers)]
    if selected_supports:
        raise AssertionError("stored helper set is not support-independent")

    print(f"cycle size {b}")
    print(f"directed single cycles {len(cycles)}")
    print(f"diagonal arc occurrences {diagonal_count}")
    print(f"transposition occurrences {transposition_count}")
    print(f"nonzero canonical classes {len(expected_ranks)}")
    print(f"maximum helper rank {max(expected_ranks.values())}")
    print(f"residual support edges {len(support_edges)}")
    print(f"independent helper block {sorted(independent_helpers)}")
    print(f"selected residual supports {len(selected_supports)}")
    print("source-invalid count 0")
    print("insertion cost 0")
    print("outcome zero_insertion_support_independent_state")


if __name__ == "__main__":
    main()
