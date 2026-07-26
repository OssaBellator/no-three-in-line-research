#!/usr/bin/env python3
"""Finite checks for GC2aq--GC2au."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from random import Random


def all_subsets(items: tuple[int, ...]):
    for size in range(1, len(items) + 1):
        yield from combinations(items, size)


def canonical_minimal_core(demands, eligible, capacities):
    events = tuple(range(len(demands)))
    deficient = []
    for subset in all_subsets(events):
        resources = set().union(*(eligible[j] for j in subset))
        delta = sum((demands[j] for j in subset), Fraction(0)) - sum(
            (capacities[p] for p in resources), Fraction(0)
        )
        if delta > 0:
            deficient.append((subset, delta))
    if not deficient:
        return None
    inclusion_minimal = []
    deficient_sets = {frozenset(subset) for subset, _ in deficient}
    for subset, delta in deficient:
        fset = frozenset(subset)
        if not any(other < fset for other in deficient_sets):
            inclusion_minimal.append((subset, delta))
    min_size = min(len(subset) for subset, _ in inclusion_minimal)
    return min((item for item in inclusion_minimal if len(item[0]) == min_size), key=lambda x: x[0])


def canonical_role(event, support):
    b, u = event
    roles = []
    if b in support:
        roles.append((0, b))  # target
    if u in support:
        roles.append((1, u))  # partner
    assert roles
    return min(roles)


def conflict(event_a, event_b):
    b1, u1 = event_a
    b2, u2 = event_b
    return b1 == b2 or u1 == u2


def role_stock_checks(counts: Counter[str]) -> None:
    rng = Random(31415)
    for _ in range(40000):
        rank = rng.randint(1, 5)
        support = set(rng.sample(range(30), rank))
        events = []
        for _event in range(rng.randint(1, 20)):
            q = rng.choice(tuple(support))
            if rng.randrange(2) == 0:
                events.append((q, rng.randrange(30, 60)))
            else:
                events.append((rng.randrange(60, 90), q))
        groups = defaultdict(list)
        for event in events:
            groups[canonical_role(event, support)].append(event)
        assert len(groups) <= 2 * rank
        for role, fibre in groups.items():
            side, q = role
            for event in fibre:
                assert (event[0] if side == 0 else event[1]) == q
            for a, b in combinations(fibre, 2):
                assert conflict(a, b)
        counts["role-stock systems"] += 1
        counts["role fibres"] += len(groups)


def weighted_core_checks(counts: Counter[str]) -> None:
    rng = Random(271828)
    for _ in range(35000):
        event_count = rng.randint(1, 6)
        # Use disjoint target and partner label ranges.
        targets = rng.sample(range(0, 12), event_count)
        partners = rng.sample(range(20, 32), event_count)
        events = list(zip(targets, partners))

        resource_count = rng.randint(1, 7)
        supports = []
        capacities = []
        max_rank = 1
        for _p in range(resource_count):
            rank = rng.randint(1, 3)
            max_rank = max(max_rank, rank)
            supports.append(set(rng.sample(targets + partners, min(rank, len(targets + partners)))))
            capacities.append(Fraction(rng.randint(0, 8), rng.randint(1, 3)))

        eligible = []
        for event in events:
            neighbours = {
                p for p, support in enumerate(supports) if event[0] in support or event[1] in support
            }
            if not neighbours:
                # Add an occurrence-faithful singleton resource.
                supports.append({event[0]})
                capacities.append(Fraction(rng.randint(0, 4), 1))
                neighbours.add(len(supports) - 1)
                resource_count += 1
            eligible.append(neighbours)

        demands = [Fraction(rng.randint(1, 10), rng.randint(1, 3)) for _ in events]
        core = canonical_minimal_core(demands, eligible, capacities)
        if core is None:
            counts["payable systems"] += 1
            continue

        subset, delta = core
        X = set(subset)
        neighbourhood = set().union(*(eligible[j] for j in X))
        private = {}
        private_union = set()
        for j in X:
            other_neighbourhood = set().union(*(eligible[k] for k in X if k != j)) if len(X) > 1 else set()
            private[j] = neighbourhood - other_neighbourhood
            private_union.update(private[j])
        shared = neighbourhood - private_union
        uncovered = {
            j: demands[j] - sum((capacities[p] for p in private[j]), Fraction(0)) for j in X
        }
        assert all(value >= delta for value in uncovered.values())

        if len(X) == 1:
            counts["singleton cores"] += 1
            continue

        assert shared
        total_uncovered = sum(uncovered.values(), Fraction(0))
        incidence = defaultdict(Fraction)
        for j in X:
            shared_j = eligible[j] & shared
            assert shared_j
            share = uncovered[j] / len(shared_j)
            for p in shared_j:
                role = canonical_role(events[j], supports[p])
                incidence[(p, role, j)] += share

        by_resource_role = defaultdict(Fraction)
        fibre_events = defaultdict(list)
        for (p, role, j), weight in incidence.items():
            by_resource_role[(p, role)] += weight
            fibre_events[(p, role)].append((j, weight))

        best_key, best_weight = max(by_resource_role.items(), key=lambda item: item[1])
        M = len(shared)
        assert best_weight >= total_uncovered / (2 * max_rank * M)
        p, role = best_key
        fibre = fibre_events[best_key]
        for (j1, _), (j2, _) in combinations(fibre, 2):
            assert conflict(events[j1], events[j2])

        gamma = rng.randint(0, 5)
        if len(fibre) > gamma + 1:
            assert all(len(fibre) - 1 > gamma for _j, _w in fibre)
            counts["same-cell conflict overloads"] += 1
        else:
            heavy = max(weight for _j, weight in fibre)
            assert heavy >= best_weight / (gamma + 1)
            assert heavy >= len(X) * delta / (2 * max_rank * M * (gamma + 1))
            counts["heavy event incidences"] += 1
        counts["deficient physical cores"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    role_stock_checks(counts)
    weighted_core_checks(counts)
    print("GC2aq--GC2au physical Hall role-clique audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
