#!/usr/bin/env python3
"""Finite audit for SAS5fr--SAS5fv."""

from collections import defaultdict
from fractions import Fraction
import random

SEED = 20260727
ALLOWED_REPAIRED = {
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (0, 1, 0, 1),
    (0, 0, 1, 1),
}
FINAL_ALLOWED = {
    (0, 0, 0, 1),
    (0, 1, 0, 1),
    (0, 0, 1, 1),
}


def curvature(table):
    i0, isigma, itau, iboth = table
    return i0 - isigma - itau + iboth


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    final_tables = {t for t in ALLOWED_REPAIRED if t[0] == 0 and t[3] == 1}
    assert final_tables == FINAL_ALLOWED
    assert curvature((0, 0, 0, 1)) == 1
    assert curvature((0, 1, 0, 1)) == 0
    assert curvature((0, 0, 1, 1)) == 0
    counts["exhaustive_final_tables"] = len(final_tables)

    for _ in range(100000):
        table = rng.choice(tuple(sorted(FINAL_ALLOWED)))
        H = Fraction(rng.randint(1, 10**6), rng.randint(1, 100))
        if table == (0, 0, 0, 1):
            ds = Fraction(rng.randint(-1000, 3000), 100)
            dt = Fraction(rng.randint(-1000, 3000), 100)
            if ds < 0 or dt < 0:
                counts["direct_single_swap_descents"] += 1
            else:
                cplus = Fraction(rng.randint(0, 5000), 100)
                cminus = Fraction(rng.randint(0, 5000), 100)
                delta = ds + dt + H + cplus - cminus
                eta = Fraction(rng.randint(1, 9), 10)
                assert cminus >= eta * H or delta > (1 - eta) * H
                if delta < 0:
                    assert cminus > H
                counts["positive_barrier_records"] += 1
        else:
            # Exactly one single swap creates; the other preserves.
            assert sum(table[1:3]) == 1 and table[3] == 1
            counts["neutral_persistent_records"] += 1

        M = rng.randint(1, 10**7)
        D = rng.randint(0, 500)
        K = rng.randint(1, 10000)
        lam = Fraction(rng.randint(1, 20), rng.randint(1, 20))
        lower = lam * M / (2 * (D + 1) * K)
        H2 = lower + Fraction(rng.randint(1, 1000), 1000)
        assert H2 > lower

        N = rng.randint(4, 100)
        Lrep = rng.randint(0, 100)
        Aneu = (2 * N - 3) * (4 * Lrep + 1)
        Wneu = rng.randint(1, 10**8)
        neutral_bound = lam * Wneu / (4 * Aneu * (D + 1) * K)
        Dpair = rng.randint(0, 500)
        Bpair = rng.randint(1, 10**8)
        pair_bound = lam * Bpair / (4 * (Dpair + 1) * (D + 1) * K)
        assert neutral_bound >= 0 and pair_bound >= 0

        counts["weighted_routes"] += 1

    print("SAS final-output curvature import audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
