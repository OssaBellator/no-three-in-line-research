#!/usr/bin/env python3
"""Finite checks for AC3pu--AC3pz."""

from __future__ import annotations

from collections import Counter
from itertools import product
from random import Random


def strongly_connected(rho: tuple[tuple[int, ...], ...]) -> bool:
    n = len(rho)
    if n == 0:
        return False

    def reach(start: int, reverse: bool = False) -> set[int]:
        seen = {start}
        stack = [start]
        while stack:
            a = stack.pop()
            for v in range(n):
                edge = rho[v][a] if reverse else rho[a][v]
                if edge > 0 and v not in seen:
                    seen.add(v)
                    stack.append(v)
        return seen

    return len(reach(0)) == n and len(reach(0, True)) == n


def is_positive_cyclic_component(rho: tuple[tuple[int, ...], ...]) -> bool:
    return strongly_connected(rho) and all(sum(row) >= 1 for row in rho)


def output_slots(row: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple((v, k) for v, rate in enumerate(row) for k in range(1, rate + 1))


def check_component(rho: tuple[tuple[int, ...], ...], counts: Counter[str]) -> None:
    n = len(rho)
    assert is_positive_cyclic_component(rho)
    gains = [sum(row) for row in rho]

    # A directed positive cycle rules out strict positive separable weights.
    for weights in product(range(1, 5), repeat=n):
        strict = all(
            weights[a] > sum(rho[a][v] * weights[v] for v in range(n))
            for a in range(n)
        )
        assert not strict
    counts["weight-vector exclusions"] += 1

    if all(gain == 1 for gain in gains):
        successor = []
        for row in rho:
            positive = [(v, rate) for v, rate in enumerate(row) if rate > 0]
            assert len(positive) == 1 and positive[0][1] == 1
            successor.append(positive[0][0])
        visited = set()
        a = 0
        for _ in range(n):
            assert a not in visited
            visited.add(a)
            a = successor[a]
        assert a == 0 and len(visited) == n
        counts["conservative unit cycles"] += 1
    else:
        a_star = min(a for a, gain in enumerate(gains) if gain >= 2)
        slots = output_slots(rho[a_star])
        assert len(slots) >= 2 and slots[0] != slots[1]
        counts["multi-output addresses"] += 1
        counts["declared output slots"] += len(slots)


def exhaustive_components(counts: Counter[str]) -> None:
    for n in range(1, 4):
        for flat in product(range(3), repeat=n * n):
            rho = tuple(tuple(flat[a * n + v] for v in range(n)) for a in range(n))
            if is_positive_cyclic_component(rho):
                check_component(rho, counts)
                counts["exhaustive cyclic SCCs"] += 1
            elif n == 1 and rho[0][0] == 0:
                counts["excluded acyclic singleton SCCs"] += 1


def random_components(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(30000):
        n = rng.randint(2, 8)
        rho = [[0] * n for _ in range(n)]
        order = list(range(n))
        rng.shuffle(order)
        for i, a in enumerate(order):
            rho[a][order[(i + 1) % n]] = rng.randint(1, 3)
        for a in range(n):
            for v in range(n):
                if rng.randrange(6) == 0:
                    rho[a][v] = max(rho[a][v], rng.randint(1, 3))
        matrix = tuple(tuple(row) for row in rho)
        check_component(matrix, counts)
        counts["random cyclic SCCs"] += 1


def conservative_histories(counts: Counter[str]) -> None:
    rng = Random(911)
    for _ in range(50000):
        n = rng.randint(1, 10)
        stock = [rng.randint(0, 20) for _ in range(n)]
        tickets = [rng.randint(0, 12) for _ in range(n)]
        initial_budget = sum(stock) + sum(tickets)
        accepted = 0
        stutters_erased = 0

        for _step in range(200):
            available = [a for a, value in enumerate(stock) if value > 0]
            if not available:
                break
            a = rng.choice(available)
            successor = (a + 1) % n
            preserve = rng.randrange(4) != 0
            if preserve and tickets[a] == 0:
                stutters_erased += 1
                continue
            stock[a] -= 1
            if preserve:
                stock[successor] += 1
                tickets[a] -= 1
            accepted += 1

        assert accepted <= initial_budget
        counts["conservative histories"] += 1
        counts["accepted cycle steps"] += accepted
        counts["erased quotient stutters"] += stutters_erased


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_components(counts)
    random_components(counts)
    conservative_histories(counts)
    print("AC3pu--AC3pz cyclic-source SCC audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
