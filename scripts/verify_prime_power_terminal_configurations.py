#!/usr/bin/env python3
"""Verify the companion-offset terminal configurations in CMR24."""
from __future__ import annotations

from itertools import combinations

TERMINAL_CONFIGURATIONS: dict[int, tuple[tuple[int, ...], tuple[int, ...]]] = {
    3: ((1, 0, 2), (0, 2, 1)),
    5: ((1, 4, 0, 3, 2), (2, 3, 1, 0, 4)),
    7: ((4, 5, 3, 0, 1, 6, 2), (2, 1, 5, 6, 0, 3, 4)),
    11: ((8, 6, 3, 9, 7, 0, 2, 10, 4, 1, 5), (2, 9, 3, 7, 0, 6, 1, 10, 5, 8, 4)),
    13: ((6, 2, 1, 4, 9, 3, 0, 11, 8, 7, 12, 10, 5), (1, 10, 12, 7, 4, 3, 9, 5, 2, 8, 11, 0, 6)),
    17: ((12, 8, 13, 16, 2, 15, 6, 3, 7, 0, 9, 5, 10, 14, 4, 11, 1), (12, 14, 7, 3, 15, 11, 6, 10, 0, 1, 4, 5, 16, 8, 9, 2, 13)),
    19: ((5, 7, 12, 18, 1, 17, 6, 13, 8, 14, 9, 3, 16, 4, 15, 0, 2, 10, 11), (7, 11, 18, 10, 1, 14, 17, 6, 3, 2, 5, 16, 13, 15, 8, 0, 12, 9, 4)),
    23: ((7, 19, 10, 2, 4, 16, 22, 12, 15, 3, 13, 21, 18, 6, 8, 1, 5, 0, 17, 11, 9, 14, 20), (4, 12, 15, 22, 2, 0, 8, 6, 18, 1, 5, 3, 17, 21, 19, 9, 14, 11, 20, 10, 16, 7, 13)),
    29: ((26, 12, 2, 16, 10, 18, 25, 7, 14, 19, 22, 8, 5, 0, 4, 23, 21, 9, 11, 17, 27, 15, 24, 28, 3, 6, 20, 1, 13), (16, 24, 14, 12, 4, 19, 20, 22, 25, 15, 8, 7, 21, 28, 0, 13, 6, 2, 23, 10, 1, 17, 5, 9, 18, 26, 11, 3, 27)),
    31: ((21, 26, 1, 13, 8, 15, 7, 0, 28, 9, 18, 22, 2, 19, 17, 6, 25, 30, 14, 5, 27, 29, 24, 16, 10, 20, 11, 23, 3, 12, 4), (4, 14, 25, 10, 28, 8, 19, 23, 13, 1, 20, 12, 11, 24, 18, 27, 0, 7, 29, 2, 26, 16, 9, 5, 22, 17, 3, 21, 15, 30, 6)),
}


def determinant(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def points(p: int, first: tuple[int, ...], second: tuple[int, ...], scale: int):
    return (
        [(j * scale, first[j] * scale) for j in range(p)]
        + [(j * scale, 1 + second[j] * scale) for j in range(p)]
    )


def main() -> None:
    triple_checks = 0
    for p, (first, second) in TERMINAL_CONFIGURATIONS.items():
        assert sorted(first) == list(range(p))
        assert sorted(second) == list(range(p))
        selected = points(p, first, second, p)
        assert len(set(selected)) == 2 * p
        for triple in combinations(selected, 3):
            assert determinant(*triple) != 0, (p, triple)
            triple_checks += 1

        # Also check one higher exponent as a direct sanity check of the lift proof.
        lifted = points(p, first, second, p * p)
        assert all(determinant(*triple) != 0 for triple in combinations(lifted, 3))

    print(
        f"verified terminal configurations={len(TERMINAL_CONFIGURATIONS)}; "
        f"base triple checks={triple_checks}; exponents k=2,3"
    )


if __name__ == "__main__":
    main()
