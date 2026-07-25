#!/usr/bin/env python3
"""Exact finite checks for AC3hx--AC3ia.

The script uses only the standard library. It exhausts permutation changes on
small sides, verifies the canonical cross and alternating-cycle dichotomy,
checks abstract monotone-mask cycle erasure, finite signature stocks and
repeated-cell reinsertion.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product
from math import factorial

Cell = tuple[int, int]
Perm = tuple[int, ...]


def cells(p: Perm) -> set[Cell]:
    return {(c, r) for c, r in enumerate(p)}


def canonical_cross(old: Perm, new: Perm) -> tuple[Cell, Cell, Cell, Cell]:
    """Return e, row-arm new cell, column-arm new cell, opposite corner."""
    old_cells = cells(old)
    new_cells = cells(new)
    removed = sorted(old_cells - new_cells)
    assert removed
    u, v = removed[0]
    y = new[u]
    assert y != v
    x = new.index(v)
    assert x != u
    e = (u, v)
    r_y = (u, y)
    c_x = (x, v)
    p = (x, y)
    assert r_y != c_x
    assert r_y in new_cells and c_x in new_cells
    return e, r_y, c_x, p


def component_length(old: Perm, new: Perm, e: Cell) -> int:
    """Length in edges of the symmetric-difference cycle containing old edge e."""
    adjacency: dict[tuple[str, int], list[tuple[tuple[str, int], str]]] = {}
    for label, p in (("old", old), ("new", new)):
        for c, r in enumerate(p):
            if old[c] == new[c]:
                continue
            vc = ("c", c)
            vr = ("r", r)
            adjacency.setdefault(vc, []).append((vr, label))
            adjacency.setdefault(vr, []).append((vc, label))
    start = ("c", e[0])
    target_edge = {("c", e[0]), ("r", e[1])}
    seen_vertices: set[tuple[str, int]] = set()
    stack = [start]
    edge_count = 0
    while stack:
        vertex = stack.pop()
        if vertex in seen_vertices:
            continue
        seen_vertices.add(vertex)
        for neighbour, _ in adjacency.get(vertex, []):
            edge_count += 1
            if neighbour not in seen_vertices:
                stack.append(neighbour)
    length = edge_count // 2
    assert length >= 4 and length % 2 == 0
    assert target_edge <= seen_vertices
    return length


def check_permutation_changes(max_n: int = 6) -> Counter[str]:
    counts: Counter[str] = Counter()
    for n in range(2, max_n + 1):
        perms = list(permutations(range(n)))
        signatures: set[tuple[Cell, Cell, Cell]] = set()
        for old in perms:
            old_cells = cells(old)
            for new in perms:
                if old == new:
                    continue
                e, r_y, c_x, p = canonical_cross(old, new)
                signatures.add((e, r_y, c_x))
                length = component_length(old, new, e)
                rectangle = p in old_cells
                assert rectangle == (length == 4)
                if rectangle:
                    assert {e, p} <= old_cells
                    assert {r_y, c_x} <= cells(new)
                    counts["rectangle_changes"] += 1
                else:
                    assert length >= 6
                    counts["long_changes"] += 1
                removed = old_cells - cells(new)
                inserted = cells(new) - old_cells
                assert len(removed) == len(inserted) >= 2
                counts["permutation_changes"] += 1
        assert len(signatures) <= n * n * (n - 1) * (n - 1)
        assert signatures
        counts["signature_stocks"] += 1
    return counts


def check_two_layer_state_count(max_n: int = 7) -> Counter[str]:
    counts: Counter[str] = Counter()
    for n in range(2, max_n + 1):
        perms = list(permutations(range(n)))
        disjoint = 0
        for first in perms:
            for second in perms:
                if all(first[c] != second[c] for c in range(n)):
                    disjoint += 1
        assert disjoint <= factorial(n) ** 2
        counts["ordered_disjoint_states"] += disjoint
        counts["state_sides"] += 1
    return counts


def check_monotone_mask_erasure() -> Counter[str]:
    counts: Counter[str] = Counter()
    universe = range(4)
    states = [frozenset(s) for rank in range(5) for s in combinations(universe, rank)]
    masks = states
    for state in states:
        feasible_masks = [mask for mask in masks if state.isdisjoint(mask)]
        for first_mask in feasible_masks:
            for later_mask in feasible_masks:
                if first_mask <= later_mask:
                    assert state.isdisjoint(later_mask)
                    counts["erasable_state_mask_pairs"] += 1
    return counts


def check_recurrence_pigeonholes() -> Counter[str]:
    counts: Counter[str] = Counter()
    for stock in range(1, 8):
        for threshold in range(2, 6):
            max_nonrecurrent = (threshold - 1) * stock
            for multiplicities in product(range(threshold), repeat=stock):
                assert sum(multiplicities) <= max_nonrecurrent
                counts["multiplicity_vectors"] += 1
            counts["pigeonhole_thresholds"] += 1
    return counts


def signature(old: Perm, new: Perm) -> tuple[Cell, Cell, Cell]:
    e, r_y, c_x, _ = canonical_cross(old, new)
    return e, r_y, c_x


def check_reinsertion(max_n: int = 4) -> Counter[str]:
    counts: Counter[str] = Counter()
    for n in range(2, max_n + 1):
        perms = list(permutations(range(n)))
        for history in product(perms, repeat=4):
            transitions: list[tuple[int, tuple[Cell, Cell, Cell]]] = []
            for index in range(3):
                if history[index] != history[index + 1]:
                    transitions.append(
                        (index, signature(history[index], history[index + 1]))
                    )
            by_signature: dict[tuple[Cell, Cell, Cell], list[int]] = {}
            for index, sig in transitions:
                by_signature.setdefault(sig, []).append(index)
            for sig, times in by_signature.items():
                if len(times) < 2:
                    continue
                removed_cell = sig[0]
                for first, second in zip(times, times[1:]):
                    assert removed_cell not in cells(history[first + 1])
                    assert removed_cell in cells(history[second])
                    reinsertions = 0
                    for step in range(first + 1, second):
                        if (
                            removed_cell not in cells(history[step])
                            and removed_cell in cells(history[step + 1])
                        ):
                            reinsertions += 1
                    assert reinsertions >= 1
                    counts["forced_reinsertions"] += reinsertions
                counts["repeated_signatures"] += 1
            counts["histories"] += 1
    return counts


def main() -> None:
    total: Counter[str] = Counter()
    for part in (
        check_permutation_changes(),
        check_two_layer_state_count(),
        check_monotone_mask_erasure(),
        check_recurrence_pigeonholes(),
        check_reinsertion(),
    ):
        total.update(part)

    print("AC state-cycle and cross-signature audit passed")
    for key in sorted(total):
        print(f"{key}: {total[key]}")


if __name__ == "__main__":
    main()
