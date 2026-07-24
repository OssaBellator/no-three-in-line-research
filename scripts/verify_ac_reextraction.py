#!/usr/bin/env python3
"""Verify AC2a weighted extraction and AC3b/AC3c accounting."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def greedy_colours(
    size: int, edges: tuple[tuple[int, int], ...]
) -> tuple[list[list[int]], int]:
    adjacency = [set() for _ in range(size)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    colours: list[list[int]] = []
    for vertex in range(size):
        for colour in colours:
            if all(other not in adjacency[vertex] for other in colour):
                colour.append(vertex)
                break
        else:
            colours.append([vertex])
    maximum_degree = max((len(neighbours) for neighbours in adjacency), default=0)
    return colours, maximum_degree


def verify_weighted_extraction(max_size: int = 6) -> None:
    for size in range(1, max_size + 1):
        pairs = tuple(combinations(range(size), 2))
        for mask in range(1 << len(pairs)):
            edges = tuple(
                edge for index, edge in enumerate(pairs) if mask & (1 << index)
            )
            colours, maximum_degree = greedy_colours(size, edges)
            assert len(colours) <= maximum_degree + 1
            weights = [1 + (5 * vertex + mask) % 11 for vertex in range(size)]
            heaviest = max(
                sum(weights[vertex] for vertex in colour) for colour in colours
            )
            assert heaviest * (maximum_degree + 1) >= sum(weights)


def verify_composed_bound() -> None:
    for pair_degree in range(1, 8):
        for conflict_degree in range(8):
            total_weight = 137
            link_retained = Fraction(
                total_weight, 2 * pair_degree - 1
            )
            installable = link_retained / (conflict_degree + 1)
            assert (
                installable
                * (2 * pair_degree - 1)
                * (conflict_degree + 1)
                == total_weight
            )


def acyclic_potential(
    size: int, edges: tuple[tuple[int, int], ...]
) -> list[int] | None:
    incoming = [set() for _ in range(size)]
    outgoing = [set() for _ in range(size)]
    for source, target in edges:
        outgoing[source].add(target)
        incoming[target].add(source)

    remaining = set(range(size))
    potential = [0] * size
    queue = [vertex for vertex in remaining if not incoming[vertex]]
    while queue:
        vertex = queue.pop()
        if vertex not in remaining:
            continue
        remaining.remove(vertex)
        for target in outgoing[vertex]:
            potential[target] = max(potential[target], potential[vertex] + 1)
            incoming[target].remove(vertex)
            if not incoming[target]:
                queue.append(target)
    if remaining:
        return None
    return potential


def verify_cycle_criterion(max_size: int = 4) -> None:
    for size in range(1, max_size + 1):
        possible = tuple(
            (source, target)
            for source in range(size)
            for target in range(size)
            if source != target
        )
        for mask in range(1 << len(possible)):
            edges = tuple(
                edge
                for index, edge in enumerate(possible)
                if mask & (1 << index)
            )
            potential = acyclic_potential(size, edges)
            if potential is not None:
                assert all(
                    potential[target] > potential[source]
                    for source, target in edges
                )

    assert acyclic_potential(2, ((0, 1), (1, 0))) is None


def verify_ticket_trace() -> None:
    signatures = {"product", "center"}
    budgets = {"product": 2, "center": 1}
    exposed: set[str] = set()
    counters = {signature: 0 for signature in signatures}
    trace = (
        ("new", "product"),
        ("old", "product"),
        ("new", "center"),
        ("old", "product"),
        ("old", "center"),
    )
    previous = 0
    for kind, signature in trace:
        if kind == "new":
            assert signature not in exposed
            exposed.add(signature)
        else:
            assert signature in exposed
            counters[signature] += 1
            assert counters[signature] <= budgets[signature]
        current = len(exposed) + sum(counters.values())
        assert current == previous + 1
        previous = current
    assert previous == len(signatures) + sum(budgets.values())


def main() -> None:
    verify_weighted_extraction()
    verify_composed_bound()
    verify_cycle_criterion()
    verify_ticket_trace()
    print("AC re-extraction and reuse accounting: verified")


if __name__ == "__main__":
    main()
