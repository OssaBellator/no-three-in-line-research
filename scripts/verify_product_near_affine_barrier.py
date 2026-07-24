#!/usr/bin/env python3
"""Verify PX101: the near-affine rank-three spread barrier."""
from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb, prod

Permutation = tuple[int, ...]


def roots_minus_one(p: int) -> tuple[int, ...]:
    return tuple(value for value in range(p) if value * value % p == p - 1)


def affine_map(p: int, slope: int, translation: int) -> Permutation:
    return tuple((slope * x + translation) % p for x in range(p))


def one_trade_descendant(
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
    new_images = ((A + r + s) % p, (A + r) % p, (A + s) % p, A)
    for row, image in zip(rows, new_images):
        mapping[row] = image
    assert sum(
        mapping[x] != (slope * x + translation) % p
        for x in range(p)
    ) == 4
    return tuple(mapping)


def verify_root_affine_cylinder_uniqueness(p: int) -> None:
    roots = roots_minus_one(p)
    assert len(roots) == 2
    seen: set[tuple[tuple[int, int], ...]] = set()
    for slope in roots:
        for translation in range(p):
            mapping = affine_map(p, slope, translation)
            for rows in combinations(range(p), 3):
                cylinder = tuple((row, mapping[row]) for row in rows)
                assert cylinder not in seen
                seen.add(cylinder)
    assert len(seen) == 2 * p * comb(p, 3)
    print(f"p={p}: distinct root-affine cylinders={len(seen)}")


def verify_deterministic_bounds() -> None:
    for p in (5, 13, 17, 29):
        if not roots_minus_one(p):
            continue
        verify_root_affine_cylinder_uniqueness(p)
        previous = None
        for retained in range(3, p + 1):
            lower_constant = 3 * comb(retained, 3) / p
            if previous is not None:
                assert lower_constant >= previous
            previous = lower_constant
        assert 3 * comb(p, 3) / p == (p - 1) * (p - 2) / 2
    print("deterministic retained-row lower bounds checked")


def verify_order_thirteen_descendants() -> None:
    p = 13
    raw: list[Permutation] = []
    for slope in roots_minus_one(p):
        for translation in range(p):
            for a in range(p):
                for r in range(1, p):
                    raw.append(one_trade_descendant(p, slope, translation, a, r))

    assert len(raw) == 4056
    multiplicities = Counter(raw)
    assert len(multiplicities) == 1014
    assert set(multiplicities.values()) == {4}

    cylinders: Counter[tuple[tuple[int, int], ...]] = Counter()
    for mapping in raw:
        for rows in combinations(range(p), 3):
            cylinders[tuple((row, mapping[row]) for row in rows)] += 1
    maximum = max(cylinders.values())
    assert maximum == 52
    normalized_constant = maximum * prod(range(p - 2, p + 1)) / len(raw)
    assert normalized_constant == 22

    retained_rows = p - 4
    theorem_lower_bound = 3 * comb(retained_rows, 3) / p
    assert normalized_constant >= theorem_lower_bound
    print(
        f"p=13 one-trade descendants: raw={len(raw)}, unique={len(multiplicities)}, "
        f"rank-three constant={normalized_constant:g}, "
        f"PX101 lower bound={theorem_lower_bound:.6f}"
    )


def main() -> None:
    verify_deterministic_bounds()
    verify_order_thirteen_descendants()
    print("near-affine rank-three barrier verified")


if __name__ == "__main__":
    main()
