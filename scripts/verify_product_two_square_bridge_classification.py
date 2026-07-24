#!/usr/bin/env python3
"""Verify PX109: exact two-square bridge classification."""
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


def centre(p: int, block: Block) -> int:
    return sum(block) * pow(4, -1, p) % p


def radius_coset(p: int, slope: int, block: Block) -> Block:
    c = centre(p, block)
    quartic = {1, slope, p - 1, (-slope) % p}
    value = next(x for x in block if x != c)
    return frozenset((value - c) * unit % p for unit in quartic)


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
            if tuple(mapping[row] for row in rows) != expected:
                continue
            result.add(frozenset(rows))
    return result


def verify_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    quartic = {1, slope, p - 1, (-slope) % p}
    first = frozenset(quartic)
    assert centre(p, first) == 0
    blocks = all_blocks(p, slope)

    forward_coset = frozenset((1 + slope) * unit % p for unit in quartic)
    backward_multiplier = pow(1 + slope, -1, p)
    backward_coset = frozenset(backward_multiplier * unit % p for unit in quartic)
    expected_partners = {forward_coset, backward_coset}
    assert len(expected_partners) == 2

    found_partners: set[Block] = set()
    profile_counts: Counter[tuple[int, int]] = Counter()

    root = tuple(slope * x % p for x in range(p))
    for second in blocks:
        if not first.isdisjoint(second):
            continue
        mapping = list(root)
        for x in first | second:
            c = 0 if x in first else centre(p, second)
            mapping[x] = (-slope * x + 2 * slope * c) % p
        mapping = tuple(mapping)
        assert is_strong(mapping)

        overlaps = {
            support
            for support in trade_supports(mapping)
            if support & first and support & second
        }
        is_adjacent = (
            centre(p, second) == 0
            and radius_coset(p, slope, second) in expected_partners
        )
        if is_adjacent:
            found_partners.add(second)
            assert len(overlaps) == 4
            profiles = {(len(support & first), len(support & second)) for support in overlaps}
            assert profiles in ({(2, 1)}, {(1, 2)})
            profile_counts.update(profiles)
            assert all(len(support - first - second) == 1 for support in overlaps)
        else:
            assert not overlaps

    assert found_partners == expected_partners
    assert sum(profile_counts.values()) == 2
    print(
        f"p={p}: disjoint partners checked={sum(first.isdisjoint(b) for b in blocks)}, "
        f"adjacent partners=2, bridge supports=8"
    )


def main() -> None:
    for p in (13, 17, 29, 37, 41):
        verify_prime(p)
    print("two-square bridge classification verified")


if __name__ == "__main__":
    main()
