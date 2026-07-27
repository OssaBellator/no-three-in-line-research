#!/usr/bin/env python3
"""Verify RI5au--RI5ax: rank-at-most-three partial-permutation types."""

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial


EXPECTED = {
    1: {0: {(("P", 1),)}},
    2: {
        0: {(("P", 1), ("P", 1))},
        1: {(("P", 2),)},
        2: {(("C", 2),)},
    },
    3: {
        0: {(("P", 1), ("P", 1), ("P", 1))},
        1: {(("P", 1), ("P", 2))},
        2: {(("P", 3),), (("C", 2), ("P", 1))},
        3: {(("C", 3),)},
    },
}


def derangements(size):
    return [
        p for p in permutations(range(size))
        if all(p[i] != i for i in range(size))
    ]


def extension_formula(size, rank, overlap):
    free_diagonal = size - 2 * rank + overlap
    return sum(
        (-1) ** j * comb(free_diagonal, j) * factorial(size - rank - j)
        for j in range(free_diagonal + 1)
    )


def component_type(arcs):
    out = dict(arcs)
    indegree = Counter(v for _, v in arcs)
    vertices = set(out) | set(indegree)
    seen = set()
    components = []

    for vertex in sorted(vertices):
        if vertex in seen or indegree[vertex] != 0 or vertex not in out:
            continue
        current = vertex
        length = 0
        while current in out and current not in seen:
            seen.add(current)
            current = out[current]
            length += 1
        seen.add(current)
        components.append(("P", length))

    for vertex in sorted(vertices):
        if vertex in seen:
            continue
        current = vertex
        length = 0
        while current not in seen:
            seen.add(current)
            current = out[current]
            length += 1
        components.append(("C", length))

    return tuple(sorted(components))


def verify_types(size=7):
    checks = 0
    for rank in (1, 2, 3):
        by_overlap = defaultdict(set)
        for columns in combinations(range(size), rank):
            for rows in combinations(range(size), rank):
                for image in permutations(rows):
                    arcs = tuple(zip(columns, image))
                    if any(c == r for c, r in arcs):
                        continue
                    overlap = len(set(columns) & set(rows))
                    by_overlap[overlap].add(component_type(arcs))
                    checks += 1
        assert dict(by_overlap) == EXPECTED[rank]
    return checks


def verify_extension_counts(maximum_size=7):
    checks = 0
    for size in range(2, maximum_size + 1):
        bank = derangements(size)
        for rank in range(1, min(3, size) + 1):
            counts = defaultdict(set)
            for columns in combinations(range(size), rank):
                for rows in combinations(range(size), rank):
                    for image in permutations(rows):
                        arcs = tuple(zip(columns, image))
                        if any(c == r for c, r in arcs):
                            continue
                        count = sum(
                            all(p[c] == r for c, r in arcs)
                            for p in bank
                        )
                        overlap = len(set(columns) & set(rows))
                        signature = component_type(arcs)
                        counts[(overlap, signature)].add(count)
                        assert count == extension_formula(size, rank, overlap)
                        checks += 1
            for values in counts.values():
                assert len(values) == 1
    return checks


def verify_type_loss():
    type_counts = {rank: sum(len(v) for v in EXPECTED[rank].values()) for rank in EXPECTED}
    assert type_counts == {1: 1, 2: 3, 3: 5}
    assert max(len(v) for v in EXPECTED[3].values()) == 2
    assert all(len(v) == 1 for rank in (1, 2) for v in EXPECTED[rank].values())
    return type_counts


def main():
    types = verify_types()
    counts = verify_extension_counts()
    losses = verify_type_loss()
    print(
        "RI partial-permutation types: verified "
        f"{types} type instances, {counts} derangement-extension prescriptions, "
        f"with canonical type counts {losses}"
    )


if __name__ == "__main__":
    main()
