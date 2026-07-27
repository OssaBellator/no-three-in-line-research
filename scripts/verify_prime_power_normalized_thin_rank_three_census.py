#!/usr/bin/env python3
"""Exhaustive checks for CMR1686--CMR1693."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import floor


Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


def partial_matchings(edges: set[Edge], side: int) -> list[Prescription]:
    adjacency: list[list[int]] = [[] for _ in range(side)]
    for left, right in edges:
        adjacency[left].append(right)
    for neighbours in adjacency:
        neighbours.sort()

    output: list[Prescription] = []

    def recurse(
        left: int,
        used_targets: set[int],
        current: list[Edge],
    ) -> None:
        if left == side:
            output.append(tuple(current))
            return
        recurse(left + 1, used_targets, current)
        for right in adjacency[left]:
            if right in used_targets:
                continue
            used_targets.add(right)
            current.append((left, right))
            recurse(left + 1, used_targets, current)
            current.pop()
            used_targets.remove(right)

    recurse(0, set(), [])
    return output


def perfect_matchings(edges: set[Edge], side: int) -> list[tuple[int, ...]]:
    return [
        permutation
        for permutation in permutations(range(side))
        if all((left, permutation[left]) in edges for left in range(side))
    ]


def canonical_deletion(deletion: Prescription, side: int) -> Prescription:
    residual = list(range(2, side))
    best: Prescription | None = None
    for image in permutations(residual):
        relabel = {0: 0, 1: 1}
        relabel.update(
            {residual[index]: image[index] for index in range(len(residual))}
        )
        transformed = tuple(
            sorted((relabel[left], relabel[right]) for left, right in deletion)
        )
        if best is None or transformed < best:
            best = transformed
    assert best is not None
    return best


def canonical_hosts(side: int) -> dict[Prescription, list[tuple[int, ...]]]:
    host = {
        (left, right)
        for left in range(side)
        for right in range(side)
        if left != right and (left, right) != (0, 1)
    }
    result: dict[Prescription, list[tuple[int, ...]]] = {}
    for deletion in partial_matchings(host, side):
        response_edges = host.difference(deletion)
        responses = perfect_matchings(response_edges, side)
        if not responses:
            continue
        canonical = canonical_deletion(deletion, side)
        if canonical not in result:
            result[canonical] = responses
    return result


def prescription_counts(
    responses: list[tuple[int, ...]],
    rank: int,
) -> Counter[Prescription]:
    counts: Counter[Prescription] = Counter()
    side = len(responses[0])
    for response in responses:
        for sources in combinations(range(side), rank):
            prescription = tuple(
                sorted((left, response[left]) for left in sources)
            )
            counts[prescription] += 1
    return counts


def main() -> None:
    expected = {
        3: (4, 4, Fraction(0, 1)),
        4: (448, 28, Fraction(1, 2)),
        5: (15_017, 0, Fraction(1, 4)),
    }
    host_counts = {3: 4, 4: 45, 5: 124}
    total_instances = 0
    forced_instances = 0
    capacity_checks = 0

    for side in (3, 4, 5):
        hosts = canonical_hosts(side)
        assert len(hosts) == host_counts[side]
        extendable = 0
        forced = 0
        maximum_nonforced = Fraction(0, 1)

        for responses in hosts.values():
            denominator = len(responses)
            counts = prescription_counts(responses, 3)
            extendable += len(counts)
            for numerator in counts.values():
                probability = Fraction(numerator, denominator)
                if numerator == denominator:
                    forced += 1
                else:
                    maximum_nonforced = max(
                        maximum_nonforced, probability
                    )

                if side == 4 and numerator != denominator:
                    assert numerator <= floor(Fraction(denominator, 2))
                    capacity_checks += 1
                if side == 5:
                    assert numerator <= floor(Fraction(denominator, 4))
                    capacity_checks += 1

        assert (extendable, forced, maximum_nonforced) == expected[side]
        total_instances += extendable
        forced_instances += forced

    assert total_instances == 15_473
    assert forced_instances == 32

    print(
        "verified normalized rank-three thin census: "
        f"{total_instances} extendable prescription instances, "
        f"{forced_instances} forced contractions and "
        f"{capacity_checks} exact numerator-cap checks"
    )


if __name__ == "__main__":
    main()
