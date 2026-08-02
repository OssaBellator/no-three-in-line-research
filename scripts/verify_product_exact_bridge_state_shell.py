#!/usr/bin/env python3
"""Verify PX112: the exact one-step shell after a quartic bridge."""
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


def trade_supports(mapping: Permutation) -> set[Block]:
    p = len(mapping)
    result: set[Block] = set()
    for a in range(p):
        A = mapping[a]
        for r in range(1, p):
            s = (mapping[(a + r) % p] - A) % p
            if 0 in (s, (r - s) % p, (r + s) % p):
                continue
            rows = (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
            expected = (A, (A + s) % p, (A + r) % p, (A + r + s) % p)
            if tuple(mapping[row] for row in rows) == expected:
                result.add(frozenset(rows))
    return result


def bridge_state(p: int, slope: int) -> tuple[Permutation, Block, set[int]]:
    quartic = {1, slope, p - 1, (-slope) % p}
    first = frozenset(quartic)
    second = frozenset((1 + slope) * value % p for value in quartic)
    root = tuple(slope * x % p for x in range(p))
    mapping = list(root)
    for x in first | second:
        mapping[x] = (-slope * x) % p

    a = 0
    r = 1
    s = (-slope) % p
    A = mapping[a]
    rows = (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
    expected = (A, (A + s) % p, (A + r) % p, (A + r + s) % p)
    assert tuple(mapping[row] for row in rows) == expected
    new_images = ((A + r + s) % p, (A + r) % p, (A + s) % p, A)
    for row, image in zip(rows, new_images):
        mapping[row] = image

    result = tuple(mapping)
    assert is_strong(result)
    bridge = frozenset(rows)
    changed = {x for x in range(p) if result[x] != root[x]}
    assert changed == first | second | {0}
    assert len(changed) == 9
    return result, bridge, changed


def verify_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    blocks = all_blocks(p, slope)
    mapping, bridge, changed = bridge_state(p, slope)
    supports = trade_supports(mapping)
    disjoint_blocks = {block for block in blocks if block.isdisjoint(changed)}

    assert supports == disjoint_blocks | {bridge}
    assert all(
        not (support & changed)
        for support in supports
        if support != bridge
    )

    profile = Counter(len(block & changed) for block in blocks)
    if p == 13:
        assert profile == {0: 1, 2: 12, 3: 20, 4: 6}
        assert len(supports) == 2
    elif p == 17:
        assert profile == {0: 2, 1: 12, 2: 36, 3: 12, 4: 6}
        assert len(supports) == 3
    else:
        expected = {
            0: (p * p - 37 * p + 380) // 4,
            1: 9 * p - 165,
            2: 60,
            3: 4,
            4: 6,
        }
        assert profile == expected
        assert len(supports) == (p * p - 37 * p + 384) // 4

    frozen = changed - bridge
    assert len(frozen) == 5
    assert all(not (support & frozen) for support in supports)
    print(
        f"p={p}: profile={dict(sorted(profile.items()))}, "
        f"degree={len(supports)}, frozen={len(frozen)}"
    )


def main() -> None:
    for p in (13, 17, 29, 37, 41, 53):
        verify_prime(p)
    print("exact bridge-state shell verified")


if __name__ == "__main__":
    main()
