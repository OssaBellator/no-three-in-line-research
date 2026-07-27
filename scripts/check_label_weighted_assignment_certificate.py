#!/usr/bin/env python3
"""Check denominator-cleared labelled nested-assignment certificates.

With no command-line argument, run a valid built-in example and mutation tests.
With one JSON path, validate that manifest and print a compact acceptance summary.
"""

from __future__ import annotations

import copy
import json
import sys
from collections import defaultdict
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

Edge = tuple[int, int]
Matching = tuple[Edge, ...]


class CertificateError(ValueError):
    """Raised when a manifest violates one exact certificate constraint."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def parse_integer(value: Any, path: str, *, positive: bool = False) -> int:
    require(type(value) is int, f"{path}: expected integer")
    if positive:
        require(value > 0, f"{path}: expected positive integer")
    return value


def parse_edge(value: Any, path: str) -> Edge:
    require(isinstance(value, list) and len(value) == 2, f"{path}: expected [u,v]")
    left = parse_integer(value[0], f"{path}[0]")
    right = parse_integer(value[1], f"{path}[1]")
    return left, right


def perfect_matchings(side: int, allowed: set[Edge]) -> list[Matching]:
    output: list[Matching] = []
    for permutation in permutations(range(side)):
        matching = tuple((left, permutation[left]) for left in range(side))
        if all(edge in allowed for edge in matching):
            output.append(matching)
    return output


def residual_vertices(
    side: int,
    prescription: tuple[Edge, ...],
) -> tuple[list[int], list[int]]:
    used_left = {left for left, _right in prescription}
    used_right = {right for _left, right in prescription}
    return (
        [left for left in range(side) if left not in used_left],
        [right for right in range(side) if right not in used_right],
    )


def parse_potentials(
    value: Any,
    expected_vertices: list[int] | range,
    path: str,
) -> dict[int, int]:
    require(isinstance(value, dict), f"{path}: expected object")
    expected_keys = {str(vertex) for vertex in expected_vertices}
    require(set(value) == expected_keys, f"{path}: incorrect vertex keys")
    return {
        int(key): parse_integer(entry, f"{path}.{key}")
        for key, entry in value.items()
    }


def validate_manifest(manifest: Any) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest: expected object")
    require(manifest.get("version") == 1, "version: expected 1")

    states = manifest.get("states")
    rows = manifest.get("rows")
    require(isinstance(states, list) and states, "states: expected nonempty list")
    require(isinstance(rows, list) and rows, "rows: expected nonempty list")

    weights: dict[str, int] = {}
    for index, state in enumerate(states):
        path = f"states[{index}]"
        require(isinstance(state, dict), f"{path}: expected object")
        state_id = state.get("id")
        require(isinstance(state_id, str) and state_id, f"{path}.id: expected string")
        require(state_id not in weights, f"{path}.id: duplicate state")
        weights[state_id] = parse_integer(
            state.get("weight"), f"{path}.weight", positive=True
        )

    parents_seen: set[str] = set()
    coefficient_entries = 0
    inner_duals = 0
    outer_edges_checked = 0

    for row_index, row in enumerate(rows):
        row_path = f"rows[{row_index}]"
        require(isinstance(row, dict), f"{row_path}: expected object")
        parent = row.get("parent")
        require(parent in weights, f"{row_path}.parent: unknown state")
        require(parent not in parents_seen, f"{row_path}.parent: duplicate row")
        parents_seen.add(parent)

        side = parse_integer(row.get("side"), f"{row_path}.side", positive=True)
        denominator = parse_integer(
            row.get("denominator"), f"{row_path}.denominator", positive=True
        )

        raw_allowed = row.get("allowed_edges")
        require(isinstance(raw_allowed, list), f"{row_path}.allowed_edges: expected list")
        allowed_list = [
            parse_edge(value, f"{row_path}.allowed_edges[{index}]")
            for index, value in enumerate(raw_allowed)
        ]
        allowed = set(allowed_list)
        require(len(allowed) == len(allowed_list), f"{row_path}.allowed_edges: duplicates")
        require(
            all(0 <= left < side and 0 <= right < side for left, right in allowed),
            f"{row_path}.allowed_edges: vertex outside side",
        )

        responses = perfect_matchings(side, allowed)
        require(responses, f"{row_path}: response host has no perfect matching")
        extendable_edges = {edge for response in responses for edge in response}
        extendable_ordered_pairs = {
            (edge, other)
            for response in responses
            for edge in response
            for other in response
            if edge != other
        }

        coefficients = row.get("coefficients")
        require(isinstance(coefficients, dict), f"{row_path}.coefficients: expected object")
        weighted_edge: defaultdict[Edge, int] = defaultdict(int)
        weighted_pair: defaultdict[frozenset[Edge], int] = defaultdict(int)
        weighted_triple: defaultdict[frozenset[Edge], int] = defaultdict(int)
        coefficient_keys: set[tuple[int, str, frozenset[Edge]]] = set()

        for rank, name, destination in (
            (1, "edge", weighted_edge),
            (2, "pair", weighted_pair),
            (3, "triple", weighted_triple),
        ):
            entries = coefficients.get(name, [])
            require(isinstance(entries, list), f"{row_path}.coefficients.{name}: expected list")
            for entry_index, entry in enumerate(entries):
                entry_path = f"{row_path}.coefficients.{name}[{entry_index}]"
                require(isinstance(entry, dict), f"{entry_path}: expected object")
                child = entry.get("child")
                require(child in weights, f"{entry_path}.child: unknown state")
                value = parse_integer(entry.get("value"), f"{entry_path}.value")
                require(value >= 0, f"{entry_path}.value: expected nonnegative")

                if rank == 1:
                    prescription = (parse_edge(entry.get("edge"), f"{entry_path}.edge"),)
                else:
                    raw_edges = entry.get("edges")
                    require(isinstance(raw_edges, list), f"{entry_path}.edges: expected list")
                    prescription = tuple(
                        parse_edge(edge, f"{entry_path}.edges[{index}]")
                        for index, edge in enumerate(raw_edges)
                    )
                    require(len(prescription) == rank, f"{entry_path}.edges: wrong rank")

                require(
                    len(set(prescription)) == rank,
                    f"{entry_path}: repeated edge",
                )
                require(
                    all(edge in allowed for edge in prescription),
                    f"{entry_path}: edge outside host",
                )
                require(
                    len({edge[0] for edge in prescription}) == rank
                    and len({edge[1] for edge in prescription}) == rank,
                    f"{entry_path}: incompatible prescription",
                )

                key = (rank, child, frozenset(prescription))
                require(key not in coefficient_keys, f"{entry_path}: duplicate coefficient")
                coefficient_keys.add(key)
                weighted_value = weights[child] * value
                if rank == 1:
                    destination[prescription[0]] += weighted_value
                else:
                    destination[frozenset(prescription)] += weighted_value
                coefficient_entries += 1

        rank_two_records = row.get("rank2_duals")
        require(isinstance(rank_two_records, list), f"{row_path}.rank2_duals: expected list")
        rank_two_upper: dict[Edge, int] = {}
        for record_index, record in enumerate(rank_two_records):
            path = f"{row_path}.rank2_duals[{record_index}]"
            require(isinstance(record, dict), f"{path}: expected object")
            outer = parse_edge(record.get("outer"), f"{path}.outer")
            require(outer not in rank_two_upper, f"{path}.outer: duplicate")
            left_vertices, right_vertices = residual_vertices(side, (outer,))
            left = parse_potentials(record.get("left"), left_vertices, f"{path}.left")
            right = parse_potentials(record.get("right"), right_vertices, f"{path}.right")
            objective_upper = parse_integer(
                record.get("objective_upper"), f"{path}.objective_upper"
            )

            for left_vertex in left_vertices:
                for right_vertex in right_vertices:
                    residual_edge = (left_vertex, right_vertex)
                    if residual_edge in allowed:
                        score = weighted_pair[frozenset((outer, residual_edge))]
                        require(
                            left[left_vertex] + right[right_vertex] >= score,
                            f"{path}: rank-two dual infeasible at {residual_edge}",
                        )
            require(
                objective_upper >= sum(left.values()) + sum(right.values()),
                f"{path}: objective upper variable is too small",
            )
            rank_two_upper[outer] = objective_upper
            inner_duals += 1

        require(
            set(rank_two_upper) == extendable_edges,
            f"{row_path}.rank2_duals: incomplete or extraneous outer-edge coverage",
        )

        rank_three_inner_records = row.get("rank3_inner_duals")
        require(
            isinstance(rank_three_inner_records, list),
            f"{row_path}.rank3_inner_duals: expected list",
        )
        rank_three_inner_upper: dict[tuple[Edge, Edge], int] = {}
        for record_index, record in enumerate(rank_three_inner_records):
            path = f"{row_path}.rank3_inner_duals[{record_index}]"
            require(isinstance(record, dict), f"{path}: expected object")
            outer = parse_edge(record.get("outer"), f"{path}.outer")
            second = parse_edge(record.get("second"), f"{path}.second")
            key = (outer, second)
            require(key not in rank_three_inner_upper, f"{path}: duplicate ordered pair")
            left_vertices, right_vertices = residual_vertices(side, (outer, second))
            left = parse_potentials(record.get("left"), left_vertices, f"{path}.left")
            right = parse_potentials(record.get("right"), right_vertices, f"{path}.right")
            objective_upper = parse_integer(
                record.get("objective_upper"), f"{path}.objective_upper"
            )

            for left_vertex in left_vertices:
                for right_vertex in right_vertices:
                    residual_edge = (left_vertex, right_vertex)
                    if residual_edge in allowed:
                        score = weighted_triple[
                            frozenset((outer, second, residual_edge))
                        ]
                        require(
                            left[left_vertex] + right[right_vertex] >= score,
                            f"{path}: rank-three inner dual infeasible at {residual_edge}",
                        )
            require(
                objective_upper >= sum(left.values()) + sum(right.values()),
                f"{path}: objective upper variable is too small",
            )
            rank_three_inner_upper[key] = objective_upper
            inner_duals += 1

        require(
            set(rank_three_inner_upper) == extendable_ordered_pairs,
            f"{row_path}.rank3_inner_duals: incomplete or extraneous pair coverage",
        )

        rank_three_middle_records = row.get("rank3_middle_duals")
        require(
            isinstance(rank_three_middle_records, list),
            f"{row_path}.rank3_middle_duals: expected list",
        )
        rank_three_middle_upper: dict[Edge, int] = {}
        for record_index, record in enumerate(rank_three_middle_records):
            path = f"{row_path}.rank3_middle_duals[{record_index}]"
            require(isinstance(record, dict), f"{path}: expected object")
            outer = parse_edge(record.get("outer"), f"{path}.outer")
            require(outer not in rank_three_middle_upper, f"{path}.outer: duplicate")
            left_vertices, right_vertices = residual_vertices(side, (outer,))
            left = parse_potentials(record.get("left"), left_vertices, f"{path}.left")
            right = parse_potentials(record.get("right"), right_vertices, f"{path}.right")
            objective_upper = parse_integer(
                record.get("objective_upper"), f"{path}.objective_upper"
            )

            for left_vertex in left_vertices:
                for right_vertex in right_vertices:
                    residual_edge = (left_vertex, right_vertex)
                    if residual_edge in allowed:
                        score = rank_three_inner_upper.get(
                            (outer, residual_edge), 0
                        )
                        require(
                            left[left_vertex] + right[right_vertex] >= score,
                            f"{path}: rank-three middle dual infeasible at {residual_edge}",
                        )
            require(
                objective_upper >= sum(left.values()) + sum(right.values()),
                f"{path}: objective upper variable is too small",
            )
            rank_three_middle_upper[outer] = objective_upper
            inner_duals += 1

        require(
            set(rank_three_middle_upper) == extendable_edges,
            f"{row_path}.rank3_middle_duals: incomplete or extraneous outer-edge coverage",
        )

        outer_record = row.get("outer_dual")
        require(isinstance(outer_record, dict), f"{row_path}.outer_dual: expected object")
        outer_left = parse_potentials(
            outer_record.get("left"), range(side), f"{row_path}.outer_dual.left"
        )
        outer_right = parse_potentials(
            outer_record.get("right"), range(side), f"{row_path}.outer_dual.right"
        )
        slack = parse_integer(
            outer_record.get("slack"), f"{row_path}.outer_dual.slack", positive=True
        )

        for edge in allowed:
            sixfold_score = (
                6 * weighted_edge[edge]
                + 3 * rank_two_upper.get(edge, 0)
                + rank_three_middle_upper.get(edge, 0)
            )
            require(
                outer_left[edge[0]] + outer_right[edge[1]] >= sixfold_score,
                f"{row_path}.outer_dual: infeasible at {edge}",
            )
            outer_edges_checked += 1

        outer_objective = sum(outer_left.values()) + sum(outer_right.values())
        parent_budget = 6 * denominator * weights[parent]
        require(
            outer_objective <= parent_budget - slack,
            f"{row_path}.outer_dual: strict row objective failed",
        )

    require(
        parents_seen == set(weights),
        "rows: every declared state must have exactly one recurrent row",
    )
    return {
        "states": len(weights),
        "rows": len(rows),
        "coefficients": coefficient_entries,
        "inner_duals": inner_duals,
        "outer_edges": outer_edges_checked,
    }


def build_example_manifest() -> dict[str, Any]:
    side = 3
    allowed = {(left, right) for left in range(side) for right in range(side)}
    responses = perfect_matchings(side, allowed)
    extendable_edges = {edge for response in responses for edge in response}
    extendable_pairs = {
        (edge, other)
        for response in responses
        for edge in response
        for other in response
        if edge != other
    }

    compatible_pairs = {
        frozenset(pair)
        for pair in combinations(sorted(allowed), 2)
        if len({edge[0] for edge in pair}) == 2
        and len({edge[1] for edge in pair}) == 2
    }
    compatible_triples = {
        frozenset(triple)
        for triple in combinations(sorted(allowed), 3)
        if len({edge[0] for edge in triple}) == 3
        and len({edge[1] for edge in triple}) == 3
    }

    rank_two_duals = []
    for outer in sorted(extendable_edges):
        left_vertices, right_vertices = residual_vertices(side, (outer,))
        rank_two_duals.append(
            {
                "outer": list(outer),
                "left": {str(vertex): 7 for vertex in left_vertices},
                "right": {str(vertex): 0 for vertex in right_vertices},
                "objective_upper": 7 * len(left_vertices),
            }
        )

    rank_three_inner_duals = []
    for outer, second in sorted(extendable_pairs):
        left_vertices, right_vertices = residual_vertices(side, (outer, second))
        rank_three_inner_duals.append(
            {
                "outer": list(outer),
                "second": list(second),
                "left": {str(vertex): 7 for vertex in left_vertices},
                "right": {str(vertex): 0 for vertex in right_vertices},
                "objective_upper": 7 * len(left_vertices),
            }
        )

    rank_three_middle_duals = []
    for outer in sorted(extendable_edges):
        left_vertices, right_vertices = residual_vertices(side, (outer,))
        rank_three_middle_duals.append(
            {
                "outer": list(outer),
                "left": {str(vertex): 7 for vertex in left_vertices},
                "right": {str(vertex): 0 for vertex in right_vertices},
                "objective_upper": 7 * len(left_vertices),
            }
        )

    return {
        "version": 1,
        "states": [{"id": "S", "weight": 7}],
        "rows": [
            {
                "parent": "S",
                "side": side,
                "denominator": 100,
                "allowed_edges": [list(edge) for edge in sorted(allowed)],
                "coefficients": {
                    "edge": [
                        {"child": "S", "edge": list(edge), "value": 1}
                        for edge in sorted(allowed)
                    ],
                    "pair": [
                        {
                            "child": "S",
                            "edges": [list(edge) for edge in sorted(pair)],
                            "value": 1,
                        }
                        for pair in sorted(
                            compatible_pairs, key=lambda item: tuple(sorted(item))
                        )
                    ],
                    "triple": [
                        {
                            "child": "S",
                            "edges": [list(edge) for edge in sorted(triple)],
                            "value": 1,
                        }
                        for triple in sorted(
                            compatible_triples, key=lambda item: tuple(sorted(item))
                        )
                    ],
                },
                "rank2_duals": rank_two_duals,
                "rank3_inner_duals": rank_three_inner_duals,
                "rank3_middle_duals": rank_three_middle_duals,
                "outer_dual": {
                    "left": {str(vertex): 98 for vertex in range(side)},
                    "right": {str(vertex): 0 for vertex in range(side)},
                    "slack": 1,
                },
            }
        ],
    }


def run_mutation_tests(manifest: dict[str, Any]) -> int:
    mutations = []

    def add_mutation(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add_mutation(lambda data: data["states"][0].update(weight=0))
    add_mutation(
        lambda data: data["rows"][0]["coefficients"]["edge"][0].update(value=-1)
    )
    add_mutation(lambda data: data["rows"][0]["rank2_duals"].pop())

    def weaken_rank_two_potential(data: dict[str, Any]) -> None:
        record = data["rows"][0]["rank2_duals"][0]
        first_key = next(iter(record["left"]))
        record["left"][first_key] = 6

    add_mutation(weaken_rank_two_potential)
    add_mutation(
        lambda data: data["rows"][0]["rank2_duals"][0].update(
            objective_upper=13
        )
    )
    add_mutation(lambda data: data["rows"][0]["rank3_inner_duals"].pop())
    add_mutation(
        lambda data: data["rows"][0]["rank3_middle_duals"][0].update(
            objective_upper=13
        )
    )

    def weaken_outer_potential(data: dict[str, Any]) -> None:
        data["rows"][0]["outer_dual"]["left"]["0"] = 97

    add_mutation(weaken_outer_potential)
    add_mutation(lambda data: data["rows"][0]["outer_dual"].update(slack=4000))

    def add_incompatible_pair(data: dict[str, Any]) -> None:
        data["rows"][0]["coefficients"]["pair"].append(
            {"child": "S", "edges": [[0, 0], [0, 1]], "value": 1}
        )

    add_mutation(add_incompatible_pair)

    def duplicate_coefficient(data: dict[str, Any]) -> None:
        data["rows"][0]["coefficients"]["edge"].append(
            copy.deepcopy(data["rows"][0]["coefficients"]["edge"][0])
        )

    add_mutation(duplicate_coefficient)
    add_mutation(
        lambda data: data["rows"][0]["coefficients"]["edge"][0].update(
            child="unknown"
        )
    )

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except CertificateError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: invalid manifest accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_label_weighted_assignment_certificate.py [manifest.json]")

    if len(sys.argv) == 2:
        path = Path(sys.argv[1])
        with path.open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        summary = validate_manifest(manifest)
        print(
            "accepted labelled assignment certificate: "
            f"{summary['states']} states, {summary['rows']} rows, "
            f"{summary['coefficients']} coefficient entries, "
            f"{summary['inner_duals']} inner/middle duals and "
            f"{summary['outer_edges']} outer-edge inequalities"
        )
        return

    manifest = build_example_manifest()
    summary = validate_manifest(manifest)
    rejected = run_mutation_tests(manifest)
    print(
        "verified labelled assignment certificate checker: "
        f"valid example with {summary['coefficients']} coefficient entries, "
        f"{summary['inner_duals']} inner/middle duals and "
        f"{summary['outer_edges']} outer-edge inequalities; "
        f"rejected {rejected} corrupted manifests"
    )


if __name__ == "__main__":
    main()
