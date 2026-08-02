#!/usr/bin/env python3
from collections import Counter


def audit_graph(left_size, right_size, mask):
    size = left_size + right_size
    adjacency = [set() for _ in range(size)]
    for left in range(left_size):
        for right in range(right_size):
            if mask & (1 << (left * right_size + right)):
                u, v = left, left_size + right
                adjacency[u].add(v)
                adjacency[v].add(u)
    if max(map(len, adjacency), default=0) > 2:
        return None

    seen = set()
    odd_path_components = 0
    component_types = Counter()
    for start in range(size):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        vertices = []
        edge_twice = 0
        while stack:
            vertex = stack.pop()
            vertices.append(vertex)
            edge_twice += len(adjacency[vertex])
            for neighbour in adjacency[vertex]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        edges = edge_twice // 2
        cycle = len(vertices) > 1 and edges == len(vertices)
        kind = "even_cycle" if cycle else "path"
        component_types[(kind, len(vertices))] += 1
        if not cycle and len(vertices) % 2:
            odd_path_components += 1

    independence = 0
    for subset in range(1 << size):
        valid = True
        for left in range(left_size):
            if not subset & (1 << left):
                continue
            if any(subset & (1 << neighbour) for neighbour in adjacency[left]):
                valid = False
                break
        if valid:
            independence = max(independence, subset.bit_count())

    assert 2 * independence == size + odd_path_components
    return independence, odd_path_components, component_types


checked = 0
profile = Counter()
for left_size in range(1, 5):
    for right_size in range(1, 5):
        for mask in range(1 << (left_size * right_size)):
            result = audit_graph(left_size, right_size, mask)
            if result is None:
                continue
            independence, odd_paths, _ = result
            checked += 1
            profile[(left_size + right_size, odd_paths, independence)] += 1

assert checked == 10172

required_odd_paths = {
    motifs: max(0, 56 - 3 * motifs)
    for motifs in range(10, 20)
}
assert required_odd_paths[10] == 26
assert required_odd_paths[11] == 23
assert required_odd_paths[12] == 20
assert required_odd_paths[19] == 0


def retained(path_sizes, cycle_sizes):
    assert all(size >= 1 for size in path_sizes)
    assert all(size >= 4 and size % 2 == 0 for size in cycle_sizes)
    total = sum(path_sizes) + sum(cycle_sizes)
    odd_paths = sum(size % 2 for size in path_sizes)
    return total, odd_paths, (total + odd_paths) // 2


assert retained([1] * 26 + [2, 2], [])[2] == 28
assert retained([1] * 23 + [2] * 5, [])[2] == 28
assert retained([1] * 20 + [2] * 8, [])[2] == 28

print({
    "degree_two_bipartite_graphs_checked": checked,
    "exact_formula": "alpha(H)=(|V(H)|+odd_path_components(H))/2",
    "odd_paths_include_isolated_vertices": True,
    "hall_condition": "3*q+odd_path_components>=56",
    "required_odd_paths": required_odd_paths,
    "profile_cells": len(profile),
    "remaining_gap": "a coordinate host must certify q selected motifs and the odd-path count of the complete centre-conflict graph",
    "evidence_level": "exact_degree_two_odd_path_surplus_interface",
    "status": "passed",
})
