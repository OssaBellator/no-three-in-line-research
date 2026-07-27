#!/usr/bin/env python3
"""Finite audit for SAS5fw--SAS5ga."""

from collections import defaultdict
from fractions import Fraction
import random

SEED = 20260727


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for system_index in range(100000):
        square_count = rng.randint(1, 18)
        lam = Fraction(rng.randint(1, 20), 10)
        theta = Fraction(rng.randint(1, 9), 10)
        d_sq = rng.randint(0, 30)

        h_values = [rng.randint(1, 20) for _ in range(square_count)]
        h_j = sum(h_values)
        matched_weight = h_j * (d_sq + 1)

        mode = system_index % 4
        if mode == 0:
            # Low-barrier branch.
            deltas = []
            for h in h_values:
                cap = (lam * h).numerator // (lam * h).denominator
                deltas.append(rng.randint(0, cap))
            assert sum(h_values) >= Fraction(matched_weight, 2 * (d_sq + 1))
            assert sum(deltas) <= lam * sum(h_values)
            counts["low_barrier_systems"] += 1
            counts["low_matched_weight"] += h_j
            continue

        # High branch: every square is high.
        p_total = 0
        n_total = 0
        cfin_total = 0
        barrier_total = 0
        cminus_total = 0
        exact_negative_ids = set()

        for square_id, h in enumerate(h_values):
            delta_target = (lam * h).numerator // (lam * h).denominator + 1

            if mode == 1:
                # Neutral-heavy final-positive bank.
                p = rng.randint(0, 3)
                n_sigma = delta_target + rng.randint(2, 12)
                n_tau = delta_target + rng.randint(2, 12)
                current_only = max(0, p + n_sigma + n_tau - delta_target - rng.randint(0, 3))
            elif mode == 2:
                # Composed-heavy with a large aggregate barrier.
                p = 3 * delta_target + rng.randint(5, 20)
                n_sigma = rng.randint(0, 2)
                n_tau = rng.randint(0, 2)
                # Keep the final barrier comparable to P.
                current_only = rng.randint(0, max(0, p // 4))
            else:
                # Composed-heavy with small barrier density relative to P,
                # forcing negative mixed collateral.
                p = max(
                    4 * delta_target + 10,
                    (delta_target * theta.denominator) // max(theta.numerator, 1) + 20,
                )
                n_sigma = rng.randint(0, 2)
                n_tau = rng.randint(0, 2)
                current_only = p + n_sigma + n_tau - delta_target

            final_positive_total = p + n_sigma + n_tau
            delta_square = final_positive_total - current_only
            assert Fraction(delta_square, 1) > lam * h
            assert delta_square >= 0

            # Single-swap-only negative tables make both base swaps nonnegative.
            neg_sigma = max(0, current_only - n_sigma) + rng.randint(0, 3)
            neg_tau = max(0, current_only - n_tau) + rng.randint(0, 3)
            delta_sigma = n_sigma + neg_sigma - current_only
            delta_tau = n_tau + neg_tau - current_only
            assert delta_sigma >= 0
            assert delta_tau >= 0

            u_plus = current_only  # current-only positive-curvature tables
            c_minus = neg_sigma + neg_tau
            assert delta_square == delta_sigma + delta_tau + p + u_plus - c_minus
            assert c_minus >= p - delta_square

            for j in range(c_minus):
                record_id = (square_id, j)
                assert record_id not in exact_negative_ids
                exact_negative_ids.add(record_id)

            p_total += p
            n_total += n_sigma + n_tau
            cfin_total += final_positive_total
            barrier_total += delta_square
            cminus_total += c_minus

            counts["square_vertices"] += 1
            counts["composed_only_weight"] += p
            counts["neutral_weight"] += n_sigma + n_tau
            counts["negative_collateral_weight"] += c_minus

        assert cfin_total == p_total + n_total
        assert Fraction(cfin_total, 1) > lam * h_j / 2
        assert cminus_total >= p_total - barrier_total
        assert len(exact_negative_ids) == cminus_total

        generic_threshold = lam * matched_weight / (4 * (d_sq + 1))

        if Fraction(n_total, 1) >= Fraction(cfin_total, 2):
            assert Fraction(n_total, 1) > lam * h_j / 4
            assert Fraction(n_total, 1) > generic_threshold
            counts["neutral_router_systems"] += 1
        else:
            assert Fraction(p_total, 1) > lam * h_j / 4
            assert Fraction(p_total, 1) > generic_threshold
            if Fraction(barrier_total, 1) >= theta * p_total:
                assert Fraction(barrier_total, 1) > theta * lam * h_j / 4
                assert Fraction(barrier_total, 1) > theta * generic_threshold
                counts["aggregate_barrier_systems"] += 1
            else:
                assert Fraction(cminus_total, 1) > (1 - theta) * p_total
                assert Fraction(cminus_total, 1) > (1 - theta) * lam * h_j / 4
                assert Fraction(cminus_total, 1) > (1 - theta) * generic_threshold
                counts["negative_collateral_systems"] += 1

        counts["high_barrier_systems"] += 1
        counts["final_positive_weight"] += cfin_total
        counts["barrier_weight"] += barrier_total

    print("SAS aggregate final-output payment audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
