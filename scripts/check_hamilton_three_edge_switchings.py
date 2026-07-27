#!/usr/bin/env python3
"""Exhaustively audit three-edge rotations on directed Hamilton cycles."""
from __future__ import annotations

import argparse
import json
import math
from collections import deque
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

Cycle = tuple[int, ...]


def successor_map(order: Cycle) -> dict[int, int]:
    return {order[i]: order[(i + 1) % len(order)] for i in range(len(order))}


def canonical_order(successor: dict[int, int]) -> Cycle | None:
    start = min(successor)
    order = [start]
    current = successor[start]
    seen = {start}
    while current not in seen:
        seen.add(current)
        order.append(current)
        current = successor[current]
    if current != start or len(order) != len(successor):
        return None
    return tuple(order)


def three_edge_rotation(order: Cycle, sources: tuple[int, int, int]) -> Cycle:
    successor = successor_map(order)
    position = {vertex: i for i, vertex in enumerate(order)}
    cyclic_sources = sorted(sources, key=position.__getitem__)
    targets = [successor[source] for source in cyclic_sources]
    rotated = dict(successor)
    for i, source in enumerate(cyclic_sources):
        rotated[source] = targets[(i + 1) % 3]
    result = canonical_order(rotated)
    if result is None:
        raise ValueError("three-edge rotation did not produce one Hamilton cycle")
    changed = {vertex for vertex in successor if successor[vertex] != rotated[vertex]}
    if changed != set(sources):
        raise ValueError("three-edge rotation changed the wrong source set")
    if any(rotated[source] == successor[source] for source in sources):
        raise ValueError("a selected assignment survived the rotation")
    return result


def audit_length(length: int) -> dict[str, Any]:
    vertices = tuple(range(length))
    cycles = [(0,) + tail for tail in permutations(range(1, length))]
    adjacency: dict[Cycle, set[Cycle]] = {}
    inverse_checks = 0

    for cycle in cycles:
        neighbours: set[Cycle] = set()
        for sources in combinations(vertices, 3):
            moved = three_edge_rotation(cycle, sources)
            restored = three_edge_rotation(moved, sources)
            inverse_checks += 1
            if restored != cycle:
                raise ValueError(
                    f"switch is not involutive at length={length}, sources={sources}"
                )
            neighbours.add(moved)
        expected_degree = math.comb(length, 3)
        if len(neighbours) != expected_degree:
            raise ValueError(
                f"degree mismatch at length={length}: {len(neighbours)} != {expected_degree}"
            )
        adjacency[cycle] = neighbours

    start = cycles[0]
    seen = {start}
    queue = deque([start])
    while queue:
        cycle = queue.popleft()
        for neighbour in adjacency[cycle]:
            if cycle not in adjacency[neighbour]:
                raise ValueError("switching graph is not symmetric")
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)
    if len(seen) != len(cycles):
        raise ValueError(
            f"switching graph disconnected at length={length}: {len(seen)}/{len(cycles)}"
        )

    return {
        "cycle_length": length,
        "unsigned_states": len(cycles),
        "unsigned_degree": math.comb(length, 3),
        "signed_degree": 8 * math.comb(length, 3),
        "directed_unsigned_moves": sum(len(v) for v in adjacency.values()),
        "inverse_checks": inverse_checks,
        "connected": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()

    try:
        raw = json.loads(args.audit.read_text())
        if not isinstance(raw, dict):
            raise ValueError("audit object expected")
        minimum = raw.get("minimum_cycle_length")
        maximum = raw.get("maximum_cycle_length")
        if any(isinstance(v, bool) or not isinstance(v, int) for v in (minimum, maximum)):
            raise ValueError("cycle limits must be integers")
        if minimum < 4 or maximum < minimum:
            raise ValueError("expected 4 <= minimum <= maximum")
        cases = [audit_length(length) for length in range(minimum, maximum + 1)]
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(
        json.dumps(
            {
                "outcome": "hamilton_three_edge_switchings_verified",
                "minimum_cycle_length": minimum,
                "maximum_cycle_length": maximum,
                "cases": cases,
                "total_unsigned_states": sum(c["unsigned_states"] for c in cases),
                "total_directed_unsigned_moves": sum(
                    c["directed_unsigned_moves"] for c in cases
                ),
                "all_switching_graphs_connected": all(c["connected"] for c in cases),
                "asymptotic_seed_theorem_proved": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
