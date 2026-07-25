#!/usr/bin/env python3
"""Exact finite checker for single-cycle endpoint state cylinders.

The input JSON has the form

{
  "n": 6,
  "cases": [
    {"name": "one arc", "arcs": [[0, 1]]},
    ...
  ]
}

For every compatible arc set, the checker enumerates all directed n-cycles,
counts the states containing the arcs, and compares with the exact formula:
zero when the prescribed arcs contain a proper directed cycle, and
(n-r-1)! otherwise.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Iterable, Sequence

Arc = tuple[int, int]
Permutation = tuple[int, ...]


def is_single_cycle(pi: Permutation) -> bool:
    n = len(pi)
    seen: set[int] = set()
    current = 0
    for _ in range(n):
        if current in seen:
            return False
        seen.add(current)
        current = pi[current]
    return current == 0 and len(seen) == n


def validate_arcs(arcs: Sequence[Arc], n: int) -> None:
    tails: set[int] = set()
    heads: set[int] = set()
    for tail, head in arcs:
        if not (0 <= tail < n and 0 <= head < n):
            raise ValueError(f"arc {(tail, head)} is outside [0,{n})")
        if tail in tails:
            raise ValueError(f"duplicate tail {tail}")
        if head in heads:
            raise ValueError(f"duplicate head {head}")
        tails.add(tail)
        heads.add(head)


def contains_proper_directed_cycle(arcs: Sequence[Arc], n: int) -> bool:
    successor = {tail: head for tail, head in arcs}
    for start in successor:
        current = start
        path_position: dict[int, int] = {}
        step = 0
        while current in successor:
            if current in path_position:
                cycle_length = step - path_position[current]
                return cycle_length < n
            path_position[current] = step
            step += 1
            current = successor[current]
    return False


def contains_arcs(pi: Permutation, arcs: Iterable[Arc]) -> bool:
    return all(pi[tail] == head for tail, head in arcs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args()

    data = json.loads(args.fixture.read_text(encoding="utf-8"))
    n = int(data["n"])
    if n < 4:
        raise ValueError("n must be at least 4")

    cycles = [pi for pi in itertools.permutations(range(n)) if is_single_cycle(pi)]
    expected_total = math.factorial(n - 1)
    if len(cycles) != expected_total:
        raise AssertionError((len(cycles), expected_total))

    for pi in cycles:
        if any(pi[i] == i for i in range(n)):
            raise AssertionError("single cycle has a fixed point")
        if any(pi[pi[i]] == i for i in range(n)):
            raise AssertionError("single cycle has a transposition")

    results: list[dict[str, object]] = []
    for case in data["cases"]:
        name = str(case["name"])
        arcs = [tuple(map(int, arc)) for arc in case["arcs"]]
        validate_arcs(arcs, n)
        r = len(arcs)
        proper_cycle = contains_proper_directed_cycle(arcs, n)
        expected = 0 if proper_cycle else math.factorial(n - r - 1)
        actual = sum(1 for pi in cycles if contains_arcs(pi, arcs))
        if actual != expected:
            raise AssertionError(
                f"{name}: actual {actual}, expected {expected}, arcs={arcs}"
            )
        results.append(
            {
                "name": name,
                "rank": r,
                "proper_directed_cycle": proper_cycle,
                "actual_count": actual,
                "expected_count": expected,
            }
        )

    output = {
        "n": n,
        "single_cycle_count": len(cycles),
        "expected_single_cycle_count": expected_total,
        "all_states_have_no_fixed_points": True,
        "all_states_have_no_transpositions": True,
        "cases": results,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
