#!/usr/bin/env python3
"""Classify the degree-two graph underlying a matching reservoir bank."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

Point = tuple[int, int]
Vertex = tuple[str, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    pts = tuple(points)
    return all(determinant(a, b, c) != 0 for a, b, c in combinations(pts, 3))


def saturated(points: Iterable[Point], n: int) -> bool:
    pts = tuple(points)
    return (
        len(pts) == 2 * n
        and len(set(pts)) == len(pts)
        and all(sum(x == col for x, _ in pts) == 2 for col in range(1, n + 1))
        and all(sum(y == row for _, y in pts) == 2 for row in range(1, n + 1))
    )


def load_case(path: Path, selected_n: int | None) -> tuple[int, tuple[Point, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_cases = payload if isinstance(payload, list) else [payload]
    cases = []
    for ordinal, raw in enumerate(raw_cases, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"case {ordinal}: expected an object")
        n = raw.get("n")
        raw_points = raw.get("points")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise ValueError(f"case {ordinal}: invalid n")
        if not isinstance(raw_points, list):
            raise ValueError(f"case {ordinal}: points must be a list")
        points = []
        for index, raw_point in enumerate(raw_points):
            if not isinstance(raw_point, list) or len(raw_point) != 2:
                raise ValueError(f"case {ordinal}: malformed point {index}")
            x, y = raw_point
            if (
                isinstance(x, bool)
                or isinstance(y, bool)
                or not isinstance(x, int)
                or not isinstance(y, int)
            ):
                raise ValueError(f"case {ordinal}: nonintegral point {index}")
            points.append((x, y))
        if not saturated(points, n) or not no_three(points):
            raise ValueError(f"case {ordinal}: invalid source certificate")
        if selected_n is None or n == selected_n:
            cases.append((n, tuple(sorted(points))))
    if len(cases) != 1:
        raise ValueError("select exactly one source certificate with --n")
    return cases[0]


def parse_values(text: str, label: str, n: int) -> tuple[int, ...]:
    try:
        values = tuple(
            sorted({int(part) for part in text.split(",") if part.strip()})
        )
    except ValueError as exc:
        raise ValueError(f"{label} must be comma-separated integers") from exc
    if not values:
        raise ValueError(f"{label} must be nonempty")
    if any(value < 1 or value > n for value in values):
        raise ValueError(f"{label} must lie in [1,{n}]")
    return values


def vertex_json(vertex: Vertex) -> dict[str, Any]:
    return {
        "side": "column" if vertex[0] == "c" else "row",
        "value": vertex[1],
    }


def edge_point(first: Vertex, second: Vertex) -> Point:
    if first[0] == "c":
        return first[1], second[1]
    return second[1], first[1]


def ordered_component(
    vertices: set[Vertex], adjacency: dict[Vertex, list[Vertex]], is_cycle: bool
) -> list[Vertex]:
    if is_cycle:
        start = min(vertices)
    else:
        endpoints = sorted(
            vertex for vertex in vertices if len(adjacency[vertex]) == 1
        )
        start = endpoints[0]
    order = [start]
    previous: Vertex | None = None
    current = start
    while True:
        choices = [neighbor for neighbor in adjacency[current] if neighbor != previous]
        if not choices:
            break
        next_vertex = min(choices)
        if is_cycle and next_vertex == start:
            break
        order.append(next_vertex)
        previous, current = current, next_vertex
    return order


def analyze(
    n: int,
    core: tuple[Point, ...],
    columns: tuple[int, ...],
    rows: tuple[int, ...],
) -> dict[str, Any]:
    if len(columns) != len(rows):
        raise ValueError("column and row sets must have the same size")
    vertices: set[Vertex] = {("c", value) for value in columns}
    vertices.update(("r", value) for value in rows)
    adjacency: dict[Vertex, list[Vertex]] = defaultdict(list)
    induced_edges = []
    row_set = set(rows)
    column_set = set(columns)
    for point in core:
        if point[0] not in column_set or point[1] not in row_set:
            continue
        left = ("c", point[0])
        right = ("r", point[1])
        adjacency[left].append(right)
        adjacency[right].append(left)
        induced_edges.append(point)
    for vertex in vertices:
        adjacency.setdefault(vertex, [])
        if len(adjacency[vertex]) > 2:
            raise AssertionError("saturated source induced degree above two")

    unseen = set(vertices)
    components = []
    global_edge_status: dict[Point, dict[str, Any]] = {}
    perfect = True
    cycle_count = 0

    while unseen:
        root = min(unseen)
        queue = deque([root])
        component_vertices = set()
        while queue:
            vertex = queue.popleft()
            if vertex in component_vertices:
                continue
            component_vertices.add(vertex)
            unseen.discard(vertex)
            queue.extend(adjacency[vertex])

        degree_list = [len(adjacency[vertex]) for vertex in component_vertices]
        edge_count = sum(degree_list) // 2
        if edge_count == 0:
            component_type = "isolated"
            component_perfect = False
            order = [min(component_vertices)]
            component_edges = []
            matching_count = 0
        elif all(degree == 2 for degree in degree_list):
            component_type = "cycle"
            component_perfect = True
            cycle_count += 1
            order = ordered_component(component_vertices, adjacency, True)
            component_edges = [
                edge_point(order[index], order[(index + 1) % len(order)])
                for index in range(len(order))
            ]
            matching_count = 2
            for index, point in enumerate(component_edges):
                global_edge_status[point] = {
                    "status": "cycle-optional",
                    "deletion_probability": "1/2",
                    "cycle_class": index % 2,
                    "cycle_component": cycle_count,
                }
        else:
            component_type = "path"
            order = ordered_component(component_vertices, adjacency, False)
            component_edges = [
                edge_point(order[index], order[index + 1])
                for index in range(len(order) - 1)
            ]
            component_perfect = len(order) % 2 == 0
            matching_count = 1 if component_perfect else 0
            if component_perfect:
                selected = set(component_edges[0::2])
                for point in component_edges:
                    if point in selected:
                        global_edge_status[point] = {
                            "status": "forced",
                            "deletion_probability": "1",
                        }
                    else:
                        global_edge_status[point] = {
                            "status": "never-selected",
                            "deletion_probability": "0",
                        }

        perfect = perfect and component_perfect
        components.append(
            {
                "type": component_type,
                "vertex_count": len(component_vertices),
                "edge_count": edge_count,
                "has_perfect_matching": component_perfect,
                "matching_count": matching_count,
                "ordered_vertices": [vertex_json(vertex) for vertex in order],
                "edges": [list(point) for point in component_edges],
            }
        )

    components.sort(
        key=lambda item: (
            item["type"],
            json.dumps(item["ordered_vertices"], sort_keys=True),
        )
    )
    perfect_matching_count = 2**cycle_count if perfect else 0
    statuses = [
        {
            "point": list(point),
            **global_edge_status.get(
                point,
                {
                    "status": "outside-perfect-matching-support",
                    "deletion_probability": "0",
                },
            ),
        }
        for point in sorted(induced_edges)
    ]
    status_counts: dict[str, int] = defaultdict(int)
    for item in statuses:
        status_counts[item["status"]] += 1

    return {
        "source_n": n,
        "columns": list(columns),
        "rows": list(rows),
        "vertex_count": len(vertices),
        "induced_edge_count": len(induced_edges),
        "maximum_degree": max(
            (len(adjacency[vertex]) for vertex in vertices), default=0
        ),
        "component_count": len(components),
        "cycle_component_count": cycle_count,
        "has_perfect_matching": perfect,
        "perfect_matching_count": perfect_matching_count,
        "edge_status_counts": dict(sorted(status_counts.items())),
        "edge_statuses": statuses,
        "components": components,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--columns", required=True)
    parser.add_argument("--rows", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        n, core = load_case(args.certificate, args.n)
        columns = parse_values(args.columns, "columns", n)
        rows = parse_values(args.rows, "rows", n)
        result = analyze(n, core, columns, rows)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
