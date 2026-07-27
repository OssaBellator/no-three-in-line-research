#!/usr/bin/env python3
"""Validate response-compatible reuse of destroyed-triple cancellation credits.

One destroyed current triple may pay several deleted primitive witnesses provided
no response can contain two of those witnesses. The manifest therefore gives a
proper coloring of the exact deleted-witness conflict graph by destroyed triples.

With one JSON path, validate that manifest. With no argument, run deterministic
random systems and corruption tests.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from random import Random
from typing import Any

import check_geometric_owner_fate_manifest as owner_fate

Point = tuple[int, int]
Edge = tuple[int, int]
Prescription = tuple[Edge, ...]
TripleIndex = tuple[int, int, int]


class ColoredCancellationError(ValueError):
    """Raised when a conflict-colored cancellation manifest is invalid."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ColoredCancellationError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def parse_point(value: Any, path: str) -> Point:
    require(isinstance(value, list) and len(value) == 2, f"{path}: expected [x,y]")
    return parse_integer(value[0], f"{path}[0]"), parse_integer(value[1], f"{path}[1]")


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def destroyed_triples(points: list[Point], removed: set[int]) -> set[TripleIndex]:
    return {
        triple
        for triple in combinations(range(len(points)), 3)
        if removed.intersection(triple)
        and collinear(points[triple[0]], points[triple[1]], points[triple[2]])
    }


def response_contains(response: tuple[Edge, ...], prescription: Prescription) -> bool:
    return set(prescription).issubset(response)


def deleted_evidence_and_prescriptions(source: dict[str, Any]) -> dict[str, Prescription]:
    output: dict[str, Prescription] = {}
    side = source["side"]
    for rank, name in ((1, "rank1"), (2, "rank2"), (3, "rank3")):
        for index, record in enumerate(source["fates"].get(name, [])):
            if record.get("kind") != "deleted":
                continue
            evidence = record.get("evidence")
            path = f"source_manifest.fates.{name}[{index}].evidence"
            require(isinstance(evidence, str) and evidence, f"{path}: required")
            require(evidence not in output, f"{path}: deletion evidence must be unique")
            if rank == 1:
                prescription = (
                    owner_fate.parse_edge(record.get("response"), f"{path}.response", side),
                )
            else:
                prescription = tuple(
                    sorted(
                        owner_fate.parse_edge(edge, f"{path}.response", side)
                        for edge in record.get("response", [])
                    )
                )
                require(len(prescription) == rank, f"{path}.response: wrong rank")
            output[evidence] = prescription
    return output


def conflict_pairs(
    evidence_order: list[str],
    prescriptions: dict[str, Prescription],
    responses: list[tuple[Edge, ...]],
) -> set[tuple[str, str]]:
    occurrence = {
        evidence: {
            index
            for index, response in enumerate(responses)
            if response_contains(response, prescriptions[evidence])
        }
        for evidence in evidence_order
    }
    return {
        (first, second)
        for first, second in combinations(evidence_order, 2)
        if occurrence[first].intersection(occurrence[second])
    }


def parse_destroyed_triple(
    value: Any,
    path: str,
    points: list[Point],
    available: set[TripleIndex],
) -> TripleIndex:
    require(isinstance(value, list) and len(value) == 3, f"{path}: expected three indices")
    triple = tuple(parse_integer(entry, f"{path}[{index}]") for index, entry in enumerate(value))
    require(tuple(sorted(triple)) == triple, f"{path}: sort indices")
    require(len(set(triple)) == 3, f"{path}: duplicate index")
    require(all(0 <= index < len(points) for index in triple), f"{path}: index out of range")
    require(triple in available, f"{path}: not a destroyed collinear triple")
    return triple


def validate_manifest(manifest: Any, *, check_responses: bool = True) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest: expected object")
    require(manifest.get("version") == 1, "version: expected 1")
    source = manifest.get("source_manifest")
    require(isinstance(source, dict), "source_manifest: expected object")
    try:
        source_summary = owner_fate.validate_manifest(source)
    except owner_fate.FateError as error:
        raise ColoredCancellationError(f"source_manifest: {error}") from error

    raw_points = manifest.get("pre_response_points")
    require(isinstance(raw_points, list), "pre_response_points: expected list")
    points = [parse_point(value, f"pre_response_points[{index}]") for index, value in enumerate(raw_points)]
    require(len(set(points)) == len(points), "pre_response_points: duplicates")

    raw_removed = manifest.get("removed_point_indices")
    require(isinstance(raw_removed, list), "removed_point_indices: expected list")
    removed_list = [parse_integer(value, f"removed_point_indices[{index}]") for index, value in enumerate(raw_removed)]
    removed = set(removed_list)
    require(len(removed) == len(removed_list), "removed_point_indices: duplicates")
    require(removed, "removed_point_indices: expected at least one removal")
    require(all(0 <= index < len(points) for index in removed), "removed_point_indices: out of range")

    surviving = [point for index, point in enumerate(points) if index not in removed]
    source_background = [tuple(point) for point in source["background_points"]]
    require(surviving == source_background, "surviving points must equal source background_points in order")

    available = destroyed_triples(points, removed)
    deleted = deleted_evidence_and_prescriptions(source)
    evidence_order = sorted(deleted)

    raw_assignments = manifest.get("credit_assignments")
    require(isinstance(raw_assignments, list), "credit_assignments: expected list")
    assigned: dict[str, TripleIndex] = {}
    groups: defaultdict[TripleIndex, list[str]] = defaultdict(list)
    for index, record in enumerate(raw_assignments):
        path = f"credit_assignments[{index}]"
        require(isinstance(record, dict), f"{path}: expected object")
        evidence = record.get("evidence")
        require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
        require(evidence in deleted, f"{path}.evidence: unknown deleted witness")
        require(evidence not in assigned, f"{path}.evidence: duplicate")
        triple = parse_destroyed_triple(record.get("destroyed_triple"), f"{path}.destroyed_triple", points, available)
        assigned[evidence] = triple
        groups[triple].append(evidence)
    require(set(assigned) == set(deleted), "credit_assignments: omitted or extraneous deletion evidence")

    side = source["side"]
    allowed = {tuple(edge) for edge in source["allowed_edges"]}
    responses = owner_fate.perfect_matchings(side, allowed)
    conflicts = conflict_pairs(evidence_order, deleted, responses)

    for triple, members in groups.items():
        for first, second in combinations(sorted(members), 2):
            require((first, second) not in conflicts, f"destroyed credit {triple}: conflicting witnesses share one credit")

    raw_clique = manifest.get("optimality_clique", [])
    require(isinstance(raw_clique, list), "optimality_clique: expected list")
    clique: list[str] = []
    for index, evidence in enumerate(raw_clique):
        require(isinstance(evidence, str) and evidence in deleted, f"optimality_clique[{index}]: unknown evidence")
        require(evidence not in clique, f"optimality_clique[{index}]: duplicate")
        clique.append(evidence)
    for first, second in combinations(sorted(clique), 2):
        require((first, second) in conflicts, "optimality_clique: nonconflicting pair")

    used_credits = len(groups)
    deleted_count = len(deleted)
    saved_credits = deleted_count - used_credits
    unused_credit = len(available) - used_credits
    require(unused_credit >= 0, "credit assignment uses more colors than destroyed triples")
    clique_lower_bound = len(clique)
    optimal = int(bool(clique) and clique_lower_bound == used_credits)
    if manifest.get("require_optimal", False):
        require(optimal == 1, "require_optimal: coloring lacks matching clique lower bound")

    claims = manifest.get("claims")
    require(isinstance(claims, dict), "claims: expected object")
    expected_claims = {
        "deleted_witnesses": deleted_count,
        "destroyed_triples": len(available),
        "used_credits": used_credits,
        "saved_credits": saved_credits,
        "unused_credit": unused_credit,
        "conflict_edges": len(conflicts),
        "clique_lower_bound": clique_lower_bound,
        "optimal": optimal,
    }
    for key, expected in expected_claims.items():
        observed = parse_integer(claims.get(key), f"claims.{key}")
        require(observed == expected, f"claims.{key}: incorrect")

    response_checks = 0
    if check_responses:
        exported = source_summary["exported_bins"]
        edges, pairs, triples = owner_fate.extendable_prescriptions(responses)
        expected = owner_fate.expected_witnesses(edges, pairs, triples, source_background)
        for response in responses:
            for members in groups.values():
                occurring = sum(response_contains(response, deleted[evidence]) for evidence in members)
                require(occurring <= 1, "response contains two witnesses sharing one destroyed credit")
            deleted_occurring = sum(response_contains(response, prescription) for prescription in deleted.values())
            raw_occurring = sum(
                response_contains(response, prescription)
                for rank in (1, 2, 3)
                for _rank, prescription, _witness in expected[rank]
            )
            exported_occurring = sum(
                value
                for (_rank, _child, prescription), value in exported.items()
                if response_contains(response, prescription)
            )
            require(deleted_occurring <= used_credits, "responsewise colored cancellation capacity failed")
            require(
                raw_occurring - len(available) <= exported_occurring - unused_credit,
                "responsewise colored cancellation inequality failed",
            )
            response_checks += 1

    return {
        "responses": source_summary["responses"],
        "witnesses": source_summary["witnesses"],
        "deleted": deleted_count,
        "destroyed": len(available),
        "used_credits": used_credits,
        "saved_credits": saved_credits,
        "unused_credit": unused_credit,
        "conflict_edges": len(conflicts),
        "clique_lower_bound": clique_lower_bound,
        "optimal": optimal,
        "response_checks": response_checks,
    }


def exact_small_coloring(
    evidence_order: list[str], conflicts: set[tuple[str, str]]
) -> tuple[dict[str, int], list[str]]:
    """Exact helper used only by deterministic self-tests on small graphs."""
    adjacency = {evidence: set() for evidence in evidence_order}
    for first, second in conflicts:
        adjacency[first].add(second)
        adjacency[second].add(first)

    best_clique: list[str] = []

    def clique_search(candidates: list[str], chosen: list[str]) -> None:
        nonlocal best_clique
        if len(chosen) + len(candidates) <= len(best_clique):
            return
        if not candidates:
            if len(chosen) > len(best_clique):
                best_clique = chosen[:]
            return
        vertex = candidates[0]
        clique_search([item for item in candidates[1:] if item in adjacency[vertex]], chosen + [vertex])
        clique_search(candidates[1:], chosen)

    clique_search(evidence_order, [])

    colors: dict[str, int] = {}

    def choose_vertex() -> str:
        uncolored = [evidence for evidence in evidence_order if evidence not in colors]
        return max(
            uncolored,
            key=lambda evidence: (
                len({colors[other] for other in adjacency[evidence] if other in colors}),
                len(adjacency[evidence]),
                evidence,
            ),
        )

    def try_k(k: int) -> bool:
        colors.clear()

        def search() -> bool:
            if len(colors) == len(evidence_order):
                return True
            evidence = choose_vertex()
            forbidden = {colors[other] for other in adjacency[evidence] if other in colors}
            for color in range(k):
                if color in forbidden:
                    continue
                colors[evidence] = color
                if search():
                    return True
                del colors[evidence]
            return False

        return search()

    if not evidence_order:
        return {}, []
    for color_count in range(max(1, len(best_clique)), len(evidence_order) + 1):
        if try_k(color_count):
            return dict(colors), best_clique
    raise AssertionError("coloring search failed")


def random_source(random: Random) -> dict[str, Any]:
    side = random.randint(3, 5)
    permutation = list(range(side))
    random.shuffle(permutation)
    allowed = {(left, permutation[left]) for left in range(side)}
    for left in range(side):
        for right in range(side):
            if random.random() < 0.54:
                allowed.add((left, right))
    grid = {(left, right) for left in range(side) for right in range(side)}
    background: list[Point] = []
    target_size = random.randint(3, 6)
    while len(background) < target_size:
        point = (random.randint(-4, side + 3), random.randint(-4, side + 3))
        if point not in grid and point not in background:
            background.append(point)
    return owner_fate.make_manifest(side, allowed, background, random)


def build_manifest(source: dict[str, Any], *, require_optimal: bool = True) -> dict[str, Any]:
    owner_fate.validate_manifest(source)
    deleted = deleted_evidence_and_prescriptions(source)
    responses = owner_fate.perfect_matchings(source["side"], {tuple(edge) for edge in source["allowed_edges"]})
    evidence_order = sorted(deleted)
    conflicts = conflict_pairs(evidence_order, deleted, responses)
    coloring, clique = exact_small_coloring(evidence_order, conflicts)
    color_count = 0 if not coloring else max(coloring.values()) + 1

    background = [tuple(point) for point in source["background_points"]]
    target_credits = max(1, color_count + 1)
    construction_random = Random(700000 + len(background) * 101 + target_credits)
    points: list[Point] | None = None
    removed: set[int] | None = None
    available: list[TripleIndex] | None = None
    for attempt in range(2000):
        removed_points: list[Point] = []
        base_x = 100000 + 10000 * attempt
        for color in range(target_credits):
            x = base_x + 100 * color + construction_random.randint(0, 20)
            y = 200000 + 1000 * color + construction_random.randint(0, 50)
            dx = 1 + construction_random.randint(0, 20)
            dy = 100 + 3 * color + construction_random.randint(0, 20)
            removed_points.extend([(x, y), (x + dx, y + dy), (x + 2 * dx, y + 2 * dy)])
        candidate_points = background + removed_points
        candidate_removed = set(range(len(background), len(candidate_points)))
        candidate_available = sorted(destroyed_triples(candidate_points, candidate_removed))
        if len(candidate_available) == target_credits:
            points = candidate_points
            removed = candidate_removed
            available = candidate_available
            break
    require(points is not None and removed is not None and available is not None, "internal generator: exact credit construction failed")
    require(len(available) >= color_count, "internal generator: insufficient destroyed credits")

    assignments = [
        {"evidence": evidence, "destroyed_triple": list(available[coloring[evidence]])}
        for evidence in evidence_order
    ]
    groups = {tuple(record["destroyed_triple"]) for record in assignments}
    used = len(groups)
    optimal = int(bool(clique) and len(clique) == used)
    manifest = {
        "version": 1,
        "source_manifest": source,
        "pre_response_points": [list(point) for point in points],
        "removed_point_indices": sorted(removed),
        "credit_assignments": assignments,
        "optimality_clique": clique if optimal else [],
        "require_optimal": bool(require_optimal and optimal),
        "claims": {
            "deleted_witnesses": len(deleted),
            "destroyed_triples": len(available),
            "used_credits": used,
            "saved_credits": len(deleted) - used,
            "unused_credit": len(available) - used,
            "conflict_edges": len(conflicts),
            "clique_lower_bound": len(clique) if optimal else 0,
            "optimal": optimal,
        },
    }
    return manifest


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(1934)
    totals: Counter[str] = Counter()
    systems = 0
    for _ in range(300):
        manifest = build_manifest(random_source(random))
        summary = validate_manifest(manifest)
        for key in (
            "responses",
            "witnesses",
            "deleted",
            "destroyed",
            "used_credits",
            "saved_credits",
            "unused_credit",
            "conflict_edges",
            "optimal",
            "response_checks",
        ):
            totals[key] += summary[key]
        systems += 1
    require(systems == 300, "random tests: wrong system count")
    require(totals["saved_credits"] > 0, "random tests: expected credit reuse")
    require(totals["optimal"] > 0, "random tests: expected optimality certificates")
    return systems, totals


def run_mutation_tests() -> int:
    random = Random(41)
    manifest = build_manifest(random_source(random))
    while len(manifest["credit_assignments"]) < 2:
        manifest = build_manifest(random_source(random))
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data["credit_assignments"].pop())
    add(lambda data: data["credit_assignments"].append(copy.deepcopy(data["credit_assignments"][0])))
    add(lambda data: data["credit_assignments"][0].update(evidence="unknown"))
    add(lambda data: data["credit_assignments"][0].update(destroyed_triple=[0, 1, 2]))
    add(lambda data: data["claims"].update(saved_credits=-1))
    add(lambda data: data["claims"].update(unused_credit=99999))
    add(lambda data: data["optimality_clique"].append(data["optimality_clique"][0]) if data["optimality_clique"] else None)
    add(lambda data: data.update(require_optimal=True, optimality_clique=[]))
    add(lambda data: data["removed_point_indices"].pop())

    def force_conflicting_share(data: dict[str, Any]) -> None:
        source = data["source_manifest"]
        deleted = deleted_evidence_and_prescriptions(source)
        responses = owner_fate.perfect_matchings(source["side"], {tuple(edge) for edge in source["allowed_edges"]})
        pairs = sorted(conflict_pairs(sorted(deleted), deleted, responses))
        if not pairs:
            raise AssertionError("mutation source unexpectedly has no conflict")
        first, second = pairs[0]
        lookup = {record["evidence"]: record for record in data["credit_assignments"]}
        lookup[second]["destroyed_triple"] = copy.deepcopy(lookup[first]["destroyed_triple"])
        data["claims"]["used_credits"] = len({tuple(record["destroyed_triple"]) for record in data["credit_assignments"]})
        data["claims"]["saved_credits"] = data["claims"]["deleted_witnesses"] - data["claims"]["used_credits"]
        data["claims"]["unused_credit"] = data["claims"]["destroyed_triples"] - data["claims"]["used_credits"]

    add(force_conflicting_share)

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except ColoredCancellationError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted manifest accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_geometric_conflict_colored_cancellation.py [manifest.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        summary = validate_manifest(manifest)
        print(
            "accepted conflict-colored cancellation manifest: "
            f"{summary['responses']} responses, {summary['deleted']} deleted witnesses, "
            f"{summary['used_credits']} used credits, {summary['saved_credits']} saved credits, "
            f"{summary['unused_credit']} unused credits and optimal={summary['optimal']}"
        )
        return
    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified conflict-colored cancellation: "
        f"{systems} systems, {totals['deleted']} deleted witnesses, "
        f"{totals['used_credits']} used credits, {totals['saved_credits']} saved credits, "
        f"{totals['unused_credit']} unused credits, {totals['optimal']} optimality certificates, "
        f"{totals['response_checks']} response checks and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
