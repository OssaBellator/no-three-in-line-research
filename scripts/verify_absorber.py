#!/usr/bin/env python3
"""Check affine subgroup absorber identities for a small composite modulus."""
from __future__ import annotations
import argparse
from collections import Counter
from math import gcd


def subgroup(n: int, h: int) -> list[int]:
    if n % h:
        raise ValueError('h must divide n')
    q = n // h
    return [(q * i) % n for i in range(h)]


def state(n: int, h: int, m: int, coset: int, shift_index: int, offset: int = 0):
    H = subgroup(n, h)
    t = H[shift_index % h]
    C = [((coset + u) % n) for u in H]
    return {(x, (m * (x + t) + offset) % n) for x in C}


def line_multiset(points, direction, n):
    a, b = direction
    return Counter((b*x - a*y) % n for x, y in points)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=30)
    ap.add_argument('--h', type=int, default=5)
    ap.add_argument('--m', type=int, default=7)
    ap.add_argument('--coset', type=int, default=1)
    args = ap.parse_args()
    n, h, m = args.n, args.h, args.m
    if gcd(m, n) != 1:
        raise SystemExit('m must be a unit modulo n')
    states = [state(n, h, m, args.coset, t) for t in range(h)]
    rowsets = [{y for _, y in s} for s in states]
    colsets = [{x for x, _ in s} for s in states]
    assert all(r == rowsets[0] for r in rowsets)
    assert all(c == colsets[0] for c in colsets)
    assert len(set().union(*states)) == h*h
    assert sum(len(s) for s in states) == h*h

    protected = [(1, 1), (1, 2), (2, 1)]
    for d in protected:
        qd = d[1] - d[0]*m
        if gcd(h, qd) == 1:
            multisets = [line_multiset(s, d, n) for s in states]
            assert all(x == multisets[0] for x in multisets)
    print(f'verified {h} states in an order-{h} block for n={n}, m={m}')


if __name__ == '__main__':
    main()
