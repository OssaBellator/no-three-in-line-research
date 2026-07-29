#!/usr/bin/env python3
"""Finite audit for SRR2cf--SRR2cj."""

import random
from itertools import combinations

SEED = 1406
SYSTEMS = 3500


def maximum_independent_weight(weights, edges):
    edge_set = {tuple(sorted(edge)) for edge in edges}
    best = 0
    for mask in range(1 << len(weights)):
        if all(not ((mask >> u) & 1 and (mask >> v) & 1) for u, v in edge_set):
            best = max(best, sum(weights[i] for i in range(len(weights)) if mask >> i & 1))
    return best


rng = random.Random(SEED)
stats = {
    "systems": 0, "retained_candidates": 0, "reference_burden": 0,
    "removed_burden": 0, "added_burden": 0, "actual_capacity": 0,
    "paid_thresholds": 0, "overloaded_thresholds": 0, "overload_units": 0,
}

for _ in range(SYSTEMS):
    candidate_count = rng.randint(3, 8)
    atom_count = rng.randint(2, 5)
    weights = [rng.randint(1, 5) for _ in range(candidate_count)]
    costs = [rng.randint(0, 4) for _ in range(candidate_count)]
    threshold = rng.randint(1, 4)
    reference_vertices = [i for i in range(candidate_count) if costs[i] <= threshold]

    reference_edges = []
    for u, v in combinations(reference_vertices, 2):
        if rng.random() < 0.30:
            reference_edges.append((u, v, rng.randrange(atom_count)))

    deleted = {v for v in reference_vertices if rng.random() < 0.18}
    retained = [v for v in reference_vertices if v not in deleted]
    retained_reference = [
        edge for edge in reference_edges if edge[0] in retained and edge[1] in retained
    ]
    existing = {tuple(sorted((u, v))) for u, v, _atom in retained_reference}
    added_edges = []
    for u, v in combinations(retained, 2):
        if (u, v) not in existing and rng.random() < 0.12:
            added_edges.append((u, v, rng.randrange(atom_count)))
    actual_edges = retained_reference + added_edges

    def burden(edges):
        result = [0] * atom_count
        for u, v, atom in edges:
            result[atom] += weights[u] + weights[v]
        return result

    reference_burden = burden(reference_edges)
    retained_burden = burden(retained_reference)
    added_burden = burden(added_edges)
    actual_burden = burden(actual_edges)
    removed_burden = [reference_burden[a] - retained_burden[a] for a in range(atom_count)]
    assert all(
        actual_burden[a] == reference_burden[a] - removed_burden[a] + added_burden[a]
        for a in range(atom_count)
    )

    reference_capacity = [
        max(0, reference_burden[a] + rng.randint(-3, 4))
        for a in range(atom_count)
    ]
    deposits = [rng.randint(0, 4) for _ in range(atom_count)]
    losses = [rng.randint(0, reference_capacity[a] + deposits[a]) for a in range(atom_count)]
    actual_capacity = [reference_capacity[a] + deposits[a] - losses[a] for a in range(atom_count)]

    local_index = {vertex: i for i, vertex in enumerate(retained)}
    independent = maximum_independent_weight(
        [weights[v] for v in retained],
        [(local_index[u], local_index[v]) for u, v, _atom in actual_edges],
    )
    total_weight = sum(weights[v] for v in retained)
    overloaded = [a for a in range(atom_count) if actual_burden[a] > actual_capacity[a]]

    if not overloaded:
        bound = 0 if total_weight == 0 else total_weight ** 2 / (
            total_weight + sum(actual_capacity)
        )
        assert independent + 1e-9 >= bound
        stats["paid_thresholds"] += 1
    else:
        stats["overloaded_thresholds"] += 1
        stats["overload_units"] += sum(actual_burden[a] - actual_capacity[a] for a in overloaded)

    stats["systems"] += 1
    stats["retained_candidates"] += len(retained)
    stats["reference_burden"] += sum(reference_burden)
    stats["removed_burden"] += sum(removed_burden)
    stats["added_burden"] += sum(added_burden)
    stats["actual_capacity"] += sum(actual_capacity)

for key, value in stats.items():
    print(f"{key}: {value}")
