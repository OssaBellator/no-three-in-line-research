#!/usr/bin/env python3
"""Finite audit for GC2eq--GC2eu."""

from collections import defaultdict
from math import comb
import random

SEED = 20260727
TOL = 1e-10


def greedy_edge_coloring(edges):
    colors = {}
    for edge_id in sorted(
        range(len(edges)),
        key=lambda i: (
            -sum(
                1
                for j, other in enumerate(edges)
                if j != i and set(edges[i][:2]) & set(other[:2])
            ),
            i,
        ),
    ):
        used = {
            colors[j]
            for j, other in enumerate(edges)
            if j in colors and set(edges[edge_id][:2]) & set(other[:2])
        }
        color = 0
        while color in used:
            color += 1
        colors[edge_id] = color
    return colors


def falling(t, r):
    out = 1
    for j in range(r):
        out *= t - j
    return out


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(25000):
        n = rng.randint(3, 16)
        cells = list(range(n * n))
        label_cap = rng.randint(1, 6)
        address_stock = []

        # Unique decorated physical occurrences.
        for _candidate in range(rng.randint(3, min(220, label_cap * 140))):
            triple = tuple(sorted(rng.sample(cells, 3)))
            label = rng.randrange(label_cap)
            address_stock.append((triple, label))
        address_stock = sorted(set(address_stock))
        if not address_stock:
            continue

        birth = []
        for address in address_stock:
            weight = rng.randint(1, 10000)
            survives = bool(rng.getrandbits(1))
            birth.append((address, weight, survives))

        w_birth = sum(weight for _, weight, _ in birth)
        s_weight = sum(weight for _, weight, survives in birth if survives)
        p_weight = w_birth - s_weight
        assert w_birth == s_weight + p_weight
        counts["systems"] += 1
        counts["birth_lineages"] += len(birth)

        if p_weight * 2 >= w_birth:
            counts["payment_branches"] += 1
            continue

        surviving = [
            (address, weight)
            for address, weight, survives in birth
            if survives
        ]
        loads = [0] * (n * n)
        for (triple, _label), weight in surviving:
            for cell in triple:
                loads[cell] += weight
        anchor = max(range(n * n), key=loads.__getitem__)
        h_anchor = loads[anchor]
        assert h_anchor * n * n >= 3 * s_weight

        anchored = []
        pair_multiplicity = defaultdict(int)
        for (triple, label), weight in surviving:
            if anchor not in triple:
                continue
            outside = tuple(cell for cell in triple if cell != anchor)
            anchored.append((outside[0], outside[1], weight, triple, label))
            for other in outside:
                pair_multiplicity[other] += 1

        delta_cap = label_cap * (n * n - 2)
        assert max(pair_multiplicity.values(), default=0) <= delta_cap

        colors = greedy_edge_coloring(anchored)
        by_color = defaultdict(int)
        for edge_id, color in colors.items():
            by_color[color] += anchored[edge_id][2]
        star_weight = max(by_color.values(), default=0)
        assert star_weight * (2 * delta_cap - 1) >= h_anchor
        lower_star = 3 * w_birth / (2 * n * n * (2 * delta_cap - 1))
        assert star_weight > lower_star - TOL
        counts["survival_branches"] += 1
        counts["selected_star_lineages"] += sum(
            1 for edge_id in colors
            if colors[edge_id] == max(by_color, key=by_color.get)
        )

        if len(anchored) < 7 or star_weight <= 0:
            counts["unrealized_small_star_contracts"] += 1
            continue

        rho = rng.uniform(0.05, 1.0)
        epsilon = rng.uniform(0.05, 0.95)
        a = rho * star_weight * rng.uniform(1.0, 1.15)
        assert a + TOL >= rho * star_weight

        fixed = rng.random() * 1.8 * a
        rank_terms = [rng.random() * 0.9 * a for _ in range(3)]
        e_an = sum(rank_terms)

        if fixed + e_an <= (1 - epsilon) * a:
            descent = a - fixed - e_an
            assert descent + TOL >= epsilon * a
            integrated = (
                3 * epsilon * rho * w_birth
                / (2 * n * n * (2 * delta_cap - 1))
            )
            assert descent > integrated - TOL
            counts["descent_branches"] += 1
        else:
            threshold = (1 - epsilon) * a / 2
            assert fixed > threshold or e_an > threshold
            if fixed > threshold:
                integrated_fixed = (
                    3 * (1 - epsilon) * rho * w_birth
                    / (4 * n * n * (2 * delta_cap - 1))
                )
                assert fixed > integrated_fixed - TOL
                counts["fixed_switch_branches"] += 1
            else:
                assert e_an > threshold
                rank_index = max(range(3), key=rank_terms.__getitem__)
                rank_term = rank_terms[rank_index]
                assert rank_term + TOL >= e_an / 3
                r = rank_index + 1
                t = rng.randint(7, 18)
                t_r = rank_term * falling(t, r) / 128
                prescription_weight = t_r / falling(t, r)
                assert prescription_weight + TOL >= (
                    (1 - epsilon) * a / 768
                )
                k_tri = comb(n * n, 2)
                exact_weight = prescription_weight / k_tri
                integrated_exact = (
                    (1 - epsilon) * rho * w_birth
                    / (
                        512
                        * n
                        * n
                        * (2 * delta_cap - 1)
                        * k_tri
                    )
                )
                assert exact_weight > integrated_exact - TOL
                counts["exact_certificate_branches"] += 1

    print("GC finite-label star execution audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
