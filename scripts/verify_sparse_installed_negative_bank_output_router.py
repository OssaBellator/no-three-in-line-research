#!/usr/bin/env python3
"""Finite audit for SAS5gg--SAS5gk."""

from collections import defaultdict
import random

SEED = 20260727


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    positive_tables = {(1, 0, 0, 0), (0, 0, 0, 1)}
    negative_tables = {(0, 1, 0, 0), (0, 0, 1, 0)}
    for table in positive_tables:
        curvature = table[0] - table[1] - table[2] + table[3]
        assert curvature == 1
    for table in negative_tables:
        curvature = table[0] - table[1] - table[2] + table[3]
        assert curvature == -1
    counts["positive table types"] = len(positive_tables)
    counts["negative table types"] = len(negative_tables)

    for _ in range(100000):
        squares = rng.randint(1, 20)
        k_num = rng.randint(0, 9)
        k_den = 10
        kappa = k_num / k_den
        if kappa >= 1:
            kappa = 0.9

        rows = []
        r_total = 0
        for _a in range(squares):
            r = rng.randint(1, 40)
            c_minus = r + rng.randint(0, 20)
            creator = rng.randint(0, max(0, int(kappa * r)))
            opposite = rng.randint(0, 50)
            p_cur = rng.randint(0, 50)
            p_comp = rng.randint(0, 50)
            deficit = c_minus - creator - opposite - p_cur - p_comp
            if deficit > 0:
                bucket = rng.randrange(3)
                if bucket == 0:
                    opposite += deficit
                elif bucket == 1:
                    p_cur += deficit
                else:
                    p_comp += deficit
            delta = creator + opposite + p_cur + p_comp - c_minus
            assert delta >= 0
            rows.append((r, c_minus, creator, opposite, p_cur, p_comp, delta))
            r_total += r

        creator_total = sum(row[2] for row in rows)
        assert creator_total <= kappa * r_total + 1e-12
        opposite_total = sum(row[3] for row in rows)
        p_cur_total = sum(row[4] for row in rows)
        p_comp_total = sum(row[5] for row in rows)
        c_minus_total = sum(row[1] for row in rows)

        assert c_minus_total >= r_total
        assert creator_total + opposite_total + p_cur_total + p_comp_total >= r_total
        residual = (1 - kappa) * r_total
        assert opposite_total + p_cur_total + p_comp_total + 1e-12 >= residual
        largest = max(opposite_total, p_cur_total, p_comp_total)
        assert largest + 1e-12 >= residual / 3

        if largest == opposite_total:
            counts["opposite barrier routes"] += 1
        elif largest == p_cur_total:
            counts["current payment routes"] += 1
        else:
            counts["composed output routes"] += 1

        m = rng.randint(1, 10000)
        d_sq = rng.randint(0, 40)
        lam = rng.randint(1, 9) / 10
        theta = rng.randint(1, 9) / 10
        lower = (1 - theta) * lam * m / (16 * (d_sq + 1))
        r_installed = lower + rng.random() * 100 + 1e-9
        integrated = (1 - kappa) * (1 - theta) * lam * m / (48 * (d_sq + 1))
        assert (1 - kappa) * r_installed / 3 > integrated

        counts["square-bank systems"] += 1
        counts["square vertices"] += squares
        counts["installed negative weight"] += r_total
        counts["current-only positive weight"] += p_cur_total
        counts["composed-only positive weight"] += p_comp_total
        counts["opposite barrier units"] += opposite_total

    print("SAS installed-negative-bank output audit passed")
    for key in sorted(counts):
        print(f"  {key}: {counts[key]}")


if __name__ == "__main__":
    main()
