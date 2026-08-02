#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache
from itertools import combinations

REQUIRED_GOOD = 28

def minimum_vertex_cover(vertex_count, edges):
    edges = tuple(edges)
    for size in range(vertex_count + 1):
        for chosen in combinations(range(vertex_count), size):
            cover = set(chosen)
            if all(u in cover or v in cover for u, v in edges):
                return size
    raise AssertionError("finite graph must have a vertex cover")

def maximum_matching(vertex_count, edges):
    adjacency = [set() for _ in range(vertex_count)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)

    @lru_cache(None)
    def solve(mask):
        if mask == 0:
            return 0
        low = mask & -mask
        u = low.bit_length() - 1
        best = solve(mask ^ low)
        for v in adjacency[u]:
            bit = 1 << v
            if mask & bit:
                best = max(best, 1 + solve(mask ^ low ^ bit))
        return best

    return solve((1 << vertex_count) - 1)

def is_bipartite(vertex_count, edges):
    adjacency = [[] for _ in range(vertex_count)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    colour = [-1] * vertex_count
    for start in range(vertex_count):
        if colour[start] != -1:
            continue
        colour[start] = 0
        stack = [start]
        while stack:
            u = stack.pop()
            for v in adjacency[u]:
                if colour[v] == -1:
                    colour[v] = 1 - colour[u]
                    stack.append(v)
                elif colour[v] == colour[u]:
                    return False
    return True

def maximum_conflict_free_centres(total_good_centres, edges):
    return total_good_centres - minimum_vertex_cover(total_good_centres, edges)

def minimum_motifs_for_matching_bound(matching_bound):
    return (REQUIRED_GOOD + matching_bound + 2) // 3

all_edges = tuple(combinations(range(6), 2))
bipartite_graphs = 0
cover_histogram = Counter()
for mask in range(1 << len(all_edges)):
    edges = tuple(all_edges[index] for index in range(len(all_edges)) if mask & (1 << index))
    tau = minimum_vertex_cover(6, edges)
    cover_histogram[tau] += 1
    alpha = 6 - tau
    assert alpha + tau == 6
    assert tau <= len(edges)
    if is_bipartite(6, edges):
        bipartite_graphs += 1
        assert tau == maximum_matching(6, edges)

assert bipartite_graphs == 5177
assert cover_histogram == Counter({0:1, 1:171, 2:4970, 3:21837, 4:5788, 5:1})

for corruption_edges in range(0, 8):
    matching = tuple((2*i, 2*i+1) for i in range(corruption_edges))
    vertex_count = max(30, 2 * corruption_edges)
    assert minimum_vertex_cover(vertex_count, matching) == corruption_edges
    assert maximum_matching(vertex_count, matching) == corruption_edges
    assert maximum_conflict_free_centres(vertex_count, matching) == vertex_count - corruption_edges

assert minimum_motifs_for_matching_bound(0) == 10
assert minimum_motifs_for_matching_bound(2) == 10
assert minimum_motifs_for_matching_bound(3) == 11
assert minimum_motifs_for_matching_bound(5) == 11
assert minimum_motifs_for_matching_bound(6) == 12
assert 3 * 10 - 2 == 28
assert 3 * 10 - 3 == 27

print({
    "intrinsic_good_centres_per_motif": 3,
    "required_good_centres": REQUIRED_GOOD,
    "exact_conflict_free_count": "3t - tau(H)",
    "exact_hall_condition": "3t - tau(H) >= 28",
    "bipartite_reduction": "tau(H) = nu(H)",
    "bipartite_hall_condition": "3t - nu(H) >= 28",
    "minimum_motifs_for_matching_bound": "ceil((28+nu)/3)",
    "ten_motif_matching_tolerance": 2,
    "eleven_motif_matching_tolerance": 5,
    "six_vertex_graphs_checked": 32768,
    "six_vertex_bipartite_graphs_checked": bipartite_graphs,
    "vertex_cover_histogram_n6": dict(sorted(cover_histogram.items())),
    "remaining_gap": "the geometry must construct resource-disjoint motifs and prove that cross-copy incompatibility is represented by the certified conflict graph while preserving the two degree-two restrictions",
    "evidence_level": "exact_conditional_conflict_graph_interface",
    "status": "passed",
})
