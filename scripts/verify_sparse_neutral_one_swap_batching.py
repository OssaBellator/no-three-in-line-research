#!/usr/bin/env python3
"""Finite audit for SAS5ex--SAS5fb."""

from collections import defaultdict
from itertools import combinations
import random

SEED = 20260727


def greedy_coloring(vertices, adjacency):
    color = {}
    for vertex in sorted(vertices, key=lambda x: len(adjacency[x]), reverse=True):
        used = {color[other] for other in adjacency[vertex] if other in color}
        candidate = 0
        while candidate in used:
            candidate += 1
        color[vertex] = candidate
    return color


def heaviest_color(vertices, weights, color):
    totals = defaultdict(float)
    for vertex in vertices:
        totals[color[vertex]] += weights[vertex]
    best = max(totals, key=totals.get)
    return [vertex for vertex in vertices if color[vertex] == best], totals[best]


def interaction_graph(vertices, operations, scopes):
    graph = {i: set() for i in vertices}
    for i, j in combinations(vertices, 2):
        endpoints_i = set(operations[i])
        endpoints_j = set(operations[j])
        if any(
            endpoints_i & set(scope) and endpoints_j & set(scope)
            for scope in scopes
        ):
            graph[i].add(j)
            graph[j].add(i)
    return graph


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(30000):
        n = rng.randint(6, 26)
        all_swaps = list(combinations(range(n), 2))
        operation_count = rng.randint(2, min(len(all_swaps), 45))
        operations = rng.sample(all_swaps, operation_count)

        exact_records = {}
        used_scopes = set()
        for operation_id, endpoints in enumerate(operations):
            local = []
            for _ in range(rng.randint(1, 5)):
                anchor = rng.choice(endpoints)
                others = rng.sample([z for z in range(n) if z != anchor], 2)
                scope = tuple(sorted((anchor, *others)))
                attempts = 0
                while scope in used_scopes and attempts < 30:
                    others = rng.sample([z for z in range(n) if z != anchor], 2)
                    scope = tuple(sorted((anchor, *others)))
                    attempts += 1
                if scope in used_scopes:
                    continue
                used_scopes.add(scope)
                local.append((scope, rng.randint(1, 10000)))
            if not local:
                anchor = endpoints[0]
                others = rng.sample([z for z in range(n) if z != anchor], 2)
                scope = tuple(sorted((anchor, *others)))
                local = [(scope, rng.randint(1, 10000))]
                used_scopes.add(scope)
            exact_records[operation_id] = local

        weights = {
            operation_id: sum(weight for _, weight in exact_records[operation_id])
            for operation_id in range(operation_count)
        }
        total_weight = sum(weights.values())

        overlap = {i: set() for i in range(operation_count)}
        for i, j in combinations(range(operation_count), 2):
            if set(operations[i]) & set(operations[j]):
                overlap[i].add(j)
                overlap[j].add(i)
        assert max(map(len, overlap.values()), default=0) <= 2 * n - 4
        first_colors = greedy_coloring(range(operation_count), overlap)
        first_bank, first_weight = heaviest_color(
            range(operation_count), weights, first_colors
        )
        assert first_weight * (2 * n - 3) >= total_weight
        for i, j in combinations(first_bank, 2):
            assert not (set(operations[i]) & set(operations[j]))

        scopes = [
            scope
            for records in exact_records.values()
            for scope, _ in records
        ]
        for _ in range(rng.randint(0, 80)):
            scopes.append(tuple(sorted(rng.sample(range(n), 3))))

        incidence = [0] * n
        for scope in scopes:
            for column in scope:
                incidence[column] += 1
        lam = max(incidence)

        interaction = interaction_graph(first_bank, operations, scopes)
        assert max(map(len, interaction.values()), default=0) <= 4 * lam

        second_colors = greedy_coloring(first_bank, interaction)
        second_bank, second_weight = heaviest_color(
            first_bank, weights, second_colors
        )
        assert second_weight * (4 * lam + 1) >= first_weight

        for scope in scopes:
            met = [
                i
                for i in second_bank
                if set(scope) & set(operations[i])
            ]
            assert len(met) <= 1

        union_weight = 0
        selected_scopes = set()
        for operation_id in second_bank:
            for scope, weight in exact_records[operation_id]:
                assert scope not in selected_scopes
                selected_scopes.add(scope)
                union_weight += weight
                met = [
                    other
                    for other in second_bank
                    if set(scope) & set(operations[other])
                ]
                assert met == [operation_id]
        assert union_weight == second_weight

        single_sum = 0
        simultaneous = 0
        for scope in scopes:
            met = [
                i
                for i in second_bank
                if set(scope) & set(operations[i])
            ]
            delta = rng.randint(-3, 3) if met else 0
            single_sum += delta
            simultaneous += delta
        assert simultaneous == single_sum

        gains = {
            i: max(0, rng.randint(-5000, 10000))
            for i in range(operation_count)
        }
        positive = [i for i in range(operation_count) if gains[i] > 0]
        total_gain = sum(gains[i] for i in positive)
        if positive:
            positive_set = set(positive)
            overlap_positive = {
                i: overlap[i] & positive_set
                for i in positive
            }
            colors_gain_1 = greedy_coloring(positive, overlap_positive)
            gain_bank_1, gain_1 = heaviest_color(
                positive, gains, colors_gain_1
            )
            assert gain_1 * (2 * n - 3) >= total_gain
            for i, j in combinations(gain_bank_1, 2):
                assert not (set(operations[i]) & set(operations[j]))

            interaction_positive = interaction_graph(
                gain_bank_1, operations, scopes
            )
            assert max(
                map(len, interaction_positive.values()), default=0
            ) <= 4 * lam
            colors_gain_2 = greedy_coloring(
                gain_bank_1, interaction_positive
            )
            gain_bank_2, gain_2 = heaviest_color(
                gain_bank_1, gains, colors_gain_2
            )
            assert gain_2 * (4 * lam + 1) >= gain_1
            assert all(gains[i] > 0 for i in gain_bank_2)
            simultaneous_descent = sum(gains[i] for i in gain_bank_2)
            assert simultaneous_descent == gain_2
            counts["positive_gain_systems"] += 1
            counts["selected_improving_operations"] += len(gain_bank_2)

        declared_cap = rng.randint(1, max(1, lam + 3))
        if lam > declared_cap:
            assert max(incidence) > declared_cap
            counts["high_incidence_branches"] += 1
        else:
            counts["cap_respecting_systems"] += 1

        counts["systems"] += 1
        counts["operations"] += operation_count
        counts["selected_operations"] += len(second_bank)
        counts["selected_records"] += len(selected_scopes)

    print("SAS neutral one-swap batching audit passed")
    print(f"  operation systems: {counts['systems']}")
    print(f"  neutral creating operations: {counts['operations']}")
    print(f"  selected compatible operations: {counts['selected_operations']}")
    print(f"  selected exact records: {counts['selected_records']}")
    print(f"  positive-gain systems: {counts['positive_gain_systems']}")
    print(
        "  selected improving operations: "
        f"{counts['selected_improving_operations']}"
    )
    print(f"  cap-respecting systems: {counts['cap_respecting_systems']}")
    print(f"  high-incidence branches: {counts['high_incidence_branches']}")


if __name__ == "__main__":
    main()
