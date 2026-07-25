#!/usr/bin/env python3
"""Verify PX168--PX169 all-completion secant-star counts."""
from __future__ import annotations

from collections import Counter

Edge = tuple[int, int, int, int]


def edge(prime: int, row: int, column: int) -> Edge:
    return row, column, (row - column) % prime, (row + column) % prime


def is_matching(first: Edge, second: Edge) -> bool:
    return all(first[part] != second[part] for part in range(4))


def occurrences(prime: int, slope: int) -> list[tuple[Edge, Edge]]:
    result = []
    for base_row in range(prime):
        for step in range(1, prime):
            for base_image in range(prime):
                pair = (
                    edge(prime, base_row, base_image),
                    edge(
                        prime,
                        (base_row + step) % prime,
                        (base_image + slope * step) % prime,
                    ),
                )
                assert is_matching(*pair)
                result.append(pair)
    return result


def verify_prime(prime: int) -> None:
    for slope in range(prime):
        if slope in (0, 1, prime - 1):
            continue
        pairs = occurrences(prime, slope)
        assert len(pairs) == prime * prime * (prime - 1)

        row_role = Counter()
        edge_role = Counter()
        row_any = Counter()
        for first, second in pairs:
            row_role[(0, first[0])] += 1
            row_role[(1, second[0])] += 1
            edge_role[(0, first)] += 1
            edge_role[(1, second)] += 1
            row_any[first[0]] += 1
            row_any[second[0]] += 1

        assert set(row_role.values()) == {prime * (prime - 1)}
        assert set(edge_role.values()) == {prime - 1}
        assert set(row_any.values()) == {2 * prime * (prime - 1)}

        # Fixing two scalar rows and the slope leaves exactly p image translates.
        row_pairs = Counter((first[0], second[0]) for first, second in pairs)
        assert set(row_pairs.values()) == {prime}

    print(
        f"p={prime}: slopes={prime - 3}, pairs/slope={prime * prime * (prime - 1)}"
    )


def main() -> None:
    for prime in (5, 7, 11, 13):
        verify_prime(prime)
    print("PX168--PX169 secant completion framework verified")


if __name__ == "__main__":
    main()
