#!/usr/bin/env python3
"""Finite audit for RI5hy--RI5ib."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import ceil
from random import Random


@dataclass(frozen=True)
class Job:
    debt_id: int
    footprint: frozenset[int]


def run(seed: int = 101, systems: int = 2500) -> Counter[str]:
    rng = Random(seed)
    totals: Counter[str] = Counter()
    for _ in range(systems):
        primitives = list(range(rng.randint(16, 44)))
        jobs = [
            Job(j, frozenset(rng.sample(primitives, rng.randint(1, min(6, len(primitives))))))
            for j in range(rng.randint(1, 24))
        ]
        multiplicity = Counter(x for job in jobs for x in job.footprint)
        eta = max(multiplicity.values(), default=0)
        h_edit = rng.randint(0, min(6, len(primitives)))
        edit = set(rng.sample(primitives, h_edit))
        touched = [job for job in jobs if job.footprint & edit]
        untouched = [job for job in jobs if not job.footprint & edit]
        assert len(touched) <= h_edit * eta
        assert len(touched) + len(untouched) == len(jobs)

        active = {job.debt_id for job in jobs}
        for job in touched:
            outcome = rng.randrange(3)
            if outcome == 1:
                active.remove(job.debt_id)  # owner ceased to be unmatched
            # outcomes 0 and 2 keep the same debt identity
        disturbance = rng.randint(0, 6)
        first_new = len(jobs)
        active.update(range(first_new, first_new + disturbance))
        assert len(active) <= len(jobs) + disturbance
        assert len(active) == len(set(active))

        cumulative_touched = 0
        cumulative_bound = 0
        for _epoch in range(rng.randint(1, 8)):
            size = rng.randint(0, min(5, len(primitives)))
            support = set(rng.sample(primitives, size))
            inspected = sum(bool(job.footprint & support) for job in jobs)
            assert inspected <= size * eta
            cumulative_touched += inspected
            cumulative_bound += size * eta
        assert cumulative_touched <= cumulative_bound

        head = jobs[0]
        footprint_size = len(head.footprint)
        blocks = rng.randint(1, 12)
        hits: Counter[int] = Counter()
        serviced = False
        for _block in range(blocks):
            if rng.random() < 0.30:
                serviced = True
                break
            hits[rng.choice(tuple(head.footprint))] += 1
        if not serviced:
            assert max(hits.values()) >= ceil(blocks / footprint_size)
            totals["repeated_touch_cases"] += 1
        else:
            totals["service_cases"] += 1

        totals["systems"] += 1
        totals["jobs"] += len(jobs)
        totals["touched"] += len(touched)
        totals["inspection_bound"] += h_edit * eta
        totals["cumulative_touched"] += cumulative_touched
        totals["cumulative_bound"] += cumulative_bound
    return totals


if __name__ == "__main__":
    result = run()
    print("RI queue revalidation audit passed")
    for key in sorted(result):
        print(f"{key}: {result[key]}")
