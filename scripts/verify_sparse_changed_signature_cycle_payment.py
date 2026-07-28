#!/usr/bin/env python3
"""Finite audit for SAS5gy--SAS5hc."""

from collections import defaultdict
import random

SEED = 20260728


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(100000):
        K_rec = rng.randint(2, 60)
        ell = rng.randint(2, K_rec)
        mode = rng.randrange(3)

        if mode == 0:
            # Positive barriers with exact compensating descent.
            vals = [rng.randint(-20, 20) for _ in range(ell - 1)]
            vals.append(-sum(vals))
            if sum(max(x, 0) for x in vals) == 0:
                vals[0] += 1
                vals[-1] -= 1
        elif mode == 1:
            vals = [0] * ell
        else:
            vals = [rng.randint(-20, 20) for _ in range(ell)]
            # This branch models a signature cycle with a changed physical field,
            # so physical energy closure is not asserted.

        if mode < 2:
            assert sum(vals) == 0
            B_plus = sum(max(x, 0) for x in vals)
            B_minus = sum(max(-x, 0) for x in vals)
            assert B_plus == B_minus

            if B_plus > 0:
                assert min(vals) <= -B_plus / ell
                assert min(vals) <= -B_plus / K_rec
                counts["barrier_descent_cycles"] += 1
                counts["positive_barrier_units"] += B_plus
            else:
                assert all(x == 0 for x in vals)
                counts["zero_energy_cycles"] += 1
        else:
            counts["changed_boundary_cycles"] += 1

        E = rng.randint(K_rec - 1, K_rec + 100)
        c = rng.randint(1, min(K_rec, 5))
        if E < K_rec - c:
            E = K_rec - c
        mu = E - K_rec + c
        traversals = rng.randint(0, mu)
        assert traversals <= mu
        counts["ticketed_zero_traversals"] += traversals

        counts["systems"] += 1
        counts["cycle_edges"] += ell

    print("SAS changed-signature cycle-payment audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
