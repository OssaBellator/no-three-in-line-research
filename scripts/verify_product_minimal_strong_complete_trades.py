#!/usr/bin/env python3
"""Verify PX102: no nontrivial strong-complete trade has support below four."""
from __future__ import annotations

from itertools import combinations, permutations


def preserves_colours(
    p: int,
    rows: tuple[int, ...],
    old_images: tuple[int, ...],
    new_images: tuple[int, ...],
) -> bool:
    return (
        sorted(old_images) == sorted(new_images)
        and sorted((x - y) % p for x, y in zip(rows, old_images))
        == sorted((x - y) % p for x, y in zip(rows, new_images))
        and sorted((x + y) % p for x, y in zip(rows, old_images))
        == sorted((x + y) % p for x, y in zip(rows, new_images))
    )


def verify_prime(p: int) -> None:
    for support in (2, 3):
        derangements = tuple(
            permutation
            for permutation in permutations(range(support))
            if all(permutation[index] != index for index in range(support))
        )
        checked = 0
        for rows in combinations(range(p), support):
            for old_images in permutations(range(p), support):
                for relative in derangements:
                    new_images = tuple(old_images[relative[index]] for index in range(support))
                    assert not preserves_colours(p, rows, old_images, new_images), (
                        p,
                        rows,
                        old_images,
                        new_images,
                    )
                    checked += 1
        print(f"p={p}, support={support}: checked {checked} nontrivial assignments")


def verify_four_trade_exists(p: int) -> None:
    a = 0
    A = 0
    r = 1
    s = 2 if p != 5 else 2
    assert all(value % p != 0 for value in (r, s, r - s, r + s))
    rows = (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
    old_images = (A, (A + s) % p, (A + r) % p, (A + r + s) % p)
    new_images = ((A + r + s) % p, (A + r) % p, (A + s) % p, A)
    assert preserves_colours(p, rows, old_images, new_images)
    assert old_images != new_images


def main() -> None:
    for p in (5, 7, 11, 13):
        verify_prime(p)
        verify_four_trade_exists(p)
    print("minimal strong-complete trade support verified")


if __name__ == "__main__":
    main()
