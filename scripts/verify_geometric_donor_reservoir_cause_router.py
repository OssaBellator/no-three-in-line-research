#!/usr/bin/env python3
"""Finite audit for GC2fp--GC2ft."""

from collections import defaultdict
import random

SEED = 20260727


def rectangle_support(target, donor):
    rb, cb = target
    ru, cu = donor
    return {target, donor, (rb, cu), (ru, cb)}


def geometry_audit(rng, counts):
    for _ in range(25000):
        p = rng.randint(1, 60)
        cols = list(range(1, p + 1))
        rng.shuffle(cols)
        donors = [(r + 1, cols[r]) for r in range(p)]
        target = (0, 0)
        supports = [rectangle_support(target, donor) for donor in donors]

        z = (rng.randint(0, p + 1), rng.randint(0, p + 1))
        inserted_only = z != target and z not in donors
        if inserted_only:
            degree = sum(z in support for support in supports)
            assert degree <= 2
            counts["collision cells checked"] += 1

        # A non-axis affine line ar+bc=c0 with both coefficients nonzero.
        a = rng.choice([i for i in range(-4, 5) if i])
        b = rng.choice([i for i in range(-4, 5) if i])
        c0 = rng.randint(-4 * p, 4 * p)
        line_degree = 0
        for donor in donors:
            rb, cb = target
            ru, cu = donor
            x = (rb, cu)
            y = (ru, cb)
            if a * x[0] + b * x[1] == c0 or a * y[0] + b * y[1] == c0:
                line_degree += 1
        assert line_degree <= 2
        counts["non-axis lines checked"] += 1

        universe = [(r, c) for r in range(p + 2) for c in range(p + 2) if (r, c) != target]
        size = rng.randint(0, min(7, len(universe)))
        q_support = set(rng.sample(universe, size))
        degree = sum(bool(support & q_support) for support in supports)
        assert degree <= 3 * len(q_support)
        counts["bounded supports checked"] += 1
        counts["bounded support cells"] += len(q_support)


def partition_audit(rng, counts):
    for _ in range(50000):
        p = rng.randint(0, 150)
        coll = rng.randint(0, 8)
        line = rng.randint(0, 8)
        support_sizes = [rng.randint(0, 8) for _ in range(rng.randint(0, 10))]
        caps = [2] * coll + [2] * line + [3 * size for size in support_sizes]
        d_phys = sum(caps)

        remaining = p
        bounded_loads = []
        for cap in caps:
            load = rng.randint(0, min(cap, remaining))
            bounded_loads.append(load)
            remaining -= load

        k_res = rng.randint(0, 8)
        residual_loads = [0] * k_res
        for _unit in range(rng.randint(0, remaining) if k_res else 0):
            residual_loads[rng.randrange(k_res)] += 1
        illegal = sum(bounded_loads) + sum(residual_loads)
        legal = p - illegal
        assert legal >= 0
        assert sum(bounded_loads) <= d_phys

        r_don = max(p - legal - d_phys, 0)
        assert sum(residual_loads) >= r_don
        if k_res:
            assert max(residual_loads, default=0) * k_res >= r_don
        else:
            assert legal >= p - d_phys

        counts["partition systems"] += 1
        counts["candidate donors"] += p
        counts["legal donors"] += legal
        counts["bounded blocked donors"] += sum(bounded_loads)
        counts["target or context blocked donors"] += sum(residual_loads)
        if r_don > 0:
            counts["positive residual shortages"] += 1
        if p > d_phys and k_res == 0:
            assert legal > 0
            counts["automatic nonempty menus"] += 1


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)
    geometry_audit(rng, counts)
    partition_audit(rng, counts)
    print("GC donor-reservoir cause audit passed")
    for key in sorted(counts):
        print(f"  {key}: {counts[key]}")


if __name__ == "__main__":
    main()
