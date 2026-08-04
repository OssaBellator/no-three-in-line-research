#!/usr/bin/env python3
from itertools import permutations, product
from math import floor

N = 3
ARCS = tuple((i, j) for i in range(N) for j in range(N) if i != j)


def floyd_warshall(cost):
    distance = [[0 if i == j else cost[(i, j)] for j in range(N)] for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance


def hamiltonian_cost(distance):
    best = None
    best_order = None
    for middle in permutations(range(1, N)):
        order = (0,) + middle
        value = sum(distance[order[i]][order[(i + 1) % N]] for i in range(N))
        if best is None or value < best:
            best = value
            best_order = order
    return best, best_order


def balanced(counts):
    outgoing = [0] * N
    incoming = [0] * N
    for count, (u, v) in zip(counts, ARCS):
        outgoing[u] += count
        incoming[v] += count
    return outgoing == incoming


def weakly_connected(counts):
    adjacency = [set() for _ in range(N)]
    for count, (u, v) in zip(counts, ARCS):
        if count:
            adjacency[u].add(v)
            adjacency[v].add(u)
    seen = {0}
    stack = [0]
    while stack:
        current = stack.pop()
        for nxt in adjacency[current]:
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return len(seen) == N


def brute_connector(cost):
    best = None
    best_counts = None
    for counts in product(range(3), repeat=len(ARCS)):
        if not balanced(counts) or not weakly_connected(counts):
            continue
        value = sum(count * cost[arc] for count, arc in zip(counts, ARCS))
        if best is None or value < best:
            best = value
            best_counts = counts
    assert best is not None
    return best, best_counts


def repetitions_needed(bundle_gain, connector_loss, setup):
    assert bundle_gain > 0
    return floor((setup + connector_loss) / bundle_gain) + 1


cases = 0
strict_metric_improvements = 0
maximum_metric_improvement = 0
multiplicity_histogram = {}
example = None
for values in product((1, 2, 3), repeat=len(ARCS)):
    cost = dict(zip(ARCS, values))
    direct, _ = hamiltonian_cost(
        [[0 if i == j else cost[(i, j)] for j in range(N)] for i in range(N)]
    )
    metric = floyd_warshall(cost)
    metric_tour, order = hamiltonian_cost(metric)
    brute, counts = brute_connector(cost)
    assert brute == metric_tour
    maximum_multiplicity = max(counts)
    multiplicity_histogram[maximum_multiplicity] = (
        multiplicity_histogram.get(maximum_multiplicity, 0) + 1
    )
    if metric_tour < direct:
        strict_metric_improvements += 1
        maximum_metric_improvement = max(maximum_metric_improvement, direct - metric_tour)
        candidate = (direct - metric_tour, values, direct, metric_tour, counts, order)
        if example is None or candidate > example:
            example = candidate
    cases += 1

assert cases == 3 ** len(ARCS)
assert strict_metric_improvements > 0
assert example is not None
assert repetitions_needed(3, 4, 7) == 4
assert 3 * 3 - 4 <= 7 < 4 * 3 - 4

print({
    "three_component_cost_matrices": cases,
    "cost_alphabet": (1, 2, 3),
    "exact_eulerian_equals_metric_tour": True,
    "strict_metric_closure_improvements": strict_metric_improvements,
    "maximum_metric_improvement": maximum_metric_improvement,
    "optimal_maximum_arc_multiplicity_histogram": multiplicity_histogram,
    "example_arc_costs": dict(zip(ARCS, example[1])),
    "example_direct_hamiltonian_cost": example[2],
    "example_metric_connector_cost": example[3],
    "example_connector_multiplicities": dict(
        (arc, count) for arc, count in zip(ARCS, example[4]) if count
    ),
    "repetition_formula": "floor((S+L*)/G)+1",
    "repetition_example": {
        "bundle_gain": 3,
        "connector_loss": 4,
        "setup": 7,
        "least_repetitions": 4,
    },
    "status": "passed",
})
