#!/usr/bin/env python3
"""Finite checks for SRR2ac--SRR2af."""

from itertools import combinations, permutations


def subsets(xs):
    xs = tuple(xs)
    for r in range(len(xs) + 1):
        yield from combinations(xs, r)


def matching_rank(A, S, edges):
    A, S = tuple(A), tuple(S)
    best = 0
    for r in range(1, min(len(A), len(S)) + 1):
        for left in combinations(A, r):
            for right in combinations(S, r):
                if any(all((a, b) in edges for a, b in zip(left, p)) for p in permutations(right)):
                    best = r
    return best


def hall(A, B, edges):
    for X in subsets(A):
        if not X:
            continue
        nbh = {b for a in X for b in B if (a, b) in edges}
        if len(nbh) < len(X):
            return False
    return True


def main():
    checked = 0
    # Exhaust all graphs through 3x4; structured samples at 4x5.
    cases = [(2, 3), (2, 4), (3, 3), (3, 4)]
    for na, nb in cases:
        A, B = tuple(range(na)), tuple(range(nb))
        ambient = [(a, b) for a in A for b in B]
        for mask in range(1 << len(ambient)):
            edges = {e for i, e in enumerate(ambient) if mask >> i & 1}
            if not hall(A, B, edges):
                continue
            holes = {a: set(B) - {b for b in B if (a, b) in edges} for a in A}
            for S0 in subsets(B):
                S = set(S0)
                rank = matching_rank(A, S, edges)
                deficiency = len(A) - rank
                rhs = 0
                for X0 in subsets(A):
                    if not X0:
                        continue
                    common = set(B)
                    for a in X0:
                        common &= holes[a]
                    rhs = max(rhs, len(X0) - len(S) + len(S & common))
                rhs = max(rhs, 0)
                assert deficiency == rhs
                checked += 1

            # Threshold-cost identity for deterministic endpoint costs.
            costs = {b: (2 * b + na) % 4 for b in B}
            C = max(costs.values())
            deltas = []
            for k in range(1, C + 1):
                S = {b for b in B if costs[b] < k}
                deltas.append(len(A) - matching_rank(A, S, edges))
            opt = min(
                sum(costs[b] for b in p)
                for p in permutations(B, len(A))
                if all((a, b) in edges for a, b in zip(A, p))
            )
            assert opt == sum(deltas)

            # Conditioning is the same formula on surviving endpoints.
            for D0 in subsets(B):
                if len(D0) > 1:
                    continue
                Bp = set(B) - set(D0)
                if hall(A, Bp, edges):
                    for S0 in subsets(Bp):
                        S = set(S0)
                        deficiency = len(A) - matching_rank(A, S, edges)
                        rhs = 0
                        for X0 in subsets(A):
                            if not X0:
                                continue
                            common = set(B)
                            for a in X0:
                                common &= holes[a]
                            rhs = max(rhs, len(X0) - len(S) + len(S & common))
                        assert deficiency == max(rhs, 0)

    print(f"verified {checked} common-hole rank identities")


if __name__ == "__main__":
    main()
