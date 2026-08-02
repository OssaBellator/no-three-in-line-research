#!/usr/bin/env python3
"""Verify PX129-PX131: affine-orbit strong-complete spread."""
from __future__ import annotations

from collections import Counter
from itertools import combinations

Permutation = tuple[int, ...]
SEED = (0, 2, 4, 9, 7, 12, 3, 11, 6, 1, 5, 10, 8)


def strong_complete_mappings(p: int) -> tuple[Permutation, ...]:
    mapping = [-1] * p
    result: list[Permutation] = []

    def search(row: int, used_images: int, used_minus: int, used_plus: int) -> None:
        if row == p:
            result.append(tuple(mapping))
            return
        for image in range(p):
            image_bit = 1 << image
            minus = (row - image) % p
            plus = (row + image) % p
            if (
                used_images & image_bit
                or used_minus & (1 << minus)
                or used_plus & (1 << plus)
            ):
                continue
            mapping[row] = image
            search(
                row + 1,
                used_images | image_bit,
                used_minus | (1 << minus),
                used_plus | (1 << plus),
            )

    search(0, 0, 0, 0)
    return tuple(result)


def is_strong(mapping: Permutation) -> bool:
    p = len(mapping)
    return (
        len(set(mapping)) == p
        and len({(x - mapping[x]) % p for x in range(p)}) == p
        and len({(x + mapping[x]) % p for x in range(p)}) == p
    )


def multiplicities(mapping: Permutation) -> tuple[int, int]:
    p = len(mapping)
    secants: Counter[int] = Counter()
    triangles: Counter[tuple[int, int, int]] = Counter()

    for first in range(p):
        for second in range(p):
            if first == second:
                continue
            dx = (second - first) % p
            dy = (mapping[second] - mapping[first]) % p
            inverse_dx = pow(dx, -1, p)
            inverse_dy = pow(dy, -1, p)
            slope = dy * inverse_dx % p
            secants[slope] += 1
            for third in range(p):
                if third == first or third == second:
                    continue
                row_ratio = (third - first) * inverse_dx % p
                image_ratio = (
                    (mapping[third] - mapping[first]) * inverse_dy % p
                )
                triangles[(slope, row_ratio, image_ratio)] += 1

    return max(secants.values()), max(triangles.values())


def transform(
    mapping: Permutation,
    scale: int,
    row_shift: int,
    image_shift: int,
) -> Permutation:
    p = len(mapping)
    inverse_scale = pow(scale, -1, p)
    result = tuple(
        (
            scale
            * mapping[((row - row_shift) * inverse_scale) % p]
            + image_shift
        )
        % p
        for row in range(p)
    )
    assert is_strong(result)
    return result


def affine_parameter_multiset(mapping: Permutation) -> tuple[Permutation, ...]:
    p = len(mapping)
    return tuple(
        transform(mapping, scale, row_shift, image_shift)
        for scale in range(1, p)
        for row_shift in range(p)
        for image_shift in range(p)
    )


def maximum_cylinder_count(
    mappings: tuple[Permutation, ...], rank: int
) -> int:
    p = len(mappings[0])
    counts: Counter[tuple[tuple[int, int], ...]] = Counter()
    for mapping in mappings:
        for rows in combinations(range(p), rank):
            counts[tuple((row, mapping[row]) for row in rows)] += 1
    return max(counts.values())


def verify_census() -> None:
    mappings = strong_complete_mappings(13)
    assert len(mappings) == 4524
    distribution: Counter[tuple[int, int]] = Counter(
        multiplicities(mapping) for mapping in mappings
    )
    assert distribution == {
        (28, 8): 2028,
        (42, 24): 1352,
        (72, 48): 1014,
        (156, 156): 130,
    }
    assert SEED in mappings
    assert multiplicities(SEED) == (28, 8)
    print(f"order-thirteen multiplicity classes: {dict(distribution)}")


def verify_seed_orbit() -> None:
    parameter_multiset = affine_parameter_multiset(SEED)
    assert len(parameter_multiset) == 13 * 13 * 12
    assert len(set(parameter_multiset)) == 1014
    maxima = {
        rank: maximum_cylinder_count(parameter_multiset, rank)
        for rank in (1, 2, 3)
    }
    assert maxima == {1: 156, 2: 28, 3: 8}
    assert 28 / 13 < 3
    assert 8 * 11 / 13 < 7
    print(
        f"seed orbit: parameters={len(parameter_multiset)}, "
        f"distinct={len(set(parameter_multiset))}, maxima={maxima}"
    )


def verify_conditional_composition() -> None:
    orbit = affine_parameter_multiset(SEED)
    representatives = (
        orbit[0],
        orbit[137],
        orbit[911],
    )
    for phi in representatives:
        for h in orbit[::173]:
            composed = tuple(h[phi[row]] for row in range(13))
            assert len(set(composed)) == 13
            assert len(
                {(composed[row] - phi[row]) % 13 for row in range(13)}
            ) == 13
            assert len(
                {(composed[row] + phi[row]) % 13 for row in range(13)}
            ) == 13

        # A prescribed P-cylinder becomes an h-cylinder after reindexing by phi.
        for rows in ((0,), (0, 4), (0, 4, 9)):
            inputs = tuple(phi[row] for row in rows)
            assert len(set(inputs)) == len(inputs)
            target_h = orbit[29]
            targets = tuple(target_h[value] for value in inputs)
            conditional_count = sum(
                all(h[value] == target for value, target in zip(inputs, targets))
                for h in orbit
            )
            direct_count = sum(
                all(
                    h[phi[row]] == target
                    for row, target in zip(rows, targets)
                )
                for h in orbit
            )
            assert direct_count == conditional_count
            assert conditional_count <= {1: 156, 2: 28, 3: 8}[len(rows)]
    print("conditional strong-complete composition checked")


def main() -> None:
    verify_census()
    verify_seed_orbit()
    verify_conditional_composition()
    print("affine-orbit strong-complete spread verified")


if __name__ == "__main__":
    main()
