#!/usr/bin/env python3
"""Finite audit for GC2fu--GC2fy."""

import math
import random

SEED = 20260727


def main():
    rng = random.Random(SEED)
    counts = {
        "systems": 0,
        "candidate_donors": 0,
        "legal_donors": 0,
        "empty_menus": 0,
        "capacity_overloads": 0,
        "capacity_certified_menus": 0,
        "blocker_incidence_units": 0,
    }

    for _ in range(100000):
        k_blk = rng.randint(1, 20)
        d0 = rng.randint(1, 200)
        h = rng.randint(1, 1000)
        assignments = [rng.randint(-1, k_blk - 1) for _ in range(d0)]
        d = assignments.count(-1)
        n = [assignments.count(p) for p in range(k_blk)]
        assert d0 == d + sum(n)

        gamma = rng.randint(0, max(n) if n else 0)
        if all(x <= gamma for x in n):
            assert d >= d0 - k_blk * gamma
        else:
            assert any(x > gamma for x in n)

        if d == 0:
            assert max(n) >= math.ceil(d0 / k_blk)
            p = max(range(k_blk), key=n.__getitem__)
            assert n[p] * h >= d0 * h / k_blk
            counts["empty_menus"] += 1
            counts["blocker_incidence_units"] += n[p] * h

        caps = [rng.randint(0, max(0, d0 // 4)) for _ in range(k_blk)]
        overloaded = [p for p in range(k_blk) if n[p] > caps[p]]
        if overloaded:
            counts["capacity_overloads"] += 1
        else:
            assert d >= d0 - sum(caps)
            if d0 > sum(caps):
                assert d >= 1
            counts["capacity_certified_menus"] += 1

        n_board = rng.randint(5, 50)
        q_ch = rng.randint(1, 8)
        l_cert = rng.randint(1, 10)
        delta_cap = l_cert * (n_board * n_board - 2)
        w_b = rng.randint(1, 10**6)
        h_lower = w_b / (8 * q_ch * n_board**2 * (2 * delta_cap - 1))
        if d == 0:
            p = max(range(k_blk), key=n.__getitem__)
            h_inst = h_lower * (1 + rng.random()) + 1e-9
            assert n[p] * h_inst > d0 * h_lower / k_blk

        counts["systems"] += 1
        counts["candidate_donors"] += d0
        counts["legal_donors"] += d

    print("GC donor-blocker concentration audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
