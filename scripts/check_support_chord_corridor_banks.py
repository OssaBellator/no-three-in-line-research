#!/usr/bin/env python3
"""Finite corridor audits for PP3bxm--PP3bxo."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import ceil, floor, log2, sqrt


def cyclic_distance(m: int, u: int, v: int) -> int:
    forward = (v - u) % m
    backward = (u - v) % m
    return min(forward, backward)


def short_arc(m: int, u: int, v: int) -> frozenset[int]:
    forward_distance = (v - u) % m
    backward_distance = (u - v) % m
    if forward_distance <= backward_distance:
        return frozenset((u + step) % m for step in range(forward_distance + 1))
    return frozenset((u - step) % m for step in range(backward_distance + 1))


def corridor(m: int, A: tuple[int, int], B: tuple[int, int]) -> frozenset[int]:
    return short_arc(m, *A) | short_arc(m, *B)


def greedy_bank(
    states: list[tuple[frozenset[int], Fraction]],
) -> list[int]:
    remaining = set(range(len(states)))
    selected: list[int] = []
    while remaining:
        index = min(remaining)
        selected.append(index)
        chosen = states[index][0]
        remaining = {
            other for other in remaining
            if states[other][0].isdisjoint(chosen)
        }
    return selected


def main() -> None:
    configurations_checked = 0
    by_type: dict[tuple[int, int, int], list[frozenset[int]]] = {}
    for m in range(5, 13):
        vertices = range(m)
        for leaves in combinations(vertices, 4):
            for A_indices in combinations(range(4), 2):
                A_index_set = set(A_indices)
                A = tuple(leaves[i] for i in A_indices)
                B = tuple(leaves[i] for i in range(4) if i not in A_index_set)
                if A[0] > B[0]:
                    continue
                delta_a = cyclic_distance(m, *A)
                delta_b = cyclic_distance(m, *B)
                j_a = floor(log2(delta_a))
                j_b = floor(log2(delta_b))
                cor = corridor(m, A, B)
                ell = 2 ** (j_a + 1) + 2 ** (j_b + 1)
                assert len(cor) <= ell
                assert set(A + B) <= cor
                key = (m, min(j_a, j_b), max(j_a, j_b))
                by_type.setdefault(key, []).append(cor)
                configurations_checked += 1

    candidate_key = max(by_type, key=lambda key: len(by_type[key]))
    corridors = by_type[candidate_key][:12]
    weights = [Fraction((3 * i) % 7 + 1, 5) for i in range(len(corridors))]
    states = list(zip(corridors, weights))
    W = sum(weights, Fraction(0))
    M = max(weights)
    _, j_a, j_b = candidate_key
    ell = 2 ** (j_a + 1) + 2 ** (j_b + 1)

    loads: dict[int, Fraction] = {}
    for cor, weight in states:
        for vertex in cor:
            loads[vertex] = loads.get(vertex, Fraction(0)) + weight

    q_squared = W / (M * ell)
    q = sqrt(float(q_squared))
    bank = greedy_bank(states)

    exact_H0 = max(loads.values())
    exact_bank = greedy_bank(states)
    assert len(exact_bank) >= ceil(W / (ell * exact_H0))
    for i, j in combinations(exact_bank, 2):
        assert states[i][0].isdisjoint(states[j][0])

    max_normalized_load = max(loads.values()) / M
    if max_normalized_load * max_normalized_load <= q_squared:
        assert len(bank) >= ceil(q)

    print({
        "all_checks_passed": True,
        "configurations_checked": configurations_checked,
        "weighted_type": candidate_key,
        "weighted_states": len(states),
        "total_weight": str(W),
        "ell": ell,
        "maximum_normalized_vertex_load": str(max_normalized_load),
        "greedy_bank_size": len(bank),
    })


if __name__ == "__main__":
    main()
