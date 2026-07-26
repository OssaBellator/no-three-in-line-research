#!/usr/bin/env python3
"""Finite checks for GC2ba--GC2bf."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from random import Random


def edge_coloring(edges: list[tuple[int, int]], delta: int) -> list[int]:
    colors: list[int] = []
    for i, edge in enumerate(edges):
        forbidden = {
            colors[j]
            for j in range(i)
            if edge[0] in edges[j] or edge[1] in edges[j]
        }
        color = 0
        while color in forbidden:
            color += 1
        assert color < 2 * delta - 1
        colors.append(color)
    return colors


def one_system(rng: Random, counts: Counter[str]) -> None:
    d = rng.randint(1, 18)
    u = Fraction(rng.randint(1, 60), rng.randint(1, 8))
    theta = rng.randint(1, 8)
    rank_cap = rng.randint(1, 5)
    value = u / d

    capacities: list[Fraction] = []
    sides: list[int] = []
    ranks: list[int] = []
    edges: list[tuple[int, int] | None] = []

    for _ in range(d):
        mode = rng.randrange(6)
        if mode == 0:
            capacity = Fraction(0)
        elif mode <= 2:
            capacity = value / (theta * rng.randint(2, 5))
        else:
            capacity = value * rng.randint(1, 5) / theta
        capacities.append(capacity)
        sides.append(rng.randrange(2))
        rank = rng.randint(1, rank_cap)
        ranks.append(rank)
        if rank == 3:
            x = rng.randint(0, 8)
            y = rng.randint(0, 8)
            while y == x:
                y = rng.randint(0, 8)
            edges.append((min(x, y), max(x, y)))
        else:
            edges.append(None)

    moderate = [p for p, capacity in enumerate(capacities) if capacity >= value / theta]
    high = [p for p in range(d) if p not in moderate]

    if len(moderate) * 2 >= d:
        paid = len(moderate) * value / theta
        assert paid >= u / (2 * theta)
        assert all(value / theta <= capacities[p] for p in moderate)
        counts["moderate payment systems"] += 1
        return

    assert len(high) * 2 > d
    assert len(high) * value > u / 2
    counts["high-ratio systems"] += 1

    zero = [p for p in high if capacities[p] == 0]
    if zero:
        counts["zero-capacity outputs"] += 1
        return

    assert all(value / capacities[p] > theta for p in high)

    by_side: dict[int, list[int]] = defaultdict(list)
    for p in high:
        by_side[sides[p]].append(p)
    chosen_side = max(by_side, key=lambda side: len(by_side[side]))
    side_family = by_side[chosen_side]
    assert len(side_family) * value > u / 4
    counts["deleted-cell families"] += 1

    by_rank: dict[int, list[int]] = defaultdict(list)
    for p in side_family:
        by_rank[ranks[p]].append(p)
    chosen_rank = max(by_rank, key=lambda rank: len(by_rank[rank]))
    family = by_rank[chosen_rank]
    weight = len(family) * value
    assert weight > u / (4 * rank_cap)
    counts["rank-localized families"] += 1

    if chosen_rank != 3:
        counts["lower-rank outputs"] += 1
        return

    delta = rng.randint(1, 5)
    link_edges = [edges[p] for p in family]
    assert all(edge is not None for edge in link_edges)
    typed_edges = [edge for edge in link_edges if edge is not None]
    degree: Counter[int] = Counter()
    for x, y in typed_edges:
        degree[x] += 1
        degree[y] += 1

    if degree and max(degree.values()) > delta:
        counts["pair-codegree outputs"] += 1
        return

    colors = edge_coloring(typed_edges, delta)
    classes: dict[int, list[int]] = defaultdict(list)
    for local_index, color in enumerate(colors):
        classes[color].append(family[local_index])
    selected = max(classes.values(), key=len)

    for i, p in enumerate(selected):
        for q in selected[i + 1 :]:
            assert set(edges[p]) .isdisjoint(set(edges[q]))  # type: ignore[arg-type]

    selected_weight = len(selected) * value
    assert selected_weight >= weight / (2 * delta - 1)
    assert selected_weight > u / (4 * rank_cap * (2 * delta - 1))
    selected_capacity = sum(capacities[p] for p in selected)
    assert selected_capacity < selected_weight / theta
    counts["endpoint-disjoint stars"] += 1
    counts["star factor occurrences"] += len(selected)


def exhaustive_thresholds(counts: Counter[str]) -> None:
    for d in range(1, 9):
        for moderate_count in range(d + 1):
            u = Fraction(12, 1)
            theta = 3
            value = u / d
            capacities = [value / theta] * moderate_count + [value / (2 * theta)] * (d - moderate_count)
            moderate = [capacity for capacity in capacities if capacity >= value / theta]
            if len(moderate) * 2 >= d:
                assert len(moderate) * value / theta >= u / (2 * theta)
            else:
                assert (d - len(moderate)) * value > u / 2
            counts["exhaustive threshold splits"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_thresholds(counts)
    rng = Random(20260726)
    for _ in range(80000):
        one_system(rng, counts)
    print("GC2ba--GC2bf event-local high-ratio audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
