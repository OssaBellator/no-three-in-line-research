#!/usr/bin/env python3
"""Finite checks for AC5bf--AC5bl."""

from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial


def det(x, y):
    return x[0] * y[1] - x[1] * y[0]


def subsets(items):
    items = list(items)
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            yield set(c)


def exact_deficiency(A, S, holes):
    best = 0
    for X in subsets(A):
        if not X:
            continue
        common = set(S)
        for a in X:
            common &= holes[a]
        best = max(best, len(X) - len(S) + len(common))
    return max(best, 0)


def hole_bound(A, S, holes):
    mult = {b: sum(b in holes[a] for a in A) for b in S}
    mu = max(mult.values(), default=0)
    mass = sum(mult.values())
    vals = [max(len(A) - len(S), 0)]
    for x in range(1, min(len(A), mu) + 1):
        vals.append(max(x - len(S) + mass // x, 0))
    return max(vals)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def transposition(n, a, b):
    t = list(range(n))
    t[a], t[b] = t[b], t[a]
    return tuple(t)


def cycle_list(alpha):
    seen, out = set(), []
    for i in range(len(alpha)):
        if i in seen or alpha[i] == i:
            continue
        cyc, x = [], i
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = alpha[x]
        out.append(cyc)
    return out


def poly_eval(coeffs, x, p):
    total, power = 0, 1
    for c in coeffs:
        total = (total + c * power) % p
        power = (power * x) % p
    return total


def main():
    checks = 0

    # Hole-multiplicity interface.
    for na in range(1, 5):
        A = tuple(range(na))
        for nb in range(1, 5):
            B = tuple(range(nb))
            edges = [(a, b) for a in A for b in B]
            for chosen in combinations(edges, min(3, len(edges))):
                holes = {a: set() for a in A}
                for a, b in chosen:
                    holes[a].add(b)
                for S in subsets(B):
                    assert exact_deficiency(A, S, holes) <= hole_bound(A, S, holes)
                    checks += 1

    # Physical RI product-bank count.
    for m in range(1, 6):
        for h in range(1, 4):
            count = sum(1 for _ in permutations(range(m)) for _ in product(range(h), repeat=m))
            assert count == factorial(m) * h**m
            checks += 1

    # Mixed BDA identities.
    for a, b, h, q, u, v in product(range(1, 4), repeat=6):
        H = h + q
        d = (a, b)
        zA, zB = (h*a, h*b), (H*a, H*b)
        zC, zD = (h*a, H*b), (H*a, h*b)
        diff = (zC[0]-zD[0], zC[1]-zD[1])
        base = det(zC, zD)
        assert (v * det(diff, zA) == u * base) == (2*h*v == u*(2*h+q))
        assert (v * det(diff, zB) == u * base) == (2*H*v == u*(2*h+q))
        assert det(d, zC) != 0 and det(d, zD) != 0
        t = Fraction(u*(2*h+q), 2)
        assert det(diff, (t*a, t*b)) == u*base
        checks += 1

    # Canonical sparse permutation compression.
    for n in range(1, 8):
        ident = tuple(range(n))
        for alpha in permutations(range(n)):
            cur = ident
            length = 0
            cs = cycle_list(alpha)
            for cyc in cs:
                for j in range(1, len(cyc)):
                    cur = compose(transposition(n, cyc[0], cyc[j]), cur)
                    length += 1
            assert cur == alpha
            r = sum(len(c) for c in cs)
            assert length == r - len(cs)
            checks += 1

    # Phase coboundary cancellation.
    for R in range(1, 7):
        for P in product(range(3), repeat=R):
            D = tuple((2*j + R) % 3 for j in range(R))
            phi = tuple((j*j + 1) % 5 for j in range(R))
            G = tuple(P[j]-D[j]+phi[j]-phi[(j+1)%R] for j in range(R))
            assert sum(G) == sum(P)-sum(D)
            checks += 1

    # Polynomial root/fibre bound.
    for p in (2, 3, 5, 7):
        for coeffs in product(range(p), repeat=4):
            if coeffs == (0, 0, 0, 0):
                continue
            d = max(i for i, c in enumerate(coeffs) if c)
            roots = [x for x in range(p) if poly_eval(coeffs, x, p) == 0]
            assert len(roots) <= d
            for mult in range(1, 4):
                assert len(roots)*mult <= d*mult
                checks += 1

    print(f"verified {checks} fourth-frontier interface instances")


if __name__ == "__main__":
    main()
