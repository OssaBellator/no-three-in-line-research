#!/usr/bin/env python3
"""Finite checks for GC2ag--GC2ak."""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from itertools import combinations
from random import Random


def all_subsets(items: tuple[int, ...]):
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def hall_holds(demands, eligible, capacities):
    events = tuple(range(len(demands)))
    for subset in all_subsets(events):
        demand = sum((demands[j] for j in subset), Fraction(0))
        resources = set().union(*(eligible[j] for j in subset)) if subset else set()
        capacity = sum((capacities[p] for p in resources), Fraction(0))
        if demand > capacity:
            return False, subset
    return True, None


def max_flow_feasible(demands, eligible, capacities):
    event_count = len(demands)
    resource_count = len(capacities)
    source = event_count + resource_count
    sink = source + 1
    graph = [[] for _ in range(sink + 1)]
    cap = {}

    def add_edge(u, v, capacity):
        graph[u].append(v)
        graph[v].append(u)
        cap[(u, v)] = cap.get((u, v), Fraction(0)) + capacity
        cap.setdefault((v, u), Fraction(0))

    total = sum(demands, Fraction(0))
    inf = total + sum(capacities, Fraction(0)) + 1
    for j, demand in enumerate(demands):
        add_edge(source, j, demand)
        for p in eligible[j]:
            add_edge(j, event_count + p, inf)
    for p, capacity in enumerate(capacities):
        add_edge(event_count + p, sink, capacity)

    flow = Fraction(0)
    while True:
        parent = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            u = queue.popleft()
            for v in graph[u]:
                if v not in parent and cap[(u, v)] > 0:
                    parent[v] = u
                    queue.append(v)
        if sink not in parent:
            break
        aug = None
        v = sink
        while v != source:
            u = parent[v]
            aug = cap[(u, v)] if aug is None else min(aug, cap[(u, v)])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            cap[(u, v)] -= aug
            cap[(v, u)] += aug
            v = u
        flow += aug
    return flow == total


def normalization_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(40000):
        count = rng.randint(1, 14)
        capacities = [Fraction(rng.randint(1, 20), rng.randint(1, 6)) for _ in range(count)]
        ratios = [Fraction(rng.randint(1, 30), rng.randint(1, 5)) for _ in range(count)]
        excesses = [capacities[i] * ratios[i] for i in range(count)]
        total = sum(excesses, Fraction(0))
        bound = max(Fraction(1), max(ratios))
        paid = sum((e / bound for e in excesses), Fraction(0))
        assert all(excesses[i] / bound <= capacities[i] for i in range(count))
        assert paid == total / bound
        counts["bounded-ratio systems"] += 1

        theta = Fraction(rng.randint(1, 10), 1)
        moderate = [i for i in range(count) if excesses[i] <= theta * capacities[i]]
        heavy = [i for i in range(count) if i not in moderate]
        e_m = sum((excesses[i] for i in moderate), Fraction(0))
        e_h = sum((excesses[i] for i in heavy), Fraction(0))
        assert e_m + e_h == total
        if e_m * 2 >= total:
            assert sum((excesses[i] / theta for i in moderate), Fraction(0)) * 2 * theta >= total
            assert all(excesses[i] / theta <= capacities[i] for i in moderate)
        else:
            assert e_h * 2 > total
            assert all(excesses[i] > theta * capacities[i] for i in heavy)
        counts["threshold routers"] += 1


def weighted_hall_checks(counts: Counter[str]) -> None:
    rng = Random(811)
    for _ in range(5000):
        event_count = rng.randint(1, 6)
        resource_count = rng.randint(1, 6)
        # Integral samples are rational systems with common denominator one and
        # keep the exact max-flow audit fast.
        capacities = [Fraction(rng.randint(0, 12), 1) for _ in range(resource_count)]
        demands = [Fraction(rng.randint(0, 10), 1) for _ in range(event_count)]
        eligible = []
        for _event in range(event_count):
            neighbours = {p for p in range(resource_count) if rng.randrange(3) != 0}
            if not neighbours:
                neighbours.add(rng.randrange(resource_count))
            eligible.append(neighbours)
        hall, witness = hall_holds(demands, eligible, capacities)
        feasible = max_flow_feasible(demands, eligible, capacities)
        assert hall == feasible
        if not hall:
            assert witness is not None
            demand = sum((demands[j] for j in witness), Fraction(0))
            resources = set().union(*(eligible[j] for j in witness))
            capacity = sum((capacities[p] for p in resources), Fraction(0))
            assert demand > capacity
            counts["weighted Hall deficits"] += 1
        else:
            counts["weighted Hall payments"] += 1
        counts["weighted event systems"] += 1


def singleton_factor_checks(counts: Counter[str]) -> None:
    rng = Random(17)
    for _ in range(10000):
        count = rng.randint(1, 15)
        ratio = Fraction(rng.randint(1, 12), 1)
        capacities = [Fraction(rng.randint(1, 20), rng.randint(1, 5)) for _ in range(count)]
        excesses = [capacity * Fraction(rng.randint(0, int(ratio)), 1) for capacity in capacities]
        demands = [excess / ratio for excess in excesses]
        eligible = [{i} for i in range(count)]
        hall, witness = hall_holds(demands, eligible, capacities)
        assert hall and witness is None
        assert max_flow_feasible(demands, eligible, capacities)
        counts["singleton normalized systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    normalization_checks(counts)
    weighted_hall_checks(counts)
    singleton_factor_checks(counts)
    print("GC2ag--GC2ak excess normalization/weighted Hall audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
