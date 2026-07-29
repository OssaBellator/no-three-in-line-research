#!/usr/bin/env python3
"""Finite checks for SRR2ag--SRR2aj."""

from itertools import combinations


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


def bound(A, S, holes):
    mult = {b: sum(b in holes[a] for a in A) for b in S}
    mu = max(mult.values(), default=0)
    M = sum(mult.values())
    vals = [max(len(A) - len(S), 0)]
    for x in range(1, min(len(A), mu) + 1):
        vals.append(max(x - len(S) + M // x, 0))
    return max(vals)


def main():
    checks = 0
    # Exhaust every hole mask with at most four holes on boards through 4x4.
    for na in range(1, 5):
        A = tuple(range(na))
        for nb in range(1, 5):
            B = tuple(range(nb))
            all_edges = [(a, b) for a in A for b in B]
            for r in range(min(4, len(all_edges)) + 1):
                for chosen in combinations(all_edges, r):
                    holes = {a: set() for a in A}
                    for a, b in chosen:
                        holes[a].add(b)
                    for S in subsets(B):
                        d = exact_deficiency(A, S, holes)
                        assert d <= bound(A, S, holes)
                        for X in subsets(A):
                            if not X:
                                continue
                            common = set(S)
                            for a in X:
                                common &= holes[a]
                            mass = sum(len(S & holes[a]) for a in X)
                            assert len(common) * len(X) <= mass
                        checks += 1
    print(f"verified {checks} threshold hole systems")


if __name__ == "__main__":
    main()
