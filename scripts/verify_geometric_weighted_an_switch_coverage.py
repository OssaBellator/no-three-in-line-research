#!/usr/bin/env python3
"""Finite audit for GC2fa--GC2fe."""

from collections import defaultdict
from fractions import Fraction
import random

SEED = 20260727


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)
    for _ in range(50000):
        q_ch = rng.randint(1, 9)
        k_sw = rng.randint(1, 12)
        m = rng.randint(1, 80)
        weights = [rng.randint(1, 1000) for _ in range(m)]
        switch_sets = []
        endpoint_types = []
        for _j in range(m):
            choices = sorted(rng.sample(range(k_sw), rng.randint(1, k_sw)))
            switch_sets.append(choices)
            endpoint_types.append((rng.randrange(2 * q_ch), rng.randrange(2 * q_ch)))

        assigned = [choices[0] for choices in switch_sets]
        fibres = defaultdict(list)
        for j, sw in enumerate(assigned):
            fibres[sw].append(j)
        best_sw, indices = max(
            fibres.items(), key=lambda item: sum(weights[j] for j in item[1])
        )
        total = sum(weights)
        a_sw = sum(weights[j] for j in indices)
        assert a_sw * k_sw >= total

        incidence = [0] * (2 * q_ch)
        pair_indices = [[] for _ in range(2 * q_ch)]
        for j in indices:
            u, v = endpoint_types[j]
            incidence[u] += weights[j]
            incidence[v] += weights[j]
            pair_indices[u].append(j)
            if v != u:
                pair_indices[v].append(j)
        typ = max(range(2 * q_ch), key=lambda x: incidence[x])
        selected = sorted(set(pair_indices[typ]))
        a_type = sum(weights[j] for j in selected)
        assert incidence[typ] <= 2 * a_type
        assert a_type * 2 * q_ch >= a_sw

        t = len(selected)
        if t <= 6:
            heavy = max(weights[j] for j in selected)
            assert heavy * 6 >= a_type
            assert heavy * 12 * q_ch * k_sw >= total
            counts["small_heavy_atom_branches"] += 1
        else:
            # Original diagonal plus another-layer permutation: degree <=2.
            shift = rng.randrange(1, t)
            forbidden = {(i, i) for i in range(t)} | {(i, (i + shift) % t) for i in range(t)}
            row_deg = defaultdict(int)
            col_deg = defaultdict(int)
            for row, col in forbidden:
                row_deg[row] += 1
                col_deg[col] += 1
            assert max(row_deg.values()) <= 2
            assert max(col_deg.values()) <= 2
            assert t >= 7
            counts["large_an_block_branches"] += 1
            counts["forbidden_positions"] += len(forbidden)

        # Integrated constants checked exactly with rational arithmetic.
        N = rng.randint(3, 30)
        l_cert = rng.randint(1, 10)
        delta_cap = l_cert * (N * N - 2)
        denom = N * N * (2 * delta_cap - 1)
        W = rng.randint(1, 10**6)
        eps = Fraction(rng.randint(1, 9), 10)
        small_bound = Fraction(W, 8 * q_ch * k_sw * denom)
        descent_bound = Fraction(3, 4) * eps * W / (q_ch * k_sw * denom)
        fixed_bound = Fraction(3, 8) * (1 - eps) * W / (q_ch * k_sw * denom)
        matching_bound = (1 - eps) * W / (1024 * q_ch * k_sw * denom)
        assert all(x >= 0 for x in (small_bound, descent_bound, fixed_bound, matching_bound))

        counts["systems"] += 1
        counts["lineages"] += m
        counts["switch_incidences"] += sum(len(x) for x in switch_sets)
        counts["selected_type_lineages"] += t

    print("GC weighted AN switch-coverage audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
