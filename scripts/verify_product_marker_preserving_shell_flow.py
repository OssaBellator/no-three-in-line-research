#!/usr/bin/env python3
"""Verify PX113-PX115: marker-preserving shell flow."""
from __future__ import annotations

from collections import Counter

Block = frozenset[int]
Permutation = tuple[int, ...]


def roots_minus_one(p: int) -> tuple[int, ...]:
    return tuple(value for value in range(p) if value * value % p == p - 1)


def is_strong(mapping: Permutation) -> bool:
    p = len(mapping)
    return (
        len(set(mapping)) == p
        and len({(x - mapping[x]) % p for x in range(p)}) == p
        and len({(x + mapping[x]) % p for x in range(p)}) == p
    )


def all_blocks(p: int, slope: int) -> set[Block]:
    vertices = (0, 1, (-slope) % p, (1 - slope) % p)
    return {
        frozenset((a + r * value) % p for value in vertices)
        for a in range(p)
        for r in range(1, p)
    }


def quartic_class(p: int, slope: int, centre: int) -> tuple[Block, ...]:
    quartic = {1, slope, p - 1, (-slope) % p}
    unseen = set(range(p)) - {centre}
    blocks: list[Block] = []
    while unseen:
        value = min(unseen)
        radius = (value - centre) % p
        block = frozenset((centre + radius * unit) % p for unit in quartic)
        blocks.append(block)
        unseen -= block
    return tuple(sorted(blocks, key=lambda block: tuple(sorted(block))))


def flip_root_block(
    mapping: Permutation,
    root: Permutation,
    slope: int,
    intercept: int,
    block: Block,
) -> Permutation:
    p = len(mapping)
    assert all(mapping[x] == root[x] for x in block)
    centre = sum(block) * pow(4, -1, p) % p
    result = list(mapping)
    for x in block:
        result[x] = (-slope * x + intercept + 2 * slope * centre) % p
    candidate = tuple(result)
    assert is_strong(candidate)
    return candidate


def run_case(
    p: int,
    centre: int,
    source_block: Block,
    target_row: int,
    condition_rows: tuple[int, ...],
) -> int:
    slope = roots_minus_one(p)[0]
    intercept = 3 % p
    root = tuple((slope * x + intercept) % p for x in range(p))
    opposite_intercept = (intercept + 2 * slope * centre) % p
    opposite_slope = (-slope) % p
    opposite = tuple(
        (opposite_slope * x + opposite_intercept) % p for x in range(p)
    )

    source = list(root)
    for x in source_block:
        source[x] = opposite[x]
    source = tuple(source)
    assert is_strong(source)
    assert target_row in source_block

    parallel_class = quartic_class(p, slope, centre)
    assert source_block in parallel_class
    row_to_block = {
        row: block for block in parallel_class for row in block
    }

    forced_markers = {
        row_to_block[row]
        for row in condition_rows
        if row not in source_block and row != centre
    }
    marker = next(
        block
        for block in parallel_class
        if block != source_block and block not in forced_markers
    )
    markers = set(forced_markers) | {marker}
    assert 1 <= len(markers) <= 3

    prefinal = list(opposite)
    for block in markers:
        for row in block:
            prefinal[row] = root[row]
    prefinal = tuple(prefinal)
    assert is_strong(prefinal)

    conditions = {(row, source[row]) for row in condition_rows}
    target_edge = (target_row, source[target_row])
    assert all(prefinal[row] == image for row, image in conditions)
    assert prefinal[target_row] == target_edge[1]

    marker_rows = set().union(*markers)
    opposite_blocks = all_blocks(p, opposite_slope)
    candidates = [
        block
        for block in opposite_blocks
        if target_row in block
        and block.isdisjoint(marker_rows)
        and not any(row in block for row in condition_rows)
        and block != source_block
    ]
    assert len(candidates) >= p - 44

    endpoints: set[Permutation] = set()
    for block in candidates:
        endpoint = flip_root_block(
            prefinal,
            opposite,
            opposite_slope,
            opposite_intercept,
            block,
        )
        assert all(endpoint[row] == image for row, image in conditions)
        assert endpoint[target_row] != target_edge[1]
        changed = {row for row in range(p) if endpoint[row] != opposite[row]}
        assert len(changed) <= 16
        endpoints.add(endpoint)
    assert len(endpoints) == len(candidates)
    return len(candidates)


def verify_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    centre = 0
    parallel_class = quartic_class(p, slope, centre)
    source_block = parallel_class[0]
    target_row = min(source_block)
    other_source_rows = tuple(sorted(source_block - {target_row}))
    outside_rows = tuple(
        row for row in range(p) if row not in source_block and row != centre
    )

    cases = (
        (),
        (centre,),
        (other_source_rows[0],),
        (centre, other_source_rows[0]),
        (outside_rows[0], outside_rows[-1]),
        (other_source_rows[0], outside_rows[0]),
    )
    counts = Counter()
    for condition_rows in cases:
        count = run_case(
            p,
            centre,
            source_block,
            target_row,
            condition_rows,
        )
        counts[len(condition_rows)] = min(counts.get(len(condition_rows), count), count)

    assert all(count >= p - 44 for count in counts.values())
    print(f"p={p}: minimum exits by condition rank={dict(sorted(counts.items()))}")


def main() -> None:
    for p in (53, 61, 73):
        verify_prime(p)
    print("marker-preserving shell flow verified")


if __name__ == "__main__":
    main()
