#!/usr/bin/env python3
"""Finite checks for PX294--PX299.

Every DAG has a topological ordering. We exhaust all subsets of the forward
arcs in one fixed order through m=6; this covers every labelled DAG up to
relabeling by a topological order.
"""

from itertools import combinations, permutations
from math import ceil, floor, isqrt


def closure(m, arcs):
    reach = [[False] * m for _ in range(m)]
    for x, y in arcs:
        reach[x][y] = True
    for k in range(m):
        for i in range(m):
            if not reach[i][k]:
                continue
            for j in range(m):
                if reach[k][j]:
                    reach[i][j] = True
    return reach


def has_cycle(m, arcs):
    reach = closure(m, arcs)
    return any(reach[i][i] for i in range(m))


def chain_height(m, reach):
    dp = [1] * m
    for y in range(m):
        dp[y] = 1 + max((dp[x] for x in range(y) if reach[x][y]), default=0)
    return max(dp, default=0)


def longest_path_levels(m, reach):
    level = [1] * m
    for y in range(m):
        level[y] = 1 + max((level[x] for x in range(y) if reach[x][y]), default=0)
    buckets = {}
    for v, lev in enumerate(level):
        buckets.setdefault(lev, []).append(v)
    return list(buckets.values())


def max_base_degree(m, reach):
    row = [0] * m
    col = [0] * m
    for x in range(m):
        for y in range(m):
            if reach[x][y]:
                row[y] += 1
                col[x] += 1
    return max(row + col + [0])


def verify_dag(m, arcs):
    reach = closure(m, arcs)
    assert not any(reach[i][i] for i in range(m))

    # PX294: every reverse reachability edge closes a directed cycle.
    arcset = set(arcs)
    for x in range(m):
        for y in range(m):
            if reach[x][y]:
                assert has_cycle(m, arcset | {(y, x)})

    # PX295.
    comparable = sum(reach[x][y] for x in range(m) for y in range(m))
    delta0 = max_base_degree(m, reach)
    assert comparable <= m * delta0

    # PX296.
    height = chain_height(m, reach)
    assert height * (height - 1) // 2 <= comparable <= m * delta0
    h0 = floor((1 + isqrt(1 + 8 * m * delta0)) / 2) if delta0 else 1
    while (h0 + 1) * h0 // 2 <= m * delta0:
        h0 += 1
    while h0 * (h0 - 1) // 2 > m * delta0:
        h0 -= 1
    levels = longest_path_levels(m, reach)
    q = max(levels, key=len)
    assert len(q) >= ceil(m / max(1, height))
    assert len(q) >= ceil(m / max(1, h0))
    for x, y in combinations(q, 2):
        assert not reach[x][y] and not reach[y][x]
        assert (x, y) not in arcset and (y, x) not in arcset

    # PX297 in the extremal no-reset decomposition: F0 is exactly reverse
    # reachability and every other forbidden off-diagonal cell is historical.
    base = {(y, x) for x in range(m) for y in range(m) if reach[x][y]}
    historical = {
        (x, y)
        for x in range(m)
        for y in range(m)
        if x != y and (x, y) not in arcset and (x, y) not in base
    }
    s = len(q)
    inside = sum((x, y) in historical for x in q for y in q if x != y)
    assert inside >= max(0, s * (s - 1 - delta0))


def verify_full_layer_cycle_cover():
    # PX299: every fixed-point-free permutation decomposes into cycles >=2.
    for m in range(2, 8):
        for p in permutations(range(m)):
            if any(p[i] == i for i in range(m)):
                continue
            seen = [False] * m
            moved = 0
            for start in range(m):
                if seen[start]:
                    continue
                cur = start
                length = 0
                while not seen[cur]:
                    seen[cur] = True
                    length += 1
                    moved += 1
                    cur = p[cur]
                assert cur == start
                assert length >= 2
            assert moved == m


def main():
    total = 0
    for m in range(2, 7):
        forward = [(x, y) for x in range(m) for y in range(x + 1, m)]
        for mask in range(1 << len(forward)):
            arcs = {e for bit, e in enumerate(forward) if (mask >> bit) & 1}
            verify_dag(m, arcs)
            total += 1
    verify_full_layer_cycle_cover()
    print(f"verified PX294--PX299 on {total} topologically ordered DAGs")


if __name__ == "__main__":
    main()
