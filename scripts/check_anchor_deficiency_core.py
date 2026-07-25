#!/usr/bin/env python3
"""Verify PP3vi--PP3vt on a small weighted ownership host."""

from __future__ import annotations

import argparse
import json
from itertools import permutations
from pathlib import Path
from typing import Any

Assignment = tuple[int, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--size-limit", type=int, default=10)
    return parser.parse_args()


def parse_weights(raw: Any, labels: int, macros: int) -> list[list[float]]:
    if not isinstance(raw, list) or len(raw) != labels:
        raise ValueError("weights must contain one row per label")
    result: list[list[float]] = []
    for row_index, row in enumerate(raw):
        if not isinstance(row, list) or len(row) != macros:
            raise ValueError(f"weights[{row_index}] must have one entry per macro")
        parsed: list[float] = []
        for col_index, value in enumerate(row):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"weights[{row_index}][{col_index}] must be numeric")
            if value < 0:
                raise ValueError(f"weights[{row_index}][{col_index}] must be nonnegative")
            parsed.append(float(value))
        result.append(parsed)
    return result


def maximum_acceptable_matching(
    weights: list[list[float]], threshold: float, macro_of_slot: list[int]
) -> Assignment:
    labels = len(weights)
    slots = len(macro_of_slot)
    best_count = -1
    best: Assignment | None = None
    current = [-1] * labels
    used = [False] * slots

    def visit(label: int, count: int) -> None:
        nonlocal best_count, best
        if label == labels:
            candidate = tuple(current)
            if count > best_count or (count == best_count and (best is None or candidate < best)):
                best_count = count
                best = candidate
            return
        if count + (labels - label) < best_count:
            return

        current[label] = -1
        visit(label + 1, count)

        for slot, macro in enumerate(macro_of_slot):
            if used[slot] or weights[label][macro] > threshold:
                continue
            used[slot] = True
            current[label] = slot
            visit(label + 1, count + 1)
            current[label] = -1
            used[slot] = False

    visit(0, 0)
    if best is None:
        raise RuntimeError("matching search failed")
    return best


def alternating_core(
    assignment: Assignment,
    weights: list[list[float]],
    threshold: float,
    macro_of_slot: list[int],
) -> tuple[set[int], set[int]]:
    labels = len(weights)
    slots = len(macro_of_slot)
    matched_label_of_slot = [-1] * slots
    for label, slot in enumerate(assignment):
        if slot >= 0:
            matched_label_of_slot[slot] = label

    reachable_labels = {label for label, slot in enumerate(assignment) if slot < 0}
    reachable_slots: set[int] = set()
    queue: list[tuple[str, int]] = [("L", label) for label in sorted(reachable_labels)]
    cursor = 0

    while cursor < len(queue):
        side, vertex = queue[cursor]
        cursor += 1
        if side == "L":
            matched_slot = assignment[vertex]
            for slot, macro in enumerate(macro_of_slot):
                if slot == matched_slot:
                    continue
                if weights[vertex][macro] <= threshold and slot not in reachable_slots:
                    reachable_slots.add(slot)
                    queue.append(("R", slot))
        else:
            label = matched_label_of_slot[vertex]
            if label >= 0 and label not in reachable_labels:
                reachable_labels.add(label)
                queue.append(("L", label))

    return reachable_labels, reachable_slots


def completion_statistics(
    unmatched_labels: list[int],
    unmatched_slots: list[int],
    weights: list[list[float]],
    macro_of_slot: list[int],
) -> dict[str, Any]:
    d = len(unmatched_labels)
    if d == 0:
        return {
            "deficiency": 0,
            "slot_energy": 0.0,
            "energy_over_deficiency": 0.0,
            "minimum_bottleneck": 0.0,
            "minimum_total_cost": 0.0,
            "minimum_bottleneck_completion": [],
            "bottleneck_bound_verified": True,
        }

    matrix = [
        [weights[label][macro_of_slot[slot]] for slot in unmatched_slots]
        for label in unmatched_labels
    ]
    slot_energy = sum(sum(row) for row in matrix)
    best_bottleneck = float("inf")
    best_total = float("inf")
    best_perm: tuple[int, ...] | None = None
    for perm in permutations(range(d)):
        selected = [matrix[row][perm[row]] for row in range(d)]
        bottleneck = max(selected)
        total = sum(selected)
        if (bottleneck, total, perm) < (best_bottleneck, best_total, best_perm or perm):
            best_bottleneck = bottleneck
            best_total = total
            best_perm = perm

    assert best_perm is not None
    completion = [
        {
            "label": unmatched_labels[row],
            "slot": unmatched_slots[best_perm[row]],
            "macro": macro_of_slot[unmatched_slots[best_perm[row]]],
            "weight": matrix[row][best_perm[row]],
        }
        for row in range(d)
    ]
    bound = slot_energy / d
    return {
        "deficiency": d,
        "slot_energy": slot_energy,
        "energy_over_deficiency": bound,
        "minimum_bottleneck": best_bottleneck,
        "minimum_total_cost": best_total,
        "minimum_bottleneck_completion": completion,
        "bottleneck_bound_verified": best_bottleneck <= bound + 1e-12,
    }


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        macros = payload.get("macros")
        capacity = payload.get("capacity")
        threshold = payload.get("threshold")
        if not isinstance(macros, int) or isinstance(macros, bool) or macros <= 0:
            raise ValueError("macros must be a positive integer")
        if not isinstance(capacity, int) or isinstance(capacity, bool) or capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        if isinstance(threshold, bool) or not isinstance(threshold, (int, float)):
            raise ValueError("threshold must be numeric")
        labels = macros * capacity
        if labels > args.size_limit:
            raise ValueError(f"T={labels} exceeds size limit {args.size_limit}")
        weights = parse_weights(payload.get("weights"), labels, macros)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    macro_of_slot = [macro for macro in range(macros) for _ in range(capacity)]
    assignment = maximum_acceptable_matching(weights, float(threshold), macro_of_slot)
    matched_slots = {slot for slot in assignment if slot >= 0}
    unmatched_labels = [label for label, slot in enumerate(assignment) if slot < 0]
    unmatched_slots = [slot for slot in range(labels) if slot not in matched_slots]
    X, Y = alternating_core(assignment, weights, float(threshold), macro_of_slot)

    acceptable_neighborhood = {
        slot
        for label in X
        for slot, macro in enumerate(macro_of_slot)
        if weights[label][macro] <= float(threshold)
    }
    no_acceptable_core_cross_edge = all(
        weights[label][macro_of_slot[slot]] > float(threshold)
        for label in X
        for slot in range(labels)
        if slot not in Y
    )

    completion = completion_statistics(
        unmatched_labels, unmatched_slots, weights, macro_of_slot
    )
    result = {
        "T": labels,
        "maximum_acceptable_matching_size": labels - len(unmatched_labels),
        "assignment_by_label": list(assignment),
        "unmatched_labels": unmatched_labels,
        "unmatched_slots": unmatched_slots,
        "reachable_label_core_X": sorted(X),
        "reachable_slot_core_Y": sorted(Y),
        "Y_equals_acceptable_neighborhood_of_X": Y == acceptable_neighborhood,
        "core_deficiency": len(X) - len(Y),
        "core_deficiency_equals_global_deficiency": (
            len(X) - len(Y) == len(unmatched_labels)
        ),
        "no_acceptable_edge_from_X_to_slot_complement": no_acceptable_core_cross_edge,
        "completion": completion,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
