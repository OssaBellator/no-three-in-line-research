#!/usr/bin/env python3
"""Finite checks for SAS5ch--SAS5cl."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from random import Random


def indicator(scope: tuple[int, int, int], labels: tuple[int, int, int], colouring: tuple[int, ...]) -> int:
    return int(all(colouring[column] == label for column, label in zip(scope, labels)))


def apply_swap(colouring: tuple[int, ...], swap: tuple[int, int]) -> tuple[int, ...]:
    out = list(colouring)
    a, b = swap
    out[a], out[b] = out[b], out[a]
    return tuple(out)


def curvature(
    scope: tuple[int, int, int],
    labels: tuple[int, int, int],
    colouring: tuple[int, ...],
    omega: tuple[int, int],
    tau: tuple[int, int],
) -> int:
    c_omega = apply_swap(colouring, omega)
    c_tau = apply_swap(colouring, tau)
    c_both = apply_swap(c_omega, tau)
    return (
        indicator(scope, labels, c_both)
        - indicator(scope, labels, c_omega)
        - indicator(scope, labels, c_tau)
        + indicator(scope, labels, colouring)
    )


def exhaustive_alias_aggregation(counts: Counter[str]) -> None:
    columns = 4
    omega = (0, 1)
    tau = (2, 3)
    for scope in combinations(range(columns), 3):
        for labels in product(range(2), repeat=3):
            for colouring in product(range(2), repeat=columns):
                aliases = (1, 2, 4)
                aggregate = sum(aliases)
                states = [
                    colouring,
                    apply_swap(colouring, omega),
                    apply_swap(colouring, tau),
                    apply_swap(apply_swap(colouring, omega), tau),
                ]
                for state in states:
                    alias_energy = sum(weight * indicator(scope, labels, state) for weight in aliases)
                    merged_energy = aggregate * indicator(scope, labels, state)
                    assert alias_energy == merged_energy
                alias_curvature = sum(
                    weight * curvature(scope, labels, colouring, omega, tau) for weight in aliases
                )
                merged_curvature = aggregate * curvature(scope, labels, colouring, omega, tau)
                assert alias_curvature == merged_curvature
                counts["alias systems"] += 1
                counts["symbolic aliases"] += len(aliases)


def random_donor_banks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        donor_count = rng.randint(1, 6)
        column_count = 2 + 2 * donor_count
        omega = (0, 1)
        donors = tuple((2 + 2 * i, 3 + 2 * i) for i in range(donor_count))
        colouring = tuple(rng.randrange(3) for _ in range(column_count))

        record_count = rng.randint(1, 80)
        records: list[tuple[tuple[int, int, int], tuple[int, int, int], int]] = []
        omega_cross_weight = 0
        sharp_budget = 0
        c_minus = [0] * donor_count

        for _record in range(record_count):
            scope = tuple(sorted(rng.sample(range(column_count), 3)))
            labels = tuple(rng.randrange(3) for _ in range(3))
            alias_weights = [rng.randint(1, 10) for _ in range(rng.randint(1, 5))]
            weight = sum(alias_weights)
            records.append((scope, labels, weight))

            original_hits = len(set(scope) & set(omega))
            nonzero_donors = 0
            for donor_index, tau in enumerate(donors):
                curv = curvature(scope, labels, colouring, omega, tau)
                if curv != 0:
                    nonzero_donors += 1
                    assert original_hits > 0
                    assert set(scope) & set(tau)
                if curv == -1:
                    c_minus[donor_index] += weight
                assert curv in {-1, 0, 1}

            if original_hits == 0:
                assert nonzero_donors == 0
            else:
                assert nonzero_donors <= 3 - original_hits <= 2
                omega_cross_weight += weight
                sharp_budget += (3 - original_hits) * weight

        assert sum(c_minus) <= sharp_budget <= 2 * omega_cross_weight

        eta_num = rng.randint(1, 9)
        eta_den = 10
        scale_weights = [rng.randint(1, 100) for _ in donors]
        heavy = [i for i, (cm, lw) in enumerate(zip(c_minus, scale_weights)) if cm * eta_den >= eta_num * lw]
        assert sum(scale_weights[i] for i in heavy) * eta_num <= 2 * omega_cross_weight * eta_den

        improving = [i for i, (cm, lw) in enumerate(zip(c_minus, scale_weights)) if cm > lw]
        assert sum(scale_weights[i] for i in improving) < 2 * omega_cross_weight or not improving

        counts["donor banks"] += 1
        counts["donor swaps"] += donor_count
        counts["physical records"] += record_count
        counts["negative donor incidences"] += sum(1 for value in c_minus if value > 0)
        counts["heavy-collateral donors"] += len(heavy)
        counts["improving-necessary donors"] += len(improving)


def capacity_split_checks(counts: Counter[str]) -> None:
    rng = Random(20260727)
    for _ in range(30000):
        aggregate = sum(rng.randint(0, 20) for _ in range(rng.randint(1, 8)))
        capacity = rng.randint(0, 100)
        if aggregate <= capacity:
            counts["within-capacity exact records"] += 1
        else:
            overload = aggregate - capacity
            assert overload > 0
            counts["multiplicity overload records"] += 1
            counts["multiplicity overload weight"] += overload


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_alias_aggregation(counts)
    random_donor_banks(counts)
    capacity_split_checks(counts)
    print("SAS5ch--SAS5cl exact-record donor-incidence audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
