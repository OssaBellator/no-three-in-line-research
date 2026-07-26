#!/usr/bin/env python3
"""Finite checks for CMR854--CMR861."""

from itertools import combinations, permutations, product
import random


def matching(perm):
    return frozenset((source, perm[source]) for source in range(len(perm)))


def perfect_matchings(side, host):
    return [
        matching(perm)
        for perm in permutations(range(side))
        if matching(perm) <= host
    ]


def distinguishing_rank(family, chosen):
    alternatives = [state for state in family if state != chosen]
    edges = tuple(chosen)
    for size in range(len(edges) + 1):
        for subset in combinations(edges, size):
            witness = set(subset)
            if all(not witness.issubset(state) for state in alternatives):
                return size, frozenset(witness)
    raise AssertionError


def exchange_graph(side, host, chosen):
    source_of_target = {target: source for source, target in chosen}
    graph = {vertex: set() for vertex in range(side)}
    for source, target in host:
        owner = source_of_target[target]
        if owner != source:
            graph[source].add(owner)
    return graph


def strongly_connected_components(graph):
    seen = set()
    order = []

    def visit(vertex):
        if vertex in seen:
            return
        seen.add(vertex)
        for target in graph[vertex]:
            visit(target)
        order.append(vertex)

    for vertex in graph:
        visit(vertex)

    reverse = {vertex: set() for vertex in graph}
    for source in graph:
        for target in graph[source]:
            reverse[target].add(source)

    seen.clear()
    components = []

    def collect(vertex, component):
        if vertex in seen:
            return
        seen.add(vertex)
        component.add(vertex)
        for target in reverse[vertex]:
            collect(target, component)

    for vertex in reversed(order):
        if vertex not in seen:
            component = set()
            collect(vertex, component)
            components.append(frozenset(component))
    return components


def component_blocks(side, host, chosen, components):
    target_of = {source: target for source, target in chosen}
    blocks = []
    for component in components:
        sources = sorted(component)
        targets = {target_of[source] for source in component}
        edges = {
            (source, target)
            for source, target in host
            if source in component and target in targets
        }
        local_index = {source: index for index, source in enumerate(sources)}
        target_index = {
            target_of[source]: index for index, source in enumerate(sources)
        }
        local_host = {
            (local_index[source], target_index[target])
            for source, target in edges
        }
        local_chosen = frozenset(
            (local_index[source], target_index[target_of[source]])
            for source in sources
        )
        blocks.append((component, local_host, local_chosen))
    return blocks


def branch_union(family, subset):
    result = set()
    for edge in subset:
        result.update(state for state in family if edge not in state)
    return result


def check_host(side, host):
    family = perfect_matchings(side, host)
    checked = 0
    for chosen in family:
        graph = exchange_graph(side, host, chosen)
        components = strongly_connected_components(graph)
        component_of = {
            vertex: index
            for index, component in enumerate(components)
            for vertex in component
        }
        source_of_target = {target: source for source, target in chosen}
        usable = set(chosen)
        for source, target in host:
            owner = source_of_target[target]
            if component_of[source] == component_of[owner]:
                usable.add((source, target))

        union = set().union(*family) if family else set()
        assert usable == union
        assert set(perfect_matchings(side, usable)) == set(family)

        blocks = component_blocks(side, usable, chosen, components)
        local_families = []
        local_ranks = []
        local_witnesses = []
        product_count = 1
        for component, local_host, local_chosen in blocks:
            local_family = set(perfect_matchings(len(component), local_host))
            rank, witness = distinguishing_rank(local_family, local_chosen)
            local_families.append(local_family)
            local_ranks.append(rank)
            local_witnesses.append((component, witness))
            product_count *= len(local_family)
            if len(component) == 1:
                assert rank == 0
            else:
                assert rank >= 1
        assert product_count == len(family)

        global_rank, _ = distinguishing_rank(set(family), chosen)
        assert global_rank == sum(local_ranks)

        global_witness = set()
        for component, witness in local_witnesses:
            sources = sorted(component)
            for local_source, _local_target in witness:
                source = sources[local_source]
                global_witness.add(next(edge for edge in chosen if edge[0] == source))
        assert len(global_witness) == global_rank
        assert branch_union(set(family), global_witness) == set(family) - {chosen}
        checked += 1
    return checked


def check_all():
    checked = 0
    for side in range(1, 4):
        edges = [
            (source, target)
            for source in range(side)
            for target in range(side)
        ]
        for mask in range(1 << len(edges)):
            host = {
                edge
                for index, edge in enumerate(edges)
                if mask & (1 << index)
            }
            checked += check_host(side, host)

    rng = random.Random(854)
    side = 4
    edges = [
        (source, target)
        for source in range(side)
        for target in range(side)
    ]
    for _ in range(3000):
        density = rng.uniform(0.2, 0.95)
        host = {edge for edge in edges if rng.random() < density}
        checked += check_host(side, host)
    return checked


def main():
    print(
        "verified generic exchange SCC width:",
        check_all(),
        "matching-owner cases",
    )


if __name__ == "__main__":
    main()
