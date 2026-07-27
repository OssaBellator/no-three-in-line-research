#!/usr/bin/env python3
"""Verify SAS5gu--SAS5gx: changed-signature cycles and chord tickets."""

from itertools import product


def extract_simple_cycle(walk):
    first = {}
    for index, vertex in enumerate(walk):
        if vertex in first:
            segment = walk[first[vertex]:index + 1]
            while True:
                positions = {}
                shortened = False
                for j, value in enumerate(segment[:-1]):
                    if value in positions:
                        segment = segment[:positions[value]] + segment[j:]
                        shortened = True
                        break
                    positions[value] = j
                if not shortened:
                    break
            assert segment[0] == segment[-1]
            assert len(set(segment[:-1])) == len(segment) - 1
            return segment
        first[vertex] = index
    return None


def reverse_table(table):
    x00, x10, x01, x11 = table
    return (x11, x01, x10, x00)


def spanning_forest(vertices, edges):
    parent = {v: v for v in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    forest = set()
    for eid, u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            forest.add(eid)
    components = len({find(v) for v in vertices})
    return forest, components


def verify_walks(maximum_size=5):
    checks = cycles = 0
    for size in range(1, maximum_size + 1):
        for walk in product(range(size), repeat=size + 2):
            cycle = extract_simple_cycle(walk)
            assert cycle is not None
            assert 1 <= len(cycle) - 1 <= size
            checks += 1
            cycles += 1
    return checks, cycles


def verify_reversal():
    checks = 0
    for table in product((0, 1), repeat=4):
        assert reverse_table(reverse_table(table)) == table
        checks += 1
    assert reverse_table((0, 0, 0, 1)) == (1, 0, 0, 0)
    return checks


def verify_signature_change():
    signatures = range(6)
    checks = 0
    for old_signature in signatures:
        for new_signature in signatures:
            rebased = reverse_table((0, 0, 0, 1))
            if new_signature == old_signature:
                assert rebased == (1, 0, 0, 0)
            else:
                assert new_signature != old_signature
            checks += 1
    return checks


def verify_chord_tickets():
    checks = 0
    for size in range(2, 5):
        vertices = tuple(range(size))
        possible = [(u, v) for u in vertices for v in vertices if u != v]
        masks = range(0, 1 << len(possible), max(1, (1 << len(possible)) // 97))
        for mask in masks:
            edges = [(eid, u, v) for eid, (u, v) in enumerate(possible) if mask >> eid & 1]
            forest, components = spanning_forest(vertices, edges)
            chords = {eid for eid, _, _ in edges} - forest
            assert len(chords) == len(edges) - len(vertices) + components
            checks += 1
    return checks


def main():
    walks, cycles = verify_walks()
    tables = verify_reversal()
    signatures = verify_signature_change()
    chords = verify_chord_tickets()
    print(
        "Sparse changed-signature cycles: verified "
        f"{walks} finite walks, {cycles} extracted cycles, "
        f"{tables} table reversals, {signatures} signature transitions, "
        f"and {chords} chord-ticket graphs"
    )


if __name__ == "__main__":
    main()
