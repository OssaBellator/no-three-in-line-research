#!/usr/bin/env python3
"""Finite checks for PX300--PX304."""

from itertools import combinations, permutations
from random import Random


def collinear(z, p, q):
    return (p[0] - z[0]) * (q[1] - z[1]) == (q[0] - z[0]) * (p[1] - z[1])


def verify_packet_identity():
    rng = Random(300)
    for h in range(3, 9):
        xs = list(range(2, 2 + h))
        ys = [3 * j + 1 for j in range(h)]
        for _ in range(100):
            p = list(range(h))
            rng.shuffle(p)
            points = [(xs[r], ys[p[r]]) for r in range(h)]
            r, s = rng.sample(range(h), 2)
            pr, ps = points[r], points[s]
            z = (2 * pr[0] - ps[0], 2 * pr[1] - ps[1])
            assert collinear(z, pr, ps)
            left = (xs[r] - z[0]) * (ys[p[s]] - z[1])
            right = (xs[s] - z[0]) * (ys[p[r]] - z[1])
            assert left == right


def apply_disjoint_swaps(perm, matching):
    out = list(perm)
    used = set()
    for r, s in matching:
        assert r not in used and s not in used
        used.add(r)
        used.add(s)
        out[r], out[s] = out[s], out[r]
    assert sorted(out) == list(range(len(perm)))
    return out


def greedy_edge_coloring(edges, rho):
    colors = {}
    for e in edges:
        x, y = e
        blocked = {c for f, c in colors.items() if x in f or y in f}
        for c in range(max(1, 2 * rho - 1)):
            if c not in blocked:
                colors[e] = c
                break
        else:
            raise AssertionError("greedy color bound failed")
    return colors


def verify_weighted_graphs():
    rng = Random(304)
    for n in range(2, 12):
        all_edges = list(combinations(range(n), 2))
        for _ in range(300):
            edges = [e for e in all_edges if rng.random() < 0.3]
            weights = {e: rng.randint(1, 9) for e in edges}
            degree = [0] * n
            for x, y in edges:
                degree[x] += 1
                degree[y] += 1
            rho = max(degree, default=0)
            colors = greedy_edge_coloring(edges, rho)
            classes = {}
            for e, c in colors.items():
                classes.setdefault(c, []).append(e)
            for cls in classes.values():
                flat = [v for e in cls for v in e]
                assert len(flat) == len(set(flat))
                apply_disjoint_swaps(list(range(n)), cls)
            total = sum(weights.values())
            best = max((sum(weights[e] for e in cls) for cls in classes.values()), default=0)
            if total:
                assert best * max(1, 2 * rho - 1) >= total


def verify_line_star_bound():
    for k in range(1, 30):
        for a in range(k + 1):
            for b in range(k + 1 - a):
                assert min(a, b) * k >= a * b


def verify_full_small_permutations():
    for n in range(2, 8):
        for p in permutations(range(n)):
            for matching_size in range(n // 2 + 1):
                matching = [(2 * i, 2 * i + 1) for i in range(matching_size)]
                apply_disjoint_swaps(p, matching)


def main():
    verify_packet_identity()
    verify_weighted_graphs()
    verify_line_star_bound()
    verify_full_small_permutations()
    print("verified PX300--PX304")


if __name__ == "__main__":
    main()
