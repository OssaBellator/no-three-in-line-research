#!/usr/bin/env python3
"""Finite checks for CMR846--CMR853."""

from itertools import combinations, permutations, product
import random


def distinguishing_rank(family, chosen):
    chosen = tuple(chosen)
    alternatives = [state for state in family if state != frozenset(chosen)]
    for size in range(len(chosen) + 1):
        for subset in combinations(chosen, size):
            witness = set(subset)
            if all(not witness.issubset(state) for state in alternatives):
                return size, frozenset(witness)
    raise AssertionError("full chosen state must distinguish itself")


def branch_union(family, subset):
    result = set()
    for edge in subset:
        result.update(state for state in family if edge not in state)
    return result


def check_set_family_covers():
    rng = random.Random(846)
    checked = 0
    for universe_size in range(1, 16):
        universe = range(universe_size)
        for state_size in range(universe_size + 1):
            states = [frozenset(state) for state in combinations(universe, state_size)]
            for _ in range(min(200, max(1, len(states) * 2))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                chosen = rng.choice(tuple(family))
                rank, witness = distinguishing_rank(family, chosen)
                assert len(witness) == rank
                assert branch_union(family, witness) == family - {chosen}
                for size in range(rank):
                    for subset in combinations(chosen, size):
                        assert branch_union(family, subset) != family - {chosen}
                for size in range(rank):
                    for subset in combinations(chosen, size):
                        assert any(set(subset).issubset(state) for state in family - {chosen})
                checked += 1
    return checked


def cartesian_family(families):
    result = set()
    for states in product(*families):
        merged = frozenset().union(*states)
        result.add(merged)
    return result


def check_product_additivity():
    rng = random.Random(849)
    checked = 0
    for factor_count in range(1, 5):
        for _ in range(1000):
            factors = []
            chosen_parts = []
            offset = 0
            expected = 0
            for _factor in range(factor_count):
                universe_size = rng.randint(1, 6)
                state_size = rng.randint(0, universe_size)
                local_states = [
                    frozenset(offset + edge for edge in state)
                    for state in combinations(range(universe_size), state_size)
                ]
                local_family = set(
                    rng.sample(local_states, rng.randint(1, len(local_states)))
                )
                chosen = rng.choice(tuple(local_family))
                rank, _ = distinguishing_rank(local_family, chosen)
                expected += rank
                factors.append(local_family)
                chosen_parts.append(chosen)
                offset += universe_size
            family = cartesian_family(factors)
            chosen = frozenset().union(*chosen_parts)
            rank, _ = distinguishing_rank(family, chosen)
            assert rank == expected
            checked += 1
    return checked


def matching(perm):
    return frozenset((source, perm[source]) for source in range(len(perm)))


def perfect_matchings(side, host):
    return [matching(perm) for perm in permutations(range(side)) if matching(perm) <= host]


def exchange_graph(side, host, chosen):
    target_of = {source: target for source, target in chosen}
    source_of_target = {target: source for source, target in chosen}
    graph = {vertex: set() for vertex in range(side)}
    for source, target in host:
        owner = source_of_target[target]
        if owner != source:
            graph[source].add(owner)
    return graph


def acyclic_after_removal(graph, removed):
    active = set(graph) - set(removed)
    indegree = {vertex: 0 for vertex in active}
    for source in active:
        for target in graph[source]:
            if target in active:
                indegree[target] += 1
    stack = [vertex for vertex, degree in indegree.items() if degree == 0]
    seen = 0
    while stack:
        source = stack.pop()
        seen += 1
        for target in graph[source]:
            if target in indegree:
                indegree[target] -= 1
                if indegree[target] == 0:
                    stack.append(target)
    return seen == len(active)


def feedback_vertex_number(graph):
    vertices = tuple(graph)
    for size in range(len(vertices) + 1):
        for removed in combinations(vertices, size):
            if acyclic_after_removal(graph, removed):
                return size
    raise AssertionError


def vertex_on_cycle(graph, start):
    frontier = list(graph[start])
    seen = set()
    while frontier:
        vertex = frontier.pop()
        if vertex == start:
            return True
        if vertex in seen:
            continue
        seen.add(vertex)
        frontier.extend(graph[vertex])
    return False


def check_host(side, host):
    family = perfect_matchings(side, host)
    checked = 0
    for chosen in family:
        rank, _ = distinguishing_rank(set(family), chosen)
        graph = exchange_graph(side, host, chosen)
        assert rank == feedback_vertex_number(graph)
        for source, edge in enumerate(sorted(chosen)):
            essential = all(edge in alternative for alternative in family)
            assert essential == (not vertex_on_cycle(graph, source))
        checked += 1
    return checked


def check_exchange_hosts():
    checked = 0
    for side in range(1, 4):
        edges = [(source, target) for source in range(side) for target in range(side)]
        for mask in range(1 << len(edges)):
            host = {edge for index, edge in enumerate(edges) if mask & (1 << index)}
            checked += check_host(side, host)

    rng = random.Random(851)
    side = 4
    edges = [(source, target) for source in range(side) for target in range(side)]
    for _ in range(4000):
        host = {edge for edge in edges if rng.random() < rng.uniform(0.25, 0.9)}
        checked += check_host(side, host)
    return checked


def main():
    print(
        "verified distinguishing rank and exchange graph:",
        check_set_family_covers(),
        "set-family cases,",
        check_product_additivity(),
        "product cases, and",
        check_exchange_hosts(),
        "matching-host cases",
    )


if __name__ == "__main__":
    main()
