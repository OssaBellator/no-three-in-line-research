#!/usr/bin/env python3
"""Finite checks for PX499--PX500 two-column selector normal form."""
from __future__ import annotations

from collections import Counter
import random

Permutation = tuple[int, ...]


def compose(first: Permutation, second: Permutation) -> Permutation:
    return tuple(first[second[index]] for index in range(len(first)))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for index, value in enumerate(permutation):
        result[value] = index
    return tuple(result)


def power(permutation: Permutation, exponent: int) -> Permutation:
    return tuple(range(len(permutation))) if exponent == 0 else permutation


def original_maps(H, T, P, Q):
    return {
        (i, j, s): compose(
            power(Q, j),
            compose(T, compose(power(H, s), power(P, i))),
        )
        for i in (0, 1)
        for j in (0, 1)
        for s in (0, 1)
    }


def two_column_maps(H, A0, A1, P):
    return {
        (i, j, s): compose(
            (A0, A1)[j],
            compose(power(H, s), power(P, i)),
        )
        for i in (0, 1)
        for j in (0, 1)
        for s in (0, 1)
    }


def abstract_adjacency(n: int, H: Permutation, P: Permutation):
    adjacency = []
    for i in (0, 1):
        for u in range(n):
            source = P[u] if i else u
            adjacency.append(
                tuple(
                    n * j + (H[source] if s else source)
                    for j in (0, 1)
                    for s in (0, 1)
                )
            )
    return adjacency


def perfect_matching(adjacency, available):
    order = len(adjacency)
    matched_column = [-1] * order

    def augment(row: int, seen: set[int]) -> bool:
        for column in adjacency[row]:
            if not available[row][column] or column in seen:
                continue
            seen.add(column)
            if matched_column[column] < 0 or augment(matched_column[column], seen):
                matched_column[column] = row
                return True
        return False

    for row in range(order):
        assert augment(row, set())

    matched_row = [-1] * order
    for column, row in enumerate(matched_column):
        matched_row[row] = column
    return matched_row


def two_factor(adjacency):
    order = len(adjacency)
    available = [[False] * order for _ in range(order)]
    for row in range(order):
        for column in adjacency[row]:
            available[row][column] = True

    selected: set[tuple[int, int]] = set()
    for _ in range(2):
        matching = perfect_matching(adjacency, available)
        for row, column in enumerate(matching):
            selected.add((row, column))
            available[row][column] = False
    return selected


def scalar_points(n, A0, A1, selected, orientation):
    points = []
    for row, column in selected:
        i, u = divmod(row, n)
        j, w = divmod(column, n)
        x = n * i + u if orientation[0] == "c" else 2 * u + i
        image = (A0, A1)[j][w]
        y = n * j + image if orientation[1] == "c" else 2 * image + j
        points.append((x, y))
    return points


def alternating_cycle(adjacency, selected, rng):
    row = rng.randrange(len(adjacency))
    first_visit = {row: 0}
    unselected_edges = []
    selected_edges = []

    for _ in range(100):
        column = rng.choice(
            [column for column in adjacency[row] if (row, column) not in selected]
        )
        next_row = rng.choice(
            [candidate for candidate in range(len(adjacency))
             if (candidate, column) in selected]
        )
        unselected_edges.append((row, column))
        selected_edges.append((next_row, column))

        if next_row in first_visit:
            start = first_visit[next_row]
            result = set(selected)
            for edge in unselected_edges[start:]:
                result.add(edge)
            for edge in selected_edges[start:]:
                result.remove(edge)
            return result

        row = next_row
        first_visit[row] = len(unselected_edges)

    raise AssertionError("alternating walk did not close")


def check() -> None:
    rng = random.Random(499)

    for n in range(2, 8):
        for _ in range(100):
            while True:
                candidate = list(range(n))
                rng.shuffle(candidate)
                H = tuple(candidate)
                if all(H[index] != index for index in range(n)):
                    break

            values = []
            for _ in range(3):
                candidate = list(range(n))
                rng.shuffle(candidate)
                values.append(tuple(candidate))
            T, P, Q = values

            A0 = T
            A1 = compose(Q, T)
            assert original_maps(H, T, P, Q) == two_column_maps(H, A0, A1, P)
            assert compose(A1, inverse(A0)) == Q

            adjacency = abstract_adjacency(n, H, P)
            selected = two_factor(adjacency)
            flipped = alternating_cycle(adjacency, selected, rng)

            for selector in (selected, flipped):
                assert all(
                    sum((row, column) in selector for column in adjacency[row]) == 2
                    for row in range(2 * n)
                )
                assert all(
                    sum((row, column) in selector for row in range(2 * n)) == 2
                    for column in range(2 * n)
                )

                for orientation in ("cc", "cf", "fc", "ff"):
                    points = scalar_points(n, A0, A1, selector, orientation)
                    row_degree = Counter(x for x, _ in points)
                    column_degree = Counter(y for _, y in points)
                    assert len(points) == 4 * n
                    assert all(row_degree[x] == 2 for x in range(2 * n))
                    assert all(column_degree[y] == 2 for y in range(2 * n))

    print("PX499--PX500 two-column selector normal-form verifier: PASS")


if __name__ == "__main__":
    check()
