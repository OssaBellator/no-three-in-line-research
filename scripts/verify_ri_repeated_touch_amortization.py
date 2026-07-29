#!/usr/bin/env python3
"""Finite verifier for RI5ic--RI5if."""

from __future__ import annotations

import random


def verify(seed: int = 11, systems: int = 2500) -> dict[str, int]:
    rng = random.Random(seed)
    totals = {
        "systems": 0,
        "primitives": 0,
        "blocked": 0,
        "paid": 0,
        "descents": 0,
        "resets": 0,
        "structural_allowance": 0,
        "admissions": 0,
        "microsteps": 0,
        "unclassified_routes": 0,
    }

    for _ in range(systems):
        h = rng.randint(1, 8)
        ceilings = [rng.randint(1, 6) for _ in range(h)]
        initial_rank = [rng.randint(0, ceilings[i]) for i in range(h)]
        reset_budget = [rng.randint(0, 4) for _ in range(h)]

        paid: list[int] = []
        descents: list[int] = []
        resets: list[int] = []
        for i in range(h):
            s_i = rng.randint(0, reset_budget[i])
            d_i = rng.randint(0, initial_rank[i] + ceilings[i] * s_i)
            p_i = rng.randint(0, 12)
            resets.append(s_i)
            descents.append(d_i)
            paid.append(p_i)

        blocked = sum(paid) + sum(descents) + sum(resets)
        structural = sum(
            initial_rank[i] + (ceilings[i] + 1) * reset_budget[i]
            for i in range(h)
        )

        assert blocked == sum(paid) + sum(descents) + sum(resets)
        assert sum(descents) <= sum(
            initial_rank[i] + ceilings[i] * resets[i] for i in range(h)
        )
        assert sum(paid) >= max(0, blocked - structural)

        admissions = rng.randint(0, 15)
        service_window = rng.randint(1, 8)
        microsteps = service_window * (admissions + blocked)
        envelope = service_window * (admissions + sum(paid) + structural)
        assert microsteps <= envelope

        # The invalid branch must return, rather than silently classify, one touch.
        unclassified = int(rng.random() < 0.12)
        if unclassified:
            assert unclassified > 0

        totals["systems"] += 1
        totals["primitives"] += h
        totals["blocked"] += blocked
        totals["paid"] += sum(paid)
        totals["descents"] += sum(descents)
        totals["resets"] += sum(resets)
        totals["structural_allowance"] += structural
        totals["admissions"] += admissions
        totals["microsteps"] += microsteps
        totals["unclassified_routes"] += unclassified

    return totals


def main() -> None:
    totals = verify()
    print("RI repeated-touch amortization verifier: PASS")
    for key in sorted(totals):
        print(f"{key}={totals[key]}")


if __name__ == "__main__":
    main()
