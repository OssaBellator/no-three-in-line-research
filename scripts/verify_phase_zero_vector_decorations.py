#!/usr/bin/env python3
"""Finite checks for OP4aw--OP4az."""

from itertools import product


def first_repeat(F, start):
    seen = {}
    seq = []
    x = start
    while x not in seen:
        seen[x] = len(seq)
        seq.append(x)
        x = F[x]
    return seq, seen[x], len(seq)


def main():
    map_checks = 0
    score_checks = 0
    for K in range(1, 6):
        maps = product(range(K), repeat=K) if K <= 4 else [tuple(range(K)), tuple((i + 1) % K for i in range(K)), tuple(0 for _ in range(K))]
        for F in maps:
            for start in range(K):
                seq, mu, nu = first_repeat(F, start)
                assert 0 <= mu < nu <= K
                assert len(seq) == nu
                assert len(set(seq)) == len(seq)
                cycle = seq[mu:nu]
                assert F[cycle[-1]] == cycle[0]
                assert len(seq) - 1 <= K - 1

                # Check cyclic cancellation for deterministic score samples.
                psi = {d: 3 * d - d * d for d in range(K)}
                P = {d: d % 3 for d in range(K)}
                D = {d: (d + 1) % 2 for d in range(K)}
                total = 0
                for d in cycle:
                    e = F[d]
                    total += P[d] - D[d] + psi[d] - psi[e]
                assert total == sum(P[d] for d in cycle) - sum(D[d] for d in cycle)
                score_checks += 1
            map_checks += 1

    print(f"verified {map_checks} decoration maps and {score_checks} cyclic score audits")


if __name__ == "__main__":
    main()
