#!/usr/bin/env python3
"""Finite regression for nested controller-shadow potentials."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Set, Tuple

Point = str
Pair = FrozenSet[Point]


def load(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def pair(a: Point, b: Point) -> Pair:
    return frozenset((a, b))


def potential(source: Set[Point], entries: List[dict]) -> int:
    total = 0
    for entry in entries:
        controller = pair(*entry["controller"])
        for a, b in entry["blocked_pairs"]:
            blocker = pair(a, b)
            if blocker.issubset(source) and blocker != controller:
                total += 1
    return total


def active_entries(all_entries: List[dict], punctured: Set[Point]) -> List[dict]:
    return [
        entry
        for entry in all_entries
        if not pair(*entry["controller"]).intersection(punctured)
    ]


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_nested_puncture_potential.py example.json")
    data = load(sys.argv[1])
    entries = data["entries"]
    source = set(data["initial_source"])
    punctured: Set[Point] = set()

    values: List[int] = [potential(source, active_entries(entries, punctured))]
    universe_sizes: List[int] = [len(active_entries(entries, punctured))]

    for stage in data["stages"]:
        centre = stage["puncture"]
        punctured.add(centre)
        before_trade = potential(source, active_entries(entries, punctured))
        for deleted in stage["delete"]:
            source.remove(deleted)
        source.update(stage["insert"])
        after_trade = potential(source, active_entries(entries, punctured))
        claimed_drop = int(stage["minimum_drop"])
        if after_trade > before_trade - claimed_drop:
            raise AssertionError(
                f"stage {centre}: after={after_trade}, before={before_trade}, "
                f"required drop={claimed_drop}"
            )
        values.append(after_trade)
        universe_sizes.append(len(active_entries(entries, punctured)))

    if any(values[i + 1] >= values[i] for i in range(len(values) - 1)):
        raise AssertionError(f"nested potentials are not strictly decreasing: {values}")
    if any(
        universe_sizes[i + 1] > universe_sizes[i]
        for i in range(len(universe_sizes) - 1)
    ):
        raise AssertionError(f"candidate universes are not nested: {universe_sizes}")

    print("initial candidate entries", universe_sizes[0])
    print("nested candidate entries", universe_sizes)
    print("nested potentials", values)
    print("strict drops", [values[i] - values[i + 1] for i in range(len(values) - 1)])
    print("outcome nested_puncture_paid_termination")


if __name__ == "__main__":
    main()
