#!/usr/bin/env python3
"""Finite checks for BDA5cc--BDA5cf."""

from itertools import combinations


def greedy_matching(n: int, edges: list[tuple[int, int]], weights: dict[tuple[int, int], int]):
    remaining = sorted(edges, key=lambda e: (-weights[e], e))
    chosen = []
    used = set()
    for e in remaining:
        a, b = e
        if a in used or b in used or weights[e] <= 0:
            continue
        chosen.append(e)
        used.add(a)
        used.add(b)
    return chosen


def main() -> None:
    checks = 0
    for n in range(2, 8):
        all_edges = list(combinations(range(n), 2))
        graph_masks = range(1 << len(all_edges)) if n <= 5 else [0, 1, 3, 0x1555, 0x2AAA, (1 << len(all_edges)) - 1]
        for mask in graph_masks:
            edges = [all_edges[i] for i in range(len(all_edges)) if mask >> i & 1]
            patterns = [
                {e: 1 for e in edges},
                {e: ((e[0] + 2 * e[1]) % 5) + 1 for e in edges},
                {e: ((3 * e[0] + e[1] + 1) % 7) for e in edges},
            ]
            for weights in patterns:
                positive = [e for e in edges if weights[e] > 0]
                if not positive:
                    continue
                degrees = [sum(v in e for e in positive) for v in range(n)]
                d = max(degrees)
                W = sum(weights[e] for e in positive)
                matching = greedy_matching(n, positive, weights)
                MW = sum(weights[e] for e in matching)
                assert MW * (2 * d - 1) >= W
                assert len({v for e in matching for v in e}) == 2 * len(matching)
                for threshold in range(1, d + 1):
                    if max(degrees) <= threshold:
                        assert MW * (2 * threshold - 1) >= W
                    else:
                        assert any(deg > threshold for deg in degrees)
                checks += 1
    print(f"verified {checks} weighted line-pair graphs")


if __name__ == "__main__":
    main()
