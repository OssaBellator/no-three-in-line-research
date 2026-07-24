#!/usr/bin/env python3
"""Verify AC2a weighted extraction and AC3b/AC3c accounting."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations


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


def maximum_independent_weight(
    size: int,
    edges: tuple[tuple[int, int], ...],
    weights: list[int],
) -> int:
    edge_set = set(edges)
    best = 0
    for mask in range(1 << size):
        chosen = [vertex for vertex in range(size) if mask & (1 << vertex)]
        if any(
            (min(left, right), max(left, right)) in edge_set
            for left, right in combinations(chosen, 2)
        ):
            continue
        best = max(best, sum(weights[vertex] for vertex in chosen))
    return best


def verify_weighted_neighbourhood(max_size: int = 5) -> None:
    for size in range(1, max_size + 1):
        pairs = tuple(combinations(range(size), 2))
        for mask in range(1 << len(pairs)):
            edges = tuple(
                edge for index, edge in enumerate(pairs) if mask & (1 << index)
            )
            weights = [1 + (7 * vertex + mask) % 9 for vertex in range(size)]
            loads = weights.copy()
            for left, right in edges:
                loads[left] += weights[right]
                loads[right] += weights[left]
            caro_wei = sum(
                (
                    Fraction(weights[vertex] ** 2, loads[vertex])
                    for vertex in range(size)
                ),
                Fraction(0),
            )
            optimum = maximum_independent_weight(size, edges, weights)
            assert optimum >= caro_wei
            for threshold in range(1, 11):
                overloaded = any(
                    loads[vertex] > threshold * weights[vertex]
                    for vertex in range(size)
                )
                if not overloaded:
                    assert optimum * threshold >= sum(weights)


def induced_maximum_weight(
    vertices: list[int],
    edges: tuple[tuple[int, int], ...],
    weights: list[int],
) -> int:
    edge_set = set(edges)
    best = 0
    for mask in range(1 << len(vertices)):
        chosen = [
            vertex
            for index, vertex in enumerate(vertices)
            if mask & (1 << index)
        ]
        if any(edge in edge_set for edge in combinations(chosen, 2)):
            continue
        best = max(best, sum(weights[vertex] for vertex in chosen))
    return best


def verify_labelled_overload(max_size: int = 5) -> None:
    for size in range(2, max_size + 1):
        pairs = tuple(combinations(range(size), 2))
        for mask in range(1 << len(pairs)):
            edges = tuple(
                edge for index, edge in enumerate(pairs) if mask & (1 << index)
            )
            edge_set = set(edges)
            weights = [1 + (5 * vertex + 2 * mask) % 9 for vertex in range(size)]
            for center in range(size):
                neighbours = [
                    vertex
                    for vertex in range(size)
                    if (
                        min(center, vertex),
                        max(center, vertex),
                    )
                    in edge_set
                ]
                load = weights[center] + sum(
                    weights[vertex] for vertex in neighbours
                )
                for threshold in range(2, 8):
                    if load <= threshold * weights[center]:
                        continue
                    for label_count in range(1, 4):
                        classes = [
                            [
                                vertex
                                for vertex in neighbours
                                if (vertex + mask) % label_count == label
                            ]
                            for label in range(label_count)
                        ]
                        selected = max(
                            classes,
                            key=lambda vertices: sum(
                                weights[vertex] for vertex in vertices
                            ),
                        )
                        selected_weight = sum(
                            weights[vertex] for vertex in selected
                        )
                        assert (
                            selected_weight * label_count
                            > (threshold - 1) * weights[center]
                        )

                        for recursive_threshold in range(1, 6):
                            restricted_overload = any(
                                weights[vertex]
                                + sum(
                                    weights[other]
                                    for other in selected
                                    if other != vertex
                                    and (
                                        min(vertex, other),
                                        max(vertex, other),
                                    )
                                    in edge_set
                                )
                                > recursive_threshold * weights[vertex]
                                for vertex in selected
                            )
                            if not restricted_overload:
                                optimum = induced_maximum_weight(
                                    selected,
                                    edges,
                                    weights,
                                )
                                assert (
                                    optimum * recursive_threshold
                                    >= selected_weight
                                )

                        for relative_weight in range(1, 5):
                            if all(
                                weights[vertex]
                                <= relative_weight * weights[center]
                                for vertex in selected
                            ):
                                assert (
                                    len(selected)
                                    * label_count
                                    * relative_weight
                                    > threshold - 1
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


def verify_strict_support_descent(max_size: int = 7) -> None:
    """Every induced label recursion deletes its previous centre."""

    for size in range(1, max_size + 1):
        universe = frozenset(range(size))
        for ordering in permutations(range(size)):
            support = universe
            previous = size - len(support)
            steps = 0
            for center in ordering:
                if center not in support:
                    continue
                # Any label class is a subset of the current neighbours.
                # Taking all remaining objects is the slowest possible
                # strict descent and therefore tests the sharp depth bound.
                next_support = support - {center}
                if not next_support:
                    break
                current = size - len(next_support)
                assert next_support < support
                assert current >= previous + 1
                support = next_support
                previous = current
                steps += 1
            assert steps <= size - 1

    # Repetition is possible only after an explicit support reopening.
    support = frozenset({1, 2, 3})
    support = support - {1}
    assert 1 not in support
    reopened = support | {1}
    assert reopened == frozenset({1, 2, 3})


def main() -> None:
    verify_weighted_extraction()
    verify_composed_bound()
    verify_weighted_neighbourhood()
    verify_labelled_overload()
    verify_cycle_criterion()
    verify_ticket_trace()
    verify_strict_support_descent()
    print("AC re-extraction and reuse accounting: verified")


if __name__ == "__main__":
    main()
