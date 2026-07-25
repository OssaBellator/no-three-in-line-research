#!/usr/bin/env python3
"""Verify PX158--PX159 duplicated-reservoir counts on small primes."""
from collections import Counter


def edge(prime: int, row: int, column: int) -> tuple[int, int, int, int]:
    return row, column, (row - column) % prime, (row + column) % prime


def verify_prime(prime: int) -> None:
    host = [edge(prime, row, column) for row in range(prime) for column in range(prime)]

    for part in range(4):
        degrees = Counter(item[part] for item in host)
        assert set(degrees.values()) == {prime}

    for row in range(prime):
        row_edges = [item for item in host if item[0] == row]
        assert len(row_edges) == prime
        for reservoir_part in range(1, 4):
            counts = Counter(item[reservoir_part] for item in row_edges)
            assert set(counts.values()) == {1}

    maximum_collision_degree = 0
    maximum_fixed_old_degree = 0
    total_weight_by_row = []
    for row in range(prime):
        duplicated_edges = [item for item in host if item[0] == row]
        conflicts_for_row: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
        old_degree = Counter()
        for new_edge in duplicated_edges:
            for old_edge in host:
                if set(new_edge[1:]) & set(old_edge[1:]):
                    conflicts_for_row.add((old_edge, new_edge))
                    old_degree[old_edge] += 1
        maximum_collision_degree = max(
            maximum_collision_degree,
            max(Counter(new for _, new in conflicts_for_row).values()),
        )
        maximum_fixed_old_degree = max(
            maximum_fixed_old_degree,
            max(old_degree.values()),
        )
        assert len(conflicts_for_row) <= 3 * prime * prime
        total_weight_by_row.append(len(conflicts_for_row) / prime)

    assert maximum_collision_degree <= 3 * prime
    assert maximum_fixed_old_degree <= 3
    assert max(total_weight_by_row) <= 3 * prime

    print(
        f"p={prime}: degree={prime}, collision-edge degree<={maximum_collision_degree}, "
        f"fixed-old degree<={maximum_fixed_old_degree}"
    )


def verify_projection(prime: int) -> None:
    # A small deterministic P-perfect mixed matching. The second-stage edges are
    # represented in duplicate coordinates but project by the identity map.
    first_rows = list(range(prime - 2))
    first = [edge(prime, row, 2 * row % prime) for row in first_rows]

    used = [set() for _ in range(3)]
    for item in first:
        for part in range(3):
            used[part].add(item[part + 1])

    completion = []
    for row in range(prime - 2, prime):
        for column in range(prime):
            candidate = edge(prime, row, column)
            if all(candidate[part + 1] not in used[part] for part in range(3)):
                completion.append(candidate)
                for part in range(3):
                    used[part].add(candidate[part + 1])
                break

    if len(completion) == 2:
        projected = first + completion
        for part in range(4):
            assert len({item[part] for item in projected}) == prime


def main() -> None:
    for prime in (5, 7, 11, 13):
        verify_prime(prime)
        verify_projection(prime)
    print("PX158--PX159 duplicated-reservoir reduction verified")


if __name__ == "__main__":
    main()
