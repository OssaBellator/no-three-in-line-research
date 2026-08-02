#!/usr/bin/env python3
"""Verify PX116-PX118: marker flow for frozen bridge-core edges."""
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


def root_trade_values(
    p: int,
    slope: int,
    intercept: int,
    block: Block,
) -> dict[int, int]:
    centre = sum(block) * pow(4, -1, p) % p
    return {
        x: (-slope * x + intercept + 2 * slope * centre) % p
        for x in block
    }


def bridge_source(
    p: int,
    slope: int,
    intercept: int,
    centre: int,
) -> tuple[Permutation, Permutation, Permutation, Block, set[int], Block, Block]:
    root = tuple((slope * x + intercept) % p for x in range(p))
    opposite_intercept = (intercept + 2 * slope * centre) % p
    opposite_slope = (-slope) % p
    opposite = tuple(
        (opposite_slope * x + opposite_intercept) % p for x in range(p)
    )
    quartic = {1, slope, p - 1, (-slope) % p}
    first = frozenset((centre + value) % p for value in quartic)
    second = frozenset(
        (centre + (1 + slope) * value) % p for value in quartic
    )

    double = list(root)
    for x in first | second:
        double[x] = opposite[x]

    z = 1
    a = centre
    r = z
    s = (-slope * z) % p
    A = double[a]
    rows = (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
    expected = (A, (A + s) % p, (A + r) % p, (A + r + s) % p)
    assert tuple(double[row] for row in rows) == expected
    new_images = ((A + r + s) % p, (A + r) % p, (A + s) % p, A)
    for row, image in zip(rows, new_images):
        double[row] = image

    source = tuple(double)
    assert is_strong(source)
    bridge = frozenset(rows)
    changed = {x for x in range(p) if source[x] != root[x]}
    assert changed == first | second | {centre}
    assert len(changed) == 9
    return source, root, opposite, bridge, changed, first, second


def apply_root_trade(
    mapping: Permutation,
    root: Permutation,
    slope: int,
    intercept: int,
    block: Block,
) -> Permutation:
    assert all(mapping[x] == root[x] for x in block)
    result = list(mapping)
    for x, image in root_trade_values(len(mapping), slope, intercept, block).items():
        result[x] = image
    candidate = tuple(result)
    assert is_strong(candidate)
    return candidate


def run_case(
    p: int,
    target_row: int,
    condition_rows: tuple[int, ...],
) -> int:
    slope = roots_minus_one(p)[0]
    intercept = 3 % p
    centre = 0
    source, root, opposite, bridge, changed, first, second = bridge_source(
        p, slope, intercept, centre
    )
    assert target_row in changed - bridge

    opposite_slope = (-slope) % p
    opposite_intercept = (intercept + 2 * slope * centre) % p
    parallel_class = quartic_class(p, slope, centre)
    row_to_block = {
        row: block for block in parallel_class for row in block
    }

    forced = {
        row_to_block[row]
        for row in condition_rows
        if row not in changed
    }
    marker = next(
        block
        for block in parallel_class
        if block not in {first, second} and block not in forced
    )
    restoration_blocks = set(forced) | {marker}

    prefinal = list(opposite)
    bridge_values = root_trade_values(
        p, opposite_slope, opposite_intercept, bridge
    )
    assert all(bridge_values[row] == source[row] for row in bridge)
    for row, image in bridge_values.items():
        prefinal[row] = image
    for block in restoration_blocks:
        values = root_trade_values(
            p, opposite_slope, opposite_intercept, block
        )
        assert all(values[row] == root[row] for row in block)
        for row, image in values.items():
            prefinal[row] = image
    prefinal = tuple(prefinal)
    assert is_strong(prefinal)

    conditions = {(row, source[row]) for row in condition_rows}
    target_edge = (target_row, source[target_row])
    assert all(prefinal[row] == image for row, image in conditions)
    assert prefinal[target_row] == target_edge[1]

    protected_supports = restoration_blocks | {bridge}
    protected_rows = set().union(*protected_supports)
    candidates = [
        block
        for block in all_blocks(p, opposite_slope)
        if target_row in block
        and block.isdisjoint(protected_rows)
        and not any(row in block for row in condition_rows)
    ]
    assert len(candidates) >= p - 55

    endpoints: set[Permutation] = set()
    for block in candidates:
        endpoint = apply_root_trade(
            prefinal,
            opposite,
            opposite_slope,
            opposite_intercept,
            block,
        )
        assert all(endpoint[row] == image for row, image in conditions)
        assert endpoint[target_row] != target_edge[1]
        changed_from_opposite = {
            row for row in range(p) if endpoint[row] != opposite[row]
        }
        assert len(changed_from_opposite) <= 20
        endpoints.add(endpoint)
    assert len(endpoints) == len(candidates)
    return len(candidates)


def verify_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    source, _, _, bridge, changed, _, _ = bridge_source(p, slope, 3 % p, 0)
    frozen = tuple(sorted(changed - bridge))
    outside = tuple(row for row in range(p) if row not in changed)
    bridge_rows = tuple(sorted(bridge))

    target = frozen[0]
    cases = (
        (),
        (bridge_rows[0],),
        (frozen[1],),
        (outside[0],),
        (bridge_rows[0], outside[0]),
        (frozen[1], outside[-1]),
        (0, outside[0]),
    )
    minima: Counter[int] = Counter()
    for condition_rows in cases:
        if target in condition_rows:
            continue
        count = run_case(p, target, condition_rows)
        rank = len(condition_rows)
        minima[rank] = min(minima.get(rank, count), count)

    assert all(count >= p - 55 for count in minima.values())
    print(f"p={p}: minimum exits by condition rank={dict(sorted(minima.items()))}")


def main() -> None:
    for p in (61, 73, 89):
        verify_prime(p)
    print("frozen bridge-core flow verified")


if __name__ == "__main__":
    main()
