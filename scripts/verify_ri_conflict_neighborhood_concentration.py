#!/usr/bin/env python3
"""Finite checks for RI5bv--RI5by."""

from itertools import combinations


def independent(mask: int, edges: set[tuple[int, int]], n: int) -> bool:
    verts = [i for i in range(n) if mask >> i & 1]
    return all((min(a, b), max(a, b)) not in edges for a, b in combinations(verts, 2))


def maximal(mask: int, edges: set[tuple[int, int]], n: int) -> bool:
    if not independent(mask, edges, n):
        return False
    return all(not independent(mask | (1 << v), edges, n) for v in range(n) if not (mask >> v & 1))


def closed_neighborhood(v: int, edges: set[tuple[int, int]], n: int) -> set[int]:
    out = {v}
    for a, b in edges:
        if a == v:
            out.add(b)
        elif b == v:
            out.add(a)
    return out


def main() -> None:
    checks = 0
    for n in range(1, 7):
        pairs = list(combinations(range(n), 2))
        # Exhaust all graphs through n=5; use deterministic masks for n=6.
        graph_masks = range(1 << len(pairs)) if n <= 5 else [0, 1, (1 << len(pairs)) - 1, 0x1555, 0x2AAA]
        weight_patterns = [
            [1] * n,
            [i + 1 for i in range(n)],
            [((3 * i + 1) % 5) + 1 for i in range(n)],
        ]
        for gmask in graph_masks:
            edges = {pairs[i] for i in range(len(pairs)) if gmask >> i & 1}
            inds = [mask for mask in range(1 << n) if independent(mask, edges, n)]
            alpha = max(mask.bit_count() for mask in inds)
            maximals = [mask for mask in inds if maximal(mask, edges, n)]
            assert maximals
            for weights in weight_patterns:
                W = sum(weights)
                q = alpha + 1
                for mask in maximals:
                    I = [v for v in range(n) if mask >> v & 1]
                    covered = set().union(*(closed_neighborhood(v, edges, n) for v in I))
                    assert covered == set(range(n))
                    neighborhood_weights = [sum(weights[u] for u in closed_neighborhood(v, edges, n)) for v in I]
                    assert max(neighborhood_weights) * (q - 1) >= W
                    checks += 1
    print(f"verified {checks} maximal independent neighborhood bounds")


if __name__ == "__main__":
    main()
