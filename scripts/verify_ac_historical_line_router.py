#!/usr/bin/env python3
"""Finite audit for AC3hl--AC3hp."""

from __future__ import annotations

from itertools import combinations, permutations, product
from fractions import Fraction


def edges_on(n: int):
    return list(combinations(range(n), 2))


def closed_load(edge, chosen_edges, weights):
    x, y = edge
    return sum(
        weights[e]
        for e in chosen_edges
        if e == edge or x in e or y in e
    )


def greedy_matching(chosen_edges, weights):
    remaining = set(chosen_edges)
    selected = []
    while remaining:
        e = min(remaining)
        selected.append(e)
        x, y = e
        remaining = {
            f for f in remaining
            if not (x in f or y in f)
        }
    return selected


def verify_graph_router():
    systems = 0
    overloads = 0
    matching_cases = 0
    fixed_pair_cases = 0

    for n in range(3, 7):
        all_edges = edges_on(n)
        if n <= 4:
            masks = list(range(1, 1 << len(all_edges)))
        else:
            sparse = [m for m in range(1, 1 << len(all_edges)) if m.bit_count() <= 3]
            denser = [m for m in range(1, 1 << len(all_edges)) if 4 <= m.bit_count() <= 5][:200]
            masks = sparse + denser
        for mask in masks:
            chosen = [e for i, e in enumerate(all_edges) if (mask >> i) & 1]
            m = len(chosen)
            patterns = [
                tuple(1 for _ in range(m)),
                tuple(3 for _ in range(m)),
                tuple(1 + (i % 3) for i in range(m)),
                tuple(1 + ((i + 1) % 3) for i in range(m)),
                tuple(3 if i == 0 else 1 for i in range(m)),
            ]
            if m <= 3:
                patterns.extend(product(range(1, 4), repeat=m))
            for weight_word in dict.fromkeys(patterns):
                weights = dict(zip(chosen, weight_word))
                W = sum(weight_word)
                for K in range(1, 5):
                    systems += 1
                    bad = [
                        e for e in chosen
                        if closed_load(e, chosen, weights) > K * weights[e]
                    ]
                    if bad:
                        overloads += 1
                        e = bad[0]
                        x, y = e
                        mu_x = sum(weights[f] for f in chosen if x in f)
                        mu_y = sum(weights[f] for f in chosen if y in f)
                        assert max(mu_x, mu_y) * 2 > K * weights[e]
                        v = x if mu_x >= mu_y else y
                        M = max(mu_x, mu_y)
                        incident = [f for f in chosen if v in f]
                        d = len(incident)
                        if d <= 12:
                            assert max(weights[f] for f in incident) * 12 >= M
                        fixed_pair_cases += 1
                    else:
                        matching_cases += 1
                        M = greedy_matching(chosen, weights)
                        assert sum(weights[e] for e in M) * K >= W

    for d in range(1, 17):
        weight_patterns = [
            [1] * d,
            [3] * d,
            [1 + (i % 3) for i in range(d)],
            [3 if i == 0 else 1 for i in range(d)],
            [3 if i % 2 == 0 else 1 for i in range(d)],
        ]
        layer_patterns = [
            [0] * d,
            [1] * d,
            [i % 2 for i in range(d)],
            [(i // 2) % 2 for i in range(d)],
            [0 if i < d // 3 else 1 for i in range(d)],
        ]
        for weights in weight_patterns:
            total = sum(weights)
            if d <= 12:
                assert max(weights) * 12 >= total
            else:
                for layers in layer_patterns:
                    w0 = sum(w for w, ell in zip(weights, layers) if ell == 0)
                    w1 = total - w0
                    heavy_layer = 0 if w0 >= w1 else 1
                    heavy = max(w0, w1)
                    assert heavy * 2 >= total
                    selected = [w for w, ell in zip(weights, layers) if ell == heavy_layer]
                    if len(selected) < 7:
                        assert max(selected) * 6 >= heavy

    return systems, overloads, matching_cases, fixed_pair_cases


def verify_layer_incidence():
    checks = 0
    weight_patterns = {
        m: [
            tuple(1 + ((i + shift) % 3) for i in range(m))
            for shift in range(3)
        ] + [tuple(1 for _ in range(m)), tuple(3 for _ in range(m))]
        for m in range(1, 8)
    }
    for m in range(1, 8):
        for layer_pairs in product(((0, 0), (0, 1), (1, 0), (1, 1)), repeat=m):
            for weights in weight_patterns[m]:
                W = sum(weights)
                incidence = [
                    sum(w * pair.count(ell) for pair, w in zip(layer_pairs, weights))
                    for ell in (0, 1)
                ]
                ell = 0 if incidence[0] >= incidence[1] else 1
                represented = sum(
                    w for pair, w in zip(layer_pairs, weights) if ell in pair
                )
                assert incidence[ell] >= W
                assert 2 * represented >= incidence[ell]
                assert 2 * represented >= W
                if sum(1 for pair in layer_pairs if ell in pair) <= 6:
                    selected = [
                        w for pair, w in zip(layer_pairs, weights) if ell in pair
                    ]
                    if selected:
                        assert max(selected) * 6 >= represented
                checks += 1
    return checks


def allowed_permutations(t: int, blocker):
    out = []
    for pi in permutations(range(t)):
        good = True
        for i, j in enumerate(pi):
            if j == i or j == blocker[i]:
                good = False
                break
        if good:
            out.append(pi)
    return out


def verify_rematching():
    t = 7
    checks = 0
    blockers = 0
    states = 0
    partial_checks = 0

    blocker_representatives = [
        (1, 2, 3, 4, 5, 6, 0),
        (1, 2, 3, 4, 0, 6, 5),
        (1, 2, 3, 0, 5, 6, 4),
        (1, 2, 0, 4, 3, 6, 5),
    ]
    for blocker in blocker_representatives:
        blockers += 1
        allowed = allowed_permutations(t, blocker)
        assert allowed, blocker
        for pi in allowed:
            states += 1
            assert all(pi[i] != i for i in range(t))
            assert all(pi[i] != blocker[i] for i in range(t))
            checks += t

        total = len(allowed)
        nonforbidden = [
            (i, j)
            for i in range(t)
            for j in range(t)
            if j != i and j != blocker[i]
        ]
        for r in range(1, 4):
            samples = 0
            for Q in combinations(nonforbidden, r):
                rows = [i for i, _ in Q]
                cols = [j for _, j in Q]
                if len(set(rows)) < r or len(set(cols)) < r:
                    continue
                count = sum(all(pi[i] == j for i, j in Q) for pi in allowed)
                falling = 1
                for k in range(r):
                    falling *= t - k
                assert count * falling <= 128 * total
                partial_checks += 1
                samples += 1
                if samples >= 60:
                    break
    return blockers, states, checks, partial_checks


def verify_rank_and_constants():
    rank_checks = 0
    constant_checks = 0
    for D in range(1, 40):
        for E in product(range(0, 20), repeat=3):
            if sum(E) >= D:
                assert max(E) * 3 >= D
            rank_checks += 1
        for K in range(1, 8):
            for Kp in range(1, 8):
                W = 2 * K * D
                assert Fraction(D, 3 * Kp) == Fraction(W, 6 * K * Kp)
                assert Fraction(D, 9 * Kp) == Fraction(W, 18 * K * Kp)
                constant_checks += 1
    return rank_checks, constant_checks


def main():
    graph = verify_graph_router()
    layers = verify_layer_incidence()
    rematch = verify_rematching()
    ranks = verify_rank_and_constants()
    print("AC historical line router audit passed")
    print(f"weighted graph systems: {graph[0]}")
    print(f"overload systems: {graph[1]}")
    print(f"matching systems: {graph[2]}")
    print(f"fixed-pair systems: {graph[3]}")
    print(f"endpoint-layer incidence systems: {layers}")
    print(f"normalized blocker permutations: {rematch[0]}")
    print(f"allowed rematching states: {rematch[1]}")
    print(f"destroyed endpoint checks: {rematch[2]}")
    print(f"cylinder samples: {rematch[3]}")
    print(f"rank ledgers: {ranks[0]}")
    print(f"composition constants: {ranks[1]}")


if __name__ == "__main__":
    main()
