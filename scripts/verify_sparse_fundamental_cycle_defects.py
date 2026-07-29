#!/usr/bin/env python3
"""Finite checks for SAS5ib--SAS5if."""

from collections import deque
from itertools import combinations, product


def spanning_forest(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    parent = [-1] * n
    roots = []
    tree_edges = set()
    order = []
    for root in range(n):
        if parent[root] != -1:
            continue
        roots.append(root)
        parent[root] = root
        q = deque([root])
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    tree_edges.add((min(u, v), max(u, v)))
                    q.append(v)
    return parent, roots, tree_edges, order


def oriented(charge, u, v):
    e = (min(u, v), max(u, v))
    return charge[e] if u < v else -charge[e]


def main() -> None:
    checks = 0
    for n in range(1, 7):
        pairs = list(combinations(range(n), 2))
        masks = range(1 << len(pairs)) if n <= 5 else [0, 1, 3, 0x1555, 0x2AAA, (1 << len(pairs)) - 1]
        for mask in masks:
            edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
            parent, roots, tree_edges, order = spanning_forest(n, edges)
            kappa = len(roots)
            non_tree = [e for e in edges if e not in tree_edges]
            assert len(non_tree) == len(edges) - n + kappa

            patterns = []
            # Coboundary charges from deterministic potentials.
            for phi in ([i for i in range(n)], [((3 * i + 1) % 7) for i in range(n)]):
                patterns.append({(a, b): phi[b] - phi[a] for a, b in edges})
            # General antisymmetric charge patterns.
            patterns.append({e: ((e[0] + 2 * e[1]) % 5) - 2 for e in edges})
            patterns.append({e: ((3 * e[0] + e[1] + 1) % 7) - 3 for e in edges})

            for charge in patterns:
                psi = [0] * n
                root_set = set(roots)
                for v in order:
                    if v in root_set:
                        psi[v] = 0
                    else:
                        p = parent[v]
                        psi[v] = psi[p] + oriented(charge, p, v)
                for a, b in tree_edges:
                    assert oriented(charge, a, b) == psi[b] - psi[a]

                defects = {}
                for a, b in non_tree:
                    defects[(a, b)] = psi[a] + oriented(charge, a, b) - psi[b]
                all_zero = all(v == 0 for v in defects.values())
                edge_potential = all(oriented(charge, a, b) == psi[b] - psi[a] for a, b in edges)
                assert all_zero == edge_potential
                D = sum(abs(v) for v in defects.values())
                if D:
                    assert max(abs(v) for v in defects.values()) * len(defects) >= D
                checks += 1
    print(f"verified {checks} state-graph charge systems")


if __name__ == "__main__":
    main()
