#!/usr/bin/env python3
from collections import Counter


def components(vertex_count, adjacency):
    seen = set()
    answer = []
    for start in range(vertex_count):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        current = []
        while stack:
            vertex = stack.pop()
            current.append(vertex)
            for neighbour in adjacency[vertex]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        answer.append(tuple(sorted(current)))
    return tuple(answer)


def is_bipartite(vertex_count, adjacency):
    colours = {}
    for start in range(vertex_count):
        if start in colours:
            continue
        colours[start] = 0
        stack = [start]
        while stack:
            vertex = stack.pop()
            for neighbour in adjacency[vertex]:
                if neighbour in colours:
                    if colours[neighbour] == colours[vertex]:
                        return False
                else:
                    colours[neighbour] = 1 - colours[vertex]
                    stack.append(neighbour)
    return True


def independence_number(vertex_count, adjacency):
    best = 0
    for mask in range(1 << vertex_count):
        if mask.bit_count() <= best:
            continue
        if all(
            not ((mask >> first) & 1 and (mask >> second) & 1)
            for first in range(vertex_count)
            for second in adjacency[first]
            if first < second
        ):
            best = mask.bit_count()
    return best


def bipartite_matching(left_size, right_size, edges):
    neighbours = [[] for _ in range(left_size)]
    for left, right in edges:
        neighbours[left].append(right)
    matched_left = [-1] * right_size

    def augment(left, seen):
        for right in neighbours[left]:
            if seen[right]:
                continue
            seen[right] = True
            if matched_left[right] < 0 or augment(matched_left[right], seen):
                matched_left[right] = left
                return True
        return False

    return sum(augment(left, [False] * right_size) for left in range(left_size))


graphs_checked = 0
degree_two_graphs = 0
edge_histogram = Counter()
component_histogram = Counter()

for left_size in range(1, 5):
    for right_size in range(1, 5):
        possible = tuple(
            (left, right)
            for left in range(left_size)
            for right in range(right_size)
        )
        for mask in range(1 << len(possible)):
            graphs_checked += 1
            edges = tuple(
                edge for index, edge in enumerate(possible)
                if mask & (1 << index)
            )

            # First-stage resource incidence: motif-overlap components are exactly
            # the motif projections of the incidence components.
            incidence_adjacency = [set() for _ in range(left_size + right_size)]
            for left, right in edges:
                incidence_adjacency[left].add(left_size + right)
                incidence_adjacency[left_size + right].add(left)

            overlap_adjacency = [set() for _ in range(left_size)]
            for right in range(right_size):
                users = [left for left in range(left_size) if (left, right) in edges]
                for first_index, first in enumerate(users):
                    for second in users[first_index + 1:]:
                        overlap_adjacency[first].add(second)
                        overlap_adjacency[second].add(first)

            incidence_motif_parts = sorted(
                tuple(vertex for vertex in component if vertex < left_size)
                for component in components(
                    left_size + right_size, incidence_adjacency
                )
                if any(vertex < left_size for vertex in component)
            )
            assert incidence_motif_parts == sorted(
                components(left_size, overlap_adjacency)
            )

            degrees = [0] * (left_size + right_size)
            for left, right in edges:
                degrees[left] += 1
                degrees[left_size + right] += 1
            if max(degrees, default=0) > 2:
                continue

            degree_two_graphs += 1
            edge_count = len(edges)
            conflict_adjacency = [set() for _ in range(edge_count)]
            for first_index, (first_source, first_host) in enumerate(edges):
                for second_index in range(first_index + 1, edge_count):
                    second_source, second_host = edges[second_index]
                    if first_source == second_source or first_host == second_host:
                        conflict_adjacency[first_index].add(second_index)
                        conflict_adjacency[second_index].add(first_index)

            assert max((len(part) for part in conflict_adjacency), default=0) <= 2
            assert is_bipartite(edge_count, conflict_adjacency)

            odd_paths = 0
            component_retention = 0
            for component in components(edge_count, conflict_adjacency):
                size = len(component)
                is_cycle = size >= 4 and all(
                    len(conflict_adjacency[vertex]) == 2
                    for vertex in component
                )
                if is_cycle:
                    component_retention += size // 2
                    component_histogram[("even_cycle", size)] += 1
                else:
                    component_retention += (size + 1) // 2
                    odd_paths += size % 2
                    component_histogram[("path", size)] += 1

            matching = bipartite_matching(left_size, right_size, edges)
            retained = independence_number(edge_count, conflict_adjacency)
            assert retained == matching == component_retention
            assert 2 * retained == edge_count + odd_paths
            edge_histogram[edge_count] += 1

assert graphs_checked == 74954
assert degree_two_graphs == 10172

print({
    "bipartite_incidence_graphs_checked": graphs_checked,
    "maximum_degree_two_incidence_graphs": degree_two_graphs,
    "first_stage_component_projection_verified": True,
    "centre_conflict_representation": "H=line_graph(D)",
    "degree_two_label_load_implies": "H is bipartite with path/even-cycle components",
    "exact_retention": "alpha(H)=nu(D)=(|E(D)|+odd_path_components(H))/2",
    "edge_count_histogram": dict(sorted(edge_histogram.items())),
    "remaining_gap": "a coordinate host must supply complete defect labels and bounded packet interfaces",
    "evidence_level": "exact_unified_incidence_hall_interface",
    "status": "passed",
})
