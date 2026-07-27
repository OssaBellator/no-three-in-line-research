#!/usr/bin/env python3
"""Verify OP4t--OP4x on small completion systems and I6 state models."""
from itertools import combinations, permutations, product
from fractions import Fraction


def invert(p):
    q = [0] * len(p)
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)


def closure(current, X, target_rows):
    inv = invert(current)
    sigma = {x: inv[target_rows[x]] for x in X}
    starts = [x for x in X if all(sigma[z] != x for z in X)]
    Q = {}
    seen = set()
    for start in starts:
        v = start
        path = []
        while v in X and v not in seen:
            seen.add(v)
            path.append(v)
            v = sigma[v]
        if v not in X:
            Q[v] = current[path[0]]
    return sigma, Q


def verify_completion(max_n=4):
    checks = 0
    for n in range(3, max_n + 1):
        for current in permutations(range(n)):
            for size in range(1, min(4, n) + 1):
                for Xtuple in combinations(range(n), size):
                    X = set(Xtuple)
                    for rows in combinations(range(n), size):
                        for row_perm in permutations(rows):
                            target = dict(zip(Xtuple, row_perm))
                            sigma, Q = closure(current, X, target)
                            for x in X:
                                if current[x] == target[x]:
                                    assert sigma[x] == x
                            cols = set(X) | set(Q)
                            target_cells = {(x, target[x]) for x in X} | set(Q.items())
                            assert len({c for c, _ in target_cells}) == len(target_cells)
                            assert len({r for _, r in target_cells}) == len(target_cells)
                            assert {r for _, r in target_cells} == {current[c] for c in cols}
                            for perm_rows in permutations(row_perm):
                                state = {(x, r) for x, r in zip(Xtuple, perm_rows)} | set(Q.items())
                                assert {c for c, _ in state} == cols
                                assert {r for _, r in state} == {current[c] for c in cols}
                            checks += 1
    return checks


def verify_i6(max_m=4, max_h=4):
    checks = 0
    for m in range(1, max_m + 1):
        for h in range(1, max_h + 1):
            states = list(product(permutations(range(m)), product(range(h), repeat=m)))
            total = len(states)
            for r in range(1, min(3, m) + 1):
                src = tuple(range(r))
                tgt = tuple(reversed(range(r)))
                shifts = tuple((i + 1) % h for i in range(r))
                count = 0
                for pi, sh in states:
                    if all(pi[src[i]] == tgt[i] and sh[src[i]] == shifts[i] for i in range(r)):
                        count += 1
                expected = Fraction(1, 1)
                for j in range(r):
                    expected /= (m - j) * h
                assert Fraction(count, total) == expected
                checks += 1
    return checks


def main():
    print(f"OP closed fixed edge: verified {verify_completion()} completion systems and {verify_i6()} I6 cylinder laws")


if __name__ == '__main__':
    main()
