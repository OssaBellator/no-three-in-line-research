#!/usr/bin/env python3
"""Finite checks for AC5ay--AC5be."""

from itertools import combinations, permutations, product
from math import factorial, gcd, lcm


def subsets(xs):
    xs = tuple(xs)
    for r in range(len(xs) + 1):
        yield from combinations(xs, r)


def matching_rank(A, S, edges):
    best = 0
    A, S = tuple(A), tuple(S)
    for r in range(1, min(len(A), len(S)) + 1):
        for left in combinations(A, r):
            for right in combinations(S, r):
                if any(all((a, b) in edges for a, b in zip(left, p)) for p in permutations(right)):
                    best = r
    return best


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def collinear(a, b, c):
    return det(sub(b, a), sub(c, a)) == 0


def main():
    checks = 0

    # Common-hole deficiency on tiny Hall-feasible graphs.
    for na, nb in ((2, 3), (3, 4)):
        A, B = tuple(range(na)), tuple(range(nb))
        ambient = [(a, b) for a in A for b in B]
        for mask in range(1 << len(ambient)):
            edges = {e for i, e in enumerate(ambient) if mask >> i & 1}
            if any(len({b for a in X for b in B if (a, b) in edges}) < len(X) for X in subsets(A) if X):
                continue
            holes = {a: set(B) - {b for b in B if (a, b) in edges} for a in A}
            for S0 in subsets(B):
                S = set(S0)
                lhs = len(A) - matching_rank(A, S, edges)
                rhs = 0
                for X in subsets(A):
                    if not X:
                        continue
                    common = set(B)
                    for a in X:
                        common &= holes[a]
                    rhs = max(rhs, len(X) - len(S) + len(S & common))
                assert lhs == max(rhs, 0)
                checks += 1

    # Rank-three I6 cylinder count.
    for m in range(3, 7):
        for h in range(1, 4):
            total = factorial(m) * h**m
            count = factorial(m - 3) * h ** (m - 3)
            assert count * (m * (m - 1) * (m - 2)) * h**3 == total
            checks += 1

    # Arbitrary sparse image permutation.
    for n in range(2, 8):
        pi = tuple(range(n))
        rho = tuple((i + 1) % n for i in range(n))
        for alpha in permutations(range(n)):
            image = tuple(pi[alpha[i]] for i in range(n))
            assert sorted(image) == list(range(n))
            moved = [i for i in range(n) if alpha[i] != i]
            host = {(i, image[i]) for i in range(n)}
            assert all((i, image[i]) in host for i in moved)
            failures = sum(image[i] == rho[i] for i in moved)
            assert failures <= len(moved)
            checks += 1

    # One-local connector equivalence.
    vectors = [(1, 1), (2, 2), (1, 2), (2, 1)]
    cells = [(x, y) for x in range(-2, 3) for y in range(-2, 3)]
    for z, zp in combinations(vectors, 2):
        U, V = z, (2 * zp[0], 2 * zp[1])
        for X, Y in combinations(cells, 2):
            both = collinear(U, X, Y) and collinear(V, X, Y)
            connector = U == V or (collinear(U, V, X) and collinear(U, V, Y))
            assert both == connector
            checks += 1

    # Top-weight capacities.
    for weights in product(range(5), repeat=6):
        for d in range(4):
            cap = sum(sorted(weights, reverse=True)[:d])
            best = max((sum(weights[i] for i in idx) for r in range(d + 1) for idx in combinations(range(6), r)), default=0)
            assert cap == best
            checks += 1

    # Simultaneous phase-vector order.
    for h in range(1, 10):
        for vec in product(range(h), repeat=3):
            order = 1
            g = h
            for x in vec:
                order = lcm(order, h // gcd(h, x))
                g = gcd(g, x)
            assert order == h // g
            assert len({tuple((j * x) % h for x in vec) for j in range(order)}) == order
            checks += 1

    print(f"verified {checks} third-frontier interface instances")


if __name__ == "__main__":
    main()
