#!/usr/bin/env python3
"""Exhaustively count small saturated seeds and boundary-only one-strip moves."""
from __future__ import annotations

import argparse
import json
from itertools import combinations, permutations
from pathlib import Path

Point = tuple[int, int]
State = tuple[Point, ...]


def det(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(state: State) -> bool:
    return all(det(a, b, c) != 0 for a, b, c in combinations(state, 3))


def saturated_states(n: int) -> set[State]:
    perms = tuple(permutations(range(1, n + 1)))
    states: set[State] = set()
    for i, first in enumerate(perms):
        for second in perms[i + 1 :]:
            if any(first[j] == second[j] for j in range(n)):
                continue
            states.add(tuple(sorted(
                [(j + 1, first[j]) for j in range(n)]
                + [(j + 1, second[j]) for j in range(n)]
            )))
    return states


def extensions(state: State, n: int) -> set[State]:
    q = n + 1
    out: set[State] = set()
    for x, y in state:
        kept = tuple(p for p in state if p != (x, y))
        candidate = tuple(sorted(kept + ((x, q), (q, y), (q, q))))
        if no_three(candidate):
            out.add(candidate)
    for first, second in combinations(state, 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        kept = tuple(p for p in state if p not in (first, second))
        added = ((first[0], q), (second[0], q), (q, first[1]), (q, second[1]))
        candidate = tuple(sorted(kept + added))
        if no_three(candidate):
            out.add(candidate)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not 2 <= args.max_n <= 6:
        raise SystemExit("max-n must lie between 2 and 6")

    good_by_n: dict[int, set[State]] = {}
    summary = []
    for n in range(2, args.max_n + 1):
        states = saturated_states(n)
        good = {state for state in states if no_three(state)}
        good_by_n[n] = good
        targets_by_source = {state: extensions(state, n) for state in good}
        targets = set().union(*targets_by_source.values()) if targets_by_source else set()
        summary.append({
            "n": n,
            "saturated_states": len(states),
            "no_three_states": len(good),
            "one_strip_extendable_states": sum(bool(v) for v in targets_by_source.values()),
            "directed_extensions": sum(len(v) for v in targets_by_source.values()),
            "distinct_targets": len(targets),
        })

    reachable = set(good_by_n[2])
    reachability = [{"n": 2, "reachable_states": len(reachable)}]
    for n in range(2, args.max_n + 1):
        reachable = set().union(*(extensions(state, n) for state in reachable)) if reachable else set()
        reachability.append({"n": n + 1, "reachable_states": len(reachable)})

    payload = {
        "max_n": args.max_n,
        "summary": summary,
        "recursive_reachability_from_n2": reachability,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
