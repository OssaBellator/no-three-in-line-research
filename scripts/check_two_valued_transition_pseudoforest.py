#!/usr/bin/env python3
"""Exact checker for one-/two-valued transition choice families.

For each fixture case, the script:

1. enumerates all injective representatives;
2. constructs the labelled choice multigraph;
3. checks the pseudoforest criterion componentwise;
4. verifies the exact component-state product when feasible;
5. returns an inclusion-minimal Hall witness when infeasible.

The checker is finite regression support for PP3zw--PP3aab.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict, deque
from pathlib import Path
from typing import Iterable, Mapping, Sequence

ChoiceMap = dict[str, tuple[int, ...]]


def validate_choices(raw: Mapping[str, Sequence[int]]) -> ChoiceMap:
    choices: ChoiceMap = {}
    for label, values_raw in raw.items():
        values = tuple(dict.fromkeys(int(value) for value in values_raw))
        if not 1 <= len(values) <= 2:
            raise ValueError(f"{label}: choice set must have size one or two")
        choices[str(label)] = values
    return choices


def enumerate_injective_assignments(choices: ChoiceMap) -> list[dict[str, int]]:
    labels = list(choices)
    assignments: list[dict[str, int]] = []
    for selected in itertools.product(*(choices[label] for label in labels)):
        if len(set(selected)) != len(selected):
            continue
        assignments.append(dict(zip(labels, selected, strict=True)))
    return assignments


def component_data(choices: ChoiceMap) -> list[dict[str, object]]:
    vertices = sorted({value for values in choices.values() for value in values})
    adjacency: dict[int, set[int]] = {vertex: set() for vertex in vertices}
    labels_at_vertex: dict[int, set[str]] = defaultdict(set)

    for label, values in choices.items():
        for vertex in values:
            labels_at_vertex[vertex].add(label)
        if len(values) == 2:
            u, v = values
            adjacency[u].add(v)
            adjacency[v].add(u)

    components: list[dict[str, object]] = []
    unseen = set(vertices)
    while unseen:
        start = min(unseen)
        queue = deque([start])
        component_vertices: set[int] = set()
        while queue:
            vertex = queue.popleft()
            if vertex not in unseen:
                continue
            unseen.remove(vertex)
            component_vertices.add(vertex)
            queue.extend(adjacency[vertex] & unseen)

        component_labels = {
            label
            for vertex in component_vertices
            for label in labels_at_vertex[vertex]
            if set(choices[label]) <= component_vertices
        }
        edge_count = len(component_labels)
        vertex_count = len(component_vertices)
        excess = edge_count - vertex_count
        if excess < 0:
            kind = "tree"
            predicted_states = vertex_count
        elif excess == 0:
            loops = sum(1 for label in component_labels if len(choices[label]) == 1)
            kind = "loop-unicyclic" if loops else "unicyclic"
            predicted_states = 1 if loops else 2
        else:
            kind = "bicyclic-or-denser"
            predicted_states = 0

        components.append(
            {
                "vertices": sorted(component_vertices),
                "labels": sorted(component_labels),
                "vertex_count": vertex_count,
                "edge_count": edge_count,
                "excess": excess,
                "kind": kind,
                "predicted_states": predicted_states,
            }
        )
    return components


def is_pseudoforest(components: Iterable[Mapping[str, object]]) -> bool:
    return all(int(component["excess"]) <= 0 for component in components)


def minimal_hall_witness(choices: ChoiceMap) -> dict[str, object] | None:
    labels = list(choices)
    for size in range(1, len(labels) + 1):
        for subset in itertools.combinations(labels, size):
            union = sorted({value for label in subset for value in choices[label]})
            if len(subset) > len(union):
                return {
                    "labels": list(subset),
                    "vertices": union,
                    "edge_count": len(subset),
                    "vertex_count": len(union),
                    "excess": len(subset) - len(union),
                }
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args()

    data = json.loads(args.fixture.read_text(encoding="utf-8"))
    output_cases: list[dict[str, object]] = []

    for raw_case in data["cases"]:
        name = str(raw_case["name"])
        choices = validate_choices(raw_case["choices"])
        assignments = enumerate_injective_assignments(choices)
        components = component_data(choices)
        pseudoforest = is_pseudoforest(components)
        predicted_count = 1
        if pseudoforest:
            for component in components:
                predicted_count *= int(component["predicted_states"])
        else:
            predicted_count = 0

        if bool(assignments) != pseudoforest:
            raise AssertionError(
                f"{name}: enumeration and pseudoforest criterion disagree"
            )
        if len(assignments) != predicted_count:
            raise AssertionError(
                f"{name}: actual {len(assignments)}, predicted {predicted_count}"
            )

        witness = minimal_hall_witness(choices)
        if pseudoforest and witness is not None:
            raise AssertionError(f"{name}: feasible case has Hall witness")
        if not pseudoforest:
            if witness is None:
                raise AssertionError(f"{name}: infeasible case lacks Hall witness")
            if int(witness["excess"]) != 1:
                raise AssertionError(f"{name}: minimal Hall excess is not one")

        output_cases.append(
            {
                "name": name,
                "choice_count": len(choices),
                "injective_assignment_count": len(assignments),
                "pseudoforest": pseudoforest,
                "predicted_assignment_count": predicted_count,
                "components": components,
                "minimal_hall_witness": witness,
                "sample_assignments": assignments[:6],
            }
        )

    print(json.dumps({"cases": output_cases}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
