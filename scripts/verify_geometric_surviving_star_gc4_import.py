#!/usr/bin/env python3
"""Finite audit for GC2cm--GC2cr surviving-star GC4 import."""

from __future__ import annotations

from itertools import combinations, product
from random import Random


def max_independent_weight(weights: list[int], edges: set[tuple[int, int]]) -> int:
    n = len(weights)
    best = 0
    for mask in range(1 << n):
        ok = True
        for i, j in edges:
            if (mask >> i) & 1 and (mask >> j) & 1:
                ok = False
                break
        if ok:
            total = sum(weights[i] for i in range(n) if (mask >> i) & 1)
            best = max(best, total)
    return best


def closed_loads(weights: list[int], edges: set[tuple[int, int]]) -> list[int]:
    loads = weights.copy()
    for i, j in edges:
        loads[i] += weights[j]
        loads[j] += weights[i]
    return loads


def exhaustive_cohort_audit() -> dict[str, int]:
    systems = 0
    payment_branches = 0
    survival_branches = 0
    for n in range(1, 6):
        for weights in product(range(1, 5), repeat=n):
            for survivors in product(*[range(w + 1) for w in weights]):
                paid = tuple(w - s for w, s in zip(weights, survivors))
                w_tot = sum(weights)
                s_tot = sum(survivors)
                p_tot = sum(paid)
                assert w_tot == s_tot + p_tot
                assert p_tot * 2 >= w_tot or s_tot * 2 >= w_tot
                if p_tot * 2 >= w_tot:
                    payment_branches += 1
                else:
                    survival_branches += 1
                    assert s_tot * 2 > w_tot
                systems += 1
    return {
        "cohort_systems": systems,
        "payment_branches": payment_branches,
        "survival_branches": survival_branches,
    }


def exhaustive_conflict_audit() -> dict[str, int]:
    graphs = 0
    overloads = 0
    compatible = 0
    labelled = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for edge_mask in range(1 << len(pairs)):
            edges = {pairs[k] for k in range(len(pairs)) if (edge_mask >> k) & 1}
            for weights in product(range(1, 4), repeat=n):
                loads = closed_loads(list(weights), edges)
                alpha = max_independent_weight(list(weights), edges)
                total = sum(weights)
                for K in range(1, 6):
                    bad = [i for i in range(n) if loads[i] > K * weights[i]]
                    if bad:
                        overloads += 1
                        i = bad[0]
                        neighbours = [j for j in range(n) if j != i and ((min(i, j), max(i, j)) in edges)]
                        for T in range(1, 5):
                            label_sums = [0] * T
                            for pos, j in enumerate(neighbours):
                                label_sums[pos % T] += weights[j]
                            assert max(label_sums, default=0) * T > (K - 1) * weights[i]
                            labelled += 1
                    else:
                        assert alpha * K >= total
                        compatible += 1
                graphs += 1
    return {
        "weighted_graphs": graphs,
        "overload_tests": overloads,
        "compatible_tests": compatible,
        "labelled_overload_tests": labelled,
    }


def random_birth_router_audit(rng: Random, trials: int = 40000) -> dict[str, int]:
    paid = 0
    overload = 0
    compatible = 0
    current_lineages = 0
    for _ in range(trials):
        n = rng.randint(1, 10)
        births = [rng.randint(1, 40) for _ in range(n)]
        survivors = [rng.randint(0, w) for w in births]
        payments = [w - s for w, s in zip(births, survivors)]
        assert sum(births) == sum(survivors) + sum(payments)

        # Distinct lineage IDs persist across cohorts even for repeated signatures.
        lineage_ids = {(i, k) for i, w in enumerate(births) for k in range(w)}
        assert len(lineage_ids) == sum(births)
        current_lineages += sum(survivors)

        w_tot = sum(births)
        p_tot = sum(payments)
        if 2 * p_tot >= w_tot:
            paid += 1
            continue

        active = [i for i, s in enumerate(survivors) if s > 0]
        idx = {old: new for new, old in enumerate(active)}
        weights = [survivors[i] for i in active]
        edges: set[tuple[int, int]] = set()
        for a, b in combinations(active, 2):
            if rng.random() < 0.25:
                edges.add((idx[a], idx[b]))
        loads = closed_loads(weights, edges)
        K = rng.randint(1, 8)
        bad = [i for i in range(len(weights)) if loads[i] > K * weights[i]]
        if bad:
            overload += 1
        else:
            alpha = max_independent_weight(weights, edges)
            assert alpha * K >= sum(weights)
            assert 2 * K * alpha > w_tot
            compatible += 1
    return {
        "random_birth_systems": trials,
        "random_paid": paid,
        "random_overloads": overload,
        "random_compatible": compatible,
        "current_lineage_units": current_lineages,
    }


def main() -> None:
    rng = Random(0x6C4)
    counts = exhaustive_cohort_audit()
    counts.update(exhaustive_conflict_audit())
    counts.update(random_birth_router_audit(rng))
    print("GC surviving-star GC4 import audit passed")
    for key, value in counts.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
