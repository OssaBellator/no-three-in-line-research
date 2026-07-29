#!/usr/bin/env python3
"""Deterministic audit for AC5jj--AC5jo."""

from __future__ import annotations

from collections import defaultdict, deque
import random

SEED = 20260801
SYSTEMS = 2500


def topological_order(vertex_count: int, edges: list[list[int]]) -> list[int] | None:
    indegree = [0] * vertex_count
    for source in range(vertex_count):
        for target in edges[source]:
            indegree[target] += 1

    queue = deque(sorted(index for index, degree in enumerate(indegree) if degree == 0))
    order: list[int] = []
    while queue:
        source = queue.popleft()
        order.append(source)
        for target in sorted(edges[source]):
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return order if len(order) == vertex_count else None


def extend_rank(
    old_ranks: list[int],
    edges: list[list[int]],
    rank_cap: int,
) -> tuple[str, object, object]:
    old_count = len(old_ranks)
    order = topological_order(len(edges), edges)
    if order is None:
        return ("cycle", None, None)

    ranks: list[int | None] = [None] * len(edges)
    for index, rank in enumerate(old_ranks):
        ranks[index] = rank

    for source in reversed(order):
        required = max(
            (int(ranks[target]) + 1 for target in edges[source]),
            default=0,
        )
        if source < old_count:
            assert ranks[source] is not None
            if int(ranks[source]) < required:
                return ("old_violation", source, required)
        else:
            ranks[source] = required
            if required > rank_cap:
                return ("cap", source, required)

    final_ranks = [int(rank) for rank in ranks]
    for source in range(len(edges)):
        for target in edges[source]:
            assert final_ranks[source] > final_ranks[target]
    return ("ok", final_ranks, max(final_ranks))


def verify() -> dict[str, int]:
    rng = random.Random(SEED)
    totals: defaultdict[str, int] = defaultdict(int)

    for system_index in range(SYSTEMS):
        route_class = system_index % 4
        old_count = rng.randint(2, 6)
        shell_count = max(rng.randint(1, 5), 2 if route_class == 1 else 1)
        vertex_count = old_count + shell_count
        rank_cap = rng.randint(4, 12)
        old_ranks = [rng.randint(1, rank_cap) for _ in range(old_count)]
        edge_sets: list[set[int]] = [set() for _ in range(vertex_count)]

        if route_class == 0:
            hidden_ranks = old_ranks + [
                rng.randint(0, rank_cap) for _ in range(shell_count)
            ]
            for source in range(vertex_count):
                for target in range(vertex_count):
                    if (
                        source != target
                        and hidden_ranks[source] > hidden_ranks[target]
                        and rng.random() < 0.10
                    ):
                        edge_sets[source].add(target)
            result = extend_rank(
                old_ranks,
                [sorted(targets) for targets in edge_sets],
                rank_cap,
            )
            assert result[0] == "ok"
            totals["valid_extensions"] += 1
            totals["new_states"] += shell_count
            totals["maximum_rank_sum"] += int(result[2])

        elif route_class == 1:
            first = old_count
            second = old_count + 1
            edge_sets[first].add(second)
            edge_sets[second].add(first)
            result = extend_rank(
                old_ranks,
                [sorted(targets) for targets in edge_sets],
                rank_cap,
            )
            assert result[0] == "cycle"
            totals["progress_cycles"] += 1

        elif route_class == 2:
            edge_sets = [set() for _ in range(vertex_count)]
            old_ranks[0] = 1
            old_ranks[1] = 0
            shell_vertex = old_count
            edge_sets[shell_vertex].add(1)
            edge_sets[0].add(shell_vertex)
            result = extend_rank(
                old_ranks,
                [sorted(targets) for targets in edge_sets],
                rank_cap,
            )
            assert result[0] == "old_violation"
            totals["old_rank_violations"] += 1

        else:
            edge_sets = [set() for _ in range(vertex_count)]
            old_ranks[0] = rank_cap
            shell_vertex = old_count
            edge_sets[shell_vertex].add(0)
            result = extend_rank(
                old_ranks,
                [sorted(targets) for targets in edge_sets],
                rank_cap,
            )
            assert result[0] == "cap"
            totals["rank_cap_failures"] += 1

        # AC5jl bounded integer stabilization.
        component_caps = [rng.randint(2, 12) for _ in range(6)]
        component_values = [0] * 6
        strict_increases = 0
        for _level in range(rng.randint(3, 8)):
            for index, cap in enumerate(component_caps):
                if rng.random() < 0.35 and component_values[index] < cap:
                    component_values[index] += rng.randint(
                        1, cap - component_values[index]
                    )
                    strict_increases += 1
            assert all(
                component_values[index] <= component_caps[index]
                for index in range(6)
            )
        assert strict_increases <= sum(component_caps)
        totals["strict_component_increases"] += strict_increases
        totals["component_cap_sum"] += sum(component_caps)

        # AC5jm finite global address quotient.
        stocks = [rng.randint(0, 8) for _ in range(rng.randint(1, 8))]
        global_total = sum(stocks)
        selected = {
            index for index in range(len(stocks)) if rng.random() < 0.65
        }
        selected_total = sum(stocks[index] for index in selected)
        raw_total = selected_total + sum(
            stocks[index] for index in selected if rng.random() < 0.45
        )
        assert selected_total <= global_total
        assert raw_total >= selected_total
        totals["global_stock"] += global_total
        totals["selected_stock"] += selected_total
        totals["alias_removed"] += raw_total - selected_total
        totals["systems"] += 1

    expected = {
        "valid_extensions": 625,
        "new_states": 1908,
        "maximum_rank_sum": 4168,
        "strict_component_increases": 22790,
        "component_cap_sum": 105505,
        "global_stock": 44332,
        "selected_stock": 28435,
        "alias_removed": 12766,
        "systems": 2500,
        "progress_cycles": 625,
        "old_rank_violations": 625,
        "rank_cap_failures": 625,
    }
    result = dict(totals)
    assert result == expected
    return result


if __name__ == "__main__":
    result = verify()
    for key, value in result.items():
        print(f"{key}: {value}")
