#!/usr/bin/env python3
"""Exact checker for two-valued transition predecessor cores.

The fixture contains cases with a balanced family of predecessor choice sets.
Every choice set has size one or two. The checker:

1. enumerates all injective representatives;
2. verifies the pseudoforest criterion;
3. returns an inclusion-minimal Hall witness when no representative exists;
4. classifies a minimal connected bicyclic witness;
5. for feasible cases, computes the alternating SCCs relative to one matching and
   verifies the exact Boolean factorization count.

This is intended for small finite regressions, not asymptotic instances.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence

Choice = tuple[int, ...]
Matching = tuple[int, ...]


def validate_case(name: str, choices: Sequence[Choice]) -> None:
    n = len(choices)
    if n == 0:
        raise ValueError(f"{name}: empty case")
    for index, choice in enumerate(choices):
        if not 1 <= len(choice) <= 2:
            raise ValueError(f"{name}: choice {index} must have size one or two")
        if len(set(choice)) != len(choice):
            raise ValueError(f"{name}: choice {index} repeats a resource")
        if any(resource < 0 or resource >= n for resource in choice):
            raise ValueError(f"{name}: choice {index} is outside [0,{n})")


def enumerate_representatives(choices: Sequence[Choice]) -> list[Matching]:
    n = len(choices)
    if n > 11:
        raise ValueError("exact enumeration is limited to n<=11")
    representatives: list[Matching] = []
    for selected in itertools.product(*choices):
        if len(set(selected)) == n:
            representatives.append(tuple(selected))
    return representatives


def choice_edges(choices: Sequence[Choice]) -> list[tuple[int, int]]:
    edges: list[tuple[int, int]] = []
    for choice in choices:
        if len(choice) == 1:
            edges.append((choice[0], choice[0]))
        else:
            edges.append((choice[0], choice[1]))
    return edges


def graph_components(
    n: int, edges: Sequence[tuple[int, int]]
) -> list[tuple[list[int], list[int]]]:
    adjacency: list[set[int]] = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)

    seen: set[int] = set()
    components: list[tuple[list[int], list[int]]] = []
    for start in range(n):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        vertices: list[int] = []
        while stack:
            vertex = stack.pop()
            vertices.append(vertex)
            for neighbour in adjacency[vertex]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        vertex_set = set(vertices)
        component_edges = [
            edge_id
            for edge_id, (u, v) in enumerate(edges)
            if u in vertex_set and v in vertex_set
        ]
        components.append((sorted(vertices), component_edges))
    return components


def pseudoforest_profile(
    n: int, edges: Sequence[tuple[int, int]]
) -> tuple[bool, list[dict[str, object]]]:
    profile: list[dict[str, object]] = []
    is_pseudoforest = True
    for vertices, edge_ids in graph_components(n, edges):
        edge_count = len(edge_ids)
        vertex_count = len(vertices)
        if edge_count > vertex_count:
            is_pseudoforest = False
        profile.append(
            {
                "vertices": vertices,
                "edge_ids": edge_ids,
                "vertex_count": vertex_count,
                "edge_count": edge_count,
                "cyclomatic_number": edge_count - vertex_count + 1,
            }
        )
    return is_pseudoforest, profile


def minimal_hall_witness(
    choices: Sequence[Choice],
) -> tuple[list[int], list[int]] | None:
    n = len(choices)
    for size in range(1, n + 1):
        for subset in itertools.combinations(range(n), size):
            neighbourhood: set[int] = set()
            for index in subset:
                neighbourhood.update(choices[index])
            if len(neighbourhood) < len(subset):
                return list(subset), sorted(neighbourhood)
    return None


def degrees_on_witness(
    edge_ids: Iterable[int], edges: Sequence[tuple[int, int]], vertices: Iterable[int]
) -> dict[int, int]:
    degree = {vertex: 0 for vertex in vertices}
    for edge_id in edge_ids:
        u, v = edges[edge_id]
        if u == v:
            degree[u] += 2
        else:
            degree[u] += 1
            degree[v] += 1
    return degree


def has_bridge(
    vertices: Sequence[int], edge_ids: Sequence[int], edges: Sequence[tuple[int, int]]
) -> bool:
    adjacency: dict[int, list[tuple[int, int]]] = {vertex: [] for vertex in vertices}
    for edge_id in edge_ids:
        u, v = edges[edge_id]
        if u == v:
            continue
        adjacency[u].append((v, edge_id))
        adjacency[v].append((u, edge_id))

    discovery: dict[int, int] = {}
    low: dict[int, int] = {}
    time = 0
    bridge_found = False

    def dfs(vertex: int, parent_edge: int | None) -> None:
        nonlocal time, bridge_found
        discovery[vertex] = time
        low[vertex] = time
        time += 1
        for neighbour, edge_id in adjacency[vertex]:
            if edge_id == parent_edge:
                continue
            if neighbour not in discovery:
                dfs(neighbour, edge_id)
                low[vertex] = min(low[vertex], low[neighbour])
                if low[neighbour] > discovery[vertex]:
                    bridge_found = True
            else:
                low[vertex] = min(low[vertex], discovery[neighbour])

    if vertices:
        dfs(vertices[0], None)
    return bridge_found


def classify_bicyclic_witness(
    subset: Sequence[int], neighbourhood: Sequence[int], edges: Sequence[tuple[int, int]]
) -> dict[str, object]:
    degree = degrees_on_witness(subset, edges, neighbourhood)
    branch_degrees = sorted(value for value in degree.values() if value > 2)
    if branch_degrees == [4]:
        core_type = "figure-eight"
    elif branch_degrees == [3, 3]:
        core_type = "barbell" if has_bridge(neighbourhood, subset, edges) else "theta"
    else:
        core_type = "unclassified-bicyclic"
    return {
        "edge_count": len(subset),
        "vertex_count": len(neighbourhood),
        "deficiency": len(subset) - len(neighbourhood),
        "cyclomatic_number": len(subset) - len(neighbourhood) + 1,
        "degrees": {str(key): value for key, value in sorted(degree.items())},
        "minimum_degree": min(degree.values()) if degree else 0,
        "suppressed_core_type": core_type,
    }


def strongly_connected_components(adjacency: Sequence[Sequence[int]]) -> list[list[int]]:
    n = len(adjacency)
    index = 0
    indices = [-1] * n
    low = [0] * n
    stack: list[int] = []
    on_stack = [False] * n
    components: list[list[int]] = []

    def visit(vertex: int) -> None:
        nonlocal index
        indices[vertex] = index
        low[vertex] = index
        index += 1
        stack.append(vertex)
        on_stack[vertex] = True

        for neighbour in adjacency[vertex]:
            if indices[neighbour] == -1:
                visit(neighbour)
                low[vertex] = min(low[vertex], low[neighbour])
            elif on_stack[neighbour]:
                low[vertex] = min(low[vertex], indices[neighbour])

        if low[vertex] == indices[vertex]:
            component: list[int] = []
            while True:
                member = stack.pop()
                on_stack[member] = False
                component.append(member)
                if member == vertex:
                    break
            components.append(sorted(component))

    for vertex in range(n):
        if indices[vertex] == -1:
            visit(vertex)
    return components


def alternating_profile(
    choices: Sequence[Choice], reference: Matching
) -> tuple[list[list[int]], list[list[int]]]:
    n = len(choices)
    left_to_right = {left: right for right, left in enumerate(reference)}
    adjacency: list[list[int]] = [[] for _ in range(n)]
    for right, choice in enumerate(choices):
        for left in choice:
            source = left_to_right[left]
            if source != right:
                adjacency[source].append(right)

    components = strongly_connected_components(adjacency)
    flexible = [component for component in components if len(component) > 1]
    return adjacency, flexible


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args()

    data = json.loads(args.fixture.read_text(encoding="utf-8"))
    output_cases: list[dict[str, object]] = []

    for case in data["cases"]:
        name = str(case["name"])
        choices = [tuple(map(int, choice)) for choice in case["choices"]]
        validate_case(name, choices)
        n = len(choices)
        edges = choice_edges(choices)
        representatives = enumerate_representatives(choices)
        is_pseudoforest, component_profile = pseudoforest_profile(n, edges)

        if bool(representatives) != is_pseudoforest:
            raise AssertionError(
                f"{name}: enumeration and pseudoforest criterion disagree"
            )

        result: dict[str, object] = {
            "name": name,
            "n": n,
            "representative_count": len(representatives),
            "pseudoforest": is_pseudoforest,
            "components": component_profile,
        }

        expected_count = case.get("expected_representative_count")
        if expected_count is not None and len(representatives) != int(expected_count):
            raise AssertionError(
                f"{name}: representative count {len(representatives)} != {expected_count}"
            )

        if representatives:
            reference = representatives[0]
            adjacency, flexible = alternating_profile(choices, reference)
            expected_factor_count = 2 ** len(flexible)
            if len(representatives) != expected_factor_count:
                raise AssertionError(
                    f"{name}: {len(representatives)} matchings != "
                    f"2^{len(flexible)}"
                )
            result.update(
                {
                    "reference_matching": list(reference),
                    "alternating_adjacency": adjacency,
                    "flexible_sccs": flexible,
                    "boolean_factor_count": expected_factor_count,
                }
            )
        else:
            witness = minimal_hall_witness(choices)
            if witness is None:
                raise AssertionError(f"{name}: missing Hall witness")
            subset, neighbourhood = witness
            result.update(
                {
                    "hall_subset": subset,
                    "hall_neighbourhood": neighbourhood,
                    "hall_core": classify_bicyclic_witness(
                        subset, neighbourhood, edges
                    ),
                }
            )

        output_cases.append(result)

    print(json.dumps({"cases": output_cases}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
