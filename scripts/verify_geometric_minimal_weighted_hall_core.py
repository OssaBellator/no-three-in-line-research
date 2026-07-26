#!/usr/bin/env python3
"""Finite checks for GC2al--GC2ap."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from random import Random


def subsets(items: tuple[int, ...]):
    for size in range(1, len(items) + 1):
        yield from combinations(items, size)


def deficiency(subset, demands, eligible, capacities):
    demand = sum((demands[j] for j in subset), Fraction(0))
    neighbourhood = set().union(*(eligible[j] for j in subset))
    capacity = sum((capacities[p] for p in neighbourhood), Fraction(0))
    return demand - capacity


def canonical_core(demands, eligible, capacities):
    events = tuple(range(len(demands)))
    deficient = [subset for subset in subsets(events) if deficiency(subset, demands, eligible, capacities) > 0]
    if not deficient:
        return None
    minimal = []
    for subset in deficient:
        s = set(subset)
        if not any(set(other) < s for other in deficient):
            minimal.append(subset)
    minimum_size = min(len(subset) for subset in minimal)
    return min(subset for subset in minimal if len(subset) == minimum_size)


def max_weight_independent(vertices, edges, weights):
    vertices = list(vertices)
    edge_set = {frozenset(edge) for edge in edges}
    best = Fraction(0)
    for mask in range(1 << len(vertices)):
        chosen = [vertices[i] for i in range(len(vertices)) if mask & (1 << i)]
        if any(frozenset((u, v)) in edge_set for u, v in combinations(chosen, 2)):
            continue
        best = max(best, sum((weights[v] for v in chosen), Fraction(0)))
    return best


def core_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(45000):
        event_count = rng.randint(1, 7)
        resource_count = rng.randint(1, 7)
        demands = [Fraction(rng.randint(1, 12), rng.randint(1, 4)) for _ in range(event_count)]
        capacities = [Fraction(rng.randint(0, 12), rng.randint(1, 4)) for _ in range(resource_count)]
        eligible = []
        for _event in range(event_count):
            neighbours = {p for p in range(resource_count) if rng.randrange(3) != 0}
            if not neighbours:
                neighbours.add(rng.randrange(resource_count))
            eligible.append(neighbours)

        core = canonical_core(demands, eligible, capacities)
        if core is None:
            counts["Hall-feasible systems"] += 1
            continue
        counts["deficient systems"] += 1
        x = set(core)
        delta = deficiency(core, demands, eligible, capacities)
        assert delta > 0
        for size in range(1, len(core)):
            for proper in combinations(core, size):
                assert deficiency(proper, demands, eligible, capacities) <= 0

        neighbourhood = set().union(*(eligible[j] for j in core))
        private = {}
        private_union = set()
        for j in core:
            without = x - {j}
            n_without = set().union(*(eligible[k] for k in without)) if without else set()
            private[j] = neighbourhood - n_without
            assert private_union.isdisjoint(private[j])
            private_union |= private[j]
        shared = neighbourhood - private_union
        uncovered = {}
        for j in core:
            uncovered[j] = demands[j] - sum((capacities[p] for p in private[j]), Fraction(0))
            assert uncovered[j] >= delta
        total_u = sum(uncovered.values(), Fraction(0))
        shared_capacity = sum((capacities[p] for p in shared), Fraction(0))
        assert total_u == shared_capacity + delta
        assert shared_capacity >= (len(core) - 1) * delta
        assert total_u >= len(core) * delta

        if len(core) == 1:
            counts["singleton deficient cores"] += 1
            continue

        shared_neighbours = {j: eligible[j] & shared for j in core}
        assert all(shared_neighbours[j] for j in core)
        incidence = defaultdict(Fraction)
        for j in core:
            share = uncovered[j] / len(shared_neighbours[j])
            for p in shared_neighbours[j]:
                incidence[(j, p)] = share
            assert sum((incidence[(j, p)] for p in shared_neighbours[j]), Fraction(0)) == uncovered[j]
        assert sum(incidence.values(), Fraction(0)) == total_u

        resource_weight = {
            p: sum((incidence[(j, p)] for j in core if (j, p) in incidence), Fraction(0))
            for p in shared
        }
        p_star = max(resource_weight, key=resource_weight.get)
        assert resource_weight[p_star] * len(shared) >= total_u

        role_count = rng.randint(1, 4)
        roles = {j: rng.randrange(role_count) for j in core if (j, p_star) in incidence}
        role_weights = defaultdict(Fraction)
        for j, role in roles.items():
            role_weights[role] += incidence[(j, p_star)]
        role_star = max(role_weights, key=role_weights.get)
        fibre = [j for j in roles if roles[j] == role_star]
        fibre_weight = role_weights[role_star]
        assert fibre_weight * role_count >= resource_weight[p_star]

        edges = set()
        for u, v in combinations(fibre, 2):
            if rng.randrange(3) == 0:
                edges.add((u, v))
        degree = {j: 0 for j in fibre}
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        gamma = rng.randint(0, max(0, len(fibre) - 1))
        if degree and max(degree.values()) > gamma:
            counts["same-resource conflict overloads"] += 1
        else:
            weights = {j: incidence[(j, p_star)] for j in fibre}
            best = max_weight_independent(fibre, edges, weights)
            assert best * (gamma + 1) >= fibre_weight
            assert best * len(shared) * role_count * (gamma + 1) >= total_u
            counts["compatible deficiency fans"] += 1
        counts["minimal core decompositions"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    core_checks(counts)
    print("GC2al--GC2ap minimal weighted Hall-core audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
