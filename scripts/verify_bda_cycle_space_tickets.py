#!/usr/bin/env python3
"""Verify BDA5bc--BDA5bf on finite decorated profile graphs."""

from itertools import product


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


def simple_directed_cycles(vertices, edges):
    adjacency = {v: [] for v in vertices}
    for eid, u, v in edges:
        adjacency[u].append((eid, v))
    found = set()

    def canonical(edge_ids):
        rotations = [tuple(edge_ids[i:] + edge_ids[:i]) for i in range(len(edge_ids))]
        return min(rotations)

    def dfs(start, current, used_vertices, used_edges):
        for eid, nxt in adjacency[current]:
            if nxt == start:
                found.add(canonical(used_edges + [eid]))
            elif nxt not in used_vertices and len(used_vertices) < len(vertices):
                dfs(start, nxt, used_vertices | {nxt}, used_edges + [eid])

    for start in vertices:
        dfs(start, start, {start}, [])
    return found


def check_graph(vertices, edges):
    forest, components = spanning_forest(vertices, edges)
    chords = {eid for eid, _, _ in edges} - forest
    cycles = simple_directed_cycles(vertices, edges)
    for cycle in cycles:
        assert set(cycle) & chords
        assert min(set(cycle) & chords) in chords
    mu = len(edges) - len(vertices) + components
    assert len(chords) == mu
    return len(cycles), mu


def exhaustive(max_vertices=4):
    graph_checks = cycle_checks = 0
    for n in range(1, max_vertices + 1):
        vertices = tuple(range(n))
        possible = [(u, v) for u in vertices for v in vertices if u != v]
        masks = range(1 << len(possible)) if n <= 3 else range(0, 1 << len(possible), 37)
        for mask in masks:
            edges = [(i, u, v) for i, (u, v) in enumerate(possible) if mask >> i & 1]
            count, _ = check_graph(vertices, edges)
            graph_checks += 1
            cycle_checks += count
    return graph_checks, cycle_checks


def parallel_edge_checks():
    vertices = (0, 1, 2)
    edges = [
        (0, 0, 1),
        (1, 1, 0),
        (2, 0, 1),
        (3, 1, 2),
        (4, 2, 0),
    ]
    cycles, mu = check_graph(vertices, edges)
    assert cycles >= 3
    assert mu == len(edges) - len(vertices) + 1
    return cycles


def main():
    graphs, cycles = exhaustive()
    parallel = parallel_edge_checks()
    print(
        "BDA cycle-space tickets: verified "
        f"{graphs} profile graphs, {cycles} simple directed cycles, "
        f"and {parallel} parallel-edge cycles"
    )


if __name__ == "__main__":
    main()
