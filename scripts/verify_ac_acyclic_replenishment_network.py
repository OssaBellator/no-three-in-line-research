#!/usr/bin/env python3
"""Finite checks for AC3po--AC3pt."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from random import Random


def reverse_weights(n: int, rates: dict[tuple[int, int], int]) -> list[int]:
    """Nodes 0..n-1 are sources and n is the terminal sink; edges go upward."""
    weights = [0] * (n + 1)
    weights[n] = 1
    for a in range(n - 1, -1, -1):
        weights[a] = 1 + sum(
            rate * weights[v]
            for (u, v), rate in rates.items()
            if u == a and rate
        )
    return weights


def path_weight(a: int, n: int, rates: dict[tuple[int, int], int]) -> int:
    total = 1
    for (u, v), rate in rates.items():
        if u == a and rate:
            total += rate * (1 if v == n else path_weight(v, n, rates))
    return total


def exhaustive_weight_checks(counts: Counter[str]) -> None:
    for n in range(1, 5):
        possible = [(u, v) for u in range(n) for v in range(u + 1, n + 1)]
        # Exhaust all zero/one edge patterns; rates two and three are stressed randomly.
        for bits in product((0, 1), repeat=len(possible)):
            rates = {edge: bit for edge, bit in zip(possible, bits) if bit}
            weights = reverse_weights(n, rates)
            for a in range(n):
                assert weights[a] == path_weight(a, n, rates)
                assert weights[a] >= 1
            counts["acyclic rate graphs"] += 1


def random_step_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(100000):
        n = rng.randint(1, 7)
        rates: dict[tuple[int, int], int] = {}
        for u in range(n):
            for v in range(u + 1, n + 1):
                if rng.randrange(4) == 0:
                    rates[(u, v)] = rng.randint(1, 5)
        weights = reverse_weights(n, rates)
        s = [rng.randint(0, 15) for _ in range(n)]
        m = rng.randint(0, 25)
        debit = [rng.randint(0, value) for value in s]
        source_create = [0] * n
        for v in range(n):
            budget = sum(rates.get((a, v), 0) * debit[a] for a in range(n))
            source_create[v] = rng.randint(0, budget)
        terminal_budget = sum(rates.get((a, n), 0) * debit[a] for a in range(n))
        terminal_create = rng.randint(0, terminal_budget)
        consume = rng.randint(0, m + terminal_create)

        s2 = [s[a] - debit[a] + source_create[a] for a in range(n)]
        m2 = m - consume + terminal_create
        psi = m + sum(w * value for w, value in zip(weights, s))
        psi2 = m2 + sum(w * value for w, value in zip(weights, s2))
        assert psi2 - psi <= -consume - sum(debit)
        if consume + sum(debit) > 0:
            assert psi2 < psi
        counts["mixed DAG transitions"] += 1


def random_histories(counts: Counter[str]) -> None:
    rng = Random(314159)
    for _ in range(40000):
        n = rng.randint(1, 6)
        rates: dict[tuple[int, int], int] = {}
        for u in range(n):
            for v in range(u + 1, n + 1):
                if rng.randrange(3) == 0:
                    rates[(u, v)] = rng.randint(1, 4)
        weights = reverse_weights(n, rates)
        s = [rng.randint(0, 10) for _ in range(n)]
        m = rng.randint(0, 20)
        psi0 = m + sum(w * value for w, value in zip(weights, s))
        total_charge = 0
        steps = 0

        for _step in range(200):
            available = [a for a, value in enumerate(s) if value > 0]
            if not available and m == 0:
                break
            debit = [0] * n
            consume = 0
            if available and (m == 0 or rng.randrange(2) == 0):
                a = rng.choice(available)
                debit[a] = rng.randint(1, s[a])
            else:
                consume = rng.randint(1, m)

            source_create = [0] * n
            for v in range(n):
                budget = sum(rates.get((a, v), 0) * debit[a] for a in range(n))
                source_create[v] = rng.randint(0, budget)
            terminal_budget = sum(rates.get((a, n), 0) * debit[a] for a in range(n))
            terminal_create = rng.randint(0, terminal_budget)
            consume = min(consume, m + terminal_create)

            for a in range(n):
                s[a] = s[a] - debit[a] + source_create[a]
            m = m - consume + terminal_create
            total_charge += consume + sum(debit)
            steps += 1

        psi_final = m + sum(w * value for w, value in zip(weights, s))
        assert total_charge <= psi0 - psi_final
        assert steps <= total_charge <= psi0
        counts["DAG histories"] += 1
        counts["accepted network transitions"] += steps


def strongly_connected_components(n: int, edges: set[tuple[int, int]]) -> list[list[int]]:
    index = 0
    stack: list[int] = []
    on_stack: set[int] = set()
    indices = [-1] * n
    low = [0] * n
    out: list[list[int]] = []

    def visit(v: int) -> None:
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for a, b in edges:
            if a != v:
                continue
            if indices[b] == -1:
                visit(b)
                low[v] = min(low[v], low[b])
            elif b in on_stack:
                low[v] = min(low[v], indices[b])
        if low[v] == indices[v]:
            component: list[int] = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component.append(w)
                if w == v:
                    break
            out.append(component)

    for v in range(n):
        if indices[v] == -1:
            visit(v)
    return out


def condensation_checks(counts: Counter[str]) -> None:
    rng = Random(2718)
    for _ in range(30000):
        n = rng.randint(1, 9)
        edges = {
            (a, b)
            for a in range(n)
            for b in range(n)
            if rng.randrange(5) == 0
        }
        components = strongly_connected_components(n, edges)
        comp_of = {v: i for i, comp in enumerate(components) for v in comp}
        cond = {(comp_of[a], comp_of[b]) for a, b in edges if comp_of[a] != comp_of[b]}

        # Kahn's algorithm verifies that the condensation is acyclic.
        indegree = [0] * len(components)
        adjacency = [[] for _ in components]
        for a, b in cond:
            adjacency[a].append(b)
            indegree[b] += 1
        queue = [i for i, degree in enumerate(indegree) if degree == 0]
        seen = 0
        while queue:
            v = queue.pop()
            seen += 1
            for w in adjacency[v]:
                indegree[w] -= 1
                if indegree[w] == 0:
                    queue.append(w)
        assert seen == len(components)

        for a, b in edges:
            if a == b:
                assert len(components[comp_of[a]]) >= 1
            if comp_of[a] == comp_of[b] and a != b:
                assert len(components[comp_of[a]]) >= 2
        counts["condensation systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_weight_checks(counts)
    random_step_checks(counts)
    random_histories(counts)
    condensation_checks(counts)
    print("AC3po--AC3pt acyclic replenishment network audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
