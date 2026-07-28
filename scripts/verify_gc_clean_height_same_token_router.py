#!/usr/bin/env python3
"""Finite audit for GC4u--GC4y."""

from collections import defaultdict
from fractions import Fraction
import random

SEED = 20260728


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(100000):
        m = rng.randint(1, 40)
        weights = [rng.randint(1, 500) for _ in range(m)]
        W = sum(weights)
        k_h = rng.randint(1, 16)
        safe = [rng.random() < 0.55 for _ in range(m)]
        cause_load = [0] * k_h
        w_safe = 0
        for w, ok in zip(weights, safe):
            if ok:
                w_safe += w
            else:
                cause_load[rng.randrange(k_h)] += w
        w_bad = W - w_safe
        assert w_safe + w_bad == W
        assert sum(cause_load) == w_bad

        if 2 * w_safe >= W:
            r = rng.randint(1, 8)
            kappa = rng.randint(1, 8)
            P = rng.randint(0, 2 * W)
            lower_union = (P + r - 1) // r
            U = rng.randint(lower_union, P) if P else 0
            if 2 * kappa * P >= w_safe:
                assert 4 * r * kappa * U >= W
                counts["safe_payment_branches"] += 1
            else:
                deficiency = Fraction(w_safe, kappa) - U
                assert deficiency > Fraction(W, 4 * kappa)
                counts["safe_deficiency_branches"] += 1
            counts["safe_half_systems"] += 1
        else:
            assert max(cause_load) * 2 * k_h > W
            counts["protected_cause_branches"] += 1

        gamma = rng.randint(0, 12)
        w0 = rng.randint(W, W * (gamma + 1))
        assert W >= Fraction(w0, gamma + 1)
        if 2 * w_safe >= W:
            assert Fraction(W, 4) >= Fraction(w0, 4 * (gamma + 1))
        else:
            assert Fraction(max(cause_load), 1) > Fraction(w0, 2 * k_h * (gamma + 1))

        counts["systems"] += 1
        counts["operations"] += m
        counts["total_weight"] += W

    print("GC clean-height same-token audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
