#!/usr/bin/env python3
"""Verify conditional completion of a binary endpoint-resource star."""

from __future__ import annotations

import argparse
import json
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

Cell = tuple[int, int]
Conflict = tuple[Cell, Cell]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--enumeration-limit", type=int, default=9)
    return parser.parse_args()


def parse_cell(raw: Any, label: str, n: int) -> Cell:
    if (
        not isinstance(raw, list)
        or len(raw) != 2
        or any(isinstance(value, bool) or not isinstance(value, int) for value in raw)
    ):
        raise ValueError(f"{label}: expected [left,right] integers")
    left, right = raw
    if not (0 <= left < n and 0 <= right < n):
        raise ValueError(f"{label}: cell outside [0,n)^2")
    return left, right


def enumerate_perfect_matchings(
    left_vertices: list[int], right_vertices: list[int], edges: set[Cell]
) -> list[tuple[int, ...]]:
    result: list[tuple[int, ...]] = []
    for image_order in permutations(right_vertices):
        if all((left, right) in edges for left, right in zip(left_vertices, image_order)):
            result.append(image_order)
    return result


def hall_witness(
    left_vertices: list[int], right_vertices: list[int], edges: set[Cell]
) -> dict[str, Any] | None:
    for size in range(1, len(left_vertices) + 1):
        for left_subset_tuple in combinations(left_vertices, size):
            left_subset = set(left_subset_tuple)
            neighbourhood = {
                right
                for left in left_subset
                for right in right_vertices
                if (left, right) in edges
            }
            if len(neighbourhood) < len(left_subset):
                forbidden_right = sorted(set(right_vertices) - neighbourhood)
                return {
                    "left_set": sorted(left_subset),
                    "neighbourhood": sorted(neighbourhood),
                    "forbidden_right_set": forbidden_right,
                    "deficiency": len(left_subset) - len(neighbourhood),
                    "rectangle_size": len(left_subset) * len(forbidden_right),
                }
    return None


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        n = payload.get("n")
        resource = payload.get("left_resource")
        if not isinstance(n, int) or isinstance(n, bool) or n <= 1:
            raise ValueError("n must be an integer greater than one")
        if n > args.enumeration_limit:
            raise ValueError(f"n={n} exceeds enumeration limit {args.enumeration_limit}")
        if not isinstance(resource, int) or isinstance(resource, bool) or not (0 <= resource < n):
            raise ValueError("left_resource must lie in [0,n)")

        raw_edges = payload.get("edges")
        raw_conflicts = payload.get("conflicts")
        if not isinstance(raw_edges, list) or not isinstance(raw_conflicts, list):
            raise ValueError("edges and conflicts must be lists")
        edges = {
            parse_cell(raw, f"edges[{index}]", n)
            for index, raw in enumerate(raw_edges)
        }
        if len(edges) != len(raw_edges):
            raise ValueError("edges contains duplicates")

        conflicts: list[Conflict] = []
        seen_conflicts: set[frozenset[Cell]] = set()
        for index, raw in enumerate(raw_conflicts):
            if not isinstance(raw, list) or len(raw) != 2:
                raise ValueError(f"conflicts[{index}] must contain two cells")
            first = parse_cell(raw[0], f"conflicts[{index}][0]", n)
            second = parse_cell(raw[1], f"conflicts[{index}][1]", n)
            if first not in edges or second not in edges:
                raise ValueError(f"conflicts[{index}] uses a cell outside the host")
            if first[0] == second[0] or first[1] == second[1]:
                raise ValueError(f"conflicts[{index}] cells must be compatible")
            incident = [cell for cell in (first, second) if cell[0] == resource]
            if len(incident) != 1:
                raise ValueError(f"conflicts[{index}] must touch the fixed left resource exactly once")
            key = frozenset((first, second))
            if key in seen_conflicts:
                raise ValueError("conflicts contains duplicates")
            seen_conflicts.add(key)
            conflicts.append((first, second))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    fibres: dict[Cell, set[Cell]] = {
        cell: set() for cell in sorted(edges) if cell[0] == resource
    }
    for first, second in conflicts:
        centre, partner = (first, second) if first[0] == resource else (second, first)
        fibres[centre].add(partner)

    centre_records: list[dict[str, Any]] = []
    for centre in sorted(fibres):
        _, removed_right = centre
        residual_left = [left for left in range(n) if left != resource]
        residual_right = [right for right in range(n) if right != removed_right]
        residual_edges = {
            cell
            for cell in edges
            if cell[0] != resource and cell[1] != removed_right and cell not in fibres[centre]
        }
        residual_matchings = enumerate_perfect_matchings(
            residual_left, residual_right, residual_edges
        )
        witness = None if residual_matchings else hall_witness(
            residual_left, residual_right, residual_edges
        )
        centre_records.append(
            {
                "centre": list(centre),
                "partner_count": len(fibres[centre]),
                "partners": [list(cell) for cell in sorted(fibres[centre])],
                "conditional_perfect_matching_count": len(residual_matchings),
                "one_conditional_matching": (
                    list(residual_matchings[0]) if residual_matchings else None
                ),
                "hall_witness": witness,
            }
        )

    full_matchings = enumerate_perfect_matchings(
        list(range(n)), list(range(n)), edges
    )
    avoiding_count = 0
    equivalence_verified = True
    conflict_sets = [set(conflict) for conflict in conflicts]
    for matching in full_matchings:
        selected = {(left, matching[left]) for left in range(n)}
        avoids = all(not conflict.issubset(selected) for conflict in conflict_sets)
        centre = (resource, matching[resource])
        conditional_avoids = selected.isdisjoint(fibres[centre])
        equivalence_verified &= avoids == conditional_avoids
        avoiding_count += int(avoids)

    partner_counts = [record["partner_count"] for record in centre_records]
    result = {
        "n": n,
        "left_resource": resource,
        "allowed_centre_count": len(centre_records),
        "binary_star_conflict_count": len(conflicts),
        "fibre_partition_sum": sum(partner_counts),
        "minimum_fibre_size": min(partner_counts) if partner_counts else None,
        "maximum_fibre_size": max(partner_counts) if partner_counts else None,
        "centres_with_conditional_completion": [
            record["centre"]
            for record in centre_records
            if record["conditional_perfect_matching_count"] > 0
        ],
        "centres": centre_records,
        "full_perfect_matching_count": len(full_matchings),
        "star_avoiding_perfect_matching_count": avoiding_count,
        "conditional_equivalence_verified": equivalence_verified,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
