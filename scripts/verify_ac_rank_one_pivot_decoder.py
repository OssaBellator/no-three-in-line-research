#!/usr/bin/env python3
"""Finite checks for AC3fs--AC3fv."""

from __future__ import annotations

from itertools import combinations, permutations, product

Cell = tuple[int, int]


def cells(mapping: tuple[int, ...]) -> set[Cell]:
    return {(column, row) for column, row in enumerate(mapping)}


def is_permutation(mapping: tuple[int, ...]) -> bool:
    return sorted(mapping) == list(range(len(mapping)))


def disjoint(first: tuple[int, ...], second: tuple[int, ...]) -> bool:
    return all(first[column] != second[column] for column in range(len(first)))


def switched_active(size: int, c0: int, c1: int) -> tuple[int, ...]:
    active = list(range(size))
    active[c0], active[c1] = c1, c0
    return tuple(active)


def repair_blocker(
    blocker: tuple[int, ...], c0: int, c1: int
) -> tuple[tuple[int, ...], int]:
    size = len(blocker)
    cross0 = blocker[c0] == c1
    cross1 = blocker[c1] == c0
    occupancy = int(cross0) + int(cross1)
    repaired = list(blocker)

    if occupancy == 0:
        return tuple(repaired), occupancy

    outside = next(column for column in range(size) if column not in (c0, c1))

    if occupancy == 1:
        if cross0:
            # Pivot-column cross: use the partner blocker column.
            repaired[c0], repaired[c1] = repaired[c1], repaired[c0]
        else:
            # Partner-column cross: use an outside blocker column.
            repaired[c1], repaired[outside] = repaired[outside], repaired[c1]
        return tuple(repaired), occupancy

    # Full crossed diagonal.  The oriented three-cycle restores the partner
    # diagonal cell but never the pivot.
    r2 = repaired[outside]
    repaired[c0] = r2
    repaired[c1] = c1
    repaired[outside] = c0
    return tuple(repaired), occupancy


def verify_repairs() -> tuple[int, dict[int, int], int]:
    checks = 0
    occupancies = {0: 0, 1: 0, 2: 0}
    phase_flip_regressions = 0

    for size in range(3, 7):
        active = tuple(range(size))
        for blocker in permutations(range(size)):
            if not disjoint(active, blocker):
                continue
            for c0, c1 in permutations(range(size), 2):
                new_active = switched_active(size, c0, c1)
                repaired, occupancy = repair_blocker(blocker, c0, c1)
                pivot = (c0, c0)

                assert is_permutation(repaired)
                assert disjoint(new_active, repaired)
                assert pivot not in cells(new_active)
                assert pivot not in cells(repaired)
                occupancies[occupancy] += 1
                checks += 1

                if occupancy == 2:
                    naive = list(blocker)
                    naive[c0], naive[c1] = naive[c1], naive[c0]
                    assert pivot in cells(tuple(naive))
                    phase_flip_regressions += 1

    assert all(occupancies[value] > 0 for value in (0, 1, 2))
    return checks, occupancies, phase_flip_regressions


def verify_bucket_destruction() -> int:
    checks = 0
    for size in range(3, 7):
        active = tuple(range(size))
        for blocker in permutations(range(size)):
            if not disjoint(active, blocker):
                continue
            union_before = cells(active) | cells(blocker)
            for c0, c1 in permutations(range(size), 2):
                pivot = (c0, c0)
                if pivot not in union_before:
                    continue
                new_active = switched_active(size, c0, c1)
                repaired, _ = repair_blocker(blocker, c0, c1)
                union_after = cells(new_active) | cells(repaired)
                assert pivot not in union_after

                others = sorted(union_before - {pivot})
                for context in combinations(others, 2):
                    triple = {pivot, *context}
                    assert not triple.issubset(union_after)
                    checks += 1
    return checks


def verify_private_pivots() -> int:
    checks = 0
    universe = tuple(range(7))
    for parent_mask in range(1 << len(universe)):
        parent = {cell for cell in universe if (parent_mask >> cell) & 1}
        triples = []
        for triple in combinations(universe, 3):
            new_cells = set(triple) - parent
            if len(new_cells) == 1:
                triples.append((triple, next(iter(new_cells))))
        buckets: dict[int, set[tuple[int, int, int]]] = {}
        for triple, pivot in triples:
            buckets.setdefault(pivot, set()).add(triple)
        seen: set[tuple[int, int, int]] = set()
        for bucket in buckets.values():
            assert seen.isdisjoint(bucket)
            seen |= bucket
        assert len(seen) == len(triples)
        checks += len(triples)
    return checks


def verify_failed_ledgers() -> int:
    checks = 0
    for destroyed in range(1, 31):
        for ranks in product(range(11), repeat=3):
            if sum(ranks) < destroyed:
                continue
            assert 3 * max(ranks) >= destroyed
            checks += 1
    return checks


def verify_ticket() -> int:
    checks = 0
    for c0, c1, r0, r1 in product(range(4), repeat=4):
        if c0 == c1 or r0 == r1:
            continue
        forward = (frozenset((c0, c1)), frozenset((r0, r1)))
        reverse = (frozenset((c1, c0)), frozenset((r1, r0)))
        assert forward == reverse
        checks += 1
    return checks


def main() -> None:
    repair_checks, occupancies, phase_regressions = verify_repairs()
    bucket_checks = verify_bucket_destruction()
    private_checks = verify_private_pivots()
    ledger_checks = verify_failed_ledgers()
    ticket_checks = verify_ticket()

    print("AC rank-one pivot decoder verification passed")
    print(f"  union-safe repair checks: {repair_checks}")
    print(f"  occupancy totals: {occupancies}")
    print(f"  rejected phase-flip regressions: {phase_regressions}")
    print(f"  arbitrary context-bucket checks: {bucket_checks}")
    print(f"  private-pivot assignment checks: {private_checks}")
    print(f"  failed-bank rank ledgers: {ledger_checks}")
    print(f"  rectangle-ticket checks: {ticket_checks}")


if __name__ == "__main__":
    main()
