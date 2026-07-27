#!/usr/bin/env python3
"""Validate last-entering-owner and total-fate manifests for geometric witnesses.

With one JSON path, validate that manifest.
With no argument, run deterministic random systems and mutation tests.
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
WitnessKey = tuple[int, tuple[Edge, ...], tuple[int, ...]]


class FateError(ValueError):
    """Raised when an owner/fate manifest violates an exact condition."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FateError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def parse_point(value: Any, path: str) -> Point:
    require(isinstance(value, list) and len(value) == 2, f"{path}: expected [x,y]")
    return parse_integer(value[0], f"{path}[0]"), parse_integer(value[1], f"{path}[1]")


def parse_edge(value: Any, path: str, side: int) -> Edge:
    edge = parse_point(value, path)
    require(0 <= edge[0] < side and 0 <= edge[1] < side, f"{path}: edge outside grid")
    return edge


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def perfect_matchings(side: int, allowed: set[Edge]) -> list[tuple[Edge, ...]]:
    return [
        tuple((left, image[left]) for left in range(side))
        for image in permutations(range(side))
        if all((left, image[left]) in allowed for left in range(side))
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
) -> dict[int, set[WitnessKey]]:
    rank_one = {
        (1, (edge,), (first, second))
        for edge in edges
        for first, second in combinations(range(len(background)), 2)
        if collinear(background[first], background[second], edge)
    }
    rank_two = {
        (2, pair, (index,))
        for pair in pairs
        for index, point in enumerate(background)
        if collinear(pair[0], pair[1], point)
    }
    rank_three = {
        (3, triple, ())
        for triple in triples
        if collinear(triple[0], triple[1], triple[2])
    }
    return {1: rank_one, 2: rank_two, 3: rank_three}


def owner_of(prescription: tuple[Edge, ...], order: dict[Edge, int]) -> Edge:
    return max(prescription, key=lambda edge: order[edge])


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
    edges, pairs, triples = extendable_prescriptions(responses)

    raw_background = manifest.get("background_points")
    require(isinstance(raw_background, list), "background_points: expected list")
    background = [
        parse_point(value, f"background_points[{index}]")
        for index, value in enumerate(raw_background)
    ]
    require(len(set(background)) == len(background), "background_points: duplicates")
    grid = {(left, right) for left in range(side) for right in range(side)}
    require(not (set(background) & grid), "background_points: must be disjoint from grid")

    raw_order = manifest.get("entry_order")
    require(isinstance(raw_order, list), "entry_order: expected list")
    ordered_edges = [
        parse_edge(value, f"entry_order[{index}]", side)
        for index, value in enumerate(raw_order)
    ]
    require(len(set(ordered_edges)) == len(ordered_edges), "entry_order: duplicates")
    require(set(ordered_edges) == edges, "entry_order: must contain every extendable edge")
    order = {edge: index for index, edge in enumerate(ordered_edges)}

    raw_states = manifest.get("states")
    require(isinstance(raw_states, list) and raw_states, "states: expected nonempty list")
    states: dict[str, dict[str, Any]] = {}
    for index, raw_state in enumerate(raw_states):
        path = f"states[{index}]"
        require(isinstance(raw_state, dict), f"{path}: expected object")
        state_id = raw_state.get("id")
        require(isinstance(state_id, str) and state_id, f"{path}.id: expected string")
        require(state_id not in states, f"{path}.id: duplicate")
        role = raw_state.get("role")
        require(
            role in {"recurrent", "offdiagonal", "auxiliary", "sink"},
            f"{path}.role: invalid",
        )
        stratum = parse_integer(raw_state.get("stratum"), f"{path}.stratum")
        require(stratum >= 0, f"{path}.stratum: expected nonnegative")
        raw_owner = raw_state.get("owner")
        owner = None if raw_owner is None else parse_edge(raw_owner, f"{path}.owner", side)
        if role == "recurrent":
            require(owner in edges or owner is None, f"{path}.owner: not extendable")
        states[state_id] = {"role": role, "stratum": stratum, "owner": owner}

    parent = manifest.get("parent")
    require(parent in states, "parent: unknown state")
    require(states[parent]["role"] == "recurrent", "parent: must be recurrent")
    parent_stratum = states[parent]["stratum"]

    expected = expected_witnesses(edges, pairs, triples, background)
    raw_fates = manifest.get("fates")
    require(isinstance(raw_fates, dict), "fates: expected object")
    seen: dict[int, set[WitnessKey]] = {1: set(), 2: set(), 3: set()}
    fate_counts: Counter[str] = Counter()
    owner_counts: Counter[Edge] = Counter()
    exported: defaultdict[tuple[int, str, tuple[Edge, ...]], int] = defaultdict(int)

    for rank, name in ((1, "rank1"), (2, "rank2"), (3, "rank3")):
        records = raw_fates.get(name, [])
        require(isinstance(records, list), f"fates.{name}: expected list")
        for index, record in enumerate(records):
            path = f"fates.{name}[{index}]"
            require(isinstance(record, dict), f"{path}: expected object")

            if rank == 1:
                prescription = (
                    parse_edge(record.get("response"), f"{path}.response", side),
                )
                raw_pair = record.get("background_pair")
                require(
                    isinstance(raw_pair, list) and len(raw_pair) == 2,
                    f"{path}.background_pair: expected [i,j]",
                )
                first = parse_integer(raw_pair[0], f"{path}.background_pair[0]")
                second = parse_integer(raw_pair[1], f"{path}.background_pair[1]")
                require(0 <= first < second < len(background), f"{path}: bad background pair")
                witness = (first, second)
            elif rank == 2:
                raw_pair = record.get("response")
                require(
                    isinstance(raw_pair, list) and len(raw_pair) == 2,
                    f"{path}.response: expected two edges",
                )
                prescription = tuple(
                    sorted(
                        parse_edge(value, f"{path}.response[{entry}]", side)
                        for entry, value in enumerate(raw_pair)
                    )
                )
                require(
                    prescription[0][0] != prescription[1][0]
                    and prescription[0][1] != prescription[1][1],
                    f"{path}: incompatible response pair",
                )
                point_index = parse_integer(
                    record.get("background_point"), f"{path}.background_point"
                )
                require(0 <= point_index < len(background), f"{path}: bad background index")
                witness = (point_index,)
            else:
                raw_triple = record.get("response")
                require(
                    isinstance(raw_triple, list) and len(raw_triple) == 3,
                    f"{path}.response: expected three edges",
                )
                prescription = tuple(
                    sorted(
                        parse_edge(value, f"{path}.response[{entry}]", side)
                        for entry, value in enumerate(raw_triple)
                    )
                )
                require(
                    len({edge[0] for edge in prescription}) == 3
                    and len({edge[1] for edge in prescription}) == 3,
                    f"{path}: incompatible response triple",
                )
                witness = ()

            key: WitnessKey = (rank, prescription, witness)
            require(key not in seen[rank], f"{path}: duplicate witness")
            seen[rank].add(key)

            declared_owner = parse_edge(record.get("owner"), f"{path}.owner", side)
            computed_owner = owner_of(prescription, order)
            require(declared_owner == computed_owner, f"{path}.owner: not last-entering")
            owner_counts[computed_owner] += 1

            kind = record.get("kind")
            require(
                kind in {"retained", "deleted", "transferred", "dominated"},
                f"{path}.kind: invalid",
            )
            fate_counts[kind] += 1
            evidence = record.get("evidence")
            if kind != "retained":
                require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")

            if kind == "deleted":
                require("child" not in record, f"{path}.child: forbidden for deletion")
                require("multiplicity" not in record, f"{path}.multiplicity: forbidden")
                continue

            child = record.get("child")
            require(child in states, f"{path}.child: unknown state")
            child_state = states[child]
            if kind in {"retained", "dominated"}:
                require(
                    child_state["owner"] == computed_owner,
                    f"{path}.child: owner mismatch",
                )
                require(
                    child_state["role"] == "recurrent",
                    f"{path}.child: retained/dominated target must be recurrent",
                )
            elif kind == "transferred":
                structural_descent = (
                    child_state["role"] == "offdiagonal"
                    and child_state["stratum"] < parent_stratum
                )
                auxiliary_transfer = child_state["role"] == "auxiliary"
                require(
                    structural_descent or auxiliary_transfer,
                    f"{path}.child: transfer is neither descent nor auxiliary",
                )

            if kind == "dominated":
                multiplicity = parse_integer(
                    record.get("multiplicity"), f"{path}.multiplicity"
                )
                require(multiplicity >= 1, f"{path}.multiplicity: expected positive")
            else:
                require("multiplicity" not in record, f"{path}.multiplicity: unexpected")
                multiplicity = 1
            exported[(rank, child, prescription)] += multiplicity

    for rank in (1, 2, 3):
        require(
            seen[rank] == expected[rank],
            f"fates.rank{rank}: omitted or extraneous witness",
        )

    total_expected = sum(len(expected[rank]) for rank in (1, 2, 3))
    require(sum(fate_counts.values()) == total_expected, "fates: total partition failed")
    return {
        "responses": len(responses),
        "witnesses": total_expected,
        "rank_counts": {rank: len(expected[rank]) for rank in (1, 2, 3)},
        "fate_counts": dict(fate_counts),
        "owner_count": len(owner_counts),
        "exported_bins": dict(exported),
    }


def make_manifest(
    side: int,
    allowed: set[Edge],
    background: list[Point],
    random: Random,
) -> dict[str, Any]:
    responses = perfect_matchings(side, allowed)
    edges, pairs, triples = extendable_prescriptions(responses)
    expected = expected_witnesses(edges, pairs, triples, background)
    entry_order = sorted(edges)
    random.shuffle(entry_order)
    order = {edge: index for index, edge in enumerate(entry_order)}

    owner_state = {edge: f"O_{edge[0]}_{edge[1]}" for edge in edges}
    states = [
        {"id": "P", "role": "recurrent", "stratum": 3, "owner": None},
        {"id": "D", "role": "offdiagonal", "stratum": 2, "owner": None},
        {"id": "AUX", "role": "auxiliary", "stratum": 3, "owner": None},
    ]
    states.extend(
        {
            "id": owner_state[edge],
            "role": "recurrent",
            "stratum": 3,
            "owner": list(edge),
        }
        for edge in sorted(edges)
    )

    fates: dict[str, list[dict[str, Any]]] = {
        "rank1": [],
        "rank2": [],
        "rank3": [],
    }
    flat = sorted(
        expected[1] | expected[2] | expected[3],
        key=lambda key: (key[0], key[1], key[2]),
    )
    for index, key in enumerate(flat):
        rank, prescription, witness = key
        owner = owner_of(prescription, order)
        kind = ("retained", "transferred", "dominated", "deleted")[index % 4]
        record: dict[str, Any] = {
            "owner": list(owner),
            "kind": kind,
        }
        if rank == 1:
            record["response"] = list(prescription[0])
            record["background_pair"] = list(witness)
            bucket = "rank1"
        elif rank == 2:
            record["response"] = [list(edge) for edge in prescription]
            record["background_point"] = witness[0]
            bucket = "rank2"
        else:
            record["response"] = [list(edge) for edge in prescription]
            bucket = "rank3"

        if kind == "retained":
            record["child"] = owner_state[owner]
        elif kind == "transferred":
            record["child"] = "D"
            record["evidence"] = "strict-stratum-descent"
        elif kind == "dominated":
            record["child"] = owner_state[owner]
            record["multiplicity"] = 2
            record["evidence"] = "declared-componentwise-upper"
        else:
            record["evidence"] = "declared-rule-obligation"
        fates[bucket].append(record)

    return {
        "version": 1,
        "side": side,
        "allowed_edges": [list(edge) for edge in sorted(allowed)],
        "background_points": [list(point) for point in background],
        "entry_order": [list(edge) for edge in entry_order],
        "states": states,
        "parent": "P",
        "fates": fates,
    }


def run_random_tests() -> tuple[int, Counter[str], int]:
    random = Random(1902)
    systems = 0
    fate_totals: Counter[str] = Counter()
    witness_total = 0
    for _ in range(400):
        side = random.randint(3, 5)
        permutation = list(range(side))
        random.shuffle(permutation)
        allowed = {(left, permutation[left]) for left in range(side)}
        for left in range(side):
            for right in range(side):
                if random.random() < 0.57:
                    allowed.add((left, right))
        grid = {(left, right) for left in range(side) for right in range(side)}
        background: list[Point] = []
        target_size = random.randint(3, 7)
        while len(background) < target_size:
            point = (random.randint(-3, side + 2), random.randint(-3, side + 2))
            if point not in grid and point not in background:
                background.append(point)
        manifest = make_manifest(side, allowed, background, random)
        summary = validate_manifest(manifest)
        fate_totals.update(summary["fate_counts"])
        witness_total += summary["witnesses"]
        systems += 1
    require(systems == 400, "random tests: wrong system count")
    require(witness_total == 5586, "random tests: unexpected witness total")
    require(
        fate_totals
        == Counter(
            {
                "retained": 1552,
                "transferred": 1461,
                "dominated": 1339,
                "deleted": 1234,
            }
        ),
        "random tests: unexpected fate distribution",
    )
    return systems, fate_totals, witness_total


def run_mutation_tests() -> int:
    random = Random(7)
    side = 4
    allowed = {(left, right) for left in range(side) for right in range(side)}
    background = [(-2, -2), (5, 5), (-2, 5), (5, -2), (-1, 2)]
    manifest = make_manifest(side, allowed, background, random)
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data["entry_order"].pop())
    add(lambda data: data["entry_order"].append(data["entry_order"][0]))
    add(lambda data: data["fates"]["rank1"].pop())
    add(
        lambda data: data["fates"]["rank1"].append(
            copy.deepcopy(data["fates"]["rank1"][0])
        )
    )

    def break_owner(data: dict[str, Any]) -> None:
        record = data["fates"]["rank1"][0]
        current = record["owner"]
        replacement = next(edge for edge in data["entry_order"] if edge != current)
        record["owner"] = replacement

    add(break_owner)
    add(lambda data: data["fates"]["rank1"][0].update(child="unknown"))
    add(lambda data: data["fates"]["rank1"][0].update(kind="deleted", child="D"))
    add(
        lambda data: data["fates"]["rank2"][0].update(
            response=[[0, 0], [0, 1]]
        )
    )
    add(lambda data: data["states"].append(copy.deepcopy(data["states"][0])))

    def break_retained_owner(data: dict[str, Any]) -> None:
        for record in data["fates"]["rank1"] + data["fates"]["rank2"] + data["fates"]["rank3"]:
            if record["kind"] == "retained":
                record["child"] = "D"
                return
        raise AssertionError("no retained record")

    add(break_retained_owner)

    def break_transfer(data: dict[str, Any]) -> None:
        for record in data["fates"]["rank1"] + data["fates"]["rank2"] + data["fates"]["rank3"]:
            if record["kind"] == "transferred":
                owner = tuple(record["owner"])
                record["child"] = f"O_{owner[0]}_{owner[1]}"
                return
        raise AssertionError("no transferred record")

    add(break_transfer)

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except FateError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted manifest accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_geometric_owner_fate_manifest.py [manifest.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        summary = validate_manifest(manifest)
        print(
            "accepted geometric owner/fate manifest: "
            f"{summary['responses']} responses, {summary['witnesses']} witnesses, "
            f"{summary['owner_count']} owners and "
            f"{len(summary['exported_bins'])} exported coefficient bins"
        )
        return

    systems, fate_totals, witness_total = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified geometric owner/fate checker: "
        f"{systems} random systems, {witness_total} witnesses partitioned as "
        f"{dict(sorted(fate_totals.items()))}, and {rejected} corrupted manifests rejected"
    )


if __name__ == "__main__":
    main()
