#!/usr/bin/env python3
from itertools import product


def components(vertex_count, edges):
    adjacency = [set() for _ in range(vertex_count)]
    for first, second in edges:
        adjacency[first].add(second)
        adjacency[second].add(first)
    seen = set()
    answer = []
    for start in range(vertex_count):
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
        answer.append((tuple(vertices), edge_twice // 2))
    return answer, adjacency


def independence_number(vertex_count, edges):
    edge_masks = [(1 << first) | (1 << second) for first, second in edges]
    best = 0
    for mask in range(1 << vertex_count):
        if mask.bit_count() <= best:
            continue
        if all(mask & edge_mask != edge_mask for edge_mask in edge_masks):
            best = mask.bit_count()
    return best


graphs_checked = 0
degree_two_graphs = 0
path_components = 0
cycle_components = 0
isolated_components = 0

for left_size in range(1, 5):
    for right_size in range(1, 5):
        possible = [
            (left, left_size + right)
            for left in range(left_size)
            for right in range(right_size)
        ]
        for edge_mask in range(1 << len(possible)):
            edges = tuple(
                edge
                for index, edge in enumerate(possible)
                if edge_mask & (1 << index)
            )
            graphs_checked += 1
            component_data, adjacency = components(left_size + right_size, edges)
            if max(map(len, adjacency), default=0) > 2:
                continue
            degree_two_graphs += 1
            formula = 0
            matching_loss = 0
            for vertices, edge_count in component_data:
                size = len(vertices)
                if edge_count == 0:
                    isolated_components += 1
                    formula += 1
                elif edge_count == size - 1:
                    path_components += 1
                    formula += (size + 1) // 2
                    matching_loss += size // 2
                else:
                    assert edge_count == size
                    assert size % 2 == 0
                    assert all(len(adjacency[vertex]) == 2 for vertex in vertices)
                    cycle_components += 1
                    formula += size // 2
                    matching_loss += size // 2
            exact = independence_number(left_size + right_size, edges)
            assert formula == exact
            assert exact == left_size + right_size - matching_loss

assert graphs_checked == sum(
    1 << (left * right)
    for left in range(1, 5)
    for right in range(1, 5)
)
assert graphs_checked == 74954
assert degree_two_graphs == 10172


def required_motif_count(loss):
    return (28 + loss + 2) // 3


assert required_motif_count(0) == 10
assert required_motif_count(2) == 10
assert required_motif_count(3) == 11
assert required_motif_count(5) == 11
assert required_motif_count(6) == 12
assert required_motif_count(8) == 12
assert required_motif_count(9) == 13

print({
    "bipartite_graphs_checked": graphs_checked,
    "maximum_partition_size": 4,
    "maximum_degree_two_graphs": degree_two_graphs,
    "component_classification": "isolated vertices, paths, and even cycles",
    "retained_centres_formula": "sum_path ceil(|C|/2)+sum_even_cycle |C|/2",
    "matching_loss_formula": "sum_nontrivial_component floor(|C|/2)",
    "path_components_seen": path_components,
    "cycle_components_seen": cycle_components,
    "isolated_components_seen": isolated_components,
    "ten_motif_loss_budget": 2,
    "eleven_motif_loss_budget": 5,
    "twelve_motif_loss_budget": 8,
    "remaining_gap": "coordinate motifs must still induce a bipartite maximum-degree-two centre-conflict graph and supply enough first-stage motifs",
    "evidence_level": "exact_degree_two_centre_conflict_component_profile",
    "status": "passed",
})
