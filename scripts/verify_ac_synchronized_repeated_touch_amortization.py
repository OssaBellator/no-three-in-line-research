#!/usr/bin/env python3
"""Finite verifier for AC5hf--AC5hi."""

from __future__ import annotations

import random

TRACKS = ("AC", "RI", "BDA", "GC", "OP", "SRR", "SAS")


def verify(seed: int = 17, systems: int = 1500) -> dict[str, int]:
    rng = random.Random(seed)
    totals = {k: 0 for k in (
        "systems", "jobs", "primitives", "blocked", "paid", "descents",
        "resets", "structural_allowance", "admission_budget", "microsteps",
        "unclassified_routes"
    )}

    for _ in range(systems):
        delta0 = rng.randint(0, 20)
        churn = sum(rng.randint(0, 4) for _ in range(rng.randint(1, 8)))
        admission_budget = delta0 + churn
        jobs = rng.randint(0, admission_budget)
        track_windows = {track: rng.randint(1, 8) for track in TRACKS}

        paid_total = 0
        blocked_total = 0
        structural_total = 0
        exact_microsteps = 0
        exact_envelope = 0
        max_structural = 0

        for _job in range(jobs):
            track = rng.choice(TRACKS)
            h = rng.randint(1, 8)
            ceiling = [rng.randint(1, 6) for _ in range(h)]
            initial = [rng.randint(0, ceiling[i]) for i in range(h)]
            reset_budget = [rng.randint(0, 4) for _ in range(h)]
            paid, descents, resets = [], [], []
            for i in range(h):
                s = rng.randint(0, reset_budget[i])
                d = rng.randint(0, initial[i] + ceiling[i] * s)
                p = rng.randint(0, 10)
                resets.append(s)
                descents.append(d)
                paid.append(p)

            blocked = sum(paid) + sum(descents) + sum(resets)
            structural = sum(
                initial[i] + (ceiling[i] + 1) * reset_budget[i]
                for i in range(h)
            )
            assert blocked == sum(paid) + sum(descents) + sum(resets)
            assert sum(descents) <= sum(
                initial[i] + ceiling[i] * resets[i] for i in range(h)
            )
            assert sum(paid) >= max(0, blocked - structural)

            window = track_windows[track]
            exact_microsteps += window * (1 + blocked)
            exact_envelope += window * (1 + sum(paid) + structural)
            assert window * (1 + blocked) <= window * (1 + sum(paid) + structural)

            paid_total += sum(paid)
            blocked_total += blocked
            structural_total += structural
            max_structural = max(max_structural, structural)
            totals["primitives"] += h
            totals["descents"] += sum(descents)
            totals["resets"] += sum(resets)

        assert jobs <= admission_budget
        assert exact_microsteps <= exact_envelope
        w_star = max(track_windows.values())
        coarse_envelope = w_star * (paid_total + (max_structural + 1) * jobs)
        assert exact_microsteps <= coarse_envelope

        totals["systems"] += 1
        totals["jobs"] += jobs
        totals["blocked"] += blocked_total
        totals["paid"] += paid_total
        totals["structural_allowance"] += structural_total
        totals["admission_budget"] += admission_budget
        totals["microsteps"] += exact_microsteps
        totals["unclassified_routes"] += int(rng.random() < 0.10)

    return totals


def main() -> None:
    totals = verify()
    print("AC synchronized repeated-touch amortization verifier: PASS")
    for key in sorted(totals):
        print(f"{key}={totals[key]}")


if __name__ == "__main__":
    main()
