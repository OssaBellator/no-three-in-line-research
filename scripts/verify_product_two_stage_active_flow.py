#!/usr/bin/env python3
"""Verify PX122-PX125: unconditional two-stage active-support flow."""
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
        (
            centre,
            (centre + 1) % p,
            (centre + slope) % p,
            (centre + 1 + slope) % p,
        )
    )
    bridge_centre = sum(bridge) * pow(4, -1, p) % p

    second_root_intercept = (
        first_opposite_intercept
        + 2 * first_opposite_slope * bridge_centre
    ) % p
    second_root = tuple(
        (slope * x + second_root_intercept) % p for x in range(p)
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


def construct_prefinal(
    p: int,
    target_row: int,
    condition_rows: tuple[int, ...],
) -> tuple[
    Permutation,
    Permutation,
    Permutation,
    Block,
    set[int],
    int,
    int,
]:
    slope = roots_minus_one(p)[0]
    centre = 0
    (
        first_root,
        first_opposite,
        second_root,
        source,
        first,
        second,
        bridge,
        changed,
        bridge_centre,
    ) = bridge_source(p, slope, 3 % p, centre)
    assert target_row in bridge
    assert target_row not in condition_rows

    first_class = quartic_class(p, slope, centre)
    row_to_first = {
        row: block for block in first_class for row in block
    }
    exterior_markers = {
        row_to_first[row]
        for row in condition_rows
        if row not in changed
    }

    # H1 is the first opposite root, except that U already has K-values and
    # every exterior marker retains the original F-values.
    first_stage = list(first_opposite)
    for row in bridge:
        first_stage[row] = second_root[row]
    for block in exterior_markers:
        for row in block:
            first_stage[row] = first_root[row]
    first_stage = tuple(first_stage)
    assert is_strong(first_stage)

    second_class = quartic_class(
        p, (-slope) % p, bridge_centre
    )
    assert bridge in second_class
    protected: set[Block] = {bridge}
    for block in second_class:
        if any(not block.isdisjoint(marker) for marker in exterior_markers):
            protected.add(block)
    for row in condition_rows:
        if row in changed - bridge:
            protected.add(next(block for block in second_class if row in block))

    marker = next(block for block in second_class if block not in protected)
    protected.add(marker)
    assert len(protected) <= 12

    # Every unprotected class block is toggled from L to K.  Protected blocks
    # retain their H1 values.  The class centre is untouched.
    second_stage = list(second_root)
    for block in protected:
        for row in block:
            second_stage[row] = first_stage[row]
    second_stage[bridge_centre] = first_stage[bridge_centre]
    second_stage = tuple(second_stage)
    assert is_strong(second_stage)

    conditions = {(row, source[row]) for row in condition_rows}
    assert all(second_stage[row] == image for row, image in conditions)
    assert second_stage[target_row] == source[target_row]

    bad_rows = {
        row for row in range(p) if second_stage[row] != second_root[row]
    }
    assert len(bad_rows) <= 45
    return (
        source,
        second_root,
        second_stage,
        bridge,
        bad_rows,
        len(exterior_markers),
        len(protected),
    )


def run_case(
    p: int,
    target_row: int,
    condition_rows: tuple[int, ...],
) -> tuple[int, int, int, int]:
    slope = roots_minus_one(p)[0]
    (
        source,
        second_root,
        prefinal,
        bridge,
        bad_rows,
        exterior_marker_count,
        protected_count,
    ) = construct_prefinal(p, target_row, condition_rows)

    candidates = [
        block
        for block in all_blocks(p, slope)
        if target_row in block
        and block.isdisjoint(bad_rows)
        and not any(row in block for row in condition_rows)
    ]
    assert len(candidates) >= p - 142

    conditions = {(row, source[row]) for row in condition_rows}
    endpoints: set[Permutation] = set()
    for block in candidates:
        assert all(prefinal[row] == second_root[row] for row in block)
        endpoint = list(prefinal)
        for row, image in root_trade_values(
            p, slope, second_root[0], block
        ).items():
            endpoint[row] = image
        endpoint = tuple(endpoint)
        assert is_strong(endpoint)
        assert all(endpoint[row] == image for row, image in conditions)
        assert endpoint[target_row] != source[target_row]
        changed_from_root = {
            row for row in range(p) if endpoint[row] != second_root[row]
        }
        assert len(changed_from_root) <= 49
        endpoints.add(endpoint)
    assert len(endpoints) == len(candidates)
    return (
        len(candidates),
        len(bad_rows),
        exterior_marker_count,
        protected_count,
    )


def verify_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    _, _, _, source, _, _, bridge, changed, _ = bridge_source(
        p, slope, 3 % p
    )
    target = min(bridge)
    bridge_rows = tuple(sorted(bridge - {target}))
    frozen_rows = tuple(sorted(changed - bridge))
    exterior_rows = tuple(row for row in range(p) if row not in changed)

    cases = (
        (),
        (bridge_rows[0],),
        (frozen_rows[0],),
        (exterior_rows[0],),
        (bridge_rows[0], frozen_rows[0]),
        (bridge_rows[0], exterior_rows[0]),
        (frozen_rows[0], frozen_rows[1]),
        (frozen_rows[0], exterior_rows[0]),
        (exterior_rows[0], exterior_rows[1]),
        (exterior_rows[0], exterior_rows[-1]),
    )

    minima: Counter[int] = Counter()
    maxima_bad: Counter[int] = Counter()
    for condition_rows in cases:
        assert target not in condition_rows
        assert len({source[row] for row in condition_rows}) == len(condition_rows)
        exits, bad_count, _, _ = run_case(p, target, condition_rows)
        rank = len(condition_rows)
        minima[rank] = min(minima.get(rank, exits), exits)
        maxima_bad[rank] = max(maxima_bad.get(rank, 0), bad_count)

    assert all(exits >= p - 142 for exits in minima.values())
    print(
        f"p={p}: minimum exits={dict(sorted(minima.items()))}, "
        f"maximum bad rows={dict(sorted(maxima_bad.items()))}"
    )


def main() -> None:
    for p in (149, 157, 173):
        verify_prime(p)
    print("unconditional two-stage active-support flow verified")


if __name__ == "__main__":
    main()
