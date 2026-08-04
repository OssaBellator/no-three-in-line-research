#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

NEG = -10**9
LEFT = (0, 1)
RIGHT = (2, 3)
INTERNAL = (4,)
N = 5
PAIRS = tuple(combinations(range(N), 2))
STATES = range(1 << len(RIGHT))


def independent(mask, edges):
    return all(not ((mask >> u) & 1 and (mask >> v) & 1) for u, v in edges)


def packet_tables(edges):
    w = [[NEG for _ in STATES] for _ in STATES]
    alpha = 0
    for mask in range(1 << N):
        if not independent(mask, edges):
            continue
        alpha = max(alpha, mask.bit_count())
        left_state = sum(((mask >> v) & 1) << i for i, v in enumerate(LEFT))
        right_state = sum(((mask >> v) & 1) << i for i, v in enumerate(RIGHT))
        w[left_state][right_state] = max(w[left_state][right_state], mask.bit_count())
    transition = [[NEG for _ in STATES] for _ in STATES]
    for previous_right in STATES:
        for right_state in STATES:
            transition[previous_right][right_state] = max(
                w[left_state][right_state]
                for left_state in STATES
                if not (previous_right & left_state)
            )
    initial = [max(w[left_state][right_state] for left_state in STATES) for right_state in STATES]
    return alpha, w, transition, initial


def transfer_alpha(transition, initial, copies):
    assert copies >= 1
    dp = initial[:]
    for _ in range(1, copies):
        dp = [
            max(dp[previous] + transition[previous][current] for previous in STATES)
            for current in STATES
        ]
    return max(dp)


def chain_edges(packet_edges, copies):
    edges = set()
    for block in range(copies):
        shift = block * N
        edges.update((shift + u, shift + v) for u, v in packet_edges)
    for block in range(copies - 1):
        first = block * N
        second = (block + 1) * N
        for i in range(2):
            edges.add((first + RIGHT[i], second + LEFT[i]))
    return tuple(sorted(tuple(sorted(edge)) for edge in edges))


def exact_alpha(vertex_count, edges):
    adjacency = [0] * vertex_count
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    best = 0

    def search(candidates, chosen):
        nonlocal best
        if chosen + candidates.bit_count() <= best:
            return
        if not candidates:
            best = max(best, chosen)
            return
        vertices = [i for i in range(vertex_count) if (candidates >> i) & 1]
        vertex = max(vertices, key=lambda i: (adjacency[i] & candidates).bit_count())
        search(candidates & ~(1 << vertex) & ~adjacency[vertex], chosen + 1)
        search(candidates & ~(1 << vertex), chosen)

    search((1 << vertex_count) - 1, 0)
    return best


def maximum_cycle_mean(matrix):
    best = None

    def visit(start, current, seen, weight):
        nonlocal best
        for nxt in STATES:
            edge_weight = matrix[current][nxt]
            if edge_weight <= NEG // 2:
                continue
            if nxt == start:
                mean = Fraction(weight + edge_weight, len(seen))
                best = mean if best is None else max(best, mean)
            elif nxt not in seen:
                visit(start, nxt, seen | {nxt}, weight + edge_weight)

    for start in STATES:
        visit(start, start, {start}, 0)
    assert best is not None
    return best


cases = 0
strict_improvements = 0
maximum_improvement = 0
cycle_means = {}
threshold_examples = []
for edge_mask in range(1 << len(PAIRS)):
    packet_edges = tuple(PAIRS[i] for i in range(len(PAIRS)) if (edge_mask >> i) & 1)
    alpha, _, transition, initial = packet_tables(packet_edges)
    mean = maximum_cycle_mean(transition)
    cycle_means[str(mean)] = cycle_means.get(str(mean), 0) + 1
    for copies in range(1, 5):
        via_transfer = transfer_alpha(transition, initial, copies)
        direct = exact_alpha(N * copies, chain_edges(packet_edges, copies))
        assert via_transfer == direct
        additive = copies * alpha - 2 * (copies - 1)
        assert direct >= additive
        if direct > additive:
            strict_improvements += 1
        maximum_improvement = max(maximum_improvement, direct - additive)
        cases += 1
    exact_k = next((k for k in range(1, 20) if transfer_alpha(transition, initial, k) >= 28), None)
    additive_k = next((k for k in range(1, 20) if k * alpha - 2 * (k - 1) >= 28), None)
    if exact_k is not None and (additive_k is None or exact_k < additive_k):
        threshold_examples.append((packet_edges, alpha, mean, exact_k, additive_k))

assert cases == 4096
assert strict_improvements > 0
assert threshold_examples
example = min(threshold_examples, key=lambda item: (item[3], len(item[0]), item[0]))

print({
    "packet_graphs": 1 << len(PAIRS),
    "direct_chain_checks": cases,
    "copies_checked_directly": (1, 2, 3, 4),
    "boundary_states": len(tuple(STATES)),
    "strict_improvements_over_edge_charging": strict_improvements,
    "maximum_improvement_at_four_copies": maximum_improvement,
    "cycle_mean_values": cycle_means,
    "example_packet_edges": example[0],
    "example_packet_alpha": example[1],
    "example_cycle_mean": str(example[2]),
    "example_exact_packets_for_28": example[3],
    "example_additive_packets_for_28": example[4],
    "status": "passed",
})
