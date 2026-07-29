#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache

RISKS = (Fraction(1, 32), Fraction(1, 16), Fraction(1, 8))
TARGET = (3, 2, 1)
P0, P1 = Fraction(3, 4), Fraction(2, 3)
BAD = 2
ACCEPT = {0, 1}

def trans(q, bit):
    if q == BAD:
        return BAD
    if bit == 0:
        return 1 if q == 0 else BAD
    return 0

def multiply(a, b):
    out = defaultdict(int)
    for x, cx in a.items():
        for y, cy in b.items():
            z = tuple(x[i] + y[i] for i in range(3))
            if all(z[i] <= TARGET[i] for i in range(3)):
                out[z] += cx * cy
    return dict(out)

def coefficient(tau):
    visited = set()
    @lru_cache(None)
    def poly(q, cap):
        visited.add((q, cap))
        if q == BAD or cap < min(RISKS):
            return {}
        out = {}
        if q in ACCEPT:
            for i, risk in enumerate(RISKS):
                if risk <= cap:
                    e = [0, 0, 0]
                    e[i] = 1
                    out[tuple(e)] = out.get(tuple(e), 0) + 1
        left = poly(trans(q, 0), cap * P0)
        right = poly(trans(q, 1), cap * P1)
        if left and right:
            for key, value in multiply(left, right).items():
                out[key] = out.get(key, 0) + value
        return out
    p = poly(0, tau)
    return p.get(TARGET, 0), len(visited)

# Candidate threshold set from legal words to depth 12.
candidates = set()
def walk(q, survival, depth):
    if q in ACCEPT:
        for risk in RISKS:
            candidates.add(risk / survival)
    if depth == 12:
        return
    for bit, prob in ((0, P0), (1, P1)):
        nq = trans(q, bit)
        if nq != BAD:
            walk(nq, survival * prob, depth + 1)
walk(0, Fraction(1), 0)

optimum = None
count = 0
states = 0
for tau in sorted(candidates):
    c, s = coefficient(tau)
    if c:
        optimum, count, states = tau, c, s
        break

assert optimum == Fraction(243, 1024)
assert count == 1
assert coefficient(Fraction(3, 16))[0] == 0

print({
    "threshold": str(optimum),
    "coefficient": count,
    "product_states": states,
    "target_multiplicity": TARGET,
    "language": "avoid 00",
})
