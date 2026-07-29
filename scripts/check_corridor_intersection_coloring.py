#!/usr/bin/env python3
"""Finite coloring audits for PP3byf--PP3byh."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import ceil, floor, log2


def cyclic_distance(m: int, u: int, v: int) -> int:
    return min((v - u) % m, (u - v) % m)


def short_arc(m: int, u: int, v: int) -> frozenset[int]:
    forward = (v - u) % m
    backward = (u - v) % m
    if forward <= backward:
        return frozenset((u + step) % m for step in range(forward + 1))
    return frozenset((u - step) % m for step in range(backward + 1))


def corridor(m: int, A: tuple[int, int], B: tuple[int, int]) -> frozenset[int]:
    return short_arc(m, *A) | short_arc(m, *B)


def color_corridors(corridors: list[frozenset[int]]) -> list[int]:
    vertex_colors: dict[int, set[int]] = {}
    colors: list[int] = []
    for cor in corridors:
        forbidden: set[int] = set()
        for vertex in cor:
            forbidden |= vertex_colors.get(vertex, set())
        color = 0
        while color in forbidden:
            color += 1
        colors.append(color)
        for vertex in cor:
            vertex_colors.setdefault(vertex, set()).add(color)
    return colors


def main() -> None:
    by_type: dict[tuple[int, int, int], list[frozenset[int]]] = {}
    configurations = 0
    for m in range(5, 13):
        for leaves in combinations(range(m), 4):
            for A_indices in combinations(range(4), 2):
                A_set = set(A_indices)
                A = tuple(leaves[i] for i in A_indices)
                B = tuple(leaves[i] for i in range(4) if i not in A_set)
                if A[0] > B[0]:
                    continue
                j_a = floor(log2(cyclic_distance(m, *A)))
                j_b = floor(log2(cyclic_distance(m, *B)))
                key = (m, min(j_a, j_b), max(j_a, j_b))
                by_type.setdefault(key, []).append(corridor(m, A, B))
                configurations += 1

    maximum_colors = 0
    maximum_bound = 0
    types_checked = 0
    for key, corridors in by_type.items():
        m, j_a, j_b = key
        s_tau = 2 ** (j_a + 1) + 2 ** (j_b + 1)
        Delta = max(
            sum(vertex in cor for cor in corridors)
            for vertex in range(m)
        )
        colors = color_corridors(corridors)
        color_count = 1 + max(colors)
        bound = s_tau * (Delta - 1) + 1
        assert color_count <= bound

        for color in range(color_count):
            class_corridors = [cor for cor, assigned in zip(corridors, colors) if assigned == color]
            for first, second in combinations(class_corridors, 2):
                assert first.isdisjoint(second)

        weights = [Fraction((7 * index) % 11 + 1, 5) for index in range(len(corridors))]
        W = sum(weights, Fraction(0))
        class_weights = [
            sum((weight for weight, assigned in zip(weights, colors) if assigned == color), Fraction(0))
            for color in range(color_count)
        ]
        assert max(class_weights) * bound >= W
        largest_class = max(colors.count(color) for color in range(color_count))
        assert largest_class >= ceil(Fraction(len(corridors), bound))

        for index, cor in enumerate(corridors):
            degree = sum(
                bool(cor & other)
                for other_index, other in enumerate(corridors)
                if other_index != index
            )
            assert degree <= len(cor) * (Delta - 1) <= s_tau * (Delta - 1)

        maximum_colors = max(maximum_colors, color_count)
        maximum_bound = max(maximum_bound, bound)
        types_checked += 1

    print({
        "all_checks_passed": True,
        "configurations_checked": configurations,
        "dyadic_types_checked": types_checked,
        "maximum_colors_used": maximum_colors,
        "maximum_theorem_bound": maximum_bound,
    })


if __name__ == "__main__":
    main()
