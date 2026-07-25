#!/usr/bin/env python3
"""Verify PP3tn--PP3tt on a finite bipartite host by exact enumeration."""

from __future__ import annotations

import argparse
import json
from itertools import permutations, product
from pathlib import Path
from typing import Any

Edge = tuple[int, int]
Matching = tuple[int, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--enumeration-limit", type=int, default=10)
    return parser.parse_args()


def parse_edge(raw: Any, label: str, n: int) -> Edge:
    if (
        not isinstance(raw, list)
        or len(raw) != 2
        or any(isinstance(value, bool) or not isinstance(value, int) for value in raw)
    ):
        raise ValueError(f"{label}: expected [left,right] integers")
    left, right = raw
    if not (0 <= left < n and 0 <= right < n):
        raise ValueError(f"{label}: edge outside [0,n)^2")
    return left, right


def strongly_connected_components(adjacency: list[list[int]]) -> list[list[int]]:
    """Tarjan SCCs, returned in deterministic minimum-vertex order."""
    n = len(adjacency)
    index = 0
    indices = [-1] * n
    lowlink = [0] * n
    stack: list[int] = []
    on_stack = [False] * n
    components: list[list[int]] = []

    def visit(vertex: int) -> None:
        nonlocal index
        indices[vertex] = index
        lowlink[vertex] = index
        index += 1
        stack.append(vertex)
        on_stack[vertex] = True

        for target in adjacency[vertex]:
            if indices[target] == -1:
                visit(target)
                lowlink[vertex] = min(lowlink[vertex], lowlink[target])
            elif on_stack[target]:
                lowlink[vertex] = min(lowlink[vertex], indices[target])

        if lowlink[vertex] == indices[vertex]:
            component: list[int] = []
            while True:
                current = stack.pop()
                on_stack[current] = False
                component.append(current)
                if current == vertex:
                    break
            components.append(sorted(component))

    for vertex in range(n):
        if indices[vertex] == -1:
            visit(vertex)

    return sorted(components, key=lambda component: component[0])


def enumerate_matchings(n: int, edges: set[Edge], limit: int) -> list[Matching]:
    if n > limit:
        raise ValueError(f"n={n} exceeds enumeration limit {limit}")
    return [
        permutation
        for permutation in permutations(range(n))
        if all((left, permutation[left]) in edges for left in range(n))
    ]


def induced_component_matchings(
    component: list[int], edges: set[Edge]
) -> list[Matching]:
    """Return local images in component vertex order."""
    states: list[Matching] = []
    for image in permutations(component):
        if all((left, right) in edges for left, right in zip(component, image)):
            states.append(tuple(image))
    return states


def matching_to_edges(matching: Matching) -> list[list[int]]:
    return [[left, right] for left, right in enumerate(matching)]


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        n = payload.get("n")
        if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
            raise ValueError("n must be a positive integer")
        raw_edges = payload.get("edges")
        if not isinstance(raw_edges, list):
            raise ValueError("edges must be a list")
        edges = {
            parse_edge(raw, f"edges[{index}]", n)
            for index, raw in enumerate(raw_edges)
        }
        if len(edges) != len(raw_edges):
            raise ValueError("edges contains duplicates")
        reference_raw = payload.get("reference_matching", list(range(n)))
        if (
            not isinstance(reference_raw, list)
            or len(reference_raw) != n
            or any(
                isinstance(value, bool) or not isinstance(value, int)
                for value in reference_raw
            )
            or set(reference_raw) != set(range(n))
        ):
            raise ValueError("reference_matching must be a permutation of [0,n)")
        reference = tuple(reference_raw)
        if any((left, reference[left]) not in edges for left in range(n)):
            raise ValueError("reference_matching uses an absent edge")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    # Relabel the right side so the reference matching becomes the identity.
    inverse_reference = [0] * n
    for left, right in enumerate(reference):
        inverse_reference[right] = left
    normalized_edges = {
        (left, inverse_reference[right]) for left, right in edges
    }

    adjacency = [
        sorted(target for source, target in normalized_edges if source == vertex)
        for vertex in range(n)
    ]
    components = strongly_connected_components(adjacency)
    component_of = {
        vertex: component_index
        for component_index, component in enumerate(components)
        for vertex in component
    }

    normalized_matchings = enumerate_matchings(
        n, normalized_edges, args.enumeration_limit
    )
    original_matchings = [
        tuple(reference[normalized_right] for normalized_right in matching)
        for matching in normalized_matchings
    ]

    cross_component_allowed = sorted(
        [
            [left, right]
            for left, right in normalized_edges
            if component_of[left] != component_of[right]
        ]
    )
    selected_edge_union = {
        (left, matching[left])
        for matching in normalized_matchings
        for left in range(n)
    }
    cross_component_selected = sorted(
        [
            [left, right]
            for left, right in selected_edge_union
            if component_of[left] != component_of[right]
        ]
    )

    local_state_lists = [
        induced_component_matchings(component, normalized_edges)
        for component in components
    ]
    local_state_counts = [len(states) for states in local_state_lists]
    product_state_count = 1
    for count in local_state_counts:
        product_state_count *= count

    reconstructed: set[Matching] = set()
    for state_choice in product(*local_state_lists):
        permutation = list(range(n))
        for component, local_state in zip(components, state_choice):
            for left, right in zip(component, local_state):
                permutation[left] = right
        reconstructed.add(tuple(permutation))

    forced_reference_indices = [
        index
        for index in range(n)
        if all(matching[index] == index for matching in normalized_matchings)
    ]
    trivial_component_indices = [
        component[0] for component in components if len(component) == 1
    ]

    component_records = []
    for component, states in zip(components, local_state_lists):
        component_records.append(
            {
                "vertices": component,
                "size": len(component),
                "state_count": len(states),
                "flexible": len(states) >= 2,
                "states": [
                    [[left, right] for left, right in zip(component, state)]
                    for state in states
                ],
            }
        )

    result = {
        "n": n,
        "reference_matching": list(reference),
        "strong_components": component_records,
        "global_perfect_matching_count": len(normalized_matchings),
        "component_state_count_product": product_state_count,
        "component_factorization_verified": (
            reconstructed == set(normalized_matchings)
            and product_state_count == len(normalized_matchings)
        ),
        "forced_reference_indices": forced_reference_indices,
        "trivial_component_indices": trivial_component_indices,
        "forced_edge_characterization_verified": (
            forced_reference_indices == trivial_component_indices
        ),
        "cross_component_allowed_edges": cross_component_allowed,
        "cross_component_edges_selected_by_a_perfect_matching": cross_component_selected,
        "cross_component_nonselection_verified": not cross_component_selected,
        "global_perfect_matchings_normalized": [
            matching_to_edges(matching) for matching in normalized_matchings
        ],
        "global_perfect_matchings_original_labels": [
            matching_to_edges(matching) for matching in original_matchings
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
