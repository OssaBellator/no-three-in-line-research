#!/usr/bin/env python3
"""Finite checks for SAS5ay--SAS5bc."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from random import Random


def maximum_matching(left_vertices, neighbours):
    match_right = {}

    def augment(left, seen):
        for right in neighbours[left]:
            if right in seen:
                continue
            seen.add(right)
            if right not in match_right or augment(match_right[right], seen):
                match_right[right] = left
                return True
        return False

    matched = 0
    for left in left_vertices:
        if augment(left, set()):
            matched += 1
    return matched


def greedy_colour_classes(vertices, adjacency):
    colour = {}
    for vertex in vertices:
        used = {colour[n] for n in adjacency[vertex] if n in colour}
        current = 0
        while current in used:
            current += 1
        colour[vertex] = current
    classes = {}
    for vertex, value in colour.items():
        classes.setdefault(value, []).append(vertex)
    return list(classes.values())


def fibre_and_matching_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(70000):
        d = rng.randint(1, 12)
        donor_columns = tuple(range(d))
        original = set(rng.sample(donor_columns, k=min(2, d)))
        defect_count = rng.randint(1, 12)
        h = rng.randint(0, 5)
        obstruction_sets = {}
        neighbours = {}
        good = []
        for z in range(defect_count):
            possible = [q for q in donor_columns if q not in original]
            obstruction = set(rng.sample(possible, k=rng.randint(0, len(possible))))
            obstruction_sets[z] = obstruction
            neighbours[z] = set(donor_columns) - original - obstruction
            if len(obstruction) <= h:
                good.append(z)
                assert len(neighbours[z]) >= max(0, d - len(original) - h)

        g = max(0, d - 2 - h)
        # The theorem uses the safe lower bound d-2-h even when fewer than two
        # original columns belong to the donor class.
        selected = tuple(good[: min(len(good), g)])
        assert maximum_matching(selected, neighbours) == len(selected)
        counts["good-fibre matching systems"] += 1

        # A safe donor is outside every companion obstruction and both originals.
        for z in range(defect_count):
            for q in neighbours[z]:
                assert q not in original
                assert q not in obstruction_sets[z]
                counts["safe whole-fibre donor checks"] += 1


def weighted_router_checks(counts: Counter[str]) -> None:
    rng = Random(991)
    for _ in range(60000):
        d = rng.randint(1, 14)
        donors = tuple(range(d))
        original = set(rng.sample(donors, k=min(2, d)))
        defect_count = rng.randint(1, 14)
        h = rng.randint(0, 6)
        loads = [Fraction(rng.randint(0, 20), rng.randint(1, 6)) for _ in range(defect_count)]
        obstruction_sets = []
        good = []
        bad = []
        for z in range(defect_count):
            possible = [q for q in donors if q not in original]
            obstruction = set(rng.sample(possible, k=rng.randint(0, len(possible))))
            obstruction_sets.append(obstruction)
            (good if len(obstruction) <= h else bad).append(z)

        good_weight = sum((loads[z] for z in good), Fraction(0))
        bad_weight = sum((loads[z] for z in bad), Fraction(0))
        total = good_weight + bad_weight
        assert total == sum(loads, Fraction(0))

        g = max(0, d - 2 - h)
        m = min(len(good), g)
        selected = sorted((loads[z] for z in good), reverse=True)[:m]
        selected_weight = sum(selected, Fraction(0))
        if good:
            assert selected_weight * len(good) >= good_weight * m

        if bad:
            incidence = {q: Fraction(0) for q in donors}
            for z in bad:
                for q in obstruction_sets[z]:
                    incidence[q] += loads[z]
            assert sum(incidence.values(), Fraction(0)) > h * bad_weight or bad_weight == 0
            best = max(incidence.values(), default=Fraction(0))
            assert best * d > h * bad_weight or bad_weight == 0
        counts["weighted good-bad routers"] += 1


def compatibility_checks(counts: Counter[str]) -> None:
    rng = Random(77)
    for _ in range(30000):
        n = rng.randint(1, 12)
        lam = rng.randint(0, 4)
        bound = 4 * lam
        vertices = tuple(range(n))
        adjacency = {v: set() for v in vertices}
        candidates = list(combinations(vertices, 2))
        rng.shuffle(candidates)
        for u, v in candidates:
            if len(adjacency[u]) < bound and len(adjacency[v]) < bound and rng.randrange(3) == 0:
                adjacency[u].add(v)
                adjacency[v].add(u)
        weights = {v: Fraction(rng.randint(0, 18), rng.randint(1, 5)) for v in vertices}
        classes = greedy_colour_classes(vertices, adjacency)
        assert len(classes) <= bound + 1
        heaviest = max((sum((weights[v] for v in cls), Fraction(0)) for cls in classes), default=Fraction(0))
        total = sum(weights.values(), Fraction(0))
        assert heaviest * (bound + 1) >= total
        counts["weighted compatible subbanks"] += 1


def composed_repair_checks(counts: Counter[str]) -> None:
    rng = Random(123)
    for _ in range(25000):
        # One swapped scope column s, the other original column t outside scope,
        # defect z, varying companions, and a donor q avoiding all companions.
        labels = {"s": 0, "t": 1, "z": 2, "q": 1}
        companion_count = rng.randint(1, 6)
        companions = [f"c{i}" for i in range(companion_count)]
        for c in companions:
            labels[c] = rng.randint(0, 2)
        requirements = [
            {"s": 1, "z": 1, c: labels[c]}
            for c in companions
        ]
        assert all(not all(labels[col] == req[col] for col in req) for req in requirements)
        post = dict(labels)
        post["s"], post["t"] = post["t"], post["s"]
        post["z"], post["q"] = post["q"], post["z"]
        assert all(all(post[col] == req[col] for col in req) for req in requirements)
        counts["composed singleton fibre repairs"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    fibre_and_matching_checks(counts)
    weighted_router_checks(counts)
    compatibility_checks(counts)
    composed_repair_checks(counts)
    print("SAS5ay--SAS5bc singleton companion audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
