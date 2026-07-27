#!/usr/bin/env python3
"""Finite audit for GC2fk--GC2fo."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb
import random

SEED = 20260727


def random_permutation(n, rng):
    values = list(range(n))
    rng.shuffle(values)
    return values


def legal_donors(p1, p2, row):
    out = []
    for s in range(len(p1)):
        if s == row:
            continue
        if p1[s] == p2[row] or p1[row] == p2[s]:
            continue
        out.append(s)
    return out


def distribute(total, slots, rng):
    values = [0] * slots
    for _ in range(total):
        values[rng.randrange(slots)] += 1
    return values


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(60000):
        n = rng.randint(4, 13)
        while True:
            p1 = random_permutation(n, rng)
            p2 = random_permutation(n, rng)
            if all(p1[r] != p2[r] for r in range(n)):
                break

        row = rng.randrange(n)
        donors = legal_donors(p1, p2, row)
        if not donors:
            counts["empty donor reservoirs"] += 1
            continue

        chosen = donors[:]
        rng.shuffle(chosen)
        chosen = chosen[: rng.randint(1, len(chosen))]
        d = len(chosen)
        x = (row, p1[row])
        fixed_before = {(r, p1[r]) for r in range(n)} | {(r, p2[r]) for r in range(n)}

        for s in chosen:
            p1_after = p1[:]
            p1_after[row], p1_after[s] = p1_after[s], p1_after[row]
            assert sorted(p1_after) == list(range(n))
            assert all(p1_after[r] != p2[r] for r in range(n))
            after = {(r, p1_after[r]) for r in range(n)} | {(r, p2[r]) for r in range(n)}
            assert x not in after
            moved = {(row, p1_after[row]), (s, p1_after[s])}
            assert fixed_before - {(row, p1[row]), (s, p1[s])} == after - moved
            counts["legal donor swaps"] += 1

        board = n * n
        k1 = 2 * comb(board, 2)
        k2 = board
        k_swap = k1 + k2
        h = rng.randint(20, 400)
        epsilon = Fraction(rng.randint(1, 9), 10)
        threshold = Fraction(d * (1 - epsilon) * h)

        slot_cap = min(k_swap, rng.randint(4, 40))
        total_slots = d * slot_cap
        high = rng.random() < 0.5
        if high:
            total = int(threshold) + 1 + rng.randint(0, max(1, d * 5))
        else:
            total = rng.randint(0, int(threshold))
        weights = distribute(total, total_slots, rng)
        e_s = [sum(weights[s * slot_cap : (s + 1) * slot_cap]) for s in range(d)]
        e_bar = Fraction(sum(e_s), d)
        deltas = [value - h for value in e_s]

        if e_bar <= (1 - epsilon) * h:
            assert min(deltas) <= -epsilon * h
            counts["average descent branches"] += 1
        else:
            assert max(weights) > Fraction((1 - epsilon) * h, k_swap)
            counts["exact feedback branches"] += 1
            counts["feedback weight units"] += max(weights)

        q_ch = rng.randint(1, 5)
        l_cert = rng.randint(1, 6)
        delta_cap = l_cert * (board - 2)
        w_b = rng.randint(1, 2000)
        heavy_bound = Fraction(w_b, 8 * q_ch * board * (2 * delta_cap - 1))
        h_exact = heavy_bound + Fraction(rng.randint(1, 20), 20)
        descent_bound = epsilon * heavy_bound
        feedback_bound = (1 - epsilon) * heavy_bound / k_swap
        assert epsilon * h_exact > descent_bound
        assert (1 - epsilon) * h_exact / k_swap > feedback_bound

        counts["systems"] += 1
        counts["donor operations"] += d
        counts["collateral slots sampled"] += total_slots

    print("GC single-lineage donor-swap audit passed")
    for key in sorted(counts):
        print(f"  {key}: {counts[key]}")


if __name__ == "__main__":
    main()
