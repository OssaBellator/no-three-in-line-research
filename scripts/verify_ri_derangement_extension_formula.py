#!/usr/bin/env python3
"""Verify RI5ap--RI5at by exhaustive and symbolic derangement counts."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def derangements(n):
    return [p for p in permutations(range(n)) if all(p[i] != i for i in range(n))]


def derangement_number(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    a, b = 1, 0
    for k in range(2, n + 1):
        a, b = b, (k - 1) * (a + b)
    return b


def falling(n, s):
    out = 1
    for j in range(s):
        out *= n - j
    return out


def extension_count(t, s, q):
    free = t - 2 * s + q
    assert free >= 0
    return sum((-1) ** j * comb(free, j) * factorial(t - s - j) for j in range(free + 1))


def exhaustive(max_t=8):
    checked = 0
    for t in range(2, max_t + 1):
        bank = derangements(t)
        assert len(bank) == derangement_number(t)
        for s in range(1, min(3, t) + 1):
            counts = Counter()
            for p in bank:
                for cols in combinations(range(t), s):
                    rows = tuple(p[c] for c in cols)
                    counts[(cols, rows)] += 1
            by_q = defaultdict(set)
            for (cols, rows), count in counts.items():
                q = len(set(cols) & set(rows))
                assert count == extension_count(t, s, q)
                by_q[q].add(count)
                checked += 1
            qs = sorted(by_q)
            vals = [next(iter(by_q[q])) for q in qs]
            assert all(a >= b for a, b in zip(vals, vals[1:]))
            qmin = max(0, 2 * s - t)
            assert qs[0] == qmin
            sharp = Fraction(extension_count(t, s, qmin), len(bank))
            assert sharp <= Fraction(3, falling(t, s))
            if s == 1:
                assert sharp == Fraction(1, t - 1)
    return checked


def symbolic(max_t=40):
    checks = 0
    for t in range(2, max_t + 1):
        d = derangement_number(t)
        assert 3 * d >= factorial(t)
        for s in range(1, min(3, t) + 1):
            qmin = max(0, 2 * s - t)
            values = [extension_count(t, s, q) for q in range(qmin, s + 1)]
            assert all(a >= b for a, b in zip(values, values[1:]))
            p = Fraction(values[0], d)
            assert p <= Fraction(3, falling(t, s))
            if t >= 7:
                for D in range(1, 20):
                    raw_exact = Fraction(D, 3) / p
                    raw_universal = Fraction(falling(t, s) * D, 9)
                    assert raw_exact >= raw_universal
                    G = 12 * D
                    assert raw_universal == Fraction(falling(t, s) * G, 108)
                    checks += 1
    return checks


def main():
    print(f"RI derangement extensions: verified {exhaustive()} prescriptions and {symbolic()} amplification checks")


if __name__ == '__main__':
    main()
