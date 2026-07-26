#!/usr/bin/env python3
"""Finite checks for CMR1542--CMR1549."""
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
                pushed = dfs(source, 10**9)
                if not pushed:
                    break
                total += pushed


def allowed_graph(d: int, trace: tuple[Edge, ...]) -> set[Edge]:
    opposite = {(i, i) for i in range(d)}
    target = (0, 1)
    forbidden = opposite | {target} | set(trace)
    return {
        (i, j)
        for i in range(d)
        for j in range(d)
        if (i, j) not in forbidden
    }


def factor_exists(d: int, allowed: set[Edge], degree: int) -> bool:
    source, sink = 2 * d, 2 * d + 1
    net = Dinic(sink + 1)
    for i in range(d):
        net.add_edge(source, i, degree)
    for i, j in allowed:
        net.add_edge(i, d + j, 1)
    for j in range(d):
        net.add_edge(d + j, sink, degree)
    return net.max_flow(source, sink) == degree * d


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


def partial_matchings(edges: set[Edge], d: int):
    yield ()
    for rank in range(1, d + 1):
        for rows in combinations(range(d), rank):
            for cols in combinations(range(d), rank):
                for image in permutations(cols):
                    trace = tuple(zip(rows, image))
                    if all(edge in edges for edge in trace):
                        yield trace


def extension_signature(d: int, trace: tuple[Edge, ...]) -> tuple[bool, str]:
    target = (0, 1)
    rows = {i for i, _ in trace}
    cols = {j for _, j in trace}
    if target[0] in rows or target[1] in cols:
        return False, "target-endpoint overlap"
    union = set(trace) | {target}
    matched_rows = {i for i, _ in union}
    matched_cols = {j for _, j in union}
    unmatched_rows = [i for i in range(d) if i not in matched_rows]
    unmatched_cols = [j for j in range(d) if j not in matched_cols]
    if (
        len(unmatched_rows) == 1
        and unmatched_rows[0] == unmatched_cols[0]
    ):
        return False, "singleton opposite-edge remainder"
    return True, "derangement-extendable"


def sampled_prescriptions(
    d: int,
    allowed: set[Edge],
    rng: Random,
) -> set[tuple[Edge, ...]]:
    out: set[tuple[Edge, ...]] = set()
    attempts = 0
    while len(out) < 120 and attempts < 4000:
        attempts += 1
        rank = rng.randint(1, min(3, d))
        rows = rng.sample(range(d), rank)
        cols = rng.sample(range(d), rank)
        rng.shuffle(cols)
        prescription = tuple(sorted(zip(rows, cols)))
        if all(edge in allowed for edge in prescription):
            out.add(prescription)
    return out


def check_trace(
    d: int,
    trace: tuple[Edge, ...],
    rng: Random,
) -> tuple[int, int]:
    allowed = allowed_graph(d, trace)
    extendable, _ = extension_signature(d, trace)
    assert factor_exists(d, allowed, d - 2) == extendable
    assert factor_exists(d, allowed, d - 3)
    total = permanent_count(d, allowed)
    probability_checks = 0
    if extendable:
        assert total * d**d >= factorial(d) * (d - 2) ** d
        for prescription in sampled_prescriptions(d, allowed, rng):
            completions = permanent_count(d, allowed, prescription)
            if not completions:
                continue
            rank = len(prescription)
            falling = prod(range(d - rank + 1, d + 1))
            assert (
                completions * (d - 2) ** d * falling
                <= total * d**d
            )
            probability_checks += 1
    return int(extendable), probability_checks


def main() -> None:
    rng = Random(1542)
    hosts = extendable_hosts = probability_checks = 0
    exceptional_overlap = exceptional_singleton = 0

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
            extendable, reason = extension_signature(d, trace)
            if not extendable and reason == "target-endpoint overlap":
                exceptional_overlap += 1
            if (
                not extendable
                and reason == "singleton opposite-edge remainder"
            ):
                exceptional_singleton += 1
            flag, checks = check_trace(d, trace, rng)
            hosts += 1
            extendable_hosts += flag
            probability_checks += checks

    for d in (6, 7, 8, 9, 10):
        opposite = {(i, i) for i in range(d)}
        target = (0, 1)
        base = [
            (i, j)
            for i in range(d)
            for j in range(d)
            if (i, j) not in opposite | {target}
        ]
        for _ in range(120):
            rng.shuffle(base)
            used_rows: set[int] = set()
            used_cols: set[int] = set()
            trace: list[Edge] = []
            for i, j in base:
                if (
                    i not in used_rows
                    and j not in used_cols
                    and rng.random() < 0.24
                ):
                    trace.append((i, j))
                    used_rows.add(i)
                    used_cols.add(j)
            extendable, reason = extension_signature(d, tuple(trace))
            if not extendable and reason == "target-endpoint overlap":
                exceptional_overlap += 1
            if (
                not extendable
                and reason == "singleton opposite-edge remainder"
            ):
                exceptional_singleton += 1
            flag, checks = check_trace(d, tuple(trace), rng)
            hosts += 1
            extendable_hosts += flag
            probability_checks += checks

    print(
        "verified line-clean factor sharpening: "
        f"{hosts} hosts, {extendable_hosts} (d-2)-factor hosts, "
        f"{exceptional_overlap} endpoint-overlap exceptions, "
        f"{exceptional_singleton} singleton exceptions, and "
        f"{probability_checks} sharpened prescription checks"
    )


if __name__ == "__main__":
    main()
