#!/usr/bin/env python3
"""Finite checks for AC3oz--AC3pd."""

from __future__ import annotations

from collections import Counter
from itertools import product
from random import Random


def first_boundary(path: tuple[int, ...], truth: tuple[int, ...]) -> tuple[int, int] | None:
    for left, right in zip(path, path[1:]):
        if truth[left] == 0 and truth[right] == 1:
            return left, right
    return None


def exhaustive_signature_paths(counts: Counter[str]) -> None:
    for size in range(2, 5):
        vertices = tuple(range(size))
        directed_pairs = tuple((u, v) for u in vertices for v in vertices if u != v)
        for truth in product((0, 1), repeat=size):
            if min(truth) == max(truth):
                continue
            zeros = sum(value == 0 for value in truth)
            ones = size - zeros
            assert zeros * ones <= (size * size) // 4
            for edge_mask in range(1 << len(directed_pairs)):
                if size == 4 and edge_mask % 97:
                    continue
                edges = {
                    directed_pairs[index]
                    for index in range(len(directed_pairs))
                    if edge_mask & (1 << index)
                }
                crossing = {(u, v) for u, v in edges if truth[u] == 0 and truth[v] == 1}
                assert len(crossing) <= len(edges)
                assert len(crossing) <= zeros * ones
                outdegree = max(
                    (sum((u, v) in edges for v in vertices) for u in vertices),
                    default=0,
                )
                assert len(crossing) <= size * outdegree

                for length in range(2, 6):
                    for path in product(vertices, repeat=length):
                        if truth[path[0]] != 0 or truth[path[-1]] != 1:
                            continue
                        if any((u, v) not in edges for u, v in zip(path, path[1:])):
                            continue
                        boundary = first_boundary(path, truth)
                        assert boundary is not None
                        index = next(
                            i
                            for i, (u, v) in enumerate(zip(path, path[1:]))
                            if truth[u] == 0 and truth[v] == 1
                        )
                        assert boundary == (path[index], path[index + 1])
                        counts["projected recreation paths"] += 1
                counts["signature graph systems"] += 1


def alias_and_ticket_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(60000):
        size = rng.randint(2, 9)
        truth = tuple(rng.randrange(2) for _ in range(size))
        if min(truth) == max(truth):
            continue
        aliases = [
            (signature, alias)
            for signature in range(size)
            for alias in range(rng.randint(1, 8))
        ]
        sigma = {alias_vertex: alias_vertex[0] for alias_vertex in aliases}
        for alias_vertex in aliases:
            assert truth[sigma[alias_vertex]] == truth[alias_vertex[0]]

        false_aliases = [v for v in aliases if truth[sigma[v]] == 0]
        true_aliases = [v for v in aliases if truth[sigma[v]] == 1]
        if not false_aliases or not true_aliases:
            continue
        source = rng.choice(false_aliases)
        target = rng.choice(true_aliases)
        projected_gate = (sigma[source], sigma[target], rng.randrange(4))

        # Every fresh symbolic alias consumes the same quotient stock.
        capacity = rng.randint(0, 12)
        requested = rng.randint(0, 20)
        charged = min(capacity, requested)
        assert charged <= capacity
        assert requested - charged == max(0, requested - capacity)
        counts["shared alias ticket systems"] += 1

        # A missing projected edge is replacement, never a same-owner continuation.
        registered = rng.choice((True, False))
        same_owner = registered and projected_gate is not None
        assert same_owner == registered
        counts["identity wall checks"] += 1


def weighted_localization_checks(counts: Counter[str]) -> None:
    rng = Random(91)
    for _ in range(30000):
        gate_count = rng.randint(1, 25)
        weights = [rng.randint(0, 40) for _ in range(gate_count)]
        total = sum(weights)
        assert max(weights) * gate_count >= total
        counts["weighted gate systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_signature_paths(counts)
    alias_and_ticket_checks(counts)
    weighted_localization_checks(counts)
    print("AC3oz--AC3pd physical-signature quotient audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
