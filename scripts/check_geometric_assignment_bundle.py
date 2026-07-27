#!/usr/bin/env python3
"""Validate the exact bridge from owner/fate sources to assignment coefficients.

A bundle contains one complete geometric owner/fate manifest, its canonical SHA-256
digest, the uniform response denominator, and the exported labelled coefficient
table.  With no argument, deterministic random bundles and corruption tests run.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_geometric_owner_fate_manifest as owner_fate

Edge = tuple[int, int]


class BundleError(ValueError):
    """Raised when a geometric-to-assignment bundle is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BundleError(message)


def parse_integer(value: Any, path: str, *, positive: bool = False) -> int:
    require(type(value) is int, f"{path}: expected integer")
    if positive:
        require(value > 0, f"{path}: expected positive integer")
    return value


def canonical_digest(value: Any) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def parse_edge(value: Any, path: str, side: int) -> Edge:
    require(isinstance(value, list) and len(value) == 2, f"{path}: expected [u,v]")
    left = parse_integer(value[0], f"{path}[0]")
    right = parse_integer(value[1], f"{path}[1]")
    require(0 <= left < side and 0 <= right < side, f"{path}: edge outside grid")
    return left, right


def validate_bundle(bundle: Any) -> dict[str, int]:
    require(isinstance(bundle, dict), "bundle: expected object")
    require(bundle.get("version") == 1, "version: expected 1")
    source = bundle.get("source_manifest")
    require(isinstance(source, dict), "source_manifest: expected object")
    declared_digest = bundle.get("source_sha256")
    require(
        isinstance(declared_digest, str) and len(declared_digest) == 64,
        "source_sha256: expected hexadecimal SHA-256",
    )
    require(
        all(character in "0123456789abcdef" for character in declared_digest),
        "source_sha256: expected lowercase hexadecimal",
    )
    require(
        declared_digest == canonical_digest(source),
        "source_sha256: source digest mismatch",
    )

    try:
        source_summary = owner_fate.validate_manifest(source)
    except owner_fate.FateError as error:
        raise BundleError(f"source_manifest: {error}") from error

    side = source["side"]
    denominator = parse_integer(bundle.get("denominator"), "denominator", positive=True)
    require(
        denominator == source_summary["responses"],
        "denominator: must equal the exact uniform response count",
    )
    child_ids = {
        state["id"]
        for state in source["states"]
        if isinstance(state, dict) and isinstance(state.get("id"), str)
    }

    table = bundle.get("coefficient_table")
    require(isinstance(table, dict), "coefficient_table: expected object")
    observed: dict[tuple[int, str, tuple[Edge, ...]], int] = {}
    entries_checked = 0

    for rank, name in ((1, "edge"), (2, "pair"), (3, "triple")):
        entries = table.get(name, [])
        require(isinstance(entries, list), f"coefficient_table.{name}: expected list")
        for index, entry in enumerate(entries):
            path = f"coefficient_table.{name}[{index}]"
            require(isinstance(entry, dict), f"{path}: expected object")
            child = entry.get("child")
            require(child in child_ids, f"{path}.child: unknown source state")
            value = parse_integer(entry.get("value"), f"{path}.value", positive=True)

            if rank == 1:
                prescription = (parse_edge(entry.get("edge"), f"{path}.edge", side),)
            else:
                raw_edges = entry.get("edges")
                require(
                    isinstance(raw_edges, list) and len(raw_edges) == rank,
                    f"{path}.edges: wrong rank",
                )
                prescription = tuple(
                    sorted(
                        parse_edge(raw_edge, f"{path}.edges[{edge_index}]", side)
                        for edge_index, raw_edge in enumerate(raw_edges)
                    )
                )
                require(
                    len(set(prescription)) == rank,
                    f"{path}.edges: repeated edge",
                )
                require(
                    len({edge[0] for edge in prescription}) == rank
                    and len({edge[1] for edge in prescription}) == rank,
                    f"{path}.edges: incompatible prescription",
                )

            key = (rank, child, prescription)
            require(key not in observed, f"{path}: duplicate coefficient bin")
            observed[key] = value
            entries_checked += 1

    expected = source_summary["exported_bins"]
    require(
        observed == expected,
        "coefficient_table: does not exactly equal the owner/fate export",
    )
    return {
        "responses": denominator,
        "witnesses": source_summary["witnesses"],
        "coefficient_bins": entries_checked,
        "coefficient_mass": sum(observed.values()),
    }


def build_bundle(source: dict[str, Any]) -> dict[str, Any]:
    summary = owner_fate.validate_manifest(source)
    edge_entries: list[dict[str, Any]] = []
    pair_entries: list[dict[str, Any]] = []
    triple_entries: list[dict[str, Any]] = []

    for (rank, child, prescription), value in sorted(
        summary["exported_bins"].items(),
        key=lambda item: (item[0][0], item[0][1], item[0][2]),
    ):
        if rank == 1:
            edge_entries.append(
                {"child": child, "edge": list(prescription[0]), "value": value}
            )
        elif rank == 2:
            pair_entries.append(
                {
                    "child": child,
                    "edges": [list(edge) for edge in prescription],
                    "value": value,
                }
            )
        else:
            triple_entries.append(
                {
                    "child": child,
                    "edges": [list(edge) for edge in prescription],
                    "value": value,
                }
            )

    return {
        "version": 1,
        "source_manifest": source,
        "source_sha256": canonical_digest(source),
        "denominator": summary["responses"],
        "coefficient_table": {
            "edge": edge_entries,
            "pair": pair_entries,
            "triple": triple_entries,
        },
    }


def random_source(random: Random) -> dict[str, Any]:
    side = random.randint(3, 5)
    permutation = list(range(side))
    random.shuffle(permutation)
    allowed = {(left, permutation[left]) for left in range(side)}
    for left in range(side):
        for right in range(side):
            if random.random() < 0.56:
                allowed.add((left, right))
    grid = {(left, right) for left in range(side) for right in range(side)}
    background: list[tuple[int, int]] = []
    target_size = random.randint(3, 7)
    while len(background) < target_size:
        point = (random.randint(-3, side + 2), random.randint(-3, side + 2))
        if point not in grid and point not in background:
            background.append(point)
    return owner_fate.make_manifest(side, allowed, background, random)


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(1910)
    totals: Counter[str] = Counter()
    systems = 0
    for _ in range(300):
        bundle = build_bundle(random_source(random))
        summary = validate_bundle(bundle)
        totals["witnesses"] += summary["witnesses"]
        totals["bins"] += summary["coefficient_bins"]
        totals["mass"] += summary["coefficient_mass"]
        systems += 1
    require(systems == 300, "random tests: wrong system count")
    require(
        totals == Counter({"witnesses": 4072, "bins": 3125, "mass": 4138}),
        "random tests: unexpected bundle totals",
    )
    return systems, totals


def first_nonempty_table(bundle: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    for name in ("edge", "pair", "triple"):
        entries = bundle["coefficient_table"][name]
        if entries:
            return name, entries
    raise AssertionError("test bundle unexpectedly exports no coefficients")


def run_mutation_tests() -> int:
    random = Random(19)
    side = 4
    allowed = {(left, right) for left in range(side) for right in range(side)}
    background = [(-2, -2), (5, 5), (-2, 5), (5, -2), (-1, 2)]
    bundle = build_bundle(owner_fate.make_manifest(side, allowed, background, random))
    validate_bundle(bundle)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(bundle)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(source_sha256="0" * 64))
    add(lambda data: data.update(denominator=data["denominator"] + 1))

    def mutate_source_without_digest(data: dict[str, Any]) -> None:
        data["source_manifest"]["entry_order"].reverse()

    add(mutate_source_without_digest)

    name, _entries = first_nonempty_table(bundle)
    add(lambda data: data["coefficient_table"][name].pop())

    def change_value(data: dict[str, Any]) -> None:
        table_name, entries = first_nonempty_table(data)
        entries[0]["value"] += 1

    add(change_value)

    def duplicate_bin(data: dict[str, Any]) -> None:
        table_name, entries = first_nonempty_table(data)
        entries.append(copy.deepcopy(entries[0]))

    add(duplicate_bin)

    def unknown_child(data: dict[str, Any]) -> None:
        table_name, entries = first_nonempty_table(data)
        entries[0]["child"] = "UNKNOWN"

    add(unknown_child)

    def add_extra_bin(data: dict[str, Any]) -> None:
        data["coefficient_table"]["edge"].append(
            {"child": "P", "edge": [0, 0], "value": 1}
        )

    add(add_extra_bin)

    def zero_value(data: dict[str, Any]) -> None:
        table_name, entries = first_nonempty_table(data)
        entries[0]["value"] = 0

    add(zero_value)

    def incompatible_pair(data: dict[str, Any]) -> None:
        data["coefficient_table"]["pair"].append(
            {"child": "P", "edges": [[0, 0], [0, 1]], "value": 1}
        )

    add(incompatible_pair)

    rejected = 0
    for candidate in mutations:
        try:
            validate_bundle(candidate)
        except BundleError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted bundle accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_geometric_assignment_bundle.py [bundle.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            bundle = json.load(handle)
        summary = validate_bundle(bundle)
        print(
            "accepted geometric-to-assignment bundle: "
            f"{summary['responses']} responses, {summary['witnesses']} raw witnesses, "
            f"{summary['coefficient_bins']} exact labelled bins and "
            f"{summary['coefficient_mass']} exported coefficient mass"
        )
        return

    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified geometric-to-assignment bundle checker: "
        f"{systems} random bundles, {totals['witnesses']} source witnesses, "
        f"{totals['bins']} exact coefficient bins, {totals['mass']} exported mass, "
        f"and {rejected} corrupted bundles rejected"
    )


if __name__ == "__main__":
    main()
