#!/usr/bin/env python3
"""Finite checks for GC2br--GC2bv."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from random import Random


def audit_system(
    weights: tuple[int, ...],
    gain: int,
    capacities: tuple[Fraction, ...],
    destroyed_count: int,
    roles: tuple[int, ...],
    r_star: Fraction,
    counts: Counter[str],
) -> None:
    dsum = sum(weights)
    assert 0 < gain <= dsum
    q = [Fraction(gain * weight, dsum) for weight in weights]
    q.extend(Fraction(0) for _ in range(len(capacities) - destroyed_count))
    assert sum(q) == gain
    assert all(Fraction(0) < q[i] <= weights[i] for i in range(destroyed_count))

    c_ext = sum(capacities)
    z_raw = sum(min(c, row) for c, row in zip(capacities, q))
    assert z_raw <= c_ext

    if z_raw >= r_star:
        if r_star > 0:
            allocation = [r_star * min(c, row) / z_raw for c, row in zip(capacities, q)]
            assert sum(allocation) == r_star
            assert all(x <= c and x <= row for x, c, row in zip(allocation, capacities, q))
            assert r_star <= sum(q) == gain
        counts["raw-row descent systems"] += 1
    elif c_ext < r_star:
        counts["ordinary Hall deficits"] += 1
    else:
        delta = r_star - z_raw
        u_free = sum(capacities[destroyed_count:])
        u_ratio = sum(max(capacities[i] - q[i], Fraction(0)) for i in range(destroyed_count))
        assert u_free + u_ratio == c_ext - z_raw
        assert u_free + u_ratio >= delta
        selected_indices = list(range(destroyed_count, len(capacities))) if u_free >= delta / 2 else list(range(destroyed_count))
        selected_mass = u_free if u_free >= delta / 2 else u_ratio
        assert selected_mass >= delta / 2

        by_role: dict[int, Fraction] = defaultdict(Fraction)
        fibre_sizes: dict[int, int] = defaultdict(int)
        occurrence_mass: list[Fraction] = []
        for i in selected_indices:
            mass = capacities[i] if i >= destroyed_count else max(capacities[i] - q[i], Fraction(0))
            by_role[roles[i]] += mass
            fibre_sizes[roles[i]] += 1
            occurrence_mass.append(mass)
        t_raw = len(set(roles))
        b_raw = max(fibre_sizes.values(), default=1)
        assert max(by_role.values(), default=Fraction(0)) * t_raw >= selected_mass
        assert max(occurrence_mass, default=Fraction(0)) * t_raw * b_raw >= selected_mass

        if u_free >= delta / 2:
            counts["source-free role systems"] += 1
        else:
            lam = Fraction(gain, dsum)
            assert any(capacities[i] > lam * weights[i] for i in range(destroyed_count))
            counts["ratio-overload role systems"] += 1

    counts["audited systems"] += 1
    counts["resource occurrences"] += len(capacities)


def exhaustive_systems(counts: Counter[str]) -> None:
    for destroyed_count in range(1, 4):
        for weights in product(range(1, 4), repeat=destroyed_count):
            dsum = sum(weights)
            for gain in range(1, dsum + 1):
                total_resources = destroyed_count + 1
                for cap_ints in product(range(3), repeat=total_resources):
                    capacities = tuple(Fraction(x) for x in cap_ints)
                    c_ext = sum(capacities)
                    for r_num in range(1, 4):
                        r_star = Fraction(r_num, 2)
                        roles = tuple(i % 2 for i in range(total_resources))
                        audit_system(weights, gain, capacities, destroyed_count, roles, r_star, counts)
                        counts["exhaustive systems"] += 1


def random_systems(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        destroyed_count = rng.randint(1, 8)
        free_count = rng.randint(0, 5)
        weights = tuple(rng.randint(1, 20) for _ in range(destroyed_count))
        gain = rng.randint(1, sum(weights))
        capacities = tuple(
            Fraction(rng.randint(0, 40), rng.randint(1, 8))
            for _ in range(destroyed_count + free_count)
        )
        roles = tuple(rng.randrange(rng.randint(1, 6)) for _ in capacities)
        r_star = Fraction(rng.randint(1, 80), rng.randint(1, 8))
        audit_system(weights, gain, capacities, destroyed_count, roles, r_star, counts)
        counts["random systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_systems(counts)
    random_systems(counts)
    print("GC2br--GC2bv raw-event gain-row audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
