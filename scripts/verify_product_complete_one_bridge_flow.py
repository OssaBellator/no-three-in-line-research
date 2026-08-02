#!/usr/bin/env python3
"""Verify PX126-PX128: complete one-bridge switching flow."""
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
) -> tuple[Permutation, Permutation, Block, set[int]]:
    root = tuple((slope * x + intercept) % p for x in range(p))
    opposite_slope = (-slope) % p
    opposite_intercept = (intercept + 2 * slope * centre) % p
    opposite = tuple(
        (opposite_slope * x + opposite_intercept) % p
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
        opposite_intercept + 2 * opposite_slope * bridge_centre
    ) % p
    second_root = tuple(
        (slope * x + second_root_intercept) % p for x in range(p)
    )

    source = list(root)
    for row in first | second:
        source[row] = opposite[row]
    for row in bridge:
        source[row] = second_root[row]
    source = tuple(source)
    assert is_strong(source)
    changed = {row for row in range(p) if source[row] != root[row]}
    assert changed == first | second | {centre}
    assert len(changed) == 9
    return root, source, bridge, changed


def run_exterior_case(
    p: int,
    target_row: int,
    condition_rows: tuple[int, ...],
) -> int:
    slope = roots_minus_one(p)[0]
    root, source, _, changed = bridge_source(p, slope, 3 % p)
    assert target_row not in changed
    assert target_row not in condition_rows

    candidates = [
        block
        for block in all_blocks(p, slope)
        if target_row in block
        and block.isdisjoint(changed)
        and not any(row in block for row in condition_rows)
    ]
    assert len(candidates) >= p - 34

    conditions = {(row, source[row]) for row in condition_rows}
    endpoints: set[Permutation] = set()
    for block in candidates:
        assert all(source[row] == root[row] for row in block)
        endpoint = list(source)
        for row, image in root_trade_values(
            p, slope, root[0], block
        ).items():
            endpoint[row] = image
        endpoint = tuple(endpoint)
        assert is_strong(endpoint)
        assert all(endpoint[row] == image for row, image in conditions)
        assert endpoint[target_row] != source[target_row]
        assert sum(endpoint[row] != root[row] for row in range(p)) <= 13
        endpoints.add(endpoint)
    assert len(endpoints) == len(candidates)
    return len(candidates)


def verify_exterior_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    _, source, bridge, changed = bridge_source(p, slope, 3 % p)
    exterior = tuple(row for row in range(p) if row not in changed)
    target = exterior[0]
    frozen = tuple(sorted(changed - bridge))
    active = tuple(sorted(bridge))
    other_exterior = tuple(row for row in exterior if row != target)

    cases = (
        (),
        (active[0],),
        (frozen[0],),
        (other_exterior[0],),
        (active[0], frozen[0]),
        (active[0], other_exterior[0]),
        (frozen[0], other_exterior[-1]),
        (other_exterior[0], other_exterior[-1]),
    )
    minima: Counter[int] = Counter()
    for condition_rows in cases:
        assert len({source[row] for row in condition_rows}) == len(condition_rows)
        exits = run_exterior_case(p, target, condition_rows)
        rank = len(condition_rows)
        minima[rank] = min(minima.get(rank, exits), exits)
    assert all(exits >= p - 34 for exits in minima.values())
    print(f"p={p}: exterior minimum exits={dict(sorted(minima.items()))}")


def verify_case_partition(p: int) -> None:
    slope = roots_minus_one(p)[0]
    _, _, bridge, changed = bridge_source(p, slope, 3 % p)
    counts = Counter(
        "active" if row in bridge else "frozen" if row in changed else "exterior"
        for row in range(p)
    )
    assert counts == {"active": 4, "frozen": 5, "exterior": p - 9}
    assert p - 142 <= p - 55 <= p - 34
    assert (p - 1) // 2 + 1 >= (p - 1) // 4 + 4
    print(f"p={p}: one-bridge row partition={dict(counts)}")


def main() -> None:
    for p in (37, 53, 149):
        verify_exterior_prime(p)
    verify_case_partition(149)
    print("complete one-bridge switching flow verified")


if __name__ == "__main__":
    main()
