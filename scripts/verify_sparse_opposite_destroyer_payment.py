#!/usr/bin/env python3
"""Finite audit for SAS5gl--SAS5gp."""

import random

SEED = 20260727


def main():
    rng = random.Random(SEED)
    counts = {
        "systems": 0,
        "square_vertices": 0,
        "installed_weight": 0,
        "descent_routes": 0,
        "output_routes": 0,
        "output_records": 0,
        "word_mass": 0,
        "column_incidence": 0,
    }

    for _ in range(30000):
        n_board = rng.randint(5, 100)
        s = rng.randint(1, 20)
        r_weights = [rng.randint(1, 1000) for _ in range(s)]
        r_total = sum(r_weights)
        epsilon = rng.uniform(0.2, 0.9)
        kappa = rng.uniform(0.01, epsilon * 0.9)

        f_weights = []
        word_totals = [0] * 12
        word_columns = [[0] * n_board for _ in range(12)]
        for r in r_weights:
            f = rng.randint(0, 2 * r + 20)
            f_weights.append(f)
            remaining = f
            while remaining > 0:
                w = rng.randint(1, remaining)
                remaining -= w
                word = rng.randrange(12)
                cols = rng.sample(range(n_board), 3)
                word_totals[word] += w
                for c in cols:
                    word_columns[word][c] += w
                counts["output_records"] += 1
        f_total = sum(f_weights)

        extra_destroyed = [rng.randint(0, r) for r in r_weights]
        xi = [f - r - extra for f, r, extra in zip(f_weights, r_weights, extra_destroyed)]
        assert all(x <= f - r for x, f, r in zip(xi, f_weights, r_weights))
        assert sum(xi) <= f_total - r_total

        if f_total <= (1 - epsilon) * r_total:
            assert sum(xi) <= -epsilon * r_total + 1e-9
            creator_cost = kappa * r_total
            assert creator_cost + sum(xi) <= -(epsilon - kappa) * r_total + 1e-9
            counts["descent_routes"] += 1
        else:
            assert max(word_totals) >= f_total / 12
            best_word = max(range(12), key=word_totals.__getitem__)
            best_col = max(word_columns[best_word])
            assert best_col >= 3 * word_totals[best_word] / n_board
            assert best_col > (1 - epsilon) * r_total / (4 * n_board)
            counts["output_routes"] += 1
            counts["word_mass"] += word_totals[best_word]
            counts["column_incidence"] += best_col

        theta = rng.uniform(0.05, 0.95)
        lam = rng.uniform(0.05, 3.0)
        d_sq = rng.randint(0, 100)
        m = rng.randint(1, 10**6)
        lower = (1 - theta) * lam * m / (16 * (d_sq + 1))
        r_for_bound = max(r_total, lower + 1e-6)
        assert (epsilon - kappa) * r_for_bound > (epsilon - kappa) * lower
        assert (1 - epsilon) * r_for_bound / 12 > (1 - epsilon) * lower / 12
        assert (1 - epsilon) * r_for_bound / (4 * n_board) > (1 - epsilon) * lower / (4 * n_board)

        counts["systems"] += 1
        counts["square_vertices"] += s
        counts["installed_weight"] += r_total

    print("SAS opposite-destroyer payment audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
