#!/usr/bin/env python3
"""Validate raw geometric candidate-routing manifests for CMR1894--CMR1901.

With one JSON path, validate that external manifest.
With no argument, run 500 deterministic random systems and mutation tests.
"""

from __future__ import annotations

import copy
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path
from random import Random
from typing import Any

Edge = tuple[int, int]
Point = tuple[int, int]
PairKey = tuple[Edge, Edge]
TripleKey = tuple[Edge, Edge, Edge]


class RoutingError(ValueError):
    """Raised when a routing manifest violates one exact condition."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RoutingError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def parse_point(value: Any, path: str) -> Point:
    require(isinstance(value, list) and len(value) == 2, f"{path}: expected [x,y]")
    return parse_integer(value[0], f"{path}[0]"), parse_integer(value[1], f"{path}[1]")


def parse_edge(value: Any, path: str, side: int) -> Edge:
    edge = parse_point(value, path)
    require(
        0 <= edge[0] < side and 0 <= edge[1] < side,
        f"{path}: edge outside response grid",
    )
    return edge


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def perfect_matchings(side: int, allowed: set[Edge]) -> list[tuple[Edge, ...]]:
    return [
        tuple((left, permutation[left]) for left in range(side))
        for permutation in permutations(range(side))
        if all((left, permutation[left]) in allowed for left in range(side))
    ]


def extendable_prescriptions(
    responses: list[tuple[Edge, ...]],
) -> tuple[set[Edge], set[PairKey], set[TripleKey]]:
    edges = {edge for response in responses for edge in response}
    pairs = {
        tuple(sorted(pair))
        for response in responses
        for pair in combinations(response, 2)
    }
    triples = {
        tuple(sorted(triple))
        for response in responses
        for triple in combinations(response, 3)
    }
    return edges, pairs, triples


def expected_witnesses(
    edges: set[Edge],
    pairs: set[PairKey],
    triples: set[TripleKey],
    background: list[Point],
) -> tuple[set[tuple[Edge, tuple[int, int]]], set[tuple[PairKey, int]], set[TripleKey]]:
    rank_one = {
        (edge, (first, second))
        for edge in edges
        for first, second in combinations(range(len(background)), 2)
        if collinear(background[first], background[second], edge)
    }
    rank_two = {
        (pair, index)
        for pair in pairs
        for index, point in enumerate(background)
        if collinear(pair[0], pair[1], point)
    }
    rank_three = {
        triple for triple in triples if collinear(triple[0], triple[1], triple[2])
    }
    return rank_one, rank_two, rank_three


def validate_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "manifest: expected object")
    require(manifest.get("version") == 1, "version: expected 1")
    side = parse_integer(manifest.get("side"), "side")
    require(side >= 2, "side: expected at least 2")

    raw_allowed = manifest.get("allowed_edges")
    require(isinstance(raw_allowed, list), "allowed_edges: expected list")
    allowed_list = [
        parse_edge(value, f"allowed_edges[{index}]", side)
        for index, value in enumerate(raw_allowed)
    ]
    allowed = set(allowed_list)
    require(len(allowed) == len(allowed_list), "allowed_edges: duplicates")
    responses = perfect_matchings(side, allowed)
    require(responses, "response host has no perfect matching")

    raw_background = manifest.get("background_points")
    require(isinstance(raw_background, list), "background_points: expected list")
    background = [
        parse_point(value, f"background_points[{index}]")
        for index, value in enumerate(raw_background)
    ]
    require(len(set(background)) == len(background), "background_points: duplicates")
    grid = {(left, right) for left in range(side) for right in range(side)}
    require(not (set(background) & grid), "background_points: must be disjoint from grid")

    raw_children = manifest.get("children")
    require(isinstance(raw_children, list) and raw_children, "children: expected list")
    require(
        all(isinstance(child, str) and child for child in raw_children),
        "children: expected nonempty strings",
    )
    children = set(raw_children)
    require(len(children) == len(raw_children), "children: duplicates")

    edges, pairs, triples = extendable_prescriptions(responses)
    expected_one, expected_two, expected_three = expected_witnesses(
        edges, pairs, triples, background
    )

    routes = manifest.get("routes")
    require(isinstance(routes, dict), "routes: expected object")
    coefficient_counts: dict[tuple[int, str, tuple[Edge, ...]], int] = defaultdict(int)

    rank_one_keys: set[tuple[Edge, tuple[int, int]]] = set()
    rank_one_routes = routes.get("rank1", [])
    require(isinstance(rank_one_routes, list), "routes.rank1: expected list")
    for index, record in enumerate(rank_one_routes):
        path = f"routes.rank1[{index}]"
        require(isinstance(record, dict), f"{path}: expected object")
        edge = parse_edge(record.get("response"), f"{path}.response", side)
        raw_pair = record.get("background_pair")
        require(
            isinstance(raw_pair, list) and len(raw_pair) == 2,
            f"{path}.background_pair: expected [i,j]",
        )
        first = parse_integer(raw_pair[0], f"{path}.background_pair[0]")
        second = parse_integer(raw_pair[1], f"{path}.background_pair[1]")
        require(0 <= first < second < len(background), f"{path}: bad background pair")
        child = record.get("child")
        require(child in children, f"{path}.child: unknown label")
        key = (edge, (first, second))
        require(key not in rank_one_keys, f"{path}: duplicate witness")
        rank_one_keys.add(key)
        coefficient_counts[(1, child, (edge,))] += 1

    rank_two_keys: set[tuple[PairKey, int]] = set()
    rank_two_routes = routes.get("rank2", [])
    require(isinstance(rank_two_routes, list), "routes.rank2: expected list")
    for index, record in enumerate(rank_two_routes):
        path = f"routes.rank2[{index}]"
        require(isinstance(record, dict), f"{path}: expected object")
        raw_pair = record.get("response")
        require(isinstance(raw_pair, list) and len(raw_pair) == 2, f"{path}.response")
        pair = tuple(
            sorted(
                parse_edge(edge, f"{path}.response[{entry}]", side)
                for entry, edge in enumerate(raw_pair)
            )
        )
        require(
            pair[0][0] != pair[1][0] and pair[0][1] != pair[1][1],
            f"{path}: incompatible response pair",
        )
        point_index = parse_integer(record.get("background_point"), f"{path}.background_point")
        require(0 <= point_index < len(background), f"{path}: bad background index")
        child = record.get("child")
        require(child in children, f"{path}.child: unknown label")
        key = (pair, point_index)
        require(key not in rank_two_keys, f"{path}: duplicate witness")
        rank_two_keys.add(key)
        coefficient_counts[(2, child, pair)] += 1

    rank_three_keys: set[TripleKey] = set()
    rank_three_routes = routes.get("rank3", [])
    require(isinstance(rank_three_routes, list), "routes.rank3: expected list")
    for index, record in enumerate(rank_three_routes):
        path = f"routes.rank3[{index}]"
        require(isinstance(record, dict), f"{path}: expected object")
        raw_triple = record.get("response")
        require(
            isinstance(raw_triple, list) and len(raw_triple) == 3,
            f"{path}.response: expected three edges",
        )
        triple = tuple(
            sorted(
                parse_edge(edge, f"{path}.response[{entry}]", side)
                for entry, edge in enumerate(raw_triple)
            )
        )
        require(
            len({edge[0] for edge in triple}) == 3
            and len({edge[1] for edge in triple}) == 3,
            f"{path}: incompatible response triple",
        )
        child = record.get("child")
        require(child in children, f"{path}.child: unknown label")
        require(triple not in rank_three_keys, f"{path}: duplicate witness")
        rank_three_keys.add(triple)
        coefficient_counts[(3, child, triple)] += 1

    require(rank_one_keys == expected_one, "routes.rank1: omitted or extraneous witness")
    require(rank_two_keys == expected_two, "routes.rank2: omitted or extraneous witness")
    require(rank_three_keys == expected_three, "routes.rank3: omitted or extraneous witness")

    raw_one = Counter(edge for edge, _witness in expected_one)
    raw_two = Counter(pair for pair, _witness in expected_two)
    raw_three = Counter(expected_three)
    routed_one = Counter()
    routed_two = Counter()
    routed_three = Counter()
    for (rank, _child, prescription), value in coefficient_counts.items():
        if rank == 1:
            routed_one[prescription[0]] += value
        elif rank == 2:
            routed_two[prescription] += value
        else:
            routed_three[prescription] += value
    require(routed_one == raw_one, "rank-one coefficient conservation failed")
    require(routed_two == raw_two, "rank-two coefficient conservation failed")
    require(routed_three == raw_three, "rank-three coefficient conservation failed")

    return {
        "responses": len(responses),
        "rank1": len(expected_one),
        "rank2": len(expected_two),
        "rank3": len(expected_three),
        "coefficient_bins": len(coefficient_counts),
    }


def make_manifest(
    side: int,
    allowed: set[Edge],
    background: list[Point],
    children: list[str],
) -> dict[str, Any]:
    responses = perfect_matchings(side, allowed)
    edges, pairs, triples = extendable_prescriptions(responses)
    rank_one, rank_two, rank_three = expected_witnesses(edges, pairs, triples, background)

    def label(index: int) -> str:
        return children[index % len(children)]

    return {
        "version": 1,
        "side": side,
        "allowed_edges": [list(edge) for edge in sorted(allowed)],
        "background_points": [list(point) for point in background],
        "children": children,
        "routes": {
            "rank1": [
                {
                    "response": list(edge),
                    "background_pair": list(witness),
                    "child": label(index),
                }
                for index, (edge, witness) in enumerate(sorted(rank_one))
            ],
            "rank2": [
                {
                    "response": [list(edge) for edge in pair],
                    "background_point": witness,
                    "child": label(index + 1),
                }
                for index, (pair, witness) in enumerate(sorted(rank_two))
            ],
            "rank3": [
                {
                    "response": [list(edge) for edge in triple],
                    "child": label(index + 2),
                }
                for index, triple in enumerate(sorted(rank_three))
            ],
        },
    }


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(1894)
    totals: Counter[str] = Counter()
    systems = 0
    for _ in range(500):
        side = random.randint(3, 5)
        permutation = list(range(side))
        random.shuffle(permutation)
        allowed = {(left, permutation[left]) for left in range(side)}
        for left in range(side):
            for right in range(side):
                if random.random() < 0.55:
                    allowed.add((left, right))

        target_size = random.randint(3, 7)
        grid = {(left, right) for left in range(side) for right in range(side)}
        background: list[Point] = []
        while len(background) < target_size:
            point = (
                random.randint(-3, side + 2),
                random.randint(-3, side + 2),
            )
            if point not in background and point not in grid:
                background.append(point)

        manifest = make_manifest(side, allowed, background, ["A", "B", "C"])
        summary = validate_manifest(manifest)
        totals["rank1"] += summary["rank1"]
        totals["rank2"] += summary["rank2"]
        totals["rank3"] += summary["rank3"]
        systems += 1

    require(systems == 500, "random tests: wrong system count")
    require(
        totals == Counter({"rank1": 1355, "rank2": 2792, "rank3": 1916}),
        "random tests: unexpected witness totals",
    )
    return systems, totals


def run_mutation_tests() -> int:
    side = 4
    allowed = {(left, right) for left in range(side) for right in range(side)}
    background = [(-2, -2), (5, 5), (-2, 5), (5, -2), (-1, 2)]
    manifest = make_manifest(side, allowed, background, ["A", "B"])
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data["routes"]["rank1"][0].update(child="unknown"))
    add(lambda data: data["routes"]["rank1"].pop())
    add(
        lambda data: data["routes"]["rank1"].append(
            copy.deepcopy(data["routes"]["rank1"][0])
        )
    )
    add(lambda data: data["routes"]["rank2"].pop())
    add(
        lambda data: data["routes"]["rank2"][0].update(
            response=[[0, 0], [0, 1]]
        )
    )
    add(lambda data: data["routes"]["rank3"].pop())
    add(
        lambda data: data["routes"]["rank3"][0].update(
            response=[[0, 0], [1, 2], [2, 1]]
        )
    )
    add(lambda data: data["background_points"].append(data["background_points"][0]))
    add(lambda data: data["allowed_edges"].pop())
    add(lambda data: data["children"].append("A"))

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except RoutingError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted manifest accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_geometric_candidate_routing_manifest.py [manifest.json]")

    if len(sys.argv) == 2:
        path = Path(sys.argv[1])
        with path.open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        summary = validate_manifest(manifest)
        print(
            "accepted geometric candidate routing manifest: "
            f"{summary['responses']} responses, {summary['rank1']} rank-one, "
            f"{summary['rank2']} rank-two and {summary['rank3']} rank-three "
            f"primitive witnesses in {summary['coefficient_bins']} labelled bins"
        )
        return

    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified geometric candidate routing checker: "
        f"{systems} random systems, {sum(totals.values())} primitive witnesses "
        f"({totals['rank1']} rank one, {totals['rank2']} rank two, "
        f"{totals['rank3']} rank three), and {rejected} corrupted manifests rejected"
    )


if __name__ == "__main__":
    main()
