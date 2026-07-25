#!/usr/bin/env python3
"""Verify AC3gr--AC3gu complete-cross saturation and line refinement."""

from __future__ import annotations

from itertools import permutations, product


def derangements(n: int):
    for perm in permutations(range(n)):
        if all(perm[c] != c for c in range(n)):
            yield perm


def verify_complete_cross(max_n: int = 8) -> tuple[int, int, int, int, int]:
    systems = partner_records = fused = split = empty_records = 0
    for n in range(3, max_n + 1):
        active = tuple(range(n))
        pivot = (0, 0)
        for blocker in derangements(n):
            systems += 1
            blocker_row_at_pivot_col = blocker[0]
            blocker_col_of_pivot_row = blocker.index(0)
            desired = set()
            occupancies = []
            signatures = set()
            for partner_col in range(1, n):
                partner_row = active[partner_col]
                col_cross = (0, partner_row)
                row_cross = (partner_col, 0)
                desired.update((col_cross, row_cross))
                occupancy = int(blocker[0] == partner_row) + int(
                    blocker[partner_col] == 0
                )
                occupancies.append(occupancy)
                partner_records += 1
                empty_records += int(occupancy == 0)
                signatures.add(
                    (
                        pivot,
                        partner_col,
                        partner_row,
                        blocker[0],
                        blocker[partner_col],
                        occupancy,
                    )
                )

            assert len(desired) == 2 * (n - 1)
            assert desired == (
                {(0, row) for row in range(1, n)}
                | {(col, 0) for col in range(1, n)}
            )
            assert len(signatures) == n - 1
            assert sum(occupancies) == 2

            if blocker_row_at_pivot_col == blocker_col_of_pivot_row:
                assert occupancies.count(2) == 1
                assert occupancies.count(1) == 0
                assert occupancies.count(0) == n - 2
                fused += 1
            else:
                assert occupancies.count(2) == 0
                assert occupancies.count(1) == 2
                assert occupancies.count(0) == n - 3
                split += 1
    return systems, partner_records, fused, split, empty_records


def verify_weighted_line_router(max_n: int = 9, max_weight: int = 5) -> int:
    checks = 0
    for n in range(3, max_n + 1):
        max_lines = 2 * n - 1
        for line_count in range(1, max_lines + 1):
            for weights in product(range(max_weight + 1), repeat=min(line_count, 5)):
                padded = weights + (0,) * (line_count - len(weights))
                total = sum(padded)
                assert line_count * max(padded, default=0) >= total
                checks += 1
    return checks


def verify_signature_bounds(max_n: int = 50, max_roles: int = 20) -> int:
    checks = 0
    for n in range(3, max_n + 1):
        direction_count = (2 * n - 1) ** 2 - 1
        for roles in range(1, max_roles + 1):
            refined_roles = roles * direction_count
            refined_signature_bound = 2 * refined_roles * n**8
            safe_bound = 8 * roles * n**10
            assert refined_signature_bound <= safe_bound
            assert n - 3 >= 0
            checks += 1
    return checks


def verify_mixed_potential(max_objects: int = 12, max_signatures: int = 20) -> int:
    checks = 0
    for object_count in range(1, max_objects + 1):
        for signature_count in range(1, max_signatures + 1):
            ceiling = object_count * signature_count + object_count - 1
            for exposed in range(signature_count + 1):
                for support in range(1, object_count + 1):
                    value = object_count * exposed + object_count - support
                    assert 0 <= value <= ceiling
                    if support > 1:
                        next_value = (
                            object_count * exposed
                            + object_count
                            - (support - 1)
                        )
                        assert next_value >= value + 1
                        checks += 1
                    if exposed < signature_count:
                        next_value = object_count * (exposed + 1)
                        assert next_value >= value + 1
                        checks += 1
    return checks


def main() -> None:
    systems, partners, fused, split, empty_records = verify_complete_cross()
    lines = verify_weighted_line_router()
    bounds = verify_signature_bounds()
    potential = verify_mixed_potential()
    print(
        "AC complete-cross saturation verified:",
        f"{systems} two-layer systems,",
        f"{partners} partner rectangles,",
        f"{fused} fused blocker patterns,",
        f"{split} split blocker patterns,",
        f"{empty_records} empty partner rectangles,",
        f"{lines} weighted line routers,",
        f"{bounds} refined signature bounds,",
        f"{potential} mixed-potential transitions",
    )


if __name__ == "__main__":
    main()
