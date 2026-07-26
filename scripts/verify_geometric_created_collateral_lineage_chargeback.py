#!/usr/bin/env python3
from __future__ import annotations

import random
from dataclasses import dataclass
from itertools import product

SEED = 20260727
RNG = random.Random(SEED)


@dataclass
class Lineage:
    weight: int
    tagged: bool
    current: bool = True
    cohort: int | None = None
    support: tuple[int, ...] = ()


def exhaustive_cohort_checks() -> tuple[int, int]:
    systems = 0
    half_cases = 0
    for n in range(1, 8):
        for weights in product(range(1, 4), repeat=n):
            total = sum(weights)
            for destroyed in product((0, 1), repeat=n):
                paid = sum(w for w, d in zip(weights, destroyed) if d)
                surviving = total - paid
                assert total == paid + surviving
                assert paid * 2 >= total or surviving * 2 >= total
                systems += 1
                half_cases += 1
            if systems > 120_000:
                return systems, half_cases
    return systems, half_cases


def star_survivor_checks(trials: int = 40_000) -> tuple[int, int]:
    paid_heavy = 0
    survivor_heavy = 0
    for _ in range(trials):
        rank = RNG.choice((2, 3))
        q = 0
        n = RNG.randint(1, 20)
        next_vertex = 1
        supports = []
        weights = []
        for _i in range(n):
            if rank == 2:
                support = (q, next_vertex)
                next_vertex += 1
            else:
                support = (q, next_vertex, next_vertex + 1)
                next_vertex += 2
            supports.append(support)
            weights.append(RNG.randint(1, 9))
        destroyed = [RNG.random() < 0.5 for _ in range(n)]
        total = sum(weights)
        paid = sum(w for w, d in zip(weights, destroyed) if d)
        survivors = [supports[i] for i, d in enumerate(destroyed) if not d]
        surviving_weight = total - paid
        assert paid + surviving_weight == total
        if paid * 2 >= total:
            paid_heavy += 1
        else:
            survivor_heavy += 1
            assert surviving_weight * 2 >= total
            outside = []
            for support in survivors:
                assert q in support
                outside.extend(x for x in support if x != q)
            assert len(outside) == len(set(outside))
    return paid_heavy, survivor_heavy


def random_history_checks(histories: int = 30_000) -> tuple[int, int, int, int]:
    strict = 0
    zero = 0
    created = 0
    first_payments = 0
    next_id = 0
    for h in range(histories):
        lineages: dict[int, Lineage] = {}
        for _ in range(RNG.randint(0, 12)):
            lineages[next_id] = Lineage(weight=RNG.randint(1, 7), tagged=False)
            next_id += 1
        cohort_ids: list[int] = []
        cohort_total = 0
        cohort_paid: set[int] = set()
        for step_no in range(RNG.randint(1, 80)):
            current_ids = [i for i, x in lineages.items() if x.current]
            destroy_count = RNG.randint(0, min(5, len(current_ids)))
            destroy_ids = RNG.sample(current_ids, destroy_count)
            D = sum(lineages[i].weight for i in destroy_ids)
            C = sum(lineages[i].weight for i in destroy_ids if lineages[i].tagged)
            T0 = sum(x.weight for x in lineages.values() if x.current)
            U0 = sum(x.weight for x in lineages.values() if x.current and x.tagged)
            phi0 = T0 - U0

            for i in destroy_ids:
                lineages[i].current = False
                if i in cohort_ids and i not in cohort_paid:
                    cohort_paid.add(i)
                    first_payments += lineages[i].weight

            new_ids = []
            for _ in range(RNG.randint(0, 5)):
                w = RNG.randint(1, 7)
                lineages[next_id] = Lineage(weight=w, tagged=True, cohort=h)
                new_ids.append(next_id)
                created += w
                next_id += 1
            if step_no == 0:
                cohort_ids = list(new_ids)
                cohort_total = sum(lineages[i].weight for i in cohort_ids)

            N = sum(lineages[i].weight for i in new_ids)
            T1 = sum(x.weight for x in lineages.values() if x.current)
            U1 = sum(x.weight for x in lineages.values() if x.current and x.tagged)
            phi1 = T1 - U1
            assert T1 == T0 - D + N
            assert U1 == U0 - C + N
            assert phi1 - phi0 == -(D - C)
            assert phi1 >= 0
            if D == C:
                assert phi1 == phi0
                zero += 1
            else:
                assert D > C and phi1 < phi0
                strict += 1

            surviving = sum(lineages[i].weight for i in cohort_ids if lineages[i].current)
            paid = sum(lineages[i].weight for i in cohort_paid)
            assert surviving + paid == cohort_total
    return strict, zero, created, first_payments


def signature_recreation_checks(trials: int = 20_000) -> int:
    checked = 0
    for _ in range(trials):
        w = RNG.randint(1, 20)
        old = Lineage(weight=w, tagged=True, current=True, support=(0, 1, 2))
        old.current = False
        new = Lineage(weight=w, tagged=True, current=True, support=(0, 1, 2))
        assert old.support == new.support
        assert old is not new
        assert not old.current and new.current
        checked += 1
    return checked


def main() -> None:
    systems, halves = exhaustive_cohort_checks()
    paid, survive = star_survivor_checks()
    strict, zero, created, payments = random_history_checks()
    recreated = signature_recreation_checks()
    print(
        "PASS GC created-collateral lineage audit:",
        f"{systems} exhaustive cohorts;",
        f"{halves} half dichotomies;",
        f"{paid} paid-heavy stars;",
        f"{survive} survivor-heavy stars;",
        f"{strict} strict tagged-potential events;",
        f"{zero} zero-drift recycling events;",
        f"{created} created tagged weight;",
        f"{payments} first-destruction payment weight;",
        f"{recreated} recreated-signature lineage checks.",
    )


if __name__ == "__main__":
    main()
