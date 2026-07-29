#!/usr/bin/env python3
"""Finite checks for SRR2ao--SRR2ar."""

from itertools import combinations, product


def subsets(items):
    items = list(items)
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            yield set(c)


def main() -> None:
    checks = 0
    for na in range(1, 5):
        A = tuple(range(na))
        for nb in range(1, 6):
            B = tuple(range(nb))
            edges = [(a, b) for a in A for b in B]
            # Exhaust sparse hole masks and deterministic endpoint weights.
            for r in range(min(4, len(edges)) + 1):
                for chosen in combinations(edges, r):
                    holes = {a: set() for a in A}
                    for a, b in chosen:
                        holes[a].add(b)
                    for S in subsets(B):
                        patterns = [
                            {b: 1 for b in S},
                            {b: (b % 3) + 1 for b in S},
                            {b: ((2 * b + 1) % 5) for b in S},
                        ]
                        for weights in patterns:
                            mult = {b: sum(b in holes[a] for a in A) for b in S}
                            M = sum(mult[b] * weights[b] for b in S)
                            source_stars = [sum(weights[b] for b in S & holes[a]) for a in A]
                            assert max(source_stars, default=0) * na >= M
                            for tau in range(na + 1):
                                T = {b for b in S if mult[b] > tau}
                                exc = sum(weights[b] for b in T)
                                assert exc * (tau + 1) <= M
                                for budget in range(0, sum(weights.values()) + 1):
                                    if exc > budget:
                                        assert max(source_stars, default=0) * na > (tau + 1) * budget
                                checks += 1
    print(f"verified {checks} weighted exceptional endpoint systems")


if __name__ == "__main__":
    main()
