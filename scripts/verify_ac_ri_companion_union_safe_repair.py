#!/usr/bin/env python3
"""Finite checks for AC3fw--AC3fy."""

from __future__ import annotations

from itertools import permutations

Cell = tuple[int, int]


def layer_cells(mapping: tuple[int, ...]) -> set[Cell]:
    return {(column, row) for column, row in enumerate(mapping)}


def disjoint(first: tuple[int, ...], second: tuple[int, ...]) -> bool:
    return all(first[column] != second[column] for column in range(len(first)))


def switched_active(size: int, a0: int, a1: int) -> tuple[int, ...]:
    active = list(range(size))
    active[a0], active[a1] = a1, a0
    return tuple(active)


def repair_union_safe(
    blocker: tuple[int, ...], a0: int, a1: int
) -> tuple[tuple[int, ...], int]:
    size = len(blocker)
    cross0 = blocker[a0] == a1
    cross1 = blocker[a1] == a0
    occupancy = int(cross0) + int(cross1)
    repaired = list(blocker)
    outside = [column for column in range(size) if column not in (a0, a1)]

    if occupancy == 0:
        return tuple(repaired), occupancy

    if occupancy == 1:
        blocked_column = a0 if cross0 else a1
        forbidden_old_row = a0 if cross0 else a1
        auxiliary = next(
            column
            for column in outside
            if repaired[column] != forbidden_old_row
        )
        repaired[blocked_column], repaired[auxiliary] = (
            repaired[auxiliary],
            repaired[blocked_column],
        )
        return tuple(repaired), occupancy

    a2, a3 = outside[:2]
    s2, s3 = repaired[a2], repaired[a3]
    repaired[a0] = s2
    repaired[a1] = s3
    repaired[a2] = a0
    repaired[a3] = a1
    return tuple(repaired), occupancy


def verify() -> tuple[int, dict[int, int], int, int]:
    checks = 0
    occupancies = {0: 0, 1: 0, 2: 0}
    phase_flip_counterexamples = 0
    fixed_edge_checks = 0

    for size in range(4, 8):
        active = tuple(range(size))
        for blocker in permutations(range(size)):
            if not disjoint(active, blocker):
                continue
            for a0, a1 in permutations(range(size), 2):
                outside = [column for column in range(size) if column not in (a0, a1)]
                fixed_columns = outside[:2]
                fixed_edge = {(column, column) for column in fixed_columns}
                old_anchors = {(a0, a0), (a1, a1)}

                new_active = switched_active(size, a0, a1)
                repaired, occupancy = repair_union_safe(blocker, a0, a1)
                final_union = layer_cells(new_active) | layer_cells(repaired)

                assert sorted(repaired) == list(range(size))
                assert disjoint(new_active, repaired)
                assert old_anchors.isdisjoint(final_union)
                assert fixed_edge.issubset(layer_cells(new_active))
                occupancies[occupancy] += 1
                checks += 1
                fixed_edge_checks += len(fixed_edge)

                if occupancy == 2:
                    naive = list(blocker)
                    naive[a0], naive[a1] = naive[a1], naive[a0]
                    naive_union = layer_cells(new_active) | layer_cells(tuple(naive))
                    assert old_anchors.issubset(naive_union)
                    phase_flip_counterexamples += 1

    assert all(occupancies[value] > 0 for value in (0, 1, 2))
    return checks, occupancies, phase_flip_counterexamples, fixed_edge_checks


def main() -> None:
    checks, occupancies, regressions, fixed_checks = verify()
    print("AC RI companion union-safe repair verification passed")
    print(f"  union-safe companion repairs: {checks}")
    print(f"  blocker occupancy totals: {occupancies}")
    print(f"  fixed-edge preservation checks: {fixed_checks}")
    print(f"  phase-flip union counterexamples: {regressions}")


if __name__ == "__main__":
    main()
