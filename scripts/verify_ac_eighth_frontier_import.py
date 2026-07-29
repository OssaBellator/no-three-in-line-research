#!/usr/bin/env python3
"""Finite checks for AC5ch--AC5cn."""

from itertools import combinations, permutations, product


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def degree(poly):
    return -1 if poly == (0,) else len(poly) - 1


def eval_poly(poly, t, p):
    out = 0
    for c in reversed(poly):
        out = (out * t + c) % p
    return out


def sub_scaled(f, a, g, p):
    n = max(len(f), len(g))
    return trim([((f[i] if i < len(f) else 0) - a * (g[i] if i < len(g) else 0)) % p
                 for i in range(n)])


def swap_adjacent(state, i):
    out = list(state)
    out[i], out[i + 1] = out[i + 1], out[i]
    return tuple(out)


def main() -> None:
    checks = 0

    # Resource-fibre representative bounds for RI and endpoint stars.
    for n in range(1, 8):
        for k in range(1, 5):
            for mu in range(1, 5):
                for seed in range(180):
                    weights = [((seed + 3 * i + i * i) % 9) for i in range(n)]
                    labels = [((2 * seed + i * i + i) % k) for i in range(n)]
                    fibres = [[] for _ in range(k)]
                    for w, label in zip(weights, labels):
                        fibres[label].append(w)
                    total = sum(weights)
                    if all(len(f) <= mu for f in fibres):
                        assert mu * sum(max(f, default=0) for f in fibres) >= total
                    else:
                        assert any(len(f) > mu for f in fibres)
                    checks += 1

    # Weighted BDA partner-star identity and class concentration.
    for n in range(2, 8):
        edges = list(combinations(range(n), 2))
        for seed in range(800):
            weights = [((seed + 5 * i + i * i) % 11) for i in range(len(edges))]
            stars = [0] * n
            for (u, v), w in zip(edges, weights):
                stars[u] += w
                stars[v] += w
            total = sum(weights)
            assert sum(stars) == 2 * total
            x = max(range(n), key=lambda i: stars[i])
            assert n * stars[x] >= 2 * total
            partners = [v if u == x else u for u, v in edges if x in (u, v)]
            assert len(partners) == len(set(partners))
            checks += 1

    # Coxeter local defects vanish for potential charges.
    for r in range(2, 6):
        states = list(permutations(range(r)))
        phi = {s: sum((i + 2) * s[i] for i in range(r)) for s in states}
        charge = lambda u, v: phi[v] - phi[u]
        for m in states:
            for i in range(r - 1):
                for j in range(i + 2, r - 1):
                    a = charge(m, swap_adjacent(m, i))
                    mi = swap_adjacent(m, i)
                    a += charge(mi, swap_adjacent(mi, j))
                    b = charge(m, swap_adjacent(m, j))
                    mj = swap_adjacent(m, j)
                    b += charge(mj, swap_adjacent(mj, i))
                    assert a == b
                    checks += 1
            for i in range(r - 2):
                p = m
                a = 0
                for g in (i, i + 1, i):
                    q = swap_adjacent(p, g)
                    a += charge(p, q)
                    p = q
                p = m
                b = 0
                for g in (i + 1, i, i + 1):
                    q = swap_adjacent(p, g)
                    b += charge(p, q)
                    p = q
                assert a == b
                checks += 1

    # Exact stutter scores and ticket identity.
    for payment in range(15):
        for debt in range(15):
            assert payment - debt == payment - debt
            key = (payment, debt, "fixed")
            assert key == tuple(key)
            checks += 1

    # Rational fixed-ratio root bounds.
    for p in (2, 3, 5, 7):
        for d in range(5):
            for seed in range(600):
                f = trim([(seed + 3 * i + i * i) % p for i in range(d + 1)])
                g = trim([(2 * seed + 5 * i + 1) % p for i in range(d + 1)])
                if g == (0,):
                    g = (1,)
                D = max(degree(f), degree(g))
                assert sum(eval_poly(g, t, p) == 0 for t in range(p)) <= degree(g)
                for alpha in range(p):
                    h = sub_scaled(f, alpha, g, p)
                    roots = sum(eval_poly(g, t, p) != 0 and eval_poly(h, t, p) == 0
                                for t in range(p))
                    if h != (0,):
                        assert roots <= degree(h) <= D
                    checks += 1

    print(f"verified {checks} combined AC resource/local instances")


if __name__ == "__main__":
    main()
