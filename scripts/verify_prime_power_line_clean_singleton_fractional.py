#!/usr/bin/env python3
"""Finite checks for CMR1550--CMR1557."""
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

    def max_flow(self, source: int, sink: int) -> int:
        total = 0
        while True:
            level = [-1] * len(self.g)
            level[source] = 0
            queue = deque([source])
            while queue:
                u = queue.popleft()
                for v, cap, _ in self.g[u]:
                    if cap and level[v] < 0:
                        level[v] = level[u] + 1
                        queue.append(v)
            if level[sink] < 0:
                return total
            it = [0] * len(self.g)

            def dfs(u: int, pushed: int) -> int:
                if u == sink:
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
                pushed = dfs(source, 10**18)
                if not pushed:
                    break
                total += pushed


def partial_matchings(edges: set[Edge], d: int):
    yield ()
    for rank in range(1, d + 1):
        for rows in combinations(range(d), rank):
            for cols in combinations(range(d), rank):
                for image in permutations(cols):
                    trace = tuple(zip(rows, image))
                    if all(edge in edges for edge in trace):
                        yield trace


def singleton_trace(d: int, trace: tuple[Edge, ...]) -> bool:
    target = (0, 1)
    rows = {i for i, _ in trace}
    cols = {j for _, j in trace}
    if target[0] in rows or target[1] in cols:
        return False
    union = set(trace) | {target}
    matched_rows = {i for i, _ in union}
    matched_cols = {j for _, j in union}
    unmatched_rows = [i for i in range(d) if i not in matched_rows]
    unmatched_cols = [j for j in range(d) if j not in matched_cols]
    return (
        len(unmatched_rows) == 1
        and unmatched_rows[0] == unmatched_cols[0]
    )


def allowed_graph(d: int, trace: tuple[Edge, ...]) -> set[Edge]:
    forbidden = {(i, i) for i in range(d)} | {(0, 1)} | set(trace)
    return {
        (i, j)
        for i in range(d)
        for j in range(d)
        if (i, j) not in forbidden
    }


def scaled_fractional_flow(d: int, allowed: set[Edge]) -> int:
    denominator = d - 2
    demand = (d - 1) * (d - 3)
    source, sink = 2 * d, 2 * d + 1
    net = Dinic(sink + 1)
    for i in range(d):
        net.add_edge(source, i, demand)
    for i, j in allowed:
        net.add_edge(i, d + j, denominator)
    for j in range(d):
        net.add_edge(d + j, sink, demand)
    flow = net.max_flow(source, sink)
    assert flow == demand * d
    return flow


def permanent_count(
    d: int,
    allowed: set[Edge],
    prescription: tuple[Edge, ...] = (),
) -> int:
    used_rows = {i for i, _ in prescription}
    used_cols = {j for _, j in prescription}
    if len(used_rows) != len(prescription):
        return 0
    if len(used_cols) != len(prescription):
        return 0
    if any(edge not in allowed for edge in prescription):
        return 0
    rows = [i for i in range(d) if i not in used_rows]
    cols = [j for j in range(d) if j not in used_cols]
    index = {j: k for k, j in enumerate(cols)}
    dp = {0: 1}
    for i in rows:
        nxt: dict[int, int] = {}
        for mask, count in dp.items():
            for j in cols:
                bit = 1 << index[j]
                if not mask & bit and (i, j) in allowed:
                    nxt[mask | bit] = nxt.get(mask | bit, 0) + count
        dp = nxt
    return dp.get((1 << len(cols)) - 1, 0)


def cut_checks(d: int, allowed: set[Edge]) -> int:
    denominator = d - 2
    demand = (d - 1) * (d - 3)
    checks = 0
    for left_mask in range(1 << d):
        left = [i for i in range(d) if left_mask >> i & 1]
        for right_mask in range(1 << d):
            right = [j for j in range(d) if right_mask >> j & 1]
            if len(left) <= len(right):
                continue
            crossing = sum(
                (i, j) in allowed
                for i in left
                for j in range(d)
                if j not in right
            )
            assert (
                denominator * crossing
                >= demand * (len(left) - len(right))
            )
            checks += 1
    return checks


def random_singleton_trace(d: int, rng: Random) -> tuple[Edge, ...]:
    target = (0, 1)
    while True:
        missing = rng.randrange(2, d)
        labels = [i for i in range(d) if i != missing]
        image = labels[:]
        rng.shuffle(image)
        mapping = dict(zip(labels, image))
        if mapping.get(0) != 1:
            continue
        if any(mapping[i] == i for i in labels):
            continue
        union = {(i, mapping[i]) for i in labels}
        return tuple(sorted(union - {target}))


def sampled_prescriptions(
    d: int,
    allowed: set[Edge],
    rng: Random,
) -> set[tuple[Edge, ...]]:
    out: set[tuple[Edge, ...]] = set()
    attempts = 0
    while len(out) < 160 and attempts < 5000:
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
    rng: Random,
) -> tuple[int, int]:
    assert singleton_trace(d, trace)
    allowed = allowed_graph(d, trace)
    scaled_fractional_flow(d, allowed)
    checks = cut_checks(d, allowed) if d <= 6 else 0
    total = permanent_count(d, allowed)
    denominator = d - 2
    demand = (d - 1) * (d - 3)
    assert (
        total * (d * denominator) ** d
        >= factorial(d) * demand**d
    )
    probability_checks = 0
    for prescription in sampled_prescriptions(d, allowed, rng):
        completions = permanent_count(d, allowed, prescription)
        if not completions:
            continue
        rank = len(prescription)
        falling = prod(range(d - rank + 1, d + 1))
        assert (
            completions * demand**d * falling
            <= total * (d * denominator) ** d
        )
        probability_checks += 1
    return checks, probability_checks


def main() -> None:
    rng = Random(1550)
    hosts = cuts = probabilities = 0

    for d in (4, 5):
        opposite = {(i, i) for i in range(d)}
        target = (0, 1)
        base = {
            (i, j)
            for i in range(d)
            for j in range(d)
            if (i, j) not in opposite | {target}
        }
        for trace in partial_matchings(base, d):
            if not singleton_trace(d, trace):
                continue
            c, p = check_host(d, trace, rng)
            hosts += 1
            cuts += c
            probabilities += p

    for d in (6, 7, 8, 9, 10):
        for _ in range(100):
            trace = random_singleton_trace(d, rng)
            c, p = check_host(d, trace, rng)
            hosts += 1
            cuts += c
            probabilities += p

    print(
        "verified singleton fractional line-clean factor: "
        f"{hosts} hosts, {cuts} exact capacitated cuts, and "
        f"{probabilities} prescription checks"
    )


if __name__ == "__main__":
    main()
