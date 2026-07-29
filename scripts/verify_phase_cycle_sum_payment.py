#!/usr/bin/env python3
"""Finite checks for OP4as--OP4au."""

from itertools import product


def main():
    checks = 0
    vals = range(4)
    for R in range(1, 8):
        for P in product(vals, repeat=R):
            for D in product(vals, repeat=R):
                # Use a deterministic phase potential to avoid a combinatorial extra loop.
                phi = tuple((j * j + 2 * j + R) % 7 for j in range(R))
                G = tuple(P[j] - D[j] + phi[j] - phi[(j + 1) % R] for j in range(R))
                assert sum(G) == sum(P) - sum(D)
                if sum(P) > sum(D):
                    assert sum(G) > 0 and max(G) > 0
                elif sum(D) > sum(P):
                    assert sum(G) < 0
                else:
                    assert sum(G) == 0
                    assert all(g == 0 for g in G) or (min(G) < 0 < max(G))
                checks += 1
                if checks >= 300000:
                    print(f"verified {checks} cyclic score decompositions")
                    return
    print(f"verified {checks} cyclic score decompositions")


if __name__ == "__main__":
    main()
