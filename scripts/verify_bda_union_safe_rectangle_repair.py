#!/usr/bin/env python3
"""Finite checks for BDA5ai--BDA5ak."""

from __future__ import annotations

from itertools import permutations

Cell = tuple[int, int]


def layer_cells(mapping: tuple[int, ...]) -> set[Cell]:
    return {(column, row) for column, row in enumerate(mapping)}


def disjoint(first: tuple[int, ...], second: tuple[int, ...]) -> bool:
    return all(first[column] != second[column] for column in range(len(first)))


def switched_active(size: int, c0: int, c1: int) -> tuple[int, ...]:
    active = list(range(size))
    active[c0], active[c1] = c1, c0
    return tuple(active)


def repair_union_safe(
    blocker: tuple[int, ...], c0: int, c1: int
) -> tuple[tuple[int, ...], int]:
    size = len(blocker)
    cross0 = blocker[c0] == c1
    cross1 = blocker[c1] == c0
    occupancy = int(cross0) + int(cross1)
    repaired = list(blocker)
    outside = [column for column in range(size) if column not in (c0, c1)]

    if occupancy == 0:
        return tuple(repaired), occupancy

    if occupancy == 1:
        blocked_column = c0 if cross0 else c1
        forbidden_old_row = c0 if cross0 else c1
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

    c2, c3 = outside[:2]
    s2, s3 = repaired[c2], repaired[c3]
    repaired[c0] = s2
    repaired[c1] = s3
    repaired[c2] = c0
    repaired[c3] = c1
    return tuple(repaired), occupancy


def verify() -> tuple[int, dict[int, int], int]:
    checks = 0
    occupancies = {0: 0, 1: 0, 2: 0}
    phase_flip_counterexamples = 0

    for size in range(5, 8):
        active = tuple(range(size))
        for blocker in permutations(range(size)):
            if not disjoint(active, blocker):
                continue
            for c0, c1 in permutations(range(size), 2):
                new_active = switched_active(size, c0, c1)
                repaired, occupancy = repair_union_safe(blocker, c0, c1)
                old_endpoints = {(c0, c0), (c1, c1)}
                final_union = layer_cells(new_active) | layer_cells(repaired)

                assert sorted(repaired) == list(range(size))
                assert disjoint(new_active, repaired)
                assert old_endpoints.isdisjoint(final_union)
                occupancies[occupancy] += 1
                checks += 1

                if occupancy == 2:
                    naive = list(blocker)
                    naive[c0], naive[c1] = naive[c1], naive[c0]
                    naive_union = layer_cells(new_active) | layer_cells(tuple(naive))
                    assert old_endpoints.issubset(naive_union)
                    phase_flip_counterexamples += 1

    assert all(occupancies[value] > 0 for value in (0, 1, 2))
    return checks, occupancies, phase_flip_counterexamples


def main() -> None:
    checks, occupancies, regressions = verify()
    print("BDA union-safe rectangle repair verification passed")
    print(f"  union-safe repairs: {checks}")
    print(f"  blocker occupancy totals: {occupancies}")
    print(f"  phase-flip union counterexamples: {regressions}")


if __name__ == "__main__":
    main()
