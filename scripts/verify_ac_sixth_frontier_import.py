#!/usr/bin/env python3
"""Finite checks for AC5bt--AC5bz."""

from collections import deque
from itertools import combinations, product


def independent(mask, edges, n):
    verts = [i for i in range(n) if mask >> i & 1]
    return all((min(a, b), max(a, b)) not in edges for a, b in combinations(verts, 2))


def maximal(mask, edges, n):
    return independent(mask, edges, n) and all(
        not independent(mask | (1 << v), edges, n) for v in range(n) if not (mask >> v & 1)
    )


def neighborhood(v, edges):
    out = {v}
    for a, b in edges:
        if a == v:
            out.add(b)
        elif b == v:
            out.add(a)
    return out


def greedy_matching(edges, weights):
    chosen = []
    used = set()
    for a, b in sorted(edges, key=lambda e: (-weights[e], e)):
        if weights[(a, b)] > 0 and a not in used and b not in used:
            chosen.append((a, b))
            used.update((a, b))
    return chosen


def spanning_forest(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    parent = [-1] * n
    tree = set()
    roots = []
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
                    tree.add((min(u, v), max(u, v)))
                    q.append(v)
    return parent, roots, tree, order


def oriented(charge, u, v):
    e = (min(u, v), max(u, v))
    return charge[e] if u < v else -charge[e]


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def psub(a, b, p):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p for i in range(n)])


def pmul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def degree(a):
    return -1 if a == (0,) else len(a) - 1


def main() -> None:
    checks = 0

    # RI conflict neighborhoods and BDA line matchings.
    for n in range(2, 7):
        pairs = list(combinations(range(n), 2))
        masks = range(1 << len(pairs)) if n <= 5 else [0, 1, 3, 0x1555, 0x2AAA, (1 << len(pairs)) - 1]
        for mask in masks:
            edges = {pairs[i] for i in range(len(pairs)) if mask >> i & 1}
            inds = [m for m in range(1 << n) if independent(m, edges, n)]
            alpha = max(m.bit_count() for m in inds)
            Isets = [m for m in inds if maximal(m, edges, n)]
            weights = [i + 1 for i in range(n)]
            W = sum(weights)
            for imask in Isets:
                I = [v for v in range(n) if imask >> v & 1]
                assert set().union(*(neighborhood(v, edges) for v in I)) == set(range(n))
                assert max(sum(weights[u] for u in neighborhood(v, edges)) for v in I) * alpha >= W

            eweights = {e: ((e[0] + 2 * e[1]) % 5) + 1 for e in edges}
            if edges:
                degs = [sum(v in e for e in edges) for v in range(n)]
                d = max(degs)
                M = greedy_matching(list(edges), eweights)
                assert sum(eweights[e] for e in M) * (2 * d - 1) >= sum(eweights.values())
            checks += 1

    # Weighted endpoint stars.
    for na in range(1, 5):
        A = range(na)
        for nb in range(1, 6):
            B = range(nb)
            holes = {a: {b for b in B if (2 * a + b) % 3 == 0} for a in A}
            weights = {b: (b % 4) + 1 for b in B}
            mult = {b: sum(b in holes[a] for a in A) for b in B}
            HM = sum(mult[b] * weights[b] for b in B)
            stars = [sum(weights[b] for b in holes[a]) for a in A]
            assert max(stars) * na >= HM
            for tau in range(na + 1):
                exc = sum(weights[b] for b in B if mult[b] > tau)
                assert exc * (tau + 1) <= HM
                checks += 1

    # Fundamental cycle criterion.
    for n in range(2, 7):
        edges = list(combinations(range(n), 2))
        parent, roots, tree, order = spanning_forest(n, edges)
        charge = {e: ((3 * e[0] + e[1]) % 7) - 3 for e in edges}
        psi = [0] * n
        for v in order:
            if parent[v] != v:
                psi[v] = psi[parent[v]] + oriented(charge, parent[v], v)
        defects = [psi[a] + oriented(charge, a, b) - psi[b] for a, b in edges if (a, b) not in tree]
        all_zero = all(x == 0 for x in defects)
        assert all_zero == all(oriented(charge, a, b) == psi[b] - psi[a] for a, b in edges)
        checks += 1

    # Factorized decorations.
    for sizes in product(range(1, 5), repeat=3):
        states = list(product(*(range(k) for k in sizes)))
        assert len(states) == sizes[0] * sizes[1] * sizes[2]
        reconstructed = [x for x in states if x[2] == (x[0] + x[1]) % sizes[2]]
        assert len({(x[0], x[1]) for x in reconstructed}) == len(reconstructed)
        checks += 1

    # Polynomial determinant degree.
    for p in (2, 3, 5, 7):
        for d in range(4):
            for seed in range(2000):
                polys = []
                for i in range(6):
                    polys.append(trim([((seed + 3 * i + 5 * k) % p) for k in range(d + 1)]))
                a0, a1 = psub(polys[2], polys[0], p), psub(polys[3], polys[1], p)
                b0, b1 = psub(polys[4], polys[0], p), psub(polys[5], polys[1], p)
                det = psub(pmul(a0, b1, p), pmul(a1, b0, p), p)
                pa = max(degree(a0), degree(a1), 0)
                qb = max(degree(b0), degree(b1), 0)
                assert degree(det) <= pa + qb <= 2 * d
                checks += 1

    print(f"verified {checks} combined sixth-frontier instances")


if __name__ == "__main__":
    main()
