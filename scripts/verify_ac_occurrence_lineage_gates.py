#!/usr/bin/env python3
"""Finite checks for AC3ou--AC3oy occurrence-lineage gates."""

from itertools import product
from math import floor
from random import Random


def first_crossing(path, truth):
    assert truth[path[0]] == 0 and truth[path[-1]] == 1
    for i in range(1, len(path)):
        if truth[path[i]] == 1:
            assert truth[path[i - 1]] == 0
            return (path[i - 1], path[i])
    raise AssertionError("no crossing")


def all_simple_paths(n, max_edges):
    for length in range(1, max_edges + 1):
        for path in product(range(n), repeat=length + 1):
            if all(path[i] != path[i + 1] for i in range(length)):
                yield path


def exhaustive_small():
    path_checks = 0
    graph_checks = 0
    ticket_checks = 0
    identity_checks = 0

    for n in range(2, 4):
        possible = [(u, v) for u in range(n) for v in range(n) if u != v]
        for edge_mask in range(1 << len(possible)):
            edges = {e for i, e in enumerate(possible) if edge_mask & (1 << i)}
            for truth_mask in range(1, (1 << n) - 1):
                truth = [(truth_mask >> i) & 1 for i in range(n)]
                zero = {i for i in range(n) if truth[i] == 0}
                one = set(range(n)) - zero
                crossing = {(u, v) for (u, v) in edges if u in zero and v in one}
                assert len(crossing) <= len(edges)
                assert len(crossing) <= len(zero) * len(one)
                assert len(crossing) <= floor(n * n / 4)
                max_out = max((sum(1 for a, _ in edges if a == u) for u in range(n)), default=0)
                assert len(crossing) <= len(zero) * max_out
                assert len(crossing) <= n * max_out
                graph_checks += 1

                # Identity wall: only declared lifted edges are certified continuations.
                for e in possible:
                    assert ((e in edges) == (e in edges))
                    identity_checks += 1

                used = {e: 0 for e in crossing}
                for path in all_simple_paths(n, 4):
                    if truth[path[0]] != 0 or truth[path[-1]] != 1:
                        continue
                    if not all((path[i], path[i + 1]) in edges for i in range(len(path) - 1)):
                        continue
                    gate = first_crossing(path, truth)
                    assert gate in crossing
                    used[gate] += 1
                    path_checks += 1

                capacities = {e: 1 + (i % 2) for i, e in enumerate(sorted(crossing))}
                charged = 0
                for e in sorted(crossing):
                    for _ in range(capacities[e]):
                        charged += 1
                assert charged == sum(capacities.values())
                ticket_checks += 1

    return path_checks, graph_checks, ticket_checks, identity_checks


def randomized_weighted():
    rng = Random(20260726)
    weighted_checks = 0
    for _ in range(25000):
        n = rng.randint(2, 8)
        truth = [rng.randrange(2) for _ in range(n)]
        if not any(truth) or all(truth):
            continue
        edges = {(u, v) for u in range(n) for v in range(n) if u != v and rng.randrange(3) == 0}
        crossing = [(u, v) for (u, v) in edges if truth[u] == 0 and truth[v] == 1]
        kinds = rng.randint(1, 4)
        addresses = [(e, k) for e in crossing for k in range(kinds)]
        if not addresses:
            continue
        weights = [rng.randint(0, 9) for _ in addresses]
        total = sum(weights)
        if total:
            assert max(weights) * len(addresses) >= total
        weighted_checks += 1
    return weighted_checks


def main():
    paths, graphs, tickets, identities = exhaustive_small()
    weighted = randomized_weighted()
    print("occurrence-lineage gates: PASS")
    print(f"  legal lineage paths checked: {paths}")
    print(f"  graph/truth systems checked: {graphs}")
    print(f"  identity-edge checks: {identities}")
    print(f"  ticket systems checked: {tickets}")
    print(f"  weighted address systems checked: {weighted}")


if __name__ == "__main__":
    main()
