#!/usr/bin/env python3
"""Check automatic layer assignment after a saturation-preserving cross-wired trade."""

from __future__ import annotations

import json
import sys
from collections import defaultdict, deque
from pathlib import Path

Edge = tuple[int, int]
Vertex = tuple[str, int]


def load_edges(raw: list[list[int]]) -> set[Edge]:
    return {(int(x), int(y)) for x, y in raw}


def alternating_decomposition(m: int, edges: set[Edge]) -> tuple[set[Edge], set[Edge]]:
    incidence: dict[Vertex, list[Edge]] = defaultdict(list)
    for edge in edges:
        x, y = edge
        incidence[("c", x)].append(edge)
        incidence[("r", y)].append(edge)

    for i in range(m):
        if len(incidence[("c", i)]) != 2 or len(incidence[("r", i)]) != 2:
            raise AssertionError("post-trade source is not two-regular")

    colour: dict[Edge, int] = {}
    for start in sorted(edges):
        if start in colour:
            continue
        colour[start] = 0
        queue: deque[Edge] = deque([start])
        while queue:
            edge = queue.popleft()
            x, y = edge
            for vertex in (("c", x), ("r", y)):
                for other in incidence[vertex]:
                    if other == edge:
                        continue
                    expected = 1 - colour[edge]
                    if other in colour:
                        if colour[other] != expected:
                            raise AssertionError("alternating edge-colouring is inconsistent")
                    else:
                        colour[other] = expected
                        queue.append(other)

    layers = tuple({edge for edge, value in colour.items() if value == a} for a in (0, 1))
    for layer in layers:
        if len(layer) != m:
            raise AssertionError("a post-trade colour class is not a perfect matching")
        if {x for x, _ in layer} != set(range(m)) or {y for _, y in layer} != set(range(m)):
            raise AssertionError("a post-trade colour class misses a row or column")
    return layers[0], layers[1]


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} EXAMPLE.json")

    data = json.loads(Path(sys.argv[1]).read_text())
    m = int(data["m"])
    shift = int(data["shift"])
    deleted = load_edges(data["deleted_edges"])
    inserted = load_edges(data["inserted_edges"])

    old_layer_0 = {(i, i) for i in range(m)}
    old_layer_1 = {(i, (i + shift) % m) for i in range(m)}
    old_source = old_layer_0 | old_layer_1

    if not deleted <= old_source:
        raise AssertionError("deleted edge is absent from the old source")
    if inserted & (old_source - deleted):
        raise AssertionError("inserted edge duplicates a retained source edge")

    post_source = (old_source - deleted) | inserted
    if len(post_source) != 2 * m:
        raise AssertionError("trade does not preserve source cardinality")

    column_origin: dict[int, int] = {}
    row_origin: dict[int, int] = {}
    for edge in deleted:
        layer = 0 if edge in old_layer_0 else 1
        x, y = edge
        column_origin[x] = layer
        row_origin[y] = layer

    cross_origin = sum(column_origin[x] != row_origin[y] for x, y in inserted)
    if cross_origin != len(inserted):
        raise AssertionError("stored example is not fully cross-origin")

    post_layer_0, post_layer_1 = alternating_decomposition(m, post_source)
    assigned = [len(inserted & post_layer_0), len(inserted & post_layer_1)]
    if sum(assigned) != len(inserted):
        raise AssertionError("not every inserted edge received a post-trade layer")

    square_demand = sum(size * size for size in assigned)
    global_square = len(inserted) ** 2
    if square_demand > global_square:
        raise AssertionError("layerwise square demand exceeds the global square budget")

    print("m", m)
    print("old layer sizes", [len(old_layer_0), len(old_layer_1)])
    print("deleted edges", len(deleted))
    print("inserted edges", len(inserted))
    print("cross-origin inserted edges", cross_origin)
    print("post-trade layer sizes", [len(post_layer_0), len(post_layer_1)])
    print("inserted post-trade layer blocks", assigned)
    print("layerwise square demand", square_demand)
    print("global square budget", global_square)
    print("outcome automatic_post_trade_two_layer_assignment")


if __name__ == "__main__":
    main()
