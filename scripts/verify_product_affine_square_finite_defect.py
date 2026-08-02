#!/usr/bin/env python3
"""Verify PX110: finite-defect affine-square expansion."""
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


def flip_root_blocks(
    root: Permutation, slope: int, blocks: tuple[Block, ...]
) -> Permutation:
    result = list(root)
    for block in blocks:
        assert all(result[x] == root[x] for x in block)
        centre = sum(block) * pow(4, -1, len(root)) % len(root)
        for x in block:
            result[x] = (-slope * x + 2 * slope * centre) % len(root)
    mapping = tuple(result)
    assert is_strong(mapping)
    return mapping


def apply_bridge(
    mapping: Permutation, p: int, slope: int, scale: int = 1
) -> Permutation:
    a = 0
    r = scale % p
    s = (-slope * scale) % p
    A = mapping[a]
    rows = (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
    expected = (A, (A + s) % p, (A + r) % p, (A + r + s) % p)
    assert tuple(mapping[row] for row in rows) == expected
    result = list(mapping)
    new_images = ((A + r + s) % p, (A + r) % p, (A + s) % p, A)
    for row, image in zip(rows, new_images):
        result[row] = image
    candidate = tuple(result)
    assert is_strong(candidate)
    return candidate


def verify_state(root: Permutation, mapping: Permutation, blocks: set[Block]) -> None:
    p = len(root)
    changed = {x for x in range(p) if mapping[x] != root[x]}
    available = trade_supports(mapping)

    disjoint_blocks = {block for block in blocks if block.isdisjoint(changed)}
    total_bound = p * (p - 1) // 4 - len(changed) * (p - 1)
    assert len(disjoint_blocks) >= total_bound
    assert disjoint_blocks <= available

    for x in range(p):
        if x in changed:
            continue
        exits = {
            block for block in blocks if x in block and block.isdisjoint(changed)
        }
        assert len(exits) >= p - 1 - 3 * len(changed)
        assert exits <= available
        assert all(mapping[x] == root[x] for _ in exits)


def verify_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    root = tuple(slope * x % p for x in range(p))
    blocks = all_blocks(p, slope)
    quartic = {1, slope, p - 1, (-slope) % p}
    first = frozenset(quartic)
    adjacent = frozenset((1 + slope) * value % p for value in quartic)
    assert first.isdisjoint(adjacent)

    states: list[Permutation] = [root]
    first_state = flip_root_blocks(root, slope, (first,))
    states.append(first_state)

    disjoint_other = next(
        block
        for block in blocks
        if block.isdisjoint(first) and block != adjacent
    )
    states.append(flip_root_blocks(root, slope, (first, disjoint_other)))

    double_adjacent = flip_root_blocks(root, slope, (first, adjacent))
    states.append(double_adjacent)
    bridge_state = apply_bridge(double_adjacent, p, slope)
    states.append(bridge_state)

    for mapping in states:
        verify_state(root, mapping, blocks)

    changed_sizes = Counter(
        sum(mapping[x] != root[x] for x in range(p)) for mapping in states
    )
    print(f"p={p}: states={len(states)}, changed_sizes={dict(changed_sizes)}")


def main() -> None:
    for p in (13, 17, 29, 37):
        verify_prime(p)
    print("finite-defect affine-square expansion verified")


if __name__ == "__main__":
    main()
