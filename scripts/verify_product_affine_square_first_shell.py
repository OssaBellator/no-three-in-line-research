#!/usr/bin/env python3
"""Verify PX104-PX105: affine-square design and exact first shell."""
from __future__ import annotations

from collections import Counter
from itertools import combinations

Permutation = tuple[int, ...]
Block = frozenset[int]


def roots_minus_one(p: int) -> tuple[int, ...]:
    return tuple(value for value in range(p) if value * value % p == p - 1)


def affine_map(p: int, slope: int, translation: int = 0) -> Permutation:
    return tuple((slope * x + translation) % p for x in range(p))


def is_strong(mapping: Permutation) -> bool:
    p = len(mapping)
    return (
        len(set(mapping)) == p
        and len({(x - mapping[x]) % p for x in range(p)}) == p
        and len({(x + mapping[x]) % p for x in range(p)}) == p
    )


def apply_trade(
    mapping: Permutation, p: int, a: int, r: int, s: int
) -> Permutation | None:
    if 0 in (r % p, s % p, (r - s) % p, (r + s) % p):
        return None
    A = mapping[a]
    rows = (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
    old_images = (A, (A + s) % p, (A + r) % p, (A + r + s) % p)
    if tuple(mapping[row] for row in rows) != old_images:
        return None
    result = list(mapping)
    new_images = ((A + r + s) % p, (A + r) % p, (A + s) % p, A)
    for row, image in zip(rows, new_images):
        result[row] = image
    candidate = tuple(result)
    assert is_strong(candidate)
    return candidate


def trade_neighbours(mapping: Permutation) -> dict[Permutation, Block]:
    p = len(mapping)
    result: dict[Permutation, Block] = {}
    for a in range(p):
        for r in range(1, p):
            for s in range(1, p):
                candidate = apply_trade(mapping, p, a, r, s)
                if candidate is None:
                    continue
                support = frozenset(
                    row
                    for row, (old, new) in enumerate(zip(mapping, candidate))
                    if old != new
                )
                assert len(support) == 4
                previous = result.setdefault(candidate, support)
                assert previous == support
    return result


def verify_prime(p: int) -> None:
    roots = roots_minus_one(p)
    assert len(roots) == 2
    slope = roots[0]
    root = affine_map(p, slope)
    root_neighbours = trade_neighbours(root)
    blocks = tuple(set(root_neighbours.values()))

    assert len(blocks) == p * (p - 1) // 4
    point_counts = Counter(point for block in blocks for point in block)
    assert set(point_counts.values()) == {p - 1}
    pair_counts = Counter(
        pair for block in blocks for pair in combinations(sorted(block), 2)
    )
    assert set(pair_counts.values()) == {3}
    assert max(
        len(first & second)
        for index, first in enumerate(blocks)
        for second in blocks[index + 1 :]
    ) <= 2

    descendant, original_support = next(iter(root_neighbours.items()))
    root_intersections = Counter(len(original_support & block) for block in blocks)
    expected_intersections = {
        0: (p * p - 17 * p + 76) // 4,
        1: 4 * (p - 8),
        2: 12,
        4: 1,
    }
    assert root_intersections == expected_intersections

    descendant_neighbours = trade_neighbours(descendant)
    descendant_overlaps = Counter(
        len(original_support & support)
        for support in descendant_neighbours.values()
    )
    assert descendant_overlaps == {0: expected_intersections[0], 4: 1}
    assert root in descendant_neighbours
    assert len(descendant_neighbours) == (p * p - 17 * p + 80) // 4

    for candidate, support in descendant_neighbours.items():
        if support == original_support:
            assert candidate == root
        else:
            assert support.isdisjoint(original_support)
            assert support in blocks

    print(
        f"p={p}: blocks={len(blocks)}, intersections={dict(root_intersections)}, "
        f"shell_degree={len(descendant_neighbours)}"
    )


def main() -> None:
    for p in (13, 17, 29, 37):
        verify_prime(p)
    print("affine-square first-shell theorem verified")


if __name__ == "__main__":
    main()
