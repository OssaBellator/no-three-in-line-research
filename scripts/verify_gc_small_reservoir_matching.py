#!/usr/bin/env python3
"""Finite audit for GC2ge--GC2gi."""

from itertools import combinations, permutations


def maximum_matching(adj, n_left, n_right):
    best = ()
    for r in range(1, min(n_left, n_right) + 1):
        for lefts in combinations(range(n_left), r):
            for rights in permutations(range(n_right), r):
                pairs = tuple(zip(lefts, rights))
                if all(v in adj[u] for u, v in pairs):
                    if len(pairs) > len(best) or (len(pairs) == len(best) and pairs < best):
                        best = pairs
    return best


def least_hall_core(adj, n_left):
    vertices = range(n_left)
    bad = []
    for r in range(1, n_left + 1):
        for X in combinations(vertices, r):
            N = set().union(*(adj[u] for u in X))
            if len(N) < len(X):
                bad.append((len(X), X, tuple(sorted(N))))
    return min(bad) if bad else None


def main():
    graphs = 0
    successful = 0
    failed = 0
    tickets = set()
    for n_left in range(1, 5):
        for n_right in range(1, 5):
            all_edges = [(u, v) for u in range(n_left) for v in range(n_right)]
            # Exhaust all graphs up to 3x3, sample structured masks for larger.
            masks = range(1 << len(all_edges)) if len(all_edges) <= 9 else range(0, 1 << len(all_edges), 257)
            for mask in masks:
                adj = [set() for _ in range(n_left)]
                for i, (u, v) in enumerate(all_edges):
                    if mask >> i & 1:
                        adj[u].add(v)
                M = maximum_matching(adj, n_left, n_right)
                core = least_hall_core(adj, n_left)
                graphs += 1
                if len(M) == n_left:
                    successful += 1
                    assert core is None
                    for edge in M:
                        tickets.add((n_left, n_right, edge))
                else:
                    failed += 1
                    assert core is not None
                    _, X, N = core
                    assert len(N) < len(X)
    print("GC small-reservoir matching audit passed")
    print(f"  graphs checked: {graphs}")
    print(f"  full assignments: {successful}")
    print(f"  Hall failures: {failed}")
    print(f"  ticket address samples: {len(tickets)}")


if __name__ == "__main__":
    main()
