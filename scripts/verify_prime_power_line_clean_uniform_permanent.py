#!/usr/bin/env python3
"""Finite checks for CMR1534--CMR1541."""
from __future__ import annotations

from collections import deque
from itertools import combinations, permutations
from math import factorial, prod
from random import Random

Edge = tuple[int, int]


class Dinic:
    def __init__(self, n: int) -> None:
        self.g: list[list[list[int]]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: int) -> None:
        self.g[u].append([v, cap, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])

    def max_flow(self, s: int, t: int) -> int:
        flow, n = 0, len(self.g)
        while True:
            level = [-1] * n
            level[s] = 0
            queue = deque([s])
            while queue:
                u = queue.popleft()
                for v, cap, _ in self.g[u]:
                    if cap and level[v] < 0:
                        level[v] = level[u] + 1
                        queue.append(v)
            if level[t] < 0:
                return flow
            it = [0] * n

            def dfs(u: int, pushed: int) -> int:
                if u == t:
                    return pushed
                while it[u] < len(self.g[u]):
                    idx = it[u]
                    v, cap, rev = self.g[u][idx]
                    if cap and level[v] == level[u] + 1:
                        take = dfs(v, min(pushed, cap))
                        if take:
                            self.g[u][idx][1] -= take
                            self.g[v][rev][1] += take
                            return take
                    it[u] += 1
                return 0

            while True:
                pushed = dfs(s, 10**9)
                if not pushed:
                    break
                flow += pushed


def allowed_edges(
    d: int,
    opposite: tuple[Edge, ...],
    target: Edge,
    trace: tuple[Edge, ...],
) -> set[Edge]:
    forbidden = set(opposite) | {target} | set(trace)
    return {
        (i, j)
        for i in range(d)
        for j in range(d)
        if (i, j) not in forbidden
    }


def factor_by_flow(d: int, allowed: set[Edge]) -> set[Edge]:
    q, source, sink = d - 3, 2 * d, 2 * d + 1
    net = Dinic(sink + 1)
    for i in range(d):
        net.add_edge(source, i, q)
    slots: dict[Edge, tuple[int, int]] = {}
    for i, j in sorted(allowed):
        slots[(i, j)] = (i, len(net.g[i]))
        net.add_edge(i, d + j, 1)
    for j in range(d):
        net.add_edge(d + j, sink, q)
    assert net.max_flow(source, sink) == q * d
    factor = {
        edge
        for edge, (u, idx) in slots.items()
        if net.g[u][idx][1] == 0
    }
    assert all(
        sum((i, j) in factor for j in range(d)) == q
        for i in range(d)
    )
    assert all(
        sum((i, j) in factor for i in range(d)) == q
        for j in range(d)
    )
    return factor


def permanent_count(
    d: int,
    allowed: set[Edge],
    prescription: tuple[Edge, ...] = (),
) -> int:
    rows_used = {i for i, _ in prescription}
    cols_used = {j for _, j in prescription}
    if len(rows_used) != len(prescription):
        return 0
    if len(cols_used) != len(prescription):
        return 0
    if any(edge not in allowed for edge in prescription):
        return 0
    rows = [i for i in range(d) if i not in rows_used]
    cols = [j for j in range(d) if j not in cols_used]
    index = {j: k for k, j in enumerate(cols)}
    dp = {0: 1}
    for i in rows:
        nxt: dict[int, int] = {}
        for mask, value in dp.items():
            for j in cols:
                bit = 1 << index[j]
                if not mask & bit and (i, j) in allowed:
                    nxt[mask | bit] = nxt.get(mask | bit, 0) + value
        dp = nxt
    return dp.get((1 << len(cols)) - 1, 0)


def partial_matchings(edges: set[Edge], d: int):
    yield ()
    for rank in range(1, d + 1):
        for rows in combinations(range(d), rank):
            for cols in combinations(range(d), rank):
                for image in permutations(cols):
                    trace = tuple(zip(rows, image))
                    if all(edge in edges for edge in trace):
                        yield trace


def check_cuts(d: int, allowed: set[Edge], rng: Random) -> int:
    q, checks = d - 3, 0
    if d <= 6:
        pairs = [
            (left_mask, right_mask)
            for left_mask in range(1 << d)
            for right_mask in range(1 << d)
        ]
    else:
        pairs = [
            (rng.randrange(1 << d), rng.randrange(1 << d))
            for _ in range(1200)
        ]
    for left_mask, right_mask in pairs:
        left = [i for i in range(d) if left_mask >> i & 1]
        right = [j for j in range(d) if right_mask >> j & 1]
        if len(left) <= len(right):
            continue
        crossing = sum(
            (i, j) in allowed
            for i in left
            for j in range(d)
            if j not in right
        )
        assert crossing >= q * (len(left) - len(right))
        checks += 1
    for x in range(d + 1):
        for y in range(d + 1):
            if x <= y:
                continue
            z = d - y
            m = min(x, z)
            assert x * z - 2 * m - 1 >= q * (x - y)
            checks += 1
    return checks


def random_prescriptions(
    d: int,
    allowed: set[Edge],
    rng: Random,
    exhaustive: bool,
) -> set[tuple[Edge, ...]]:
    out: set[tuple[Edge, ...]] = set()
    if exhaustive:
        for rank in range(1, min(3, d) + 1):
            for rows in combinations(range(d), rank):
                for cols in combinations(range(d), rank):
                    for image in permutations(cols):
                        prescription = tuple(zip(rows, image))
                        if all(edge in allowed for edge in prescription):
                            out.add(prescription)
        return out
    attempts = 0
    while len(out) < 180 and attempts < 4000:
        attempts += 1
        rank = rng.randint(1, min(3, d))
        rows = rng.sample(range(d), rank)
        cols = rng.sample(range(d), rank)
        rng.shuffle(cols)
        prescription = tuple(sorted(zip(rows, cols)))
        if all(edge in allowed for edge in prescription):
            out.add(prescription)
    return out


def check_host(
    d: int,
    trace: tuple[Edge, ...],
    exhaustive: bool,
    rng: Random,
) -> tuple[int, int, int]:
    opposite = tuple((i, i) for i in range(d))
    target = (0, 1)
    allowed = allowed_edges(d, opposite, target, trace)
    cuts = check_cuts(d, allowed, rng)
    factor = factor_by_flow(d, allowed)
    total = permanent_count(d, allowed)
    assert total * d**d >= factorial(d) * (d - 3) ** d
    prescriptions = random_prescriptions(d, allowed, rng, exhaustive)
    checked = 0
    counts: dict[tuple[Edge, ...], int] = {}
    for prescription in prescriptions:
        completions = permanent_count(d, allowed, prescription)
        if not completions:
            continue
        rank = len(prescription)
        falling = prod(range(d - rank + 1, d + 1))
        assert (
            completions * (d - 3) ** d * falling
            <= total * d**d
        )
        counts[prescription] = rng.randrange(0, 8)
        checked += 1
    common = prod(range(d - 2, d + 1))
    exact_numer = sum(
        multiplicity * permanent_count(d, allowed, prescription)
        for prescription, multiplicity in counts.items()
    )
    lhs = exact_numer * (d - 3) ** d * common
    rhs = total * d**d * sum(
        multiplicity
        * (
            common
            // prod(
                range(
                    d - len(prescription) + 1,
                    d + 1,
                )
            )
        )
        for prescription, multiplicity in counts.items()
    )
    assert lhs <= rhs
    return cuts, checked, len(factor)


def main() -> None:
    rng = Random(1534)
    hosts = cuts = probabilities = factor_edges = 0
    for d in (4, 5):
        opposite = tuple((i, i) for i in range(d))
        target = (0, 1)
        base = allowed_edges(d, opposite, target, ())
        for trace in partial_matchings(base, d):
            c, p, f = check_host(
                d,
                trace,
                exhaustive=(d == 4),
                rng=rng,
            )
            hosts += 1
            cuts += c
            probabilities += p
            factor_edges += f
    for d in (6, 7, 8, 9):
        opposite = tuple((i, i) for i in range(d))
        target = (0, 1)
        base = list(allowed_edges(d, opposite, target, ()))
        for _ in range(35):
            rng.shuffle(base)
            used_rows: set[int] = set()
            used_cols: set[int] = set()
            trace: list[Edge] = []
            for i, j in base:
                if (
                    i not in used_rows
                    and j not in used_cols
                    and rng.random() < 0.25
                ):
                    trace.append((i, j))
                    used_rows.add(i)
                    used_cols.add(j)
            c, p, f = check_host(
                d,
                tuple(trace),
                exhaustive=False,
                rng=rng,
            )
            hosts += 1
            cuts += c
            probabilities += p
            factor_edges += f
    print(
        "verified line-clean uniform permanent envelope: "
        f"{hosts} hosts, {cuts} capacitated Hall cuts, "
        f"{factor_edges} factor edges, and "
        f"{probabilities} exact prescription checks"
    )


if __name__ == "__main__":
    main()
