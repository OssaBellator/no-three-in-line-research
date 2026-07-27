#!/usr/bin/env python3
"""Verify OP4y--OP4ac: source-coset types and exact I6 amplification."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product


TYPE_COUNT = {1: 1, 2: 3, 3: 5}


def component_type(arcs):
    out = dict(arcs)
    indegree = Counter(v for _, v in arcs)
    vertices = set(out) | set(indegree)
    seen = set()
    components = []

    for vertex in sorted(vertices):
        if vertex in seen or indegree[vertex] != 0 or vertex not in out:
            continue
        current = vertex
        length = 0
        while current in out and current not in seen:
            seen.add(current)
            current = out[current]
            length += 1
        seen.add(current)
        components.append(("P", length))

    for vertex in sorted(vertices):
        if vertex in seen:
            continue
        current = vertex
        length = 0
        while current not in seen:
            seen.add(current)
            current = out[current]
            length += 1
        components.append(("C", length))
    return tuple(sorted(components))


def falling(value, rank):
    result = 1
    for offset in range(rank):
        result *= value - offset
    return result


def verify_type_dictionary(size=7):
    checks = 0
    type_sets = defaultdict(set)
    for rank in (1, 2, 3):
        for sources in combinations(range(size), rank):
            for targets in permutations(range(size), rank):
                if len(set(targets)) < rank:
                    continue
                arcs = tuple(zip(sources, targets))
                if any(source == target for source, target in arcs):
                    continue
                type_sets[rank].add(component_type(arcs))
                checks += 1
    assert {rank: len(types) for rank, types in type_sets.items()} == TYPE_COUNT
    return checks


def verify_i6(m, h):
    states = [
        (perm, shifts)
        for perm in permutations(range(m))
        for shifts in product(range(h), repeat=m)
    ]

    checks = 0
    for rank in range(1, min(3, m) + 1):
        for sources in combinations(range(m), rank):
            for targets in permutations(range(m), rank):
                if len(set(targets)) < rank:
                    continue
                for prescribed_shifts in product(range(h), repeat=rank):
                    count = sum(
                        all(
                            perm[source] == target and shifts[source] == shift
                            for source, target, shift in zip(
                                sources, targets, prescribed_shifts, strict=True
                            )
                        )
                        for perm, shifts in states
                    )
                    expected = len(states) // (falling(m, rank) * h**rank)
                    assert count == expected
                    checks += 1
    return len(states), checks


def verify_amplification():
    checks = 0
    for m in range(1, 5):
        for h in range(1, 5):
            for rank in range(1, min(3, m) + 1):
                probability = Fraction(1, falling(m, rank) * h**rank)
                nu = TYPE_COUNT[rank]
                for labels in range(1, 6):
                    for gain in range(1, 20):
                        expected_class = Fraction(gain, 4 * nu * labels)
                        raw = expected_class / probability
                        target = Fraction(
                            gain * falling(m, rank) * h**rank,
                            4 * nu * labels,
                        )
                        assert raw == target
                        checks += 1
    return checks


def main():
    type_checks = verify_type_dictionary()
    state_checks = prescription_checks = 0
    for m, h in ((1, 3), (2, 3), (3, 2), (4, 2)):
        states, checks = verify_i6(m, h)
        state_checks += states
        prescription_checks += checks
    amplification = verify_amplification()
    print(
        "Orbit-phase source-coset types: verified "
        f"{type_checks} type instances, {state_checks} I6 states, "
        f"{prescription_checks} exact prescriptions, and "
        f"{amplification} amplification identities"
    )


if __name__ == "__main__":
    main()
