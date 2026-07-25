#!/usr/bin/env python3
"""Check a binary-shadow congestion cover on an endpoint matching host.

The input JSON contains:
  q: positive integer
  allowed_edges: list of [left, right]
  binary_conflicts: list of [[l1, r1], [l2, r2]]
  cover: optional proposed list of [left, right]

For small instances the program also searches exactly for a minimum-congestion
binary cover by branching on an uncovered conflict.
"""
from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path
from typing import Any

Cell = tuple[int, int]
Conflict = tuple[Cell, Cell]


def parse_cell(raw: Any, q: int, label: str) -> Cell:
    if (
        not isinstance(raw, list)
        or len(raw) != 2
        or isinstance(raw[0], bool)
        or isinstance(raw[1], bool)
        or not isinstance(raw[0], int)
        or not isinstance(raw[1], int)
    ):
        raise ValueError(f"{label}: expected [left, right]")
    cell = (raw[0], raw[1])
    if not (0 <= cell[0] < q and 0 <= cell[1] < q):
        raise ValueError(f"{label}: cell {cell} outside [0,{q})^2")
    return cell


def parse_payload(path: Path) -> tuple[int, set[Cell], list[Conflict], set[Cell] | None]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON must be an object")
    q = payload.get("q")
    if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
        raise ValueError("q must be a positive integer")

    allowed_raw = payload.get("allowed_edges")
    if not isinstance(allowed_raw, list):
        raise ValueError("allowed_edges must be a list")
    allowed = {
        parse_cell(raw, q, f"allowed_edges[{index}]")
        for index, raw in enumerate(allowed_raw)
    }
    if len(allowed) != len(allowed_raw):
        raise ValueError("allowed_edges contains duplicates")

    conflicts_raw = payload.get("binary_conflicts")
    if not isinstance(conflicts_raw, list):
        raise ValueError("binary_conflicts must be a list")
    conflicts: list[Conflict] = []
    seen_conflicts: set[frozenset[Cell]] = set()
    for index, raw in enumerate(conflicts_raw):
        if not isinstance(raw, list) or len(raw) != 2:
            raise ValueError(f"binary_conflicts[{index}]: expected two cells")
        first = parse_cell(raw[0], q, f"binary_conflicts[{index}][0]")
        second = parse_cell(raw[1], q, f"binary_conflicts[{index}][1]")
        if first == second:
            raise ValueError(f"binary_conflicts[{index}]: repeated cell")
        if first not in allowed or second not in allowed:
            raise ValueError(f"binary_conflicts[{index}]: cell is not allowed")
        if first[0] == second[0] or first[1] == second[1]:
            raise ValueError(f"binary_conflicts[{index}]: cells are incompatible")
        key = frozenset((first, second))
        if key in seen_conflicts:
            raise ValueError(f"binary_conflicts[{index}]: duplicate conflict")
        seen_conflicts.add(key)
        conflicts.append((first, second))

    cover_raw = payload.get("cover")
    cover: set[Cell] | None = None
    if cover_raw is not None:
        if not isinstance(cover_raw, list):
            raise ValueError("cover must be a list")
        cover = {
            parse_cell(raw, q, f"cover[{index}]")
            for index, raw in enumerate(cover_raw)
        }
        if len(cover) != len(cover_raw):
            raise ValueError("cover contains duplicates")
        if not cover <= allowed:
            raise ValueError("cover contains a cell outside allowed_edges")

    return q, allowed, conflicts, cover


def cover_congestion(cover: set[Cell], q: int) -> tuple[int, list[int], list[int]]:
    left = [0] * q
    right = [0] * q
    for lft, rgt in cover:
        left[lft] += 1
        right[rgt] += 1
    return max(left + right, default=0), left, right


def is_cover(cover: set[Cell], conflicts: list[Conflict]) -> bool:
    return all(first in cover or second in cover for first, second in conflicts)


def maximum_matching(
    q: int, edges: set[Cell]
) -> tuple[dict[int, int], dict[int, int]]:
    adjacency = [[] for _ in range(q)]
    for left, right in sorted(edges):
        adjacency[left].append(right)

    left_to_right: dict[int, int] = {}
    right_to_left: dict[int, int] = {}

    def augment(left: int, seen: set[int]) -> bool:
        for right in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            owner = right_to_left.get(right)
            if owner is None or augment(owner, seen):
                right_to_left[right] = left
                left_to_right[left] = right
                return True
        return False

    for left in range(q):
        augment(left, set())
    return left_to_right, right_to_left


def hall_witness(
    q: int, edges: set[Cell], left_to_right: dict[int, int], right_to_left: dict[int, int]
) -> dict[str, Any] | None:
    if len(left_to_right) == q:
        return None
    adjacency = [[] for _ in range(q)]
    for left, right in edges:
        adjacency[left].append(right)

    unmatched_left = [left for left in range(q) if left not in left_to_right]
    seen_left = set(unmatched_left)
    seen_right: set[int] = set()
    queue: deque[tuple[str, int]] = deque(("L", left) for left in unmatched_left)

    while queue:
        side, vertex = queue.popleft()
        if side == "L":
            matched_right = left_to_right.get(vertex)
            for right in adjacency[vertex]:
                if right == matched_right:
                    continue
                if right not in seen_right:
                    seen_right.add(right)
                    queue.append(("R", right))
        else:
            owner = right_to_left.get(vertex)
            if owner is not None and owner not in seen_left:
                seen_left.add(owner)
                queue.append(("L", owner))

    x = sorted(seen_left)
    neighborhood = sorted({right for left in seen_left for right in adjacency[left]})
    y = sorted(set(range(q)) - set(neighborhood))
    return {
        "X": x,
        "N_X": neighborhood,
        "Y": y,
        "X_size": len(x),
        "N_X_size": len(neighborhood),
        "Y_size": len(y),
        "hall_deficiency": len(x) - len(neighborhood),
        "rectangle_area": len(x) * len(y),
        "sum_X_Y": len(x) + len(y),
    }


def exact_minimum_congestion_cover(
    q: int, allowed: set[Cell], conflicts: list[Conflict], force: bool
) -> tuple[set[Cell], int]:
    conflict_cells = {cell for conflict in conflicts for cell in conflict}
    if len(conflict_cells) > 30 and not force:
        raise ValueError(
            "exact search has more than 30 conflict cells; pass --force to continue"
        )

    incident: dict[Cell, list[int]] = {cell: [] for cell in conflict_cells}
    for index, (first, second) in enumerate(conflicts):
        incident[first].append(index)
        incident[second].append(index)

    best_cover = set(conflict_cells)
    best_congestion, _, _ = cover_congestion(best_cover, q)

    current: set[Cell] = set()
    left_counts = [0] * q
    right_counts = [0] * q
    covered = [False] * len(conflicts)

    def add(cell: Cell) -> list[int]:
        current.add(cell)
        left_counts[cell[0]] += 1
        right_counts[cell[1]] += 1
        changed: list[int] = []
        for index in incident[cell]:
            if not covered[index]:
                covered[index] = True
                changed.append(index)
        return changed

    def remove(cell: Cell, changed: list[int]) -> None:
        current.remove(cell)
        for index in changed:
            first, second = conflicts[index]
            covered[index] = first in current or second in current
        left_counts[cell[0]] -= 1
        right_counts[cell[1]] -= 1

    def recurse() -> None:
        nonlocal best_cover, best_congestion
        current_congestion = max(left_counts + right_counts, default=0)
        if current_congestion > best_congestion:
            return
        try:
            index = next(i for i, flag in enumerate(covered) if not flag)
        except StopIteration:
            if (
                current_congestion < best_congestion
                or (
                    current_congestion == best_congestion
                    and len(current) < len(best_cover)
                )
            ):
                best_cover = set(current)
                best_congestion = current_congestion
            return

        first, second = conflicts[index]
        options = sorted(
            (first, second),
            key=lambda cell: -sum(not covered[i] for i in incident[cell]),
        )
        for cell in options:
            if cell in current:
                continue
            changed = add(cell)
            recurse()
            remove(cell, changed)

    recurse()
    assert is_cover(best_cover, conflicts)
    assert best_cover <= allowed
    return best_cover, best_congestion


def encode_cells(cells: set[Cell] | list[Cell]) -> list[list[int]]:
    return [[left, right] for left, right in sorted(cells)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    try:
        q, allowed, conflicts, proposed = parse_payload(args.input)
        optimum, optimum_congestion = exact_minimum_congestion_cover(
            q, allowed, conflicts, args.force
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    residual = allowed - optimum
    left_to_right, right_to_left = maximum_matching(q, residual)
    result: dict[str, Any] = {
        "q": q,
        "allowed_edge_count": len(allowed),
        "binary_conflict_count": len(conflicts),
        "exact_minimum_congestion": optimum_congestion,
        "exact_cover_size": len(optimum),
        "exact_cover": encode_cells(optimum),
        "residual_edge_count": len(residual),
        "residual_maximum_matching_size": len(left_to_right),
        "residual_perfect_matching_exists": len(left_to_right) == q,
        "residual_matching": encode_cells(set(left_to_right.items())),
        "hall_witness": hall_witness(q, residual, left_to_right, right_to_left),
    }

    if proposed is not None:
        proposed_congestion, left_degrees, right_degrees = cover_congestion(proposed, q)
        result["proposed_cover"] = {
            "is_cover": is_cover(proposed, conflicts),
            "congestion": proposed_congestion,
            "left_degrees": left_degrees,
            "right_degrees": right_degrees,
            "cells": encode_cells(proposed),
        }

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
