#!/usr/bin/env python3
"""Finite checks for SAS5hu--SAS5hw."""

from itertools import permutations


def compose(p, q):
    """Return p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def transposition(n, a, b):
    t = list(range(n))
    t[a], t[b] = t[b], t[a]
    return tuple(t)


def cycles(alpha):
    seen = set()
    out = []
    for i in range(len(alpha)):
        if i in seen or alpha[i] == i:
            continue
        cyc = []
        x = i
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = alpha[x]
        out.append(tuple(cyc))
    return out


def canonical_transpositions(alpha):
    n = len(alpha)
    out = []
    for cyc in cycles(alpha):
        pivot = cyc[0]
        # Successive left composition by (pivot,cyc[j]) reconstructs the cycle.
        for j in range(1, len(cyc)):
            out.append(transposition(n, pivot, cyc[j]))
    return out


def main():
    checks = 0
    for n in range(1, 9):
        ident = tuple(range(n))
        for alpha in permutations(range(n)):
            ts = canonical_transpositions(alpha)
            cur = ident
            prefixes = []
            for t in ts:
                cur = compose(t, cur)
                prefixes.append(cur)
            assert cur == alpha

            cs = cycles(alpha)
            r = sum(len(c) for c in cs)
            s = len(cs)
            assert len(ts) == r - s
            if r:
                assert len(ts) <= r - 1
            else:
                assert len(ts) == 0
            assert len(prefixes) * 2 * r <= 2 * r * max(r - 1, 0)
            checks += 1

    print(f"verified {checks} canonical permutation implementations")


if __name__ == "__main__":
    main()
