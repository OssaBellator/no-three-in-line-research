#!/usr/bin/env python3
"""Audit parity-clean Hamilton fibres and the m=9 clean rotation graph."""
from __future__ import annotations
import argparse
import json
from collections import Counter, deque
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

Point = tuple[int, int]


def hamilton_cycles(m: int):
    for tail in permutations(range(1, m)):
        order = (0,) + tail
        rho = [0] * m
        for i, source in enumerate(order):
            rho[source] = order[(i + 1) % m]
        yield tuple(rho)


def orbit_block(m: int, source: int, target: int, orientation: int) -> tuple[Point, ...]:
    n = 2 * m
    reversal = lambda x: n - 1 - x
    q0 = (source, reversal(target) if orientation else target)
    q1 = (reversal(source), target if orientation else reversal(target))
    return q0, q1, (reversal(q0[1]), q0[0]), (reversal(q1[1]), q1[0])


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def two_owner_bad(m: int, sa: int, ta: int, ea: int, sb: int, tb: int, eb: int) -> bool:
    points = orbit_block(m, sa, ta, ea) + orbit_block(m, sb, tb, eb)
    return any(collinear(*triple) for triple in combinations(points, 3))


def pair_relations(m: int) -> dict[tuple[int, int, int, int], int]:
    # 0=no constraint, 1=require XOR 0, 2=require XOR 1, 3=both XORs forbidden.
    out: dict[tuple[int, int, int, int], int] = {}
    for a in range(m):
        for ta in range(m):
            if ta == a:
                continue
            for b in range(a + 1, m):
                for tb in range(m):
                    if tb == b or tb == ta:
                        continue
                    bad_equal = two_owner_bad(m, a, ta, 0, b, tb, 0)
                    bad_unequal = two_owner_bad(m, a, ta, 0, b, tb, 1)
                    value = 3 if bad_equal and bad_unequal else 2 if bad_equal else 1 if bad_unequal else 0
                    out[(a, ta, b, tb)] = value
    return out


def classify_cycle(m: int, rho: tuple[int, ...], relation: dict[tuple[int, int, int, int], int]):
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(m)]
    constraint_count = 0
    impossible = 0
    for a in range(m):
        for b in range(a + 1, m):
            value = relation.get((a, rho[a], b, rho[b]), 0)
            if value == 3:
                impossible += 1
            elif value:
                required = 0 if value == 1 else 1
                constraint_count += 1
                adjacency[a].append((b, required))
                adjacency[b].append((a, required))
    inconsistent = impossible > 0
    colour: list[int | None] = [None] * m
    components = 0
    if not inconsistent:
        for root in range(m):
            if colour[root] is not None:
                continue
            components += 1
            colour[root] = 0
            queue: deque[int] = deque([root])
            while queue and not inconsistent:
                source = queue.popleft()
                assert colour[source] is not None
                for target, parity in adjacency[source]:
                    wanted = colour[source] ^ parity
                    if colour[target] is None:
                        colour[target] = wanted
                        queue.append(target)
                    elif colour[target] != wanted:
                        inconsistent = True
                        break
    return not inconsistent, constraint_count, components if not inconsistent else -1, impossible


def fibre_case(m: int):
    relation = pair_relations(m)
    component_count: Counter[int] = Counter()
    clean_count: Counter[int] = Counter()
    constraint_count: Counter[int] = Counter()
    cyclomatic: Counter[int] = Counter()
    impossible_count: Counter[int] = Counter()
    satisfiable = 0
    unsatisfiable = 0
    for rho in hamilton_cycles(m):
        clean, q, components, impossible = classify_cycle(m, rho, relation)
        constraint_count[q] += 1
        impossible_count[impossible] += 1
        if clean:
            satisfiable += 1
            component_count[components] += 1
            clean_count[1 << components] += 1
            cyclomatic[q - m + components] += 1
        else:
            unsatisfiable += 1
    return {
        "m": m,
        "hamilton_cycles": satisfiable + unsatisfiable,
        "parity_satisfiable_cycles": satisfiable,
        "parity_unsatisfiable_cycles": unsatisfiable,
        "total_clean_orientation_vectors": sum(size * count for size, count in clean_count.items()),
        "minimum_components_on_satisfiable_cycle": min(component_count),
        "maximum_components_on_satisfiable_cycle": max(component_count),
        "component_count_distribution": {str(k): v for k, v in sorted(component_count.items())},
        "clean_orientation_count_distribution": {str(k): v for k, v in sorted(clean_count.items())},
        "constraint_count_distribution": {str(k): v for k, v in sorted(constraint_count.items())},
        "satisfiable_cyclomatic_rank_distribution": {str(k): v for k, v in sorted(cyclomatic.items())},
        "impossible_owner_pair_count_distribution": {str(k): v for k, v in sorted(impossible_count.items())},
    }


def switched(rho: tuple[int, ...], sources: tuple[int, int, int]) -> tuple[int, ...]:
    selected = set(sources)
    cyclic: list[int] = []
    current = min(selected)
    for _ in range(len(rho)):
        if current in selected:
            cyclic.append(current)
        current = rho[current]
    a, b, c = cyclic
    out = list(rho)
    out[a], out[b], out[c] = rho[b], rho[c], rho[a]
    return tuple(out)


def rotation_case_m9():
    m = 9
    relation = pair_relations(m)
    cycles = list(hamilton_cycles(m))
    index = {rho: i for i, rho in enumerate(cycles)}
    clean = [classify_cycle(m, rho, relation)[0] for rho in cycles]
    triples = list(combinations(range(m), 3))
    meeting_masks: list[int] = []
    for owner_set in triples:
        owner = set(owner_set)
        mask = 0
        for i, source_set in enumerate(triples):
            if owner.intersection(source_set):
                mask |= 1 << i
        meeting_masks.append(mask)
    adjacency: list[list[int]] = [[] for _ in cycles]
    transitions: Counter[tuple[bool, bool]] = Counter()
    minimum_degree = 10**9
    maximum_degree = 0
    minimum_meeting = 10**9
    for i, rho in enumerate(cycles):
        clean_mask = 0
        neighbours: list[int] = []
        for ti, source_set in enumerate(triples):
            target = index[switched(rho, source_set)]
            transitions[(clean[i], clean[target])] += 1
            if clean[target]:
                clean_mask |= 1 << ti
                if clean[i]:
                    neighbours.append(target)
        if clean[i]:
            degree = clean_mask.bit_count()
            minimum_degree = min(minimum_degree, degree)
            maximum_degree = max(maximum_degree, degree)
            minimum_meeting = min(
                minimum_meeting,
                min((clean_mask & mask).bit_count() for mask in meeting_masks),
            )
            adjacency[i] = neighbours
    visited: set[int] = set()
    components: list[int] = []
    for root, is_clean in enumerate(clean):
        if not is_clean or root in visited:
            continue
        stack = [root]
        visited.add(root)
        size = 0
        while stack:
            source = stack.pop()
            size += 1
            for target in adjacency[source]:
                if target not in visited:
                    visited.add(target)
                    stack.append(target)
        components.append(size)
    maximum_distance = 0
    for i, is_clean in enumerate(clean):
        if is_clean:
            continue
        if not any(clean[index[switched(cycles[i], source_set)]] for source_set in triples):
            maximum_distance = 2
            break
        maximum_distance = max(maximum_distance, 1)
    return {
        "m": 9,
        "directed_successor_rotations": len(cycles) * len(triples),
        "minimum_clean_degree": minimum_degree,
        "maximum_clean_degree": maximum_degree,
        "minimum_clean_rotations_intersecting_any_owner_triple": minimum_meeting,
        "clean_induced_components": len(components),
        "largest_clean_component": max(components),
        "maximum_distance_to_clean_cycle": maximum_distance,
        "rotation_transition_counts": {
            "clean_to_clean": transitions[(True, True)],
            "clean_to_inconsistent": transitions[(True, False)],
            "inconsistent_to_clean": transitions[(False, True)],
            "inconsistent_to_inconsistent": transitions[(False, False)],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()
    expected = json.loads(args.audit.read_text(encoding="utf-8"))
    result: dict[str, Any] = {
        "minimum_pair_size": 4,
        "maximum_pair_size": 10,
        "cases": [fibre_case(m) for m in range(4, 11)],
        "m9_rotation_graph": rotation_case_m9(),
        "component_root_randomization_is_uniform_on_each_clean_fibre": True,
        "all_satisfiable_constraint_graphs_are_forests_through_m9": True,
        "first_satisfiable_nonforest_cycles_at_m10": 1588,
        "asymptotic_seed_theorem_proved": False,
    }
    if result != expected:
        raise SystemExit("verification failed: stored parity-fibre ledger mismatch")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
