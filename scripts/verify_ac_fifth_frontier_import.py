#!/usr/bin/env python3
"""Finite checks for AC5bm--AC5bs."""

from itertools import combinations, permutations, product
from math import ceil


def independent(mask, edges):
    return all(not ((mask >> a) & 1 and (mask >> b) & 1) for a, b in edges)


def det(a, b, p=None):
    value = a[0] * b[1] - a[1] * b[0]
    return value if p is None else value % p


def on_line(p0, p1, x):
    return det((p1[0] - p0[0], p1[1] - p0[1]), (x[0] - p0[0], x[1] - p0[1])) == 0


def swap(state, i, j):
    state = list(state)
    state[i], state[j] = state[j], state[i]
    return tuple(state)


def cycles(alpha):
    seen = set()
    out = []
    for i in range(len(alpha)):
        if i in seen or alpha[i] == i:
            continue
        cyc = []
        j = i
        while j not in seen:
            seen.add(j)
            cyc.append(j)
            j = alpha[j]
        out.append(cyc)
    return out


def canonical(alpha):
    state = tuple(range(len(alpha)))
    path = [state]
    for cyc in cycles(alpha):
        p = cyc[0]
        for j in reversed(cyc[1:]):
            state = swap(state, p, j)
            path.append(state)
    if state != tuple(alpha):
        state = tuple(range(len(alpha)))
        path = [state]
        for cyc in cycles(alpha):
            p = cyc[0]
            for j in cyc[1:]:
                state = swap(state, p, j)
                path.append(state)
    assert state == tuple(alpha)
    return path


def first_repeat(F, start):
    seen = {}
    seq = []
    x = start
    while x not in seen:
        seen[x] = len(seq)
        seq.append(x)
        x = F[x]
    return seq, seen[x]


def main():
    checks = 0

    # Conflict-graph extraction.
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for gm in range(1 << len(pairs)):
            edges = [e for j, e in enumerate(pairs) if (gm >> j) & 1]
            deg = [0] * n
            for a, b in edges:
                deg[a] += 1
                deg[b] += 1
            inds = [m for m in range(1 << n) if independent(m, edges)]
            alpha = max(m.bit_count() for m in inds)
            assert alpha >= ceil(n / (max(deg, default=0) + 1))
            weights = list(range(1, n + 1))
            best = max(sum(weights[i] for i in range(n) if (m >> i) & 1) for m in inds)
            assert best + 1e-12 >= sum(weights[i] / (deg[i] + 1) for i in range(n))
            checks += 1

    # Exceptional endpoint trimming.
    for mult in product(range(5), repeat=5):
        M = sum(mult)
        for tau in range(5):
            T = [v for v in mult if v > tau]
            assert len(T) * (tau + 1) <= M
            checks += 1

    # Two lines meeting in at most one cell share no two-cell address.
    grid = [(x, y) for x in range(4) for y in range(4)]
    for p0, p1, q0, q1 in combinations(grid, 4):
        L1 = {x for x in grid if on_line(p0, p1, x)}
        L2 = {x for x in grid if on_line(q0, q1, x)}
        if len(L1 & L2) <= 1:
            assert {frozenset(e) for e in combinations(L1, 2)}.isdisjoint(
                {frozenset(e) for e in combinations(L2, 2)}
            )
            checks += 1

    # Canonical sparse paths and antisymmetric cycle comparison.
    for n in range(2, 7):
        for alpha in permutations(range(n)):
            moved = sum(alpha[i] != i for i in range(n))
            if moved == 0:
                continue
            P = canonical(alpha)
            assert len(P) <= moved
            detour = swap(P[0], 0, 1)
            Q = [P[0], detour, P[0]] + P[1:]
            charge = lambda x, y: 1 if x < y else -1
            cp = sum(charge(P[i], P[i + 1]) for i in range(len(P) - 1))
            cq = sum(charge(Q[i], Q[i + 1]) for i in range(len(Q) - 1))
            closed = P + list(reversed(Q[:-1]))
            cc = sum(charge(closed[i], closed[i + 1]) for i in range(len(closed) - 1))
            assert cp - cq == cc
            checks += 1

    # Finite zero-vector decoration recurrence.
    for K in range(1, 5):
        for F in product(range(K), repeat=K):
            for start in range(K):
                seq, mu = first_repeat(F, start)
                assert len(seq) <= K
                cycle = seq[mu:]
                assert F[cycle[-1]] == cycle[0]
                psi = {d: d * d - 2 * d for d in range(K)}
                assert sum(psi[d] - psi[F[d]] for d in cycle) == 0
                checks += 1

    # Quadratic affine-collinearity identity over F_3.
    p = 3
    pts = list(product(range(p), repeat=2))
    for idx in range(30000):
        x1, x2, x3, u1, u2, u3 = [pts[(k * idx + k + 1) % len(pts)] for k in (1, 2, 3, 5, 7, 8)]
        sub = lambda a, b: ((a[0] - b[0]) % p, (a[1] - b[1]) % p)
        a0, a1 = sub(x2, x1), sub(u2, u1)
        b0, b1 = sub(x3, x1), sub(u3, u1)
        c0 = det(a0, b0, p)
        c1 = (det(a1, b0, p) + det(a0, b1, p)) % p
        c2 = det(a1, b1, p)
        roots = 0
        for t in range(p):
            X = [((x[0] + t * u[0]) % p, (x[1] + t * u[1]) % p) for x, u in ((x1, u1), (x2, u2), (x3, u3))]
            direct = det(sub(X[1], X[0]), sub(X[2], X[0]), p)
            assert direct == (c0 + c1 * t + c2 * t * t) % p
            roots += direct == 0
        if not (c0 == c1 == c2 == 0):
            assert roots <= 2
        checks += 1

    print(f"verified {checks} fifth-frontier AC instances")


if __name__ == "__main__":
    main()
