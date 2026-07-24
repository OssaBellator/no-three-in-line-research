#!/usr/bin/env python3
"""Verify PX98--PX99: strong-complete four-trades and the p=13 census."""
from __future__ import annotations

from collections import Counter, deque
from itertools import combinations
from math import prod

Permutation = tuple[int, ...]

EXPECTED_COUNTS = {5: 10, 7: 28, 11: 88, 13: 4524}
EXPECTED_DEGREES_13 = {0: 1456, 2: 2028, 7: 1014, 39: 26}
EXPECTED_CYLINDER_MAXIMA_13 = {1: 348, 2: 58, 3: 20}


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
        sorted(mapping) == list(range(p))
        and sorted((x - mapping[x]) % p for x in range(p)) == list(range(p))
        and sorted((x + mapping[x]) % p for x in range(p)) == list(range(p))
    )


def trade(
    mapping: Permutation,
    a: int,
    r: int,
    s: int,
) -> Permutation | None:
    p = len(mapping)
    if any(value % p == 0 for value in (r, s, r - s, r + s)):
        return None

    A = mapping[a]
    rows = (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
    old_images = (A, (A + s) % p, (A + r) % p, (A + r + s) % p)
    if tuple(mapping[row] for row in rows) != old_images:
        return None

    new_images = ((A + r + s) % p, (A + r) % p, (A + s) % p, A)
    updated = list(mapping)
    for row, image in zip(rows, new_images):
        updated[row] = image
    result = tuple(updated)
    assert sum(result[row] != mapping[row] for row in range(p)) == 4
    assert is_strong(result)
    return result


def affine_parameters(mapping: Permutation) -> tuple[int, int] | None:
    p = len(mapping)
    translation = mapping[0]
    slope = (mapping[1] - translation) % p
    if all(mapping[x] == (slope * x + translation) % p for x in range(p)):
        return slope, translation
    return None


def switching_graph(
    mappings: tuple[Permutation, ...],
) -> tuple[tuple[frozenset[int], ...], Counter[int], Counter[tuple[int, int]]]:
    p = len(mappings[0])
    index = {mapping: position for position, mapping in enumerate(mappings)}
    adjacency: list[set[int]] = [set() for _ in mappings]
    witness_multiplicity: Counter[tuple[int, int]] = Counter()

    for position, mapping in enumerate(mappings):
        for a in range(p):
            for r in range(1, p):
                for s in range(1, p):
                    neighbour = trade(mapping, a, r, s)
                    if neighbour is None:
                        continue
                    other = index[neighbour]
                    adjacency[position].add(other)
                    edge = (position, other) if position < other else (other, position)
                    witness_multiplicity[edge] += 1

    frozen = tuple(frozenset(neighbours) for neighbours in adjacency)
    degrees = Counter(len(neighbours) for neighbours in frozen)
    return frozen, degrees, witness_multiplicity


def component_sizes(adjacency: tuple[frozenset[int], ...]) -> list[int]:
    unseen = set(range(len(adjacency)))
    sizes: list[int] = []
    while unseen:
        start = unseen.pop()
        queue = deque([start])
        size = 0
        while queue:
            vertex = queue.popleft()
            size += 1
            for neighbour in adjacency[vertex]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    queue.append(neighbour)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def maximum_cylinder_count(
    mappings: tuple[Permutation, ...],
    rank: int,
) -> int:
    p = len(mappings[0])
    counts: Counter[tuple[int, ...]] = Counter()
    for mapping in mappings:
        for rows in combinations(range(p), rank):
            key: list[int] = []
            for row in rows:
                key.extend((row, mapping[row]))
            counts[tuple(key)] += 1
    return max(counts.values())


def verify_small_counts() -> dict[int, tuple[Permutation, ...]]:
    result: dict[int, tuple[Permutation, ...]] = {}
    for p, expected in EXPECTED_COUNTS.items():
        mappings = strong_complete_mappings(p)
        assert len(mappings) == expected
        assert all(is_strong(mapping) for mapping in mappings)
        result[p] = mappings
        print(f"p={p}: strong complete mappings={len(mappings)}")
    return result


def verify_order_thirteen(mappings: tuple[Permutation, ...]) -> None:
    adjacency, degrees, witness_multiplicity = switching_graph(mappings)
    assert dict(degrees) == EXPECTED_DEGREES_13
    assert sum(len(neighbours) for neighbours in adjacency) // 2 == 6084
    assert component_sizes(adjacency) == [3068] + [1] * 1456
    assert set(witness_multiplicity.values()) == {8}
    # Each undirected trade is generated four times from each endpoint.

    affine_by_degree: Counter[int] = Counter()
    nonlinear_by_degree: Counter[int] = Counter()
    for mapping, neighbours in zip(mappings, adjacency):
        target = affine_by_degree if affine_parameters(mapping) else nonlinear_by_degree
        target[len(neighbours)] += 1
    assert affine_by_degree == Counter({0: 104, 39: 26})
    assert nonlinear_by_degree == Counter({0: 1352, 2: 2028, 7: 1014})

    roots_minus_one = {
        slope
        for slope in range(13)
        if slope * slope % 13 == 12
    }
    assert roots_minus_one == {5, 8}
    assert all(
        affine_parameters(mapping) is not None
        and affine_parameters(mapping)[0] in roots_minus_one
        for mapping, neighbours in zip(mappings, adjacency)
        if len(neighbours) == 39
    )

    maxima = {
        rank: maximum_cylinder_count(mappings, rank)
        for rank in (1, 2, 3)
    }
    assert maxima == EXPECTED_CYLINDER_MAXIMA_13
    falling = {rank: prod(range(13 - rank + 1, 14)) for rank in (1, 2, 3)}
    assert maxima[1] * falling[1] == len(mappings)
    assert maxima[2] * falling[2] == 2 * len(mappings)
    assert 29 * maxima[3] * falling[3] == 220 * len(mappings)

    print(f"p=13 degree distribution: {dict(sorted(degrees.items()))}")
    print("p=13 components: one of size 3068 and 1456 isolated vertices")
    print("p=13 switching edges=6084; four witnesses per directed trade")
    print(f"p=13 cylinder maxima: {maxima}")
    print("p=13 normalized cylinder constants: 1, 2, 220/29")


def verify_symbolic_trade() -> None:
    for p in (5, 7, 11, 13):
        for a in range(p):
            for A in range(p):
                for r in range(1, p):
                    for s in range(1, p):
                        if any(value % p == 0 for value in (r - s, r + s)):
                            continue
                        rows = (a, (a + r) % p, (a - s) % p, (a - s + r) % p)
                        old = (A, (A + s) % p, (A + r) % p, (A + r + s) % p)
                        new = ((A + r + s) % p, (A + r) % p, (A + s) % p, A)
                        assert len(set(rows)) == len(set(old)) == len(set(new)) == 4
                        assert sorted((x - y) % p for x, y in zip(rows, old)) == sorted(
                            (x - y) % p for x, y in zip(rows, new)
                        )
                        assert sorted((x + y) % p for x, y in zip(rows, old)) == sorted(
                            (x + y) % p for x, y in zip(rows, new)
                        )
    print("PX98 symbolic multiset identities checked through p=13")


def main() -> None:
    verify_symbolic_trade()
    mappings = verify_small_counts()
    verify_order_thirteen(mappings[13])
    print("strong-complete four-trade theorem and census verified")


if __name__ == "__main__":
    main()
