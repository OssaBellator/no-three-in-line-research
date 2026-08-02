#!/usr/bin/env python3
"""Verify PX108: bridge trades between adjacent quartic blocks."""
from __future__ import annotations

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


def verify_prime(p: int) -> None:
    slope = roots_minus_one(p)[0]
    quartic = {1, slope, p - 1, (-slope) % p}
    quotient_size = (p - 1) // 4

    first = frozenset(quartic)
    second = frozenset((1 + slope) * value % p for value in quartic)
    assert first.isdisjoint(second)

    root = tuple(slope * x % p for x in range(p))
    double = list(root)
    for x in first | second:
        double[x] = (-slope * x) % p
    double_mapping = tuple(double)
    assert is_strong(double_mapping)

    bridges: set[Block] = set()
    first_degrees = {x: 0 for x in first}
    second_degrees = {x: 0 for x in second}
    for z in quartic:
        a = 0
        r = z
        s = (-slope * z) % p
        candidate = apply_trade(double_mapping, p, a, r, s)
        assert candidate is not None
        support = frozenset((0, z, slope * z % p, (1 + slope) * z % p))
        assert len(support & first) == 2
        assert len(support & second) == 1
        assert 0 in support
        bridges.add(support)
        for x in support & first:
            first_degrees[x] += 1
        for x in support & second:
            second_degrees[x] += 1

    assert len(bridges) == 4
    assert set(first_degrees.values()) == {2}
    assert set(second_degrees.values()) == {1}

    inverse_multiplier = pow(1 + slope, -1, p)
    backward = frozenset(inverse_multiplier * value % p for value in quartic)
    assert first.isdisjoint(backward)
    backward_mapping = list(root)
    for x in first | backward:
        backward_mapping[x] = (-slope * x) % p
    backward_mapping = tuple(backward_mapping)
    assert is_strong(backward_mapping)

    backward_representations = 0
    for a in range(p):
        A = backward_mapping[a]
        for r in range(1, p):
            s = (backward_mapping[(a + r) % p] - A) % p
            candidate = apply_trade(backward_mapping, p, a, r, s)
            if candidate is None:
                continue
            support = frozenset(
                (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
            )
            if len(support & first) == 1 and len(support & backward) == 2:
                backward_representations += 1
    assert backward_representations == 16

    assert (1 + slope) * (1 + slope) % p not in quartic
    adjacent_pairs = p * quotient_size
    labelled_bridges = 4 * adjacent_pairs
    assert labelled_bridges == p * (p - 1)

    print(
        f"p={p}: quotient={quotient_size}, bridges=4, "
        f"adjacent_pairs={adjacent_pairs}, labelled={labelled_bridges}"
    )


def main() -> None:
    for p in (13, 17, 29, 37, 41):
        verify_prime(p)
    print("quartic bridge trades verified")


if __name__ == "__main__":
    main()
