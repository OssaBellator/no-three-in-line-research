#!/usr/bin/env python3
"""Exact audits for PP3bxw--PP3bxy."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def nonempty_subsets(items: list[str]):
    for size in range(1, len(items) + 1):
        yield from combinations(items, size)


def exact_fractional_load(reservoirs: dict[str, set[str]]) -> Fraction:
    sources = sorted(reservoirs)
    return max(
        Fraction(len(A), len(set().union(*(reservoirs[x] for x in A))))
        for A in nonempty_subsets(sources)
    )


def uniform_load(reservoirs: dict[str, set[str]]) -> Fraction:
    targets = set().union(*reservoirs.values())
    return max(
        sum(
            (Fraction(1, len(reservoirs[x])) for x in reservoirs if y in reservoirs[x]),
            Fraction(0),
        )
        for y in targets
    )


def main() -> None:
    bounded = {
        "P0": {"a0", "a1", "shared01"},
        "P1": {"b0", "b1", "shared01"},
        "P2": {"c0", "c1", "c2"},
        "P3": {"d0", "d1", "d2", "d3"},
    }
    q = min(map(len, bounded.values()))
    multiplicities = {
        y: sum(y in targets for targets in bounded.values())
        for y in set().union(*bounded.values())
    }
    h = max(multiplicities.values())
    load = uniform_load(bounded)
    assert load <= Fraction(h, q)
    assert exact_fractional_load(bounded) <= Fraction(h, q)

    core = {"core-left", "core-right"}
    petals = {
        "P0": {"p0a", "p0b"},
        "P1": {"p1a", "p1b"},
        "P2": {"p2a", "p2b"},
        "P3": {"p3a", "p3b"},
    }
    boundary_sets = {source: core | petal for source, petal in petals.items()}
    for first, second in combinations(boundary_sets, 2):
        assert boundary_sets[first] & boundary_sets[second] == core
        assert petals[first].isdisjoint(petals[second])

    degrees = {"P0": 2, "P1": 3, "P2": 4, "P3": 5}
    marked: dict[str, set[str]] = {}
    marker: dict[str, str] = {}
    for source, degree in degrees.items():
        petal = sorted(petals[source])
        targets = set()
        for index in range(degree):
            mark = petal[index % len(petal)]
            target = f"target:{mark}:{index}"
            targets.add(target)
            marker[target] = mark
        marked[source] = targets

    for source, targets in marked.items():
        assert all(marker[target] in petals[source] for target in targets)
    for first, second in combinations(marked, 2):
        assert marked[first].isdisjoint(marked[second])

    exact = exact_fractional_load(marked)
    predicted = Fraction(1, min(degrees.values()))
    assert exact == predicted
    assert uniform_load(marked) == predicted

    for target, multiplicity in multiplicities.items():
        column = sum(
            (Fraction(1, len(bounded[source])) for source in bounded if target in bounded[source]),
            Fraction(0),
        )
        assert column <= Fraction(multiplicity, q) <= Fraction(h, q)

    print({
        "all_checks_passed": True,
        "bounded_reuse_q": q,
        "bounded_reuse_h": h,
        "bounded_reuse_uniform_load": str(load),
        "bounded_reuse_bound": str(Fraction(h, q)),
        "sunflower_sources": len(marked),
        "sunflower_core_size": len(core),
        "minimum_petals_targets": min(degrees.values()),
        "exact_disjoint_load": str(exact),
    })


if __name__ == "__main__":
    main()
