#!/usr/bin/env python3
"""Verify PX119-PX121: active bridge-support flow and exceptions."""
from __future__ import annotations

from collections import Counter
from itertools import combinations

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
    p: int, slope: int, intercept: int, block: Block
) -> dict[int, int]:
    centre = sum(block) * pow(4, -1, p) % p
    return {
        x: (-slope * x + intercept + 2 * slope * centre) % p
        for x in block
    }


def bridge_source(
    p: int, slope: int, intercept: int, centre: int = 0
) -> tuple[
    Permutation,
    Permutation,
    Permutation,
    Permutation,
    Block,
    Block,
    Block,
    set[int],
    int,
]:
    root = tuple((slope * x + intercept) % p for x in range(p))
    first_opposite_slope = (-slope) % p
    first_opposite_intercept = (intercept + 2 * slope * centre) % p
    first_opposite = tuple(
        (first_opposite_slope * x + first_opposite_intercept) % p
        for x in range(p)
    )

    quartic = {1, slope, p - 1, (-slope) % p}
    first = frozenset((centre + unit) % p for unit in quartic)
    second = frozenset(
        (centre + (1 + slope) * unit) % p for unit in quartic
    )
    bridge = frozenset(
        (centre, (centre + 1) % p, (centre + slope) % p, (centre + 1 + slope) % p)
    )
    bridge_centre = sum(bridge) * pow(4, -1, p) % p

    second_root_slope = slope
    second_root_intercept = (
        first_opposite_intercept + 2 * first_opposite_slope * bridge_centre
    ) % p
    second_root = tuple(
        (second_root_slope * x + second_root_intercept) % p
        for x in range(p)
    )

    source = list(root)
    for x in first | second:
        source[x] = first_opposite[x]
    for x in bridge:
        source[x] = second_root[x]
    source = tuple(source)
    assert is_strong(source)

    changed = first | second | {centre}
    assert len(changed) == 9
    assert all(source[x] == second_root[x] for x in bridge)
    assert all(source[x] == first_opposite[x] for x in changed - bridge)
    assert all(source[x] == root[x] for x in set(range(p)) - changed)
    return (
        root,
        first_opposite,
        second_root,
        source,
        first,
        second,
        bridge,
        changed,
        bridge_centre,
    )


def unique_restoration_block(
    root: Permutation,
    slope: int,
    row: int,
    target: int,
) -> Block:
    p = len(root)
    delta = (target - root[row]) % p
    assert delta != 0
    centre = (row + delta * pow((2 * slope) % p, -1, p)) % p
    radius = (row - centre) % p
    quartic = {1, slope, p - 1, (-slope) % p}
    block = frozenset((centre + radius * unit) % p for unit in quartic)
    values = root_trade_values(p, slope, root[0], block)
    assert values[row] == target
    return block


def apply_disjoint_root_trades(
    root: Permutation,
    slope: int,
    blocks: tuple[Block, ...],
) -> Permutation:
    assert all(
        first.isdisjoint(second)
        for first, second in combinations(blocks, 2)
    )
    result = list(root)
    for block in blocks:
        values = root_trade_values(len(root), slope, root[0], block)
        for row, image in values.items():
            result[row] = image
    candidate = tuple(result)
    assert is_strong(candidate)
    return candidate


def build_restorations(
    root: Permutation,
    slope: int,
    source: Permutation,
    bridge: Block,
    condition_rows: tuple[int, ...],
) -> tuple[Block, ...]:
    result: list[Block] = []
    for row in condition_rows:
        if row in bridge:
            continue
        block = unique_restoration_block(root, slope, row, source[row])
        if block not in result:
            result.append(block)
    return tuple(result)


def run_nonexceptional_case(
    p: int,
    target_row: int,
    condition_rows: tuple[int, ...],
) -> int | None:
    slope = roots_minus_one(p)[0]
    (
        first_root,
        first_opposite,
        second_root,
        source,
        _,
        _,
        bridge,
        changed,
        bridge_centre,
    ) = bridge_source(p, slope, 3 % p)
    assert target_row in bridge
    assert target_row not in condition_rows

    restorations = build_restorations(
        second_root, slope, source, bridge, condition_rows
    )
    if any(
        not first.isdisjoint(second)
        for first, second in combinations(restorations, 2)
    ):
        return None

    second_class = quartic_class(p, (-slope) % p, bridge_centre)
    assert bridge in second_class
    marker = next(
        block
        for block in second_class
        if block != bridge
        and all(block.isdisjoint(restoration) for restoration in restorations)
    )

    # Algebraic target-disjointness: no restoration square contains a bridge row.
    assert all(target_row not in restoration for restoration in restorations)

    protected_blocks = (marker,) + restorations
    protected_rows = set().union(*protected_blocks)
    candidates = [
        block
        for block in all_blocks(p, slope)
        if target_row in block
        and block.isdisjoint(protected_rows)
        and not any(row in block for row in condition_rows)
    ]
    assert len(candidates) >= p - 43

    conditions = {(row, source[row]) for row in condition_rows}
    endpoints: set[Permutation] = set()
    for final_block in candidates:
        endpoint = apply_disjoint_root_trades(
            second_root,
            slope,
            (marker, final_block) + restorations,
        )
        assert all(endpoint[row] == image for row, image in conditions)
        assert endpoint[target_row] != source[target_row]
        changed_from_root = {
            row for row in range(p) if endpoint[row] != second_root[row]
        }
        assert len(changed_from_root) <= 16
        endpoints.add(endpoint)
    assert len(endpoints) == len(candidates)
    return len(candidates)


def verify_geometry(p: int) -> None:
    slope = roots_minus_one(p)[0]
    (
        first_root,
        first_opposite,
        second_root,
        source,
        _,
        _,
        bridge,
        changed,
        bridge_centre,
    ) = bridge_source(p, slope, 3 % p)

    second_class = quartic_class(p, (-slope) % p, bridge_centre)
    assert bridge in second_class
    quartic = {1, slope, p - 1, (-slope) % p}
    offset_set = {
        bridge_centre * (1 - unit) % p for unit in quartic
    }

    for row in range(p):
        if row in bridge:
            continue
        restoration = unique_restoration_block(
            second_root, slope, row, source[row]
        )
        if row in changed - bridge:
            assert restoration in second_class
        else:
            assert restoration == frozenset(
                (row + offset) % p for offset in offset_set
            )
        assert restoration.isdisjoint(bridge)

    rows = tuple(row for row in range(p) if row not in bridge)
    exception_degrees = Counter()
    for first_row in rows:
        first_block = unique_restoration_block(
            second_root, slope, first_row, source[first_row]
        )
        degree = 0
        for second_row in rows:
            if second_row == first_row:
                continue
            second_block = unique_restoration_block(
                second_root, slope, second_row, source[second_row]
            )
            if first_block != second_block and not first_block.isdisjoint(second_block):
                degree += 1
        exception_degrees[first_row] = degree
    assert max(exception_degrees.values(), default=0) <= 32


def verify_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    _, _, _, source, _, _, bridge, _, _ = bridge_source(p, slope, 3 % p)
    target = min(bridge)
    compatible_rows = tuple(
        row
        for row in range(p)
        if row != target and source[row] != source[target]
    )

    minimum = {0: p * p, 1: p * p, 2: p * p}
    exceptional_pairs = 0
    result = run_nonexceptional_case(p, target, ())
    assert result is not None
    minimum[0] = result

    for row in compatible_rows:
        result = run_nonexceptional_case(p, target, (row,))
        assert result is not None
        minimum[1] = min(minimum[1], result)

    for first_index, first_row in enumerate(compatible_rows):
        for second_row in compatible_rows[first_index + 1 :]:
            result = run_nonexceptional_case(
                p, target, (first_row, second_row)
            )
            if result is None:
                exceptional_pairs += 1
            else:
                minimum[2] = min(minimum[2], result)

    assert all(value >= p - 43 for value in minimum.values())
    verify_geometry(p)
    print(
        f"p={p}: minimum exits={minimum}, "
        f"exceptional rank-two pairs={exceptional_pairs}"
    )


def main() -> None:
    for p in (53, 61, 73):
        verify_prime(p)
    print("active bridge-support flow verified")


if __name__ == "__main__":
    main()
