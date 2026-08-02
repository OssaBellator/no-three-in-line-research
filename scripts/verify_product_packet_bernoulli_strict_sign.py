#!/usr/bin/env python3
"""Finite checks for PX305--PX310."""

from itertools import combinations
from math import floor, sqrt
from random import Random


def expected_polynomial(weights, supports, p):
    destruction = p * sum(weights)
    creation = sum(p ** len(s) for s in supports)
    return -destruction + creation


def exact_expectation(weights, supports, p):
    q = len(weights)
    total = 0.0
    for mask in range(1 << q):
        prob = 1.0
        active = set()
        for i in range(q):
            if (mask >> i) & 1:
                active.add(i)
                prob *= p
            else:
                prob *= 1 - p
        destroyed = sum(weights[i] for i in active)
        created = sum(1 for support in supports if set(support) <= active)
        total += prob * (-destroyed + created)
    return total


def verify_bernoulli_polynomial():
    rng = Random(305)
    for q in range(1, 8):
        for _ in range(300):
            weights = [rng.randint(1, 7) for _ in range(q)]
            supports = []
            for _ in range(rng.randint(0, 30)):
                u = rng.randint(1, min(3, q))
                supports.append(tuple(sorted(rng.sample(range(q), u))))
            for p in (0.0, 0.07, 0.2, 0.5, 1.0):
                exact = exact_expectation(weights, supports, p)
                poly = expected_polynomial(weights, supports, p)
                assert abs(exact - poly) < 1e-9

            c1 = sum(len(s) == 1 for s in supports)
            c2 = sum(len(s) == 2 for s in supports)
            c3 = sum(len(s) == 3 for s in supports)
            w = sum(weights)
            g = w - c1
            if g > 0:
                b = c2 + c3
                p = 1.0 if b == 0 else min(1.0, g / (2 * b))
                bound = -p * w + p * c1 + p * p * c2 + p ** 3 * c3
                assert bound <= -p * g / 2 + 1e-12


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])


def triples(points):
    return {
        tuple(sorted(t))
        for t in combinations(points, 3)
        if collinear(*t)
    }


def verify_single_edge_decomposition():
    rng = Random(307)
    for _ in range(1000):
        fixed = set()
        while len(fixed) < 7:
            fixed.add((rng.randrange(-4, 5), rng.randrange(-4, 5)))
        fixed = list(fixed)
        f1 = (10 + rng.randrange(5), 20 + rng.randrange(5))
        f2 = (30 + rng.randrange(5), 40 + rng.randrange(5))
        if f1 == f2 or f1 in fixed or f2 in fixed:
            continue
        new_triples = triples(fixed + [f1, f2]) - triples(fixed)
        mu1 = sum(collinear(f1, x, y) for x, y in combinations(fixed, 2))
        mu2 = sum(collinear(f2, x, y) for x, y in combinations(fixed, 2))
        lam = sum(collinear(f1, f2, x) for x in fixed)
        assert len(new_triples) == mu1 + mu2 + lam


def verify_constants():
    for h in range(2, 100):
        for k in range(1, 20):
            for t in range(1, 30):
                r = k * t
                residual = (2 * r - 1) * h * k * (2 * t + 1) / 2
                assert residual < 3 * h * k * k * t * t

    for h in range(2, 100):
        for k in range(1, 20):
            for d in range(12 * h * k * k, 12 * h * k * k + 200):
                t = floor(sqrt(d / (12 * h * k * k)))
                assert t >= 1
                assert 3 * h * k * k * t * t <= d / 4 + 1e-12


def main():
    verify_bernoulli_polynomial()
    verify_single_edge_decomposition()
    verify_constants()
    print("verified PX305--PX310")


if __name__ == "__main__":
    main()
