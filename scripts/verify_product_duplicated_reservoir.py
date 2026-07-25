#!/usr/bin/env python3
"""Verify PX158--PX159 duplicated-reservoir counts on small primes."""
from collections import Counter


def edge(prime: int, row: int, column: int) -> tuple[int, int, int, int]:
    return row, column, (row - column) % prime, (row + column) % prime


def projection_collision(
    old_edge: tuple[int, int, int, int],
    new_edge: tuple[int, int, int, int],
) -> bool:
    """Compare corresponding C, D, and S coordinates only."""
    return any(old_edge[part] == new_edge[part] for part in (1, 2, 3))


def verify_prime(prime: int) -> None:
    host = [
        edge(prime, row, column)
        for row in range(prime)
        for column in range(prime)
    ]

    for part in range(4):
        degrees = Counter(item[part] for item in host)
        assert set(degrees.values()) == {prime}

    maximum_collision_degree = 0
    maximum_fixed_old_degree = 0
    for row in range(prime):
        duplicated_edges = [item for item in host if item[0] == row]
        assert len(duplicated_edges) == prime

        conflicts_for_row: set[
            tuple[tuple[int, ...], tuple[int, ...]]
        ] = set()
        old_degree = Counter()
        for new_edge in duplicated_edges:
            for old_edge in host:
                if projection_collision(old_edge, new_edge):
                    conflicts_for_row.add((old_edge, new_edge))
                    old_degree[old_edge] += 1

        new_degrees = Counter(new for _, new in conflicts_for_row)
        assert set(new_degrees.values()) == {3 * prime - 2}
        assert len(conflicts_for_row) == prime * (3 * prime - 2)

        maximum_collision_degree = max(
            maximum_collision_degree,
            max(new_degrees.values()),
        )
        maximum_fixed_old_degree = max(
            maximum_fixed_old_degree,
            max(old_degree.values()),
        )

    assert maximum_collision_degree == 3 * prime - 2
    assert maximum_fixed_old_degree == 3

    print(
        f"p={prime}: completion-edge collision degree={maximum_collision_degree}, "
        f"fixed-old per-row degree={maximum_fixed_old_degree}"
    )


def verify_projection(prime: int) -> None:
    """Exhaust small mixed P-perfect matchings and verify projection."""
    # The selected side is encoded by a bit: 0 for the original reservoir and
    # 1 for its duplicate.  Matching is checked separately inside each copy;
    # cross-copy projection collisions are forbidden explicitly.
    choices = [edge(prime, row, column) for row in range(prime) for column in range(prime)]

    selected: list[tuple[int, tuple[int, int, int, int]]] = []
    used = [[set() for _ in range(3)] for _ in range(2)]

    def search(row: int) -> bool:
        if row == prime:
            projected = [item for _, item in selected]
            for part in range(4):
                assert len({item[part] for item in projected}) == prime
            return True

        for side in (0, 1):
            for item in choices[row * prime : (row + 1) * prime]:
                if any(item[part + 1] in used[side][part] for part in range(3)):
                    continue
                if any(
                    other_side != side and projection_collision(other, item)
                    for other_side, other in selected
                ):
                    continue

                selected.append((side, item))
                for part in range(3):
                    used[side][part].add(item[part + 1])
                if search(row + 1):
                    return True
                for part in range(3):
                    used[side][part].remove(item[part + 1])
                selected.pop()
        return False

    assert search(0)


def main() -> None:
    for prime in (5, 7, 11, 13):
        verify_prime(prime)
    for prime in (3, 5):
        verify_projection(prime)
    print("PX158--PX159 duplicated-reservoir reduction verified")


if __name__ == "__main__":
    main()
