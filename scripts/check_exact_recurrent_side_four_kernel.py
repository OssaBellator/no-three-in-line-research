#!/usr/bin/env python3
"""Compile the exact 4x4 residual response-host kernel.

Local finite result only. It does not model global owner/provenance transitions
and can never certify the no-three-in-line conjecture.
"""
from __future__ import annotations

import argparse
import copy
import json
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable, Iterator

Edge = tuple[int, int]
Perm = tuple[int, ...]
SIDE = 4
DIAGONAL = frozenset((i, i) for i in range(SIDE))
TARGET: Edge = (0, 1)
ALLOWED = tuple(
    sorted(
        (r, c)
        for r in range(SIDE)
        for c in range(SIDE)
        if (r, c) not in DIAGONAL and (r, c) != TARGET
    )
)


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def edge_code(edge: Edge) -> str:
    return f"{edge[0]}{edge[1]}"


def permutation_code(perm: Perm) -> str:
    return "".join(map(str, perm))


def is_partial_matching(edges: Iterable[Edge]) -> bool:
    values = tuple(edges)
    return len({r for r, _ in values}) == len(values) == len(
        {c for _, c in values}
    )


def partial_matchings(edges: tuple[Edge, ...]) -> Iterator[tuple[Edge, ...]]:
    def walk(
        index: int,
        chosen: list[Edge],
        rows: set[int],
        columns: set[int],
    ) -> Iterator[tuple[Edge, ...]]:
        if index == len(edges):
            yield tuple(chosen)
            return
        yield from walk(index + 1, chosen, rows, columns)
        row, column = edges[index]
        if row not in rows and column not in columns:
            chosen.append((row, column))
            rows.add(row)
            columns.add(column)
            yield from walk(index + 1, chosen, rows, columns)
            columns.remove(column)
            rows.remove(row)
            chosen.pop()

    yield from walk(0, [], set(), set())


def edges_of(perm: Perm) -> frozenset[Edge]:
    return frozenset((row, perm[row]) for row in range(SIDE))


def collinear(first: Edge, second: Edge, third: Edge) -> bool:
    return (second[0] - first[0]) * (third[1] - first[1]) == (
        second[1] - first[1]
    ) * (third[0] - first[0])


def triple_count(perm: Perm) -> int:
    points = tuple((row, perm[row]) for row in range(SIDE))
    return sum(collinear(*triple) for triple in combinations(points, 3))


def base_responses() -> tuple[Perm, ...]:
    return tuple(
        perm
        for perm in permutations(range(SIDE))
        if all(
            (row, perm[row]) not in DIAGONAL and (row, perm[row]) != TARGET
            for row in range(SIDE)
        )
    )


def host_responses(
    deletions: Iterable[Edge], responses: tuple[Perm, ...]
) -> tuple[Perm, ...]:
    deleted = frozenset(deletions)
    return tuple(perm for perm in responses if edges_of(perm).isdisjoint(deleted))


def minimal_blockers(good: tuple[Perm, ...]) -> tuple[frozenset[Edge], ...]:
    good_edges = tuple(edges_of(perm) for perm in good)
    found: list[frozenset[Edge]] = []
    for size in range(1, SIDE + 1):
        for candidate in combinations(ALLOWED, size):
            if not is_partial_matching(candidate):
                continue
            block = frozenset(candidate)
            if all(block & response for response in good_edges) and not any(
                old < block for old in found
            ):
                found.append(block)
    return tuple(sorted(found, key=lambda block: tuple(sorted(block))))


def minimum_reopenings(
    deletions: tuple[Edge, ...], good: tuple[Perm, ...]
) -> tuple[tuple[tuple[Edge, ...], tuple[Perm, ...]], ...]:
    deleted = frozenset(deletions)
    for size in range(len(deletions) + 1):
        result: list[tuple[tuple[Edge, ...], tuple[Perm, ...]]] = []
        for restore in combinations(sorted(deletions), size):
            remaining = deleted.difference(restore)
            available = tuple(
                perm for perm in good if edges_of(perm).isdisjoint(remaining)
            )
            if available:
                result.append((restore, available))
        if result:
            return tuple(result)
    raise AuditError("no reopening reaches a good response")


def compile_kernel() -> dict[str, object]:
    responses = base_responses()
    counts = {perm: triple_count(perm) for perm in responses}
    good = tuple(perm for perm in responses if counts[perm] == 0)
    blockers = minimal_blockers(good)

    hosts: list[tuple[tuple[Edge, ...], tuple[Perm, ...]]] = []
    for deletions in partial_matchings(ALLOWED):
        available = host_responses(deletions, responses)
        if available:
            hosts.append((deletions, available))

    residual = [
        (deletions, available)
        for deletions, available in hosts
        if not any(perm in good for perm in available)
    ]

    records: list[dict[str, object]] = []
    for deletions, available in sorted(
        residual, key=lambda item: (len(item[0]), item[0])
    ):
        active = tuple(
            block for block in blockers if block <= frozenset(deletions)
        )
        reopenings = minimum_reopenings(deletions, good)
        records.append(
            {
                "id": "s4r-" + "-".join(edge_code(edge) for edge in deletions),
                "deletions": [edge_code(edge) for edge in deletions],
                "surviving_bad_responses": [
                    {
                        "permutation": permutation_code(perm),
                        "intrinsic_triples": counts[perm],
                    }
                    for perm in available
                ],
                "active_minimal_blockers": [
                    [edge_code(edge) for edge in sorted(block)] for block in active
                ],
                "minimum_reopening_number": len(reopenings[0][0]),
                "minimum_reopenings": [
                    {
                        "restore": [edge_code(edge) for edge in restore],
                        "available_good_responses": [
                            permutation_code(perm) for perm in available_good
                        ],
                    }
                    for restore, available_good in reopenings
                ],
            }
        )

    good_incidences = sum(
        counts[perm] == 0 for _, available in hosts for perm in available
    )
    manifest: dict[str, object] = {
        "schema": "exact-recurrent-side-four-host-kernel/v1",
        "scope": {
            "side": SIDE,
            "opposite": [edge_code(edge) for edge in sorted(DIAGONAL)],
            "target": edge_code(TARGET),
            "base_allowed": [edge_code(edge) for edge in ALLOWED],
            "deletion_rule": "partial matching",
            "response_rule": "perfect matching on remaining cells",
            "badness_rule": "intrinsic Euclidean collinear triples",
        },
        "responses": [
            {
                "permutation": permutation_code(perm),
                "intrinsic_triples": counts[perm],
                "classification": "good" if counts[perm] == 0 else "bad",
            }
            for perm in responses
        ],
        "minimal_good_response_blockers": [
            {"edges": [edge_code(edge) for edge in sorted(block)]}
            for block in blockers
        ],
        "aggregate": {
            "feasible_hosts": len(hosts),
            "response_incidences": sum(len(available) for _, available in hosts),
            "good_response_incidences": good_incidences,
            "bad_response_incidences": sum(
                len(available) for _, available in hosts
            )
            - good_incidences,
            "hosts_with_good_response": len(hosts) - len(residual),
            "residual_hosts": len(residual),
            "maximum_minimum_reopening_number": max(
                int(record["minimum_reopening_number"]) for record in records
            ),
        },
        "residual_hosts": records,
        "honesty": {
            "coordinate_host_response_complete": 1,
            "global_owner_fate_collision_interface_crt_complete": 0,
            "legal_global_reopening_proved": 0,
            "recurrent_offspring_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    validate(manifest)
    return manifest


def validate(manifest: dict[str, object]) -> None:
    require(
        manifest.get("schema") == "exact-recurrent-side-four-host-kernel/v1",
        "schema",
    )
    require(
        manifest.get("aggregate")
        == {
            "feasible_hosts": 86,
            "response_incidences": 206,
            "good_response_incidences": 137,
            "bad_response_incidences": 69,
            "hosts_with_good_response": 75,
            "residual_hosts": 11,
            "maximum_minimum_reopening_number": 2,
        },
        "aggregate",
    )
    responses = manifest.get("responses")
    require(isinstance(responses, list), "responses")
    require(
        {
            item["permutation"]: item["intrinsic_triples"]
            for item in responses
        }
        == {
            "2031": 0,
            "2301": 0,
            "2310": 0,
            "3012": 1,
            "3201": 0,
            "3210": 4,
        },
        "response spectrum",
    )
    blockers = manifest.get("minimal_good_response_blockers")
    require(isinstance(blockers, list), "blockers")
    require(
        {tuple(item["edges"]) for item in blockers}
        == {("02", "20"), ("02", "31"), ("13", "31")},
        "blocker basis",
    )
    residual = manifest.get("residual_hosts")
    require(isinstance(residual, list) and len(residual) == 11, "residual count")
    depths = [item["minimum_reopening_number"] for item in residual]
    require(depths.count(1) == 10 and depths.count(2) == 1, "reopening depths")
    require(len({item["id"] for item in residual}) == 11, "state ids")
    for item in residual:
        require(item["active_minimal_blockers"], f"{item['id']}: no blocker")
        require(item["minimum_reopenings"], f"{item['id']}: no reopening")
        require(
            all(
                len(choice["restore"]) == item["minimum_reopening_number"]
                for choice in item["minimum_reopenings"]
            ),
            f"{item['id']}: reopening size",
        )
    require(
        manifest.get("honesty")
        == {
            "coordinate_host_response_complete": 1,
            "global_owner_fate_collision_interface_crt_complete": 0,
            "legal_global_reopening_proved": 0,
            "recurrent_offspring_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "all_n_proved_by_checker": 0,
        },
        "honesty",
    )


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda value: value.update(schema="wrong"),
        lambda value: value["aggregate"].update(feasible_hosts=85),
        lambda value: value["responses"][0].update(intrinsic_triples=1),
        lambda value: value["minimal_good_response_blockers"].pop(),
        lambda value: value["residual_hosts"].pop(),
        lambda value: value["residual_hosts"][0].update(
            minimum_reopening_number=2
        ),
        lambda value: value["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate)
        except (AuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    manifest = compile_kernel()

    if arguments.write:
        arguments.write.parent.mkdir(parents=True, exist_ok=True)
        arguments.write.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if arguments.check:
        observed = json.loads(arguments.check.read_text(encoding="utf-8"))
        validate(observed)
        require(observed == manifest, "manifest differs from compiler output")

    aggregate = manifest["aggregate"]
    honesty = manifest["honesty"]
    require(isinstance(aggregate, dict), "aggregate output")
    require(isinstance(honesty, dict), "honesty output")
    print(
        json.dumps(
            {
                "checker": "exact-recurrent-side-four-host-kernel",
                **aggregate,
                "mutation_corruptions_rejected": mutation_audit(manifest),
                **honesty,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
