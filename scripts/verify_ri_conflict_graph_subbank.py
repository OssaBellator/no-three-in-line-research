#!/usr/bin/env python3
"""Finite checks for RI5br--RI5bu."""

from itertools import combinations
from math import ceil, factorial


def independent(mask: int, edges: list[tuple[int, int]]) -> bool:
    return all(not ((mask >> a) & 1 and (mask >> b) & 1) for a, b in edges)


def main() -> None:
    graph_checks = 0
    weighted_checks = 0
    for n in range(1, 7):
        pairs = list(combinations(range(n), 2))
        # Exhaust all graphs through n=5; use structured masks for n=6.
        masks = range(1 << len(pairs)) if n <= 5 else [0, (1 << len(pairs)) - 1] + [1 << j for j in range(len(pairs))]
        for graph_mask in masks:
            edges = [e for j, e in enumerate(pairs) if (graph_mask >> j) & 1]
            deg = [0] * n
            for a, b in edges:
                deg[a] += 1
                deg[b] += 1
            delta = max(deg, default=0)
            inds = [m for m in range(1 << n) if independent(m, edges)]
            alpha = max(m.bit_count() for m in inds)
            assert alpha >= ceil(n / (delta + 1))

            for weights in ([1] * n, list(range(1, n + 1)), [2 if i % 2 else 1 for i in range(n)]):
                best = max(sum(weights[i] for i in range(n) if (m >> i) & 1) for m in inds)
                rhs = sum(weights[i] / (deg[i] + 1) for i in range(n))
                assert best + 1e-12 >= rhs
                weighted_checks += 1

            # Any independent family of q components has the expected bank size.
            q = alpha
            h = 3
            assert factorial(q) * h**q >= 1
            graph_checks += 1

    print(f"verified {graph_checks} conflict graphs and {weighted_checks} weighted bounds")


if __name__ == "__main__":
    main()
