#!/usr/bin/env python3
"""Solve fixed-patch matching-reservoir selection exactly as a 2-SAT instance.

The source certificate is saturated and no-three. The chosen old row/column
sets induce a degree-two bipartite graph. Path-component matching edges are
forced; each cycle contributes one Boolean alternating-matching choice. Every
external triple certificate becomes a unary or binary clause.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

Point = tuple[int, int]
Vertex = tuple[str, int]
Literal = tuple[int, bool]
Clause = tuple[Literal, ...]


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


def json_point(raw: Any, label: str) -> Point:
    if not isinstance(raw, list) or len(raw) != 2:
        raise ValueError(f"{label}: malformed point")
    x, y = raw
    if (
        isinstance(x, bool)
        or isinstance(y, bool)
        or not isinstance(x, int)
        or not isinstance(y, int)
    ):
        raise ValueError(f"{label}: nonintegral point")
    return x, y


def parse_points(raw: Any, label: str) -> tuple[Point, ...]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected a point list")
    points = tuple(
        sorted(
            json_point(point, f"{label} point {index}")
            for index, point in enumerate(raw)
        )
    )
    if len(points) != len(set(points)):
        raise ValueError(f"{label}: duplicate point")
    return points


def load_case(path: Path, selected_n: int | None) -> tuple[int, tuple[Point, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_cases = payload if isinstance(payload, list) else [payload]
    cases: list[tuple[int, tuple[Point, ...]]] = []
    for ordinal, raw in enumerate(raw_cases, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"case {ordinal}: expected an object")
        n = raw.get("n")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise ValueError(f"case {ordinal}: invalid n")
        points = parse_points(raw.get("points"), f"case {ordinal}")
        if not saturated(points, n) or not no_three(points):
            raise ValueError(f"case {ordinal}: invalid source certificate")
        if selected_n is None or n == selected_n:
            cases.append((n, points))
    if len(cases) != 1:
        raise ValueError("select exactly one source certificate with --n")
    return cases[0]


def load_fixed_patch(path: Path) -> tuple[Point, ...]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and isinstance(payload.get("states"), list):
        raw_states = payload["states"]
        if not raw_states:
            raise ValueError("bank contains no states")
        patches: list[tuple[Point, ...]] = []
        for ordinal, state in enumerate(raw_states, 1):
            if not isinstance(state, dict):
                raise ValueError(f"state {ordinal}: expected an object")
            raw = state.get("inserted", state.get("points"))
            patches.append(parse_points(raw, f"state {ordinal} inserted"))
        first = patches[0]
        if any(patch != first for patch in patches[1:]):
            raise ValueError("bank states do not share one fixed inserted patch")
        return first
    if isinstance(payload, dict):
        raw = payload.get("inserted", payload.get("points"))
        return parse_points(raw, "inserted")
    return parse_points(payload, "inserted")


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


def edge_point(first: Vertex, second: Vertex) -> Point:
    if first[0] == "c":
        return first[1], second[1]
    return second[1], first[1]


def ordered_component(
    vertices: set[Vertex],
    adjacency: dict[Vertex, list[Vertex]],
    is_cycle: bool,
) -> list[Vertex]:
    start = min(vertices) if is_cycle else min(
        vertex for vertex in vertices if len(adjacency[vertex]) == 1
    )
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


def build_reservoir_model(
    core: tuple[Point, ...],
    columns: tuple[int, ...],
    rows: tuple[int, ...],
) -> tuple[dict[Point, tuple[str, int | None, bool | None]], list[list[Point]], int]:
    if len(columns) != len(rows):
        raise ValueError("column and row sets must have the same size")
    vertices: set[Vertex] = {("c", value) for value in columns}
    vertices.update(("r", value) for value in rows)
    adjacency: dict[Vertex, list[Vertex]] = defaultdict(list)
    column_set = set(columns)
    row_set = set(rows)
    for point in core:
        if point[0] not in column_set or point[1] not in row_set:
            continue
        left = ("c", point[0])
        right = ("r", point[1])
        adjacency[left].append(right)
        adjacency[right].append(left)
    for vertex in vertices:
        adjacency.setdefault(vertex, [])
        if len(adjacency[vertex]) > 2:
            raise AssertionError("induced degree above two")

    status: dict[Point, tuple[str, int | None, bool | None]] = {
        point: ("always", None, None) for point in core
    }
    unseen = set(vertices)
    cycles: list[list[Point]] = []
    variable = 0

    while unseen:
        root = min(unseen)
        queue = deque([root])
        component_vertices: set[Vertex] = set()
        while queue:
            vertex = queue.popleft()
            if vertex in component_vertices:
                continue
            component_vertices.add(vertex)
            unseen.discard(vertex)
            queue.extend(adjacency[vertex])
        degrees = [len(adjacency[vertex]) for vertex in component_vertices]
        edge_count = sum(degrees) // 2
        if edge_count == 0:
            raise ValueError("induced reservoir graph has an isolated vertex")
        if all(degree == 2 for degree in degrees):
            order = ordered_component(component_vertices, adjacency, True)
            component_edges = [
                edge_point(order[index], order[(index + 1) % len(order)])
                for index in range(len(order))
            ]
            cycles.append(component_edges)
            for index, point in enumerate(component_edges):
                selected_value = bool(index % 2)
                status[point] = ("cycle", variable, selected_value)
            variable += 1
            continue

        order = ordered_component(component_vertices, adjacency, False)
        if len(order) % 2:
            raise ValueError("induced reservoir graph has an odd path component")
        component_edges = [
            edge_point(order[index], order[index + 1])
            for index in range(len(order) - 1)
        ]
        selected = set(component_edges[0::2])
        for point in component_edges:
            status[point] = (
                ("forced-delete", None, None)
                if point in selected
                else ("always", None, None)
            )

    return status, cycles, variable


def survival_condition(
    point: Point,
    status: dict[Point, tuple[str, int | None, bool | None]],
) -> tuple[str, Literal | None]:
    kind, variable, selected_value = status[point]
    if kind == "forced-delete":
        return "never", None
    if kind == "always":
        return "always", None
    if kind != "cycle" or variable is None or selected_value is None:
        raise AssertionError("malformed cycle status")
    return "literal", (variable, not selected_value)


def clause_for_survivors(
    points: tuple[Point, ...],
    status: dict[Point, tuple[str, int | None, bool | None]],
) -> tuple[str, Clause | None]:
    required: dict[int, bool] = {}
    for point in points:
        kind, literal = survival_condition(point, status)
        if kind == "never":
            return "impossible", None
        if kind == "always":
            continue
        assert literal is not None
        variable, value = literal
        if variable in required and required[variable] != value:
            return "impossible", None
        required[variable] = value
    if not required:
        return "fixed", None
    if len(required) > 2:
        raise AssertionError("external certificate uses more than two old points")
    clause = tuple(sorted((variable, not value) for variable, value in required.items()))
    return "clause", clause


def solve_2sat(variable_count: int, clauses: set[Clause]) -> tuple[bool, list[bool] | None, list[int]]:
    node_count = 2 * variable_count
    graph = [[] for _ in range(node_count)]
    reverse = [[] for _ in range(node_count)]

    def node(literal: Literal) -> int:
        variable, value = literal
        return 2 * variable + int(value)

    def add_implication(source: int, target: int) -> None:
        graph[source].append(target)
        reverse[target].append(source)

    for clause in clauses:
        if len(clause) == 1:
            a = node(clause[0])
            add_implication(a ^ 1, a)
        elif len(clause) == 2:
            a = node(clause[0])
            b = node(clause[1])
            add_implication(a ^ 1, b)
            add_implication(b ^ 1, a)
        else:
            raise AssertionError("clause must be unary or binary")

    visited = [False] * node_count
    order: list[int] = []

    def dfs_first(start: int) -> None:
        stack = [(start, 0)]
        visited[start] = True
        while stack:
            vertex, index = stack[-1]
            if index < len(graph[vertex]):
                neighbor = graph[vertex][index]
                stack[-1] = (vertex, index + 1)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append((neighbor, 0))
            else:
                order.append(vertex)
                stack.pop()

    for vertex in range(node_count):
        if not visited[vertex]:
            dfs_first(vertex)

    component = [-1] * node_count

    def dfs_second(start: int, label: int) -> None:
        stack = [start]
        component[start] = label
        while stack:
            vertex = stack.pop()
            for neighbor in reverse[vertex]:
                if component[neighbor] == -1:
                    component[neighbor] = label
                    stack.append(neighbor)

    label = 0
    for vertex in reversed(order):
        if component[vertex] == -1:
            dfs_second(vertex, label)
            label += 1

    for variable in range(variable_count):
        if component[2 * variable] == component[2 * variable + 1]:
            return False, None, component

    assignment = [
        component[2 * variable] < component[2 * variable + 1]
        for variable in range(variable_count)
    ]
    if not all(
        any(assignment[variable] == value for variable, value in clause)
        for clause in clauses
    ):
        opposite = [not value for value in assignment]
        if all(
            any(opposite[variable] == value for variable, value in clause)
            for clause in clauses
        ):
            assignment = opposite
        else:
            raise AssertionError("SCC assignment extraction failed")

    return True, assignment, component


def analyze(
    m: int,
    core: tuple[Point, ...],
    t: int,
    columns: tuple[int, ...],
    rows: tuple[int, ...],
    inserted: tuple[Point, ...],
) -> dict[str, Any]:
    target_n = m + t
    if len(columns) != len(rows):
        raise ValueError("columns and rows must have equal size")
    if len(inserted) != len(columns) + 2 * t:
        raise ValueError("fixed patch size must equal reservoir matching size plus 2t")
    if any(not (1 <= x <= target_n and 1 <= y <= target_n) for x, y in inserted):
        raise ValueError("inserted point outside target grid")
    if not no_three(inserted):
        raise ValueError("fixed inserted patch has an internal triple")
    overlap = sorted(set(inserted).intersection(core))
    if overlap:
        raise ValueError(f"fixed patch overlaps source points: {overlap}")

    status, cycles, variable_count = build_reservoir_model(core, columns, rows)
    clauses: set[Clause] = set()
    fixed_contradictions = 0
    skipped_impossible = 0
    origin_counts = {"blocked_cell": 0, "retained_anchor": 0}
    clause_origin_counts = {
        "blocked_cell_unary": 0,
        "blocked_cell_binary": 0,
        "retained_anchor_unary": 0,
    }

    for first, second in combinations(core, 2):
        for point in inserted:
            if determinant(first, second, point) != 0:
                continue
            origin_counts["blocked_cell"] += 1
            kind, clause = clause_for_survivors((first, second), status)
            if kind == "impossible":
                skipped_impossible += 1
            elif kind == "fixed":
                fixed_contradictions += 1
            else:
                assert clause is not None
                clauses.add(clause)
                clause_origin_counts[
                    f"blocked_cell_{'unary' if len(clause) == 1 else 'binary'}"
                ] += 1

    for anchor in core:
        for first, second in combinations(inserted, 2):
            if determinant(anchor, first, second) != 0:
                continue
            origin_counts["retained_anchor"] += 1
            kind, clause = clause_for_survivors((anchor,), status)
            if kind == "impossible":
                skipped_impossible += 1
            elif kind == "fixed":
                fixed_contradictions += 1
            else:
                assert clause is not None and len(clause) == 1
                clauses.add(clause)
                clause_origin_counts["retained_anchor_unary"] += 1

    satisfiable = False
    assignment: list[bool] | None = None
    components: list[int] = []
    if fixed_contradictions == 0:
        satisfiable, assignment, components = solve_2sat(variable_count, clauses)

    deleted: set[Point] = set()
    for point, (kind, variable, selected_value) in status.items():
        if kind == "forced-delete":
            deleted.add(point)
        elif kind == "cycle" and satisfiable:
            assert assignment is not None and variable is not None
            if assignment[variable] == selected_value:
                deleted.add(point)

    final_points: tuple[Point, ...] = ()
    final_triples = None
    if satisfiable:
        retained = tuple(point for point in core if point not in deleted)
        final_points = tuple(sorted(retained + inserted))
        if not saturated(final_points, target_n):
            raise AssertionError("2-SAT assignment does not preserve saturation")
        final_triples = sum(
            determinant(a, b, c) == 0 for a, b, c in combinations(final_points, 3)
        )
        if final_triples != 0:
            raise AssertionError("satisfying assignment leaves a triple")

    implication_edges = sum(1 if len(clause) == 1 else 2 for clause in clauses)
    unary_count = sum(len(clause) == 1 for clause in clauses)
    binary_count = sum(len(clause) == 2 for clause in clauses)

    return {
        "source_n": m,
        "target_n": target_n,
        "t": t,
        "columns": list(columns),
        "rows": list(rows),
        "inserted_point_count": len(inserted),
        "cycle_variable_count": variable_count,
        "cycle_lengths": [len(cycle) for cycle in cycles],
        "external_certificate_counts": origin_counts,
        "certificates_impossible_by_forced_deletion_or_cycle_parity": skipped_impossible,
        "fixed_contradiction_count": fixed_contradictions,
        "distinct_clause_count": len(clauses),
        "unary_clause_count": unary_count,
        "binary_clause_count": binary_count,
        "clause_origin_counts_before_deduplication": clause_origin_counts,
        "implication_vertex_count": 2 * variable_count,
        "implication_edge_count": implication_edges,
        "satisfiable": satisfiable,
        "assignment": assignment,
        "deleted": [list(point) for point in sorted(deleted)] if satisfiable else None,
        "final_points": [list(point) for point in final_points] if satisfiable else None,
        "final_triple_count": final_triples,
        "scc_labels": components,
        "clauses": [
            [
                {"variable": variable, "required_value": value}
                for variable, value in clause
            ]
            for clause in sorted(clauses)
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("patch", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--columns", required=True)
    parser.add_argument("--rows", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.t < 1:
        raise SystemExit("t must be positive")
    try:
        m, core = load_case(args.certificate, args.n)
        columns = parse_values(args.columns, "columns", m)
        rows = parse_values(args.rows, "rows", m)
        inserted = load_fixed_patch(args.patch)
        result = analyze(m, core, args.t, columns, rows, inserted)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
