#!/usr/bin/env python3
"""Finite checks for SRR2ak--SRR2an."""

from itertools import combinations


def subsets(items):
    items = list(items)
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            yield set(c)


def deficiency(A, S, holes):
    best = 0
    for X in subsets(A):
        if not X:
            continue
        common = set(S)
        for a in X:
            common &= holes[a]
        best = max(best, len(X) - len(S) + len(common))
    return max(best, 0)


def mult_bound(A, S, holes, tau):
    mult = {b: sum(b in holes[a] for a in A) for b in S}
    M = sum(mult.values())
    T = {b for b in S if mult[b] > tau}
    R = S - T
    MR = sum(mult[b] for b in R)
    vals = [max(len(A) - len(R), 0)]
    for x in range(1, min(len(A), tau) + 1):
        vals.append(max(x - len(R) + MR // x, 0))
    return M, T, R, MR, max(vals)


def hole_masks(edges, limit):
    # Exhaust all masks through four holes, then add deterministic dense samples.
    for r in range(min(4, len(edges)) + 1):
        yield from combinations(edges, r)
    if len(edges) > 4:
        yield tuple(edges)
        yield tuple(edges[::2])
        yield tuple(edges[1::2])


def main():
    checks = 0
    for na in range(1, 5):
        A = tuple(range(na))
        for nb in range(1, 5):
            B = tuple(range(nb))
            edges = [(a, b) for a in A for b in B]
            for chosen in hole_masks(edges, 4):
                holes = {a: set() for a in A}
                for a, b in chosen:
                    holes[a].add(b)
                for S in subsets(B):
                    for tau in range(na + 1):
                        M, T, R, MR, E = mult_bound(A, S, holes, tau)
                        assert len(T) * (tau + 1) <= M
                        assert MR == M - sum(sum(b in holes[a] for a in A) for b in T)
                        assert MR <= M - (tau + 1) * len(T)
                        assert deficiency(A, R, holes) <= E
                        assert deficiency(A, S, holes) <= E
                        assert deficiency(A, S, holes) + len(T) <= E + len(T)
                        checks += 1
    print(f"verified {checks} trimmed threshold systems")


if __name__ == "__main__":
    main()
