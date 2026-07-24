#!/usr/bin/env python3
"""Verify additional exact finite saturated no-three constructions."""
from __future__ import annotations

from collections import Counter
from itertools import combinations

CONSTRUCTIONS: dict[int, tuple[tuple[int, ...], tuple[int, ...]]] = {
    12: (
        (0, 2, 6, 5, 10, 11, 1, 8, 4, 3, 9, 7),
        (5, 9, 11, 7, 1, 2, 0, 10, 6, 8, 3, 4),
    ),
}


def determinant(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def main() -> None:
    triples = 0
    for n, (first, second) in CONSTRUCTIONS.items():
        assert sorted(first) == list(range(n))
        assert sorted(second) == list(range(n))
        assert all(first[x] != second[x] for x in range(n))

        points = [(x, first[x]) for x in range(n)]
        points += [(x, second[x]) for x in range(n)]
        assert set(Counter(x for x, _ in points).values()) == {2}
        assert set(Counter(y for _, y in points).values()) == {2}

        for triple in combinations(points, 3):
            assert determinant(*triple) != 0, (n, triple)
            triples += 1

    print(
        f"verified finite extensions={len(CONSTRUCTIONS)}; "
        f"exact triples={triples}"
    )


if __name__ == "__main__":
    main()
