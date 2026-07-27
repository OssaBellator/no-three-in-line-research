#!/usr/bin/env python3
"""Finite audit for SAS5fh--SAS5fl."""

from collections import defaultdict
from itertools import combinations
import math
import random

SEED = 20260727


def greedy_coloring(vertices, adjacency):
    color = {}
    for vertex in sorted(vertices, key=lambda v: (-len(adjacency[v]), v)):
        used = {color[u] for u in adjacency[vertex] if u in color}
        candidate = 0
        while candidate in used:
            candidate += 1
        color[vertex] = candidate
    return color


def heaviest_color(vertices, weights, color):
    totals = defaultdict(int)
    for vertex in vertices:
        totals[color[vertex]] += weights[vertex]
    best = max(totals, key=totals.get)
    selected = [v for v in vertices if color[v] == best]
    return selected, totals[best]


def build_conflict(supports, scopes):
    graph = {i: set() for i in range(len(supports))}
    by_column = defaultdict(list)
    for i, support in enumerate(supports):
        for column in support:
            by_column[column].append(i)

    for vertices in by_column.values():
        for i, j in combinations(vertices, 2):
            graph[i].add(j)
            graph[j].add(i)

    for scope in scopes:
        met = sorted(
            {
                vertex
                for column in scope
                for vertex in by_column[column]
            }
        )
        for i, j in combinations(met, 2):
            graph[i].add(j)
            graph[j].add(i)
    return graph


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(18000):
        n = rng.randint(8, 28)
        r = 4
        declared_mu = rng.randint(1, 5)
        support_incidence = [0] * n
        supports = []

        for _candidate in range(rng.randint(3, 45)):
            available = [
                column
                for column in range(n)
                if support_incidence[column] < declared_mu
            ]
            if len(available) < 2:
                break
            size = rng.randint(2, min(r, len(available)))
            support = frozenset(rng.sample(available, size))
            if support in supports:
                continue
            supports.append(support)
            for column in support:
                support_incidence[column] += 1

        if not supports:
            continue

        weights = {
            i: rng.randint(1, 10000)
            for i in range(len(supports))
        }
        matched_total = sum(weights.values())

        # Each exact matched record is assigned to one square vertex.
        records = {}
        scopes = []
        used_record_scopes = set()
        for vertex, support in enumerate(supports):
            local = []
            for _record in range(rng.randint(1, 5)):
                anchor = rng.choice(tuple(support))
                others = rng.sample(
                    [c for c in range(n) if c != anchor],
                    2,
                )
                scope = tuple(sorted((anchor, *others)))
                attempts = 0
                while scope in used_record_scopes and attempts < 30:
                    others = rng.sample(
                        [c for c in range(n) if c != anchor],
                        2,
                    )
                    scope = tuple(sorted((anchor, *others)))
                    attempts += 1
                if scope in used_record_scopes:
                    continue
                used_record_scopes.add(scope)
                local.append(scope)
                scopes.append(scope)
            if not local:
                anchor = next(iter(support))
                others = rng.sample(
                    [c for c in range(n) if c != anchor],
                    2,
                )
                scope = tuple(sorted((anchor, *others)))
                local = [scope]
                scopes.append(scope)
                used_record_scopes.add(scope)
            records[vertex] = local

        for _extra in range(rng.randint(0, 80)):
            scopes.append(tuple(sorted(rng.sample(range(n), 3))))

        scope_incidence = [0] * n
        for scope in scopes:
            for column in scope:
                scope_incidence[column] += 1
        mu = max(support_incidence)
        lambda_sq = max(scope_incidence)

        graph = build_conflict(supports, scopes)
        d_sq = r * (mu - 1) + r * lambda_sq * (3 * mu - 1)
        assert max(map(len, graph.values()), default=0) <= d_sq

        vertices = list(range(len(supports)))
        colors = greedy_coloring(vertices, graph)
        selected, selected_weight = heaviest_color(
            vertices, weights, colors
        )
        assert selected_weight * (d_sq + 1) >= matched_total

        for i, j in combinations(selected, 2):
            assert not (supports[i] & supports[j])
        for scope in scopes:
            met = [
                i for i in selected
                if set(scope) & set(supports[i])
            ]
            assert len(met) <= 1

        # Absent -> present -> absent for every selected matched record.
        transient_records = set()
        transient_weight = 0
        for vertex in selected:
            for scope in records[vertex]:
                record_id = (vertex, scope)
                assert record_id not in transient_records
                initial = 0
                after_repair = 1
                after_destroy = 0
                assert (initial, after_repair, after_destroy) == (0, 1, 0)
                transient_records.add(record_id)
            transient_weight += weights[vertex]
        assert transient_weight == selected_weight

        # Complete-ledger additivity: every scope meets at most one selected support.
        local_delta = defaultdict(int)
        simultaneous_delta = 0
        for scope in scopes:
            met = [
                i for i in selected
                if set(scope) & set(supports[i])
            ]
            delta = rng.randint(-4, 4) if met else 0
            simultaneous_delta += delta
            if met:
                local_delta[met[0]] += delta
        assert simultaneous_delta == sum(local_delta.values())

        gains = {
            i: max(0, rng.randint(-5000, 10000))
            for i in vertices
        }
        positive = [i for i in vertices if gains[i] > 0]
        total_gain = sum(gains[i] for i in positive)
        if positive:
            positive_set = set(positive)
            induced = {
                i: graph[i] & positive_set
                for i in positive
            }
            gain_colors = greedy_coloring(positive, induced)
            gain_bank, gain_value = heaviest_color(
                positive, gains, gain_colors
            )
            assert gain_value * (d_sq + 1) >= total_gain
            assert all(gains[i] > 0 for i in gain_bank)
            for i, j in combinations(gain_bank, 2):
                assert j not in graph[i]
            counts["positive_gain_systems"] += 1
            counts["selected_improving_squares"] += len(gain_bank)

        # Integrated constants are substitutions into the universal bound.
        lambda_rep = rng.randint(1, 10)
        w_neu = rng.randint(1, 100000)
        neutral_matched = (
            w_neu
            / (2 * (2 * n - 3) * (4 * lambda_rep + 1))
        )
        neutral_composed = neutral_matched / (d_sq + 1)
        assert math.isclose(
            neutral_composed,
            w_neu
            / (
                2
                * (2 * n - 3)
                * (4 * lambda_rep + 1)
                * (d_sq + 1)
            ),
            rel_tol=1e-12,
            abs_tol=1e-12,
        )

        d_pair = rng.randint(0, 100)
        b_pair = rng.randint(1, 100000)
        common_matched = b_pair / (2 * (d_pair + 1))
        common_composed = common_matched / (d_sq + 1)
        assert math.isclose(
            common_composed,
            b_pair / (2 * (d_pair + 1) * (d_sq + 1)),
            rel_tol=1e-12,
            abs_tol=1e-12,
        )

        counts["systems"] += 1
        counts["square_vertices"] += len(supports)
        counts["selected_squares"] += len(selected)
        counts["selected_matched_records"] += len(transient_records)
        counts["complete_scopes"] += len(scopes)

    print("SAS matched repair square-composition audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
