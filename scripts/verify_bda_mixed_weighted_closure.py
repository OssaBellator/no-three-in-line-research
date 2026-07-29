#!/usr/bin/env python3
"""Finite checks for BDA5by--BDA5cb."""

from fractions import Fraction
from itertools import combinations


def det(x, y):
    return x[0] * y[1] - x[1] * y[0]


def on_line(p, q, x):
    return det((q[0] - p[0], q[1] - p[1]), (x[0] - p[0], x[1] - p[1])) == 0


def main():
    geometry_checks = 0
    weight_checks = 0
    grid = [(x, y) for x in range(-3, 4) for y in range(-3, 4)]

    # Distinct lines with at most one common grid cell cannot share a two-cell address.
    for p, q, r, s in combinations(grid[:12], 4):
        if p == q or r == s:
            continue
        L1 = {x for x in grid if on_line(p, q, x)}
        L2 = {x for x in grid if on_line(r, s, x)}
        if len(L1 & L2) <= 1:
            pairs1 = {frozenset(e) for e in combinations(L1, 2)}
            pairs2 = {frozenset(e) for e in combinations(L2, 2)}
            assert pairs1.isdisjoint(pairs2)
            geometry_checks += 1

    # Verify the resonance and unique-intersection identities.
    for a in range(1, 4):
        for b in range(1, 4):
            for h in range(1, 4):
                for q0 in range(1, 4):
                    H = h + q0
                    zA = (h * a, h * b)
                    zB = (H * a, H * b)
                    zC = (h * a, H * b)
                    zD = (H * a, h * b)
                    n = (zC[0] - zD[0], zC[1] - zD[1])
                    cd = det(zC, zD)
                    assert det(n, zA) == -2 * h * a * b * q0
                    assert det(n, zB) == -2 * H * a * b * q0
                    assert det(n, zC) == cd
                    assert det(n, zD) == cd
                    # CD-AB intersection parameter.
                    t = Fraction(2 * h + q0, 2)
                    d = (a, b)
                    lhs = det(n, (t * d[0], t * d[1]))
                    assert lhs == cd
                    geometry_checks += 1

    # Pointwise minimum gives exact common/exclusive decomposition.
    samples = [
        ({0: 3, 1: 2}, {0: 1, 2: 5}),
        ({0: 4, 1: 1}, {0: 4, 1: 3}),
        ({2: 7}, {3: 6}),
    ]
    for wu, wv in samples:
        keys = set(wu) | set(wv)
        O = sum(min(wu.get(k, 0), wv.get(k, 0)) for k in keys)
        Wu = sum(wu.values())
        Wv = sum(wv.values())
        ru = {k: wu.get(k, 0) - min(wu.get(k, 0), wv.get(k, 0)) for k in keys}
        rv = {k: wv.get(k, 0) - min(wu.get(k, 0), wv.get(k, 0)) for k in keys}
        assert sum(ru.values()) == Wu - O
        assert sum(rv.values()) == Wv - O
        assert all(not (ru[k] > 0 and rv[k] > 0) for k in keys)
        weight_checks += 1

    print(f"verified {geometry_checks} geometric cases and {weight_checks} weighted decompositions")


if __name__ == "__main__":
    main()
