#!/usr/bin/env python3
"""Verify PX103: the affine-root nonlinear switching layer."""
from __future__ import annotations

from collections import Counter

Permutation = tuple[int, ...]


def roots_minus_one(p: int) -> tuple[int, ...]:
    return tuple(value for value in range(p) if value * value % p == p - 1)


def affine_map(p: int, slope: int, translation: int) -> Permutation:
    return tuple((slope * x + translation) % p for x in range(p))


def trade_neighbour(
    p: int,
    slope: int,
    translation: int,
    a: int,
    r: int,
) -> Permutation:
    mapping = list(affine_map(p, slope, translation))
    s = slope * r % p
    A = mapping[a]
    rows = (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
    images = ((A + r + s) % p, (A + r) % p, (A + s) % p, A)
    assert len(set(rows)) == len(set(images)) == 4
    for row, image in zip(rows, images):
        mapping[row] = image
    return tuple(mapping)


def is_affine(mapping: Permutation) -> bool:
    p = len(mapping)
    translation = mapping[0]
    slope = (mapping[1] - translation) % p
    return all(mapping[x] == (slope * x + translation) % p for x in range(p))


def verify_prime(p: int) -> None:
    roots = roots_minus_one(p)
    assert len(roots) == 2
    all_shell: set[Permutation] = set()

    for slope in roots:
        assert slope not in (0, 1, p - 1)
        for translation in range(p):
            raw = [
                trade_neighbour(p, slope, translation, a, r)
                for a in range(p)
                for r in range(1, p)
            ]
            multiplicities = Counter(raw)
            assert set(multiplicities.values()) == {4}
            assert len(multiplicities) == p * (p - 1) // 4
            assert all(not is_affine(mapping) for mapping in multiplicities)
            if p >= 7:
                assert all_shell.isdisjoint(multiplicities)
            all_shell.update(multiplicities)

    if p >= 7:
        assert len(all_shell) == p * p * (p - 1) // 2
    print(
        f"p={p}: root degree={p * (p - 1) // 4}, "
        f"global shell={len(all_shell)}"
    )


def main() -> None:
    for p in (5, 13, 17, 29):
        verify_prime(p)
    print("affine-root switching layer verified")


if __name__ == "__main__":
    main()
