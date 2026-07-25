#!/usr/bin/env python3
"""Finite checks for PX311--PX314."""

from itertools import combinations, permutations
from math import ceil


def partial_permutations(n):
    vertices = range(n)
    yield set()
    for k in range(1, n + 1):
        for domain in combinations(vertices, k):
            for image in combinations(vertices, k):
                for p in permutations(image):
                    yield set(zip(domain, p))


def has_directed_cycle(n, edges):
    nxt = {x: y for x, y in edges}
    for start in range(n):
        seen = set()
        cur = start
        while cur in nxt:
            if cur in seen:
                return True
            seen.add(cur)
            cur = nxt[cur]
    return False


def verify_path_forest_bound():
    total = 0
    for n in range(1, 8):
        for edges in partial_permutations(n):
            if any(x == y for x, y in edges):
                continue
            total += 1
            if not has_directed_cycle(n, edges):
                assert len(edges) <= max(0, n - 1)
    return total


def verify_depth_thresholds():
    for s in range(2, 100):
        for delta0 in range(0, s + 3):
            load = max(0, s * (s - 1 - delta0))
            threshold = ceil(load / (s - 1))
            for d in range(0, 2 * s + 5):
                if d < threshold:
                    assert d * (s - 1) < load
                else:
                    assert d * (s - 1) >= load
            if delta0 == 0:
                assert threshold == s


def verify_base_free_full_layers():
    for s in range(2, 20):
        total_cells = s * (s - 1)
        layers = s - 1
        assert total_cells == layers * s
        sizes = [s] * layers
        assert sum(sizes) == total_cells


def main():
    total = verify_path_forest_bound()
    verify_depth_thresholds()
    verify_base_free_full_layers()
    print(f"verified PX311--PX314 on {total} partial permutations")


if __name__ == "__main__":
    main()
