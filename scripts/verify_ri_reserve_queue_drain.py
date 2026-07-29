#!/usr/bin/env python3
"""Finite verifier for RI5hu--RI5hx."""

from __future__ import annotations

import math
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    cost: tuple[int, ...]


def drain(jobs: list[Job], cap: tuple[int, ...], kappa: tuple[int, ...], window: int, rng: random.Random) -> tuple[int, int]:
    reserve = [rng.randint(0, cap[a]) for a in range(len(cap))]
    replenish = [max(1, math.ceil(kappa[a] / window)) for a in range(len(cap))]
    steps = 0
    head_wait = 0
    max_wait = 0
    while jobs:
        steps += 1
        head_wait += 1
        for a in range(len(cap)):
            reserve[a] = min(cap[a], reserve[a] + replenish[a])
        if all(reserve[a] >= jobs[0].cost[a] for a in range(len(cap))):
            job = jobs.pop(0)
            for a in range(len(cap)):
                reserve[a] -= job.cost[a]
            max_wait = max(max_wait, head_wait)
            head_wait = 0
    return steps, max_wait


def main() -> None:
    rng = random.Random(101)
    systems = jobs_checked = oversized = window_failures = arrivals = 0
    for _ in range(2500):
        dim = rng.randint(2, 6)
        cap = tuple(rng.randint(3, 10) for _ in range(dim))
        kappa = tuple(rng.randint(1, cap[a]) for a in range(dim))
        window = rng.randint(1, 6)
        count = rng.randint(1, 20)
        queue = []
        for _ in range(count):
            cost = tuple(rng.randint(0, kappa[a]) for a in range(dim))
            if not any(cost):
                cost = (1,) + (0,) * (dim - 1)
            queue.append(Job(cost))
        steps, max_wait = drain(queue.copy(), cap, kappa, window, rng)
        assert max_wait <= window
        assert steps <= count * window

        delta0 = rng.randint(count, count + 10)
        disturbance = sum(rng.randint(0, 4) for _ in range(rng.randint(2, 10)))
        admitted = count + rng.randint(0, delta0 + disturbance - count)
        assert admitted <= delta0 + disturbance
        arrivals += admitted

        if rng.random() < 0.12:
            a = rng.randrange(dim)
            assert cap[a] + 1 > cap[a]
            oversized += 1
        if rng.random() < 0.25:
            a = rng.randrange(dim)
            supplied = max(0, kappa[a] - rng.randint(1, max(1, kappa[a])))
            assert kappa[a] - supplied > 0
            window_failures += 1

        systems += 1
        jobs_checked += count

    print(f"verified {systems} RI queues")
    print(f"checked {jobs_checked} jobs and {arrivals} origin-accounted admissions")
    print(f"returned {oversized} oversized jobs and {window_failures} window shortages")


if __name__ == "__main__":
    main()
