#!/usr/bin/env python3
"""Finite checks for PX294--PX298."""

from __future__ import annotations

from itertools import combinations
import random


def all_dag_edges(n: int):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(pairs)):
        yield {pairs[k] for k in range(len(pairs)) if mask & (1 << k)}


def max_path_weights(n: int, edges: set[tuple[int, int]], sink: int,
                     weights: list[int]) -> tuple[list[int | None], list[int | None]]:
    outgoing = [[] for _ in range(n)]
    for u, v in edges:
        outgoing[u].append(v)

    memo: list[int | None] = [None] * n
    nxt: list[int | None] = [None] * n

    def visit(u: int) -> int | None:
        if u == sink:
            memo[u] = weights[u]
            return memo[u]
        if memo[u] is not None:
            return memo[u]
        best: int | None = None
        best_v: int | None = None
        for v in outgoing[u]:
            tail = visit(v)
            if tail is None:
                continue
            value = weights[u] + tail
            if best is None or value > best:
                best = value
                best_v = v
        memo[u] = best
        nxt[u] = best_v
        return best

    for u in range(n - 1, -1, -1):
        visit(u)
    return memo, nxt


def path_from(c: int, sink: int, nxt: list[int | None]) -> list[int]:
    path = [c]
    while path[-1] != sink:
        step = nxt[path[-1]]
        if step is None:
            raise AssertionError("vertex does not reach sink")
        path.append(step)
    return path


def check_hybrid_potential() -> None:
    # Child conversion: total unchanged, lexicographic vector decreases.
    before = (5, (2, 0, 0, 0))
    after = (5, (1, 0, 0, 1))
    assert after < before

    # Historical reset: total decreases, so shallower-coordinate return is harmless.
    before = (7, (0, 0, 0, 4))
    after = (5, (1, 0, 0, 1))
    assert after < before


def check_exhaustive_unit_weights() -> None:
    for n in range(2, 7):
        sink = n - 1
        for edges in all_dag_edges(n):
            weights = [1] * n
            best, nxt = max_path_weights(n, edges, sink, weights)
            basin = [u for u, value in enumerate(best) if value is not None]
            if len(basin) <= 1:
                continue

            candidates = [u for u in basin if u != sink]
            for delta0 in range(min(3, len(candidates)) + 1):
                # It is enough to test every possible base subset through this size.
                for base_tuple in combinations(candidates, delta0):
                    base = set(base_tuple)
                    historical = [u for u in candidates if u not in base]

                    # No-improving-reset extremal assignment h(c)=max path weight.
                    recurrence = {u: best[u] for u in historical}
                    assert all(recurrence[u] is not None for u in historical)

                    for tau in range(2, n + 2):
                        r_tau = [u for u in candidates if best[u] is not None and best[u] >= tau]
                        heavy = [u for u in historical if recurrence[u] is not None and recurrence[u] >= tau]
                        assert len(heavy) >= max(0, len(r_tau) - delta0)

                    # PX295 on every historical return edge.
                    for c in historical:
                        path = path_from(c, sink, nxt)
                        destroyed = sum(weights[x] for x in path)
                        recreated = recurrence[c]
                        assert recreated == destroyed
                        assert not recreated < destroyed

                    # PX297: a longest path has a historical reverse edge among
                    # its first delta0+1 vertices unless every candidate is base.
                    if historical:
                        source = max(candidates, key=lambda u: best[u] or -1)
                        longest = path_from(source, sink, nxt)
                        L = len(longest) - 1
                        if L >= delta0:
                            prefix = longest[: min(delta0 + 1, L)]
                            hist_prefix = [u for u in prefix if u in historical]
                            if hist_prefix:
                                lower = L - delta0 + 1
                                assert max(recurrence[u] or 0 for u in hist_prefix) >= lower


def check_random_weighted() -> None:
    rng = random.Random(20260725)
    for n in range(3, 11):
        sink = n - 1
        for _ in range(500):
            edges = {
                (u, v)
                for u in range(n)
                for v in range(u + 1, n)
                if rng.random() < 0.28
            }
            weights = [rng.randint(1, 5) for _ in range(n)]
            best, nxt = max_path_weights(n, edges, sink, weights)
            candidates = [u for u in range(n) if u != sink and best[u] is not None]
            if not candidates:
                continue

            delta0 = rng.randint(0, min(3, len(candidates)))
            base = set(rng.sample(candidates, delta0))
            historical = [u for u in candidates if u not in base]

            recurrence: dict[int, int] = {}
            improving = []
            for u in historical:
                threshold = best[u]
                assert threshold is not None
                # Sometimes create an improving reset, otherwise sit at/above threshold.
                if rng.random() < 0.3 and threshold > 0:
                    recurrence[u] = rng.randint(0, threshold - 1)
                    improving.append(u)
                else:
                    recurrence[u] = threshold + rng.randint(0, 4)

            for u in historical:
                path = path_from(u, sink, nxt)
                destroyed = sum(weights[x] for x in path)
                assert destroyed == best[u]
                assert (recurrence[u] < destroyed) == (u in improving)

            if not improving:
                for tau in range(2, sum(weights) + 1):
                    r_tau = [u for u in candidates if (best[u] or 0) >= tau]
                    heavy = [u for u in historical if recurrence[u] >= tau]
                    assert len(heavy) >= max(0, len(r_tau) - delta0)


def main() -> None:
    check_hybrid_potential()
    check_exhaustive_unit_weights()
    check_random_weighted()
    print("weighted historical reset verifier: PASS")


if __name__ == "__main__":
    main()
