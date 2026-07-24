#!/usr/bin/env python3
"""Exact checks for CMR120--CMR122 prime-seven pair spectrum."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

Point = tuple[int, int]

FAMILY: tuple[tuple[int, ...], ...] = (
    (0, 2, 6, 5, 3, 4, 1),
    (1, 0, 4, 6, 2, 3, 5),
    (2, 3, 5, 4, 1, 6, 0),
    (3, 5, 0, 2, 6, 1, 4),
    (4, 1, 3, 0, 5, 2, 6),
    (5, 6, 2, 1, 4, 0, 3),
    (6, 4, 1, 3, 0, 5, 2),
)


def det(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def verify_local() -> None:
    for mapping in FAMILY:
        assert sorted(mapping) == list(range(7))
        points = [(x, mapping[x]) for x in range(7)]
        assert all(det(*triple) != 0 for triple in combinations(points, 3))

    for x in range(7):
        assert sorted(mapping[x] for mapping in FAMILY) == list(range(7))

    maximum = 0
    checked = 0
    for u, v in combinations(range(7), 2):
        spectrum = Counter((mapping[u] - mapping[v]) % 7 for mapping in FAMILY)
        assert 0 not in spectrum
        maximum = max(maximum, max(spectrum.values()))
        for difference in range(1, 7):
            assert spectrum[difference] <= 3
            checked += 1
    assert maximum == 3
    assert checked == 126


def exact_pair_count(k: int, s: int) -> int:
    n = 7**k
    count = sum(
        1
        for x, y in combinations(range(n), 2)
        if (x - y) % (7**s) == 0 and (x - y) % (7 ** (s + 1)) != 0
    )
    expected = 3 * n * n // (7 ** (s + 1))
    assert count == expected
    return count


def verify_cluster_arithmetic(max_exponent: int = 4) -> None:
    for k in range(2, max_exponent + 1):
        n = 7**k
        for s in range(1, k):
            pairs = exact_pair_count(k, s)
            # Four same-layer assignments and the 3/7 separation atom.
            numerator = 4 * pairs * n * 3
            denominator = 7 * (7 ** (k - s - 1))
            assert numerator % denominator == 0
            assert numerator // denominator == 36 * n * n // 7


def main() -> None:
    verify_local()
    verify_cluster_arithmetic()
    print(
        "verified prime-seven pair spectrum: "
        "local triples=245, spectrum cells=126, max multiplicity=3, "
        "binary levels through N=2401"
    )


if __name__ == "__main__":
    main()
