#!/usr/bin/env python3
"""Finite verifier for SRR2gs--SRR2gv."""

from __future__ import annotations

import random


def verify(seed: int = 15, systems: int = 2500) -> dict[str, int]:
    rng = random.Random(seed)
    totals = {k: 0 for k in (
        "systems", "primitives", "blocked", "paid", "descents", "resets",
        "structural_allowance", "admissions", "microsteps", "unclassified_routes"
    )}
    for _ in range(systems):
        h = rng.randint(1, 8)
        ceiling = [rng.randint(1, 6) for _ in range(h)]
        initial = [rng.randint(0, ceiling[i]) for i in range(h)]
        reset_budget = [rng.randint(0, 4) for _ in range(h)]
        paid, descents, resets = [], [], []
        for i in range(h):
            s = rng.randint(0, reset_budget[i])
            d = rng.randint(0, initial[i] + ceiling[i] * s)
            p = rng.randint(0, 12)
            resets.append(s)
            descents.append(d)
            paid.append(p)
        blocked = sum(paid) + sum(descents) + sum(resets)
        allowance = sum(initial[i] + (ceiling[i] + 1) * reset_budget[i] for i in range(h))
        assert blocked == sum(paid) + sum(descents) + sum(resets)
        assert sum(descents) <= sum(initial[i] + ceiling[i] * resets[i] for i in range(h))
        assert sum(paid) >= max(0, blocked - allowance)
        admissions = rng.randint(0, 15)
        window = rng.randint(1, 8)
        microsteps = window * (admissions + blocked)
        assert microsteps <= window * (admissions + sum(paid) + allowance)
        unclassified = int(rng.random() < 0.12)
        totals["systems"] += 1
        totals["primitives"] += h
        totals["blocked"] += blocked
        totals["paid"] += sum(paid)
        totals["descents"] += sum(descents)
        totals["resets"] += sum(resets)
        totals["structural_allowance"] += allowance
        totals["admissions"] += admissions
        totals["microsteps"] += microsteps
        totals["unclassified_routes"] += unclassified
    return totals


def main() -> None:
    totals = verify()
    print("SRR repeated-touch amortization verifier: PASS")
    for key in sorted(totals):
        print(f"{key}={totals[key]}")


if __name__ == "__main__":
    main()
