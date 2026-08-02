#!/usr/bin/env python3
"""Exhaust normalized affine full selectors for the canonical 2 x 5 factor.

The first coarse row and column blocks use identity fine-digit maps.  The second
row and column blocks independently use all affine permutations modulo five.
For every map pair and every radix orientation, the exact degree-two no-three
selector is tested.
"""
from __future__ import annotations

from verify_product_blockwise_reversal import (
    IDENTITY,
    ORIENTATIONS,
    OUTER,
    Permutation,
    blockwise_host,
    first_no_three_degree_two,
    verify_regular,
)

CANONICAL_INNER = (
    (0, 1, 3, 4, 2),
    (2, 0, 4, 1, 3),
)


def affine_maps() -> tuple[Permutation, ...]:
    maps = {
        tuple((a * u + b) % 5 for u in range(5))
        for a in range(1, 5)
        for b in range(5)
    }
    assert len(maps) == 20
    return tuple(sorted(maps))


def main() -> None:
    tested = 0
    for row_map in affine_maps():
        for column_map in affine_maps():
            row_maps = (IDENTITY, row_map)
            column_maps = (IDENTITY, column_map)
            for orientation in ORIENTATIONS:
                tested += 1
                host = blockwise_host(
                    OUTER,
                    CANONICAL_INNER,
                    orientation,
                    row_maps,
                    column_maps,
                )
                verify_regular(host, degree=4)
                assert first_no_three_degree_two(host) is None, (
                    row_map,
                    column_map,
                    orientation,
                )

    assert tested == 20 * 20 * 4 == 1600
    print("canonical normalized-affine full-selector hosts tested: 1600")
    print("no no-three degree-two model exists in any tested host")


if __name__ == "__main__":
    main()
